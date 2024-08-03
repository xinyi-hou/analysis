import os
import requests
import json

# Define the base URL and output folder
base_url = "https://community.openai.com/top.json"
output_folder = "step1_topic"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Initialize variables
page = 1
per_page = 50
file_name = "top_topics.json"
file_path = os.path.join(output_folder, file_name)
all_topics = []

# Load existing topics if the file already exists
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        all_topics = json.load(f)

# Fetch topics page by page
while True:
    url = f"{base_url}?page={page}&per_page={per_page}&period=all"
    print(f"Fetching {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}: {response.status_code}")
        break

    data = response.json()
    topics = data.get("topic_list", {}).get("topics", [])

    if not topics:
        print(f"No more topics in {url}")
        break

    all_topics.extend(topics)
    page += 1

    # Save to JSON file incrementally
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_topics, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(all_topics)} topics to {file_path}")

print(f"Completed fetching topics from {base_url}")