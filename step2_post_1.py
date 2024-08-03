import os
import json
from glob import glob

input_folder = "step1_topic"  # Folder containing many JSON files, each JSON file contains many items
output_json = "step2_link/all_topics.json"
output_links = "step2_link/all_links.txt"

# Create the output folder if it doesn't exist
os.makedirs(os.path.dirname(output_json), exist_ok=True)

all_items = []
item_ids = set()

# Traverse all JSON files in the input_folder
for json_file in glob(os.path.join(input_folder, "*.json")):
    with open(json_file, 'r', encoding='utf-8') as f:
        items = json.load(f)
        for item in items:
            if item['id'] not in item_ids:
                all_items.append(item)
                item_ids.add(item['id'])

# Add a new topic_link field for each item
base_url = "https://community.openai.com/t/"
for item in all_items:
    item['topic_link'] = f"{base_url}{item['slug']}/{item['id']}"

# Write the merged results to output_json
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(all_items, f, ensure_ascii=False, indent=4)

# Extract all links and write them to output_links
with open(output_links, 'w', encoding='utf-8') as f:
    for item in all_items:
        f.write(f"{item['topic_link']}\n")