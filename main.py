from generator.groq_generator import generate_samples
from processing.cleaner import clean_dataset
from processing.filter import filter_dataset
from utils.file_handler import save_json
from config import NUM_SAMPLES, SAVE_INTERVAL
import os

os.makedirs("data", exist_ok=True)

def main():

    print("🚀 Generating dataset using Groq API...")

    raw_data = []
    
    for i in range(0, NUM_SAMPLES, SAVE_INTERVAL):

        batch = generate_samples(SAVE_INTERVAL)
        raw_data.extend(batch)

        save_json(raw_data, "data/raw_dataset.json")

        print(f"Saved {len(raw_data)} samples")

    print("🧹 Cleaning dataset...")
    clean_data = clean_dataset(raw_data)
    save_json(clean_data, "data/final_dataset.json")

    print("🔍 Filtering dataset...")
    filtered_data = filter_dataset(clean_data)
    save_json(filtered_data, "data/filtered_dataset.json")

    print("\n✅ DONE!")
    print(f"Final samples: {len(filtered_data)}")


if __name__ == "__main__":
    main()