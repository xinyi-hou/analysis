import os
import requests
import json

# Define URLs and output folder
urls = [
    'https://community.openai.com/c/announcements/6',
    'https://community.openai.com/c/api/7',
    'https://community.openai.com/c/chatgpt/19',
    'https://community.openai.com/c/prompting/8',
    'https://community.openai.com/c/documentation/14',
    'https://community.openai.com/c/gpts-builders/33',
    'https://community.openai.com/c/forum-feedback/22',
    'https://community.openai.com/c/community/21',
    'https://community.openai.com/c/chatgpt/19'
]
output_folder = "step1_topic"

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all URLs
for url in urls:
    base_url = url + ".json"
    page = 1
    file_name = url.split('/')[-1] + ".json"
    file_path = os.path.join(output_folder, file_name)
    all_topics = []

    if os.path.exists(file_path):
        # Load existing topics if the file already exists
        with open(file_path, 'r', encoding='utf-8') as f:
            all_topics = json.load(f)

    while True:
        print(f"Fetching {base_url}?page={page}")
        response = requests.get(f"{base_url}?page={page}")
        if response.status_code != 200:
            print(f"Failed to fetch {base_url}?page={page}: {response.status_code}")
            break

        data = response.json()
        topics = data.get("topic_list", {}).get("topics", [])

        if not topics:
            print(f"No more topics in {base_url}?page={page}")
            break

        all_topics.extend(topics)
        page += 1

        # Save to JSON file incrementally
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(all_topics, f, ensure_ascii=False, indent=4)

        print(f"Saved {len(all_topics)} topics to {file_path}")

    print(f"Completed fetching topics from {url}")