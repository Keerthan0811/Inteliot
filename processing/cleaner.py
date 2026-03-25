import re
import json

def clean_dataset(raw_dataset):

    clean_data = []

    for item in raw_dataset:
        try:
            paragraph_match = re.search(r"Paragraph:\s*(.*?)\s*JSON:", item, re.DOTALL)
            json_match = re.search(r"JSON:\s*(\[.*\])", item, re.DOTALL)

            if paragraph_match and json_match:
                paragraph = paragraph_match.group(1).strip()
                json_text = json_match.group(1).strip()

                parsed_json = json.loads(json_text)

                clean_data.append({
                    "instruction": paragraph,
                    "output": parsed_json
                })

        except:
            continue

    return clean_data