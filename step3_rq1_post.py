import csv
import json
import os

# Input and output file paths
input_file = "step4_rq1/step4_data.csv"
input_folder = "step3_post/post"
output_file_1 = "step4_rq1/step4_post.csv"
output_file_2 = "step4_rq1/step4_user.csv"
output_file_3 = "step4_rq1/step4_max_score.csv"

# Read the input CSV to map topic_id to category_id
topic_to_category = {}
with open(input_file, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        topic_to_category[row['id']] = row['category_id']

# Initialize dictionaries to store results
topic_stats = {}
user_stats = {}
max_score_stats = {}

# Process each JSON file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith("_post.json"):
        topic_id = filename.split('_')[0]
        json_path = os.path.join(input_folder, filename)

        with open(json_path, mode='r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            posts = data.get('posts', [])

            post_count = len(posts)
            total_score = sum(post['score'] for post in posts)
            avg_score = total_score / post_count if post_count > 0 else 0
            max_score = max(post['score'] for post in posts) if post_count > 0 else 0

            category_id = topic_to_category.get(topic_id, 'Unknown')

            topic_stats[topic_id] = {
                'category_id': category_id,
                'post_count': post_count,
                'avg_score': avg_score
            }

            max_score_stats[topic_id] = {
                'category_id': category_id,
                'max_score': max_score
            }

            for post in posts:
                user_id = post['user_id']
                trust_level = post['trust_level']
                
                if user_id not in user_stats:
                    user_stats[user_id] = {}
                if trust_level not in user_stats[user_id]:
                    user_stats[user_id][trust_level] = 0
                user_stats[user_id][trust_level] += 1

        print(f"Processed topic {topic_id}")

# Write the topic statistics to the first output CSV
with open(output_file_1, mode='w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['topic_id', 'category_id', 'post_count', 'avg_score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for topic_id, stats in topic_stats.items():
        writer.writerow({
            'topic_id': topic_id,
            'category_id': stats['category_id'],
            'post_count': stats['post_count'],
            'avg_score': stats['avg_score']
        })

print("Finished writing topic statistics to", output_file_1)

# Write the user statistics to the second output CSV
with open(output_file_2, mode='w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['user_id', 'trust_level', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for user_id, trust_levels in user_stats.items():
        for trust_level, count in trust_levels.items():
            writer.writerow({
                'user_id': user_id,
                'trust_level': trust_level,
                'count': count
            })

print("Finished writing user statistics to", output_file_2)

# Write the max score statistics to the third output CSV
with open(output_file_3, mode='w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['topic_id', 'category_id', 'max_score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for topic_id, stats in max_score_stats.items():
        writer.writerow({
            'topic_id': topic_id,
            'category_id': stats['category_id'],
            'max_score': stats['max_score']
        })

print("Finished writing max score statistics to", output_file_3)