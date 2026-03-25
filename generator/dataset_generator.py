from generator.prompt_builder import build_prompt
from config import NUM_SAMPLES
import torch

def generate_dataset(model, tokenizer):

    raw_data = []

    for i in range(NUM_SAMPLES):

        prompt = build_prompt()

        inputs = tokenizer(prompt, return_tensors="pt")

        outputs = model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=0.8,
            do_sample=True
        )

        text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        raw_data.append(text)

        if i % 2 == 0:
            print(f"Generated {i} samples")

    return raw_data