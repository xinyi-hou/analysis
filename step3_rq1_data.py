import json
import csv
from datetime import datetime

# Define the input JSON file and output CSV file
input_json = "step2_link/all_topics.json"
output_file_1 = "step4_rq1/step4_data.csv"

# Fields to extract
fields = [
    "id", "title", "fancy_title", "slug", "posts_count", "reply_count", 
    "highest_post_number", "image_url", "created_at", "last_posted_at", 
    "bumped", "bumped_at", "archetype", "unseen", "pinned", "unpinned", 
    "visible", "closed", "archived", "bookmarked", "liked", "tags", 
    "tags_descriptions", "views", "like_count", "has_summary", 
    "last_poster_username", "category_id", "pinned_globally", 
    "featured_link", "has_accepted_answer", "can_vote", "topic_link"
]

# Function to convert datetime format
def convert_datetime(dt_str):
    if dt_str:
        return datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m')
    return ''

# Read the JSON data
with open(input_json, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Open the CSV file for writing
with open(output_file_1, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)

    # Write the header
    writer.writeheader()

    # Write the data rows
    for item in data:
        # Extract and transform the required fields
        row = {field: item.get(field, '') for field in fields}
        row["created_at"] = convert_datetime(row["created_at"])
        row["last_posted_at"] = convert_datetime(row["last_posted_at"])
        row["bumped_at"] = convert_datetime(row["bumped_at"])
        writer.writerow(row)

print(f"Data has been successfully written to {output_file_1}")