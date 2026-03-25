from groq import Groq
from config import API_KEY, MODEL_NAME
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import re

# Initialize Groq client
client = Groq(api_key=API_KEY)


# 🔥 Prompt (balanced: fast + stable)
def build_bulk_prompt():
    return """
Generate 20 smart home command examples.

Each example must include:
- A natural paragraph with multiple commands
- A structured JSON output

Return ONLY valid JSON.
No explanation.
No markdown.

Format:

[
  {
    "instruction": "Turn off lights and switch on fan",
    "output": ["turn off lights", "turn on fan"]
  }
]
"""


# 🔥 Single API call
def generate_one_batch():
    prompt = build_bulk_prompt()

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.choices[0].message.content.strip()

        # Extract JSON safely
        json_match = re.search(r"\[.*\]", text, re.DOTALL)
        if not json_match:
            return []

        json_text = json_match.group(0)

        parsed = json.loads(json_text)

        if isinstance(parsed, list):
            return parsed

    except:
        return []

    return []


# 🔥 Ultra-fast parallel generator
def generate_samples(num_samples):

    dataset = []
    MAX_WORKERS = 20  # 🔥 Adjust (5–10 based on rate limits)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        while len(dataset) < num_samples:

            futures = [executor.submit(generate_one_batch) for _ in range(MAX_WORKERS)]

            for future in as_completed(futures):

                prev_len = len(dataset)

                result = future.result()
                dataset.extend(result)

                # ✅ Print only when new data added
                if len(dataset) > prev_len:
                    print(f"Generated: {len(dataset)} / {num_samples}")

                if len(dataset) >= num_samples:
                    break

    return dataset[:num_samples]