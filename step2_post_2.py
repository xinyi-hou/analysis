import json
import requests
from bs4 import BeautifulSoup
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def process_html_to_json(html_content, json_output_path):
    """
    This function processes HTML content, extracts JSON data from a specific div element,
    decodes nested JSON, and writes the formatted JSON to an output file.

    :param html_content: HTML content as a string
    :param json_output_path: Path to the output JSON file
    """
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract JSON data from the specified div element
    data_preloaded = soup.find('div', {'id': 'data-preloaded'})['data-preloaded']
    data_preloaded = data_preloaded.replace('&quot;', '\"')

    # Function to decode nested JSON
    def decode_nested_json(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    try:
                        nested_data = json.loads(value)
                        data[key] = decode_nested_json(nested_data)
                    except json.JSONDecodeError:
                        data[key] = value
                else:
                    data[key] = decode_nested_json(value)
        elif isinstance(data, list):
            for i in range(len(data)):
                data[i] = decode_nested_json(data[i])
        return data

    # Load and decode the JSON data
    data_dict = json.loads(data_preloaded)
    decoded_data_dict = decode_nested_json(data_dict)

    # Format the JSON data
    formatted_json = json.dumps(decoded_data_dict, indent=4, ensure_ascii=False)

    # Write the formatted JSON to an output file
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json_file.write(formatted_json)

# Ensure the output folders exist
output_folder_html = "step3_post/html"
output_folder_json = "step3_post/json"
os.makedirs(output_folder_html, exist_ok=True)
os.makedirs(output_folder_json, exist_ok=True)
print(f"Created output folders: {output_folder_html} and {output_folder_json}")

# Topic JSON file path
topic_json_path = "step2_link/all_topics.json"

# Load topics from the JSON file
print(f"Loading topics from {topic_json_path}...")
with open(topic_json_path, 'r', encoding='utf-8') as file:
    topics = json.load(file)
print(f"Loaded {len(topics)} topics.")

# User-Agent header to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Checkpoint file path
checkpoint_file = "step3_post/checkpoint.json"

# Load checkpoint if exists
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, 'r') as file:
        checkpoint = json.load(file)
        start_topic_index = checkpoint['topic_index']
        start_post_num = checkpoint['post_num']
else:
    start_topic_index = 0
    start_post_num = 1

# Configure retry parameters
retry_strategy = Retry(
    total=3,  # Total number of retries
    status_forcelist=[500, 502, 503, 504],  # Retry on these status codes
    allowed_methods=["GET", "POST"],  # Only retry on GET and POST requests
    backoff_factor=1  # Backoff factor for retry intervals
)
adapter = HTTPAdapter(max_retries=retry_strategy)

# Create a session and mount the retry strategy for http and https requests
http = requests.Session()
http.mount("http://", adapter)
http.mount("https://", adapter)

# Iterate over each topic starting from the checkpoint
for topic_index in range(start_topic_index, len(topics)):
    topic = topics[topic_index]
    topic_id = topic['id']
    topic_link = topic['topic_link']
    posts_count = topic['posts_count']
    
    print(f"\nProcessing topic {topic_id}: {topic['title']} with {posts_count} posts...")

    # Iterate over each post number starting from the checkpoint
    for post_num in range(start_post_num, posts_count + 1):
        url = f"{topic_link}/{post_num}"
        print(f"Fetching URL: {url}")
        
        try:
            response = http.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an exception if the response status code is not 200
            html_data = response.text

            soup = BeautifulSoup(html_data, 'html.parser')

            # Locate the discourse-assets-json element
            discourse_assets_json = soup.find('discourse-assets-json')
            if discourse_assets_json:
                print(f"Found discourse-assets-json for post {post_num}")
                data_preloaded = discourse_assets_json.text
                data_preloaded = data_preloaded.replace('&quot;', '\"')

                # Save only the discourse-assets-json content to a file
                html_file_name = f"{topic_id}_{post_num}.html"
                html_file_path = os.path.join(output_folder_html, html_file_name)
                with open(html_file_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(str(discourse_assets_json))
                print(f"Saved discourse-assets-json content to {html_file_path}")

                # Use process_html_to_json function to process the HTML content and save the JSON
                json_file_name = f"{topic_id}_{post_num}.json"
                json_file_path = os.path.join(output_folder_json, json_file_name)
                process_html_to_json(html_data, json_file_path)
                print(f"Saved JSON content to {json_file_path}")

                # Save checkpoint
                checkpoint = {
                    'topic_index': topic_index,
                    'post_num': post_num + 1
                }
                with open(checkpoint_file, 'w') as file:
                    json.dump(checkpoint, file)
                
            else:
                print(f"discourse-assets-json not found for post {post_num}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            # Log the error or perform other error handling logic
            continue  # Skip the current request and continue with the next one

    # Reset post number for the next topic
    start_post_num = 1

# Remove checkpoint file after processing all topics
if os.path.exists(checkpoint_file):
    os.remove(checkpoint_file)