from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_ID

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
    return model, tokenizer