import os
import json
from collections import defaultdict

input_folder = "step3_post/json"
output_folder = "step3_post/post"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Dictionary to store posts by topicid
topics_posts = defaultdict(dict)

# Traverse the input folder for json files
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        print(f"Processing file: {filename}")
        filepath = os.path.join(input_folder, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Extract the topicid from the filename
        topicid = filename.split('_')[0]
        topic_key = f"topic_{topicid}"
        
        # Check if the topic_key exists in the json data
        if topic_key in data and "post_stream" in data[topic_key] and "posts" in data[topic_key]["post_stream"]:
            posts = data[topic_key]["post_stream"]["posts"]
            for post in posts:
                post_id = post["id"]
                if post_id not in topics_posts[topicid]:
                    topics_posts[topicid][post_id] = post

# Write the combined posts to their respective output files
for topicid, posts in topics_posts.items():
    output_filepath = os.path.join(output_folder, f"{topicid}_post.json")
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        json.dump({"posts": list(posts.values())}, outfile, ensure_ascii=False, indent=4)
    print(f"Written combined posts to: {output_filepath}")

print("Processing complete.")