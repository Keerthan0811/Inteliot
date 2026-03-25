from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from config import BATCH_SIZE, MAX_NEW_TOKENS
from generator.prompt_builder import build_prompt


# ✅ REQUIRED FUNCTION
def load_model(model_id):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    # 🔥 FIX: set pad token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer


def generate_samples_batch(model, tokenizer, num_samples, label):

    data = []

    for i in range(0, num_samples, BATCH_SIZE):

        prompts = [build_prompt() for _ in range(BATCH_SIZE)]

        inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                do_sample=True,
                temperature=0.7
            )

        texts = [tokenizer.decode(o, skip_special_tokens=True) for o in outputs]

        data.extend(texts)

        print(f"{label}: Generated {len(data)} samples")

    return data[:num_samples]