import os
import requests
import json

# Define the base URL and output folder
base_url = "https://community.openai.com/latest.json?no_definitions=true"
# base_url = "https://community.openai.com/hot.json?"
output_folder = "step1_topic"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Initialize variables
page = 1
file_name = "latest_topics_1.json"
# file_name = "hot_topics.json"
file_path = os.path.join(output_folder, file_name)
all_topics = []

# Load existing topics if the file already exists
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        all_topics = json.load(f)

# Fetch topics page by page
while True:
    print(f"Fetching {base_url}&page={page}")
    response = requests.get(f"{base_url}&page={page}")
    if response.status_code != 200:
        print(f"Failed to fetch {base_url}&page={page}: {response.status_code}")
        break

    data = response.json()
    topics = data.get("topic_list", {}).get("topics", [])

    if not topics:
        print(f"No more topics in {base_url}&page={page}")
        break

    all_topics.extend(topics)
    page += 1

    # Save to JSON file incrementally
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_topics, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(all_topics)} topics to {file_path}")

print(f"Completed fetching topics from {base_url}")