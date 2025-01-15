# Comprehensive Analysis of the OpenAI Developer Forum

The OpenAI Developer Forum is a hub for developers to discuss their experiences, seek guidance, and share best practices related to OpenAI's technologies.

## Research Questions

### RQ1: Popularity Trends
- **Objective:** Analyze activity trends on the forum.
- **Focus:** Identify popular topics and user engagement trends.

### RQ2: Taxonomy of Concerns 
- **Objective:** Classify specific developer concerns.
- **Focus:** Understand common obstacles and issues in the developer community.

## Methodology
The methodology consists of five primary steps:

### Step 1: Crawl Forum Topic Lists
Collected 29,576 topics from 17 categories using a custom web crawler to gather comprehensive topic lists and verify completeness.

### Step 2: Scrape All Post Details
Extracted complete post information for each topic, including attributes like `post_id`, `username`, `content`, and `engagement metrics`.

### Step 3: Identify Popularity Trends
Conducted time series analysis to investigate the growth and decline of interest in specific topics and examined factors affecting engagement. 

### Step 4: Filter Developers' Concern Topics
Filtered 9,301 active topics from 2024 across `API`, `ChatGPT`, `GPT builders`, and `Prompting` categories for detailed analysis.

### Step 5: Construct a Taxonomy of Concerns
Developed a taxonomy of concerns based on forum categories, using a sample of 886 topics and achieving high inter-rater agreement (Cohen's Kappa of 0.835). The taxonomy includes three root categories (`API/ChatGPT`, `GPT Builders`, `Prompting`), 13 inner categories, and 50 leaf categories.

## Contributions
1. **Data Collection and Analysis:**
   - Collected 29,576 topics for analysis. 
   - Provided insights into popularity trends and user engagement.

2. **Taxonomy Development:** 
   - Filtered and analyzed 9,301 topics related to developer concerns.
   - Constructed a comprehensive taxonomy from 717 relevant topics.

3. **Pioneering Research:**
   - Conducted the first large-scale analysis of the OpenAI Developer Forum.
   - Offered insights to guide future research, tool development, and best practices in AI-assisted software engineering.

## Data sample
The 33 attributes of a topic (id:865677) and data examples are shown below:
```json
    {
        "id": 865677,
        "title": "Assistant API Response Issue",
        "fancy_title": "Assistant API Response Issue",
        "slug": "assistant-api-response-issue",
        "posts_count": 1,
        "reply_count": 0,
        "highest_post_number": 1,
        "image_url": "https://global.discourse-cdn.com/openai1/original/4X/e/9/b/e9b01385c53d1ef141332dbad4718f3452fadde7.png",
        "created_at": "2024-07-14T09:03:19.514Z",
        "last_posted_at": "2024-07-14T09:03:19.612Z",
        "bumped": true,
        "bumped_at": "2024-07-14T09:03:19.612Z",
        "archetype": "regular",
        "unseen": false,
        "pinned": false,
        "unpinned": null,
        "visible": true,
        "closed": false,
        "archived": false,
        "bookmarked": null,
        "liked": null,
        "tags": [
            "chatgpt",
            "gpt-4",
            "assistants-api"
        ],
        "tags_descriptions": {},
        "views": 75,
        "like_count": 0,
        "has_summary": false,
        "last_poster_username": "z.mahmud",
        "category_id": 7,
        "pinned_globally": false,
        "featured_link": null,
        "has_accepted_answer": false,
        "can_vote": false,
        "posters": [
            {
                "extras": "latest single",
                "description": "Original Poster, Most Recent Poster",
                "user_id": 522851,
                "primary_group_id": null,
                "flair_group_id": null
            }
        ]
    }
```
All posts of topic (id:865677), and 52 attributes.
```json
{
    "posts": [
        {
            "id": 1165161,
            "name": "Zahir Mahmud",
            "username": "z.mahmud",
            "avatar_template": "/user_avatar/community.openai.com/z.mahmud/{size}/291413_2.png",
            "created_at": "2024-07-14T09:03:19.612Z",
            "cooked": "<p>I am using Assistant streaming  API with gpt-4-turbo. My input token is almost 16K and after generating 3K tokens for output it stops generating output. Can someone tell where the issue is?</p>\n<p><div class=\"lightbox-wrapper\"><a class=\"lightbox\" href=\"https://global.discourse-cdn.com/openai1/original/4X/e/9/b/e9b01385c53d1ef141332dbad4718f3452fadde7.png\" data-download-href=\"/uploads/short-url/xliuwfKgNBVZMEHSH6OSbS841v1.png?dl=1\" title=\"image\" rel=\"noopener nofollow ugc\"><img src=\"https://global.discourse-cdn.com/openai1/original/4X/e/9/b/e9b01385c53d1ef141332dbad4718f3452fadde7.png\" alt=\"image\" data-base62-sha1=\"xliuwfKgNBVZMEHSH6OSbS841v1\" width=\"690\" height=\"272\" data-dominant-color=\"28272A\"><div class=\"meta\"><svg class=\"fa d-icon d-icon-far-image svg-icon\" aria-hidden=\"true\"><use href=\"#far-image\"></use></svg><span class=\"filename\">image</span><span class=\"informations\">829×327 12.9 KB</span><svg class=\"fa d-icon d-icon-discourse-expand svg-icon\" aria-hidden=\"true\"><use href=\"#discourse-expand\"></use></svg></div></a></div></p>",
            "post_number": 1,
            "post_type": 1,
            "updated_at": "2024-07-14T09:03:19.612Z",
            "reply_count": 0,
            "reply_to_post_number": null,
            "quote_count": 0,
            "incoming_link_count": 4,
            "reads": 14,
            "readers_count": 13,
            "score": 22.8,
            "yours": false,
            "topic_id": 865677,
            "topic_slug": "assistant-api-response-issue",
            "display_username": "Zahir Mahmud",
            "primary_group_name": null,
            "flair_name": null,
            "flair_url": null,
            "flair_bg_color": null,
            "flair_color": null,
            "flair_group_id": null,
            "version": 1,
            "can_edit": false,
            "can_delete": false,
            "can_recover": false,
            "can_see_hidden_post": false,
            "can_wiki": false,
            "read": true,
            "user_title": null,
            "bookmarked": false,
            "actions_summary": [],
            "moderator": false,
            "admin": false,
            "staff": false,
            "user_id": 522851,
            "hidden": false,
            "trust_level": 1,
            "deleted_at": null,
            "user_deleted": false,
            "edit_reason": null,
            "can_view_edit_history": true,
            "wiki": false,
            "can_accept_answer": false,
            "can_unaccept_answer": false,
            "accepted_answer": false,
            "topic_accepted_answer": false,
            "can_vote": false
        }
    ]
}
```
## Project Directory Structure

The project directory structure follows the five steps outlined in the Methodology section:
PS: The size of step2_post exceeds 20G, and a large number of posts contain sensitive information, which violates the upload rules of the repository. Therefore, the complete post data is not uploaded in this project.
```plaintext
openai-dev-forum-analysis
├── step1_topic/
│      └── topic.json
├── step2_post/
│      ├── all_links.txt
│      ├── all_topics.json
│      ├── html/
│      ├── json/
│      └── post/
├── step3_rq1/
│      ├── step4_data.csv
│      ├── step4_max_score.csv
│      ├── step4_post.csv
│      └── step4_user.csv
├── step4_concerns/
│      └── concerns_topics.xlsx
├── step5_rq2/
│      └── final_taxonomy.xlsx
│      └── sample.xlsx
├── step1_topic_1.py
├── step1_topic_2.py
├── step1_topic_3.py
├── step2_post_1.py
├── step2_post_2.py
├── step2_post_3.py  
├── step3_rq1_data.py
├── step3_rq1_post.py
└── step5_rq2_sample.py
```

Each step's functionality is explained in the corresponding part of the Methodology section in this `README.md`.

## Dependencies

This project relies on the following Python packages:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

To ensure consistent library versions across environments and prevent compatibility issues, we have included a `requirements.txt` file listing these dependencies. 

## Installation

To set up the project environment and install the required dependencies, follow these steps:

1. Clone the project repository:
   ```
   git clone https://xxx/openai-dev-forum-analysis.git
   ```

2. Navigate to the project directory:
   ```
   cd openai-dev-forum-analysis
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

After completing these steps, you will have the necessary environment set up to run the analysis scripts and reproduce the results presented in this study.
