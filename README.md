# **Reddit AI Bot**

This project is a Reddit bot that uses the **Groq AI API** to generate and post engaging content to Reddit automatically. It includes features such as daily scheduled posts, error handling, and optional comment generation.

![Sample Reddit Post](image.png)

---

## **Features**
- **Daily Automated Posts**: Posts AI-generated content at user-specified times.
- **Groq AI Integration**: Uses Groq API for dynamic and engaging content generation.
- **Error Handling and Logging**: Logs all operations, errors, and status updates.
- **Bonus Feature**: Ability to generate and post comments on other Reddit threads.

---

## **Technologies Used**
- **Programming Language**: Python
- **APIs**:
  - [Reddit API](https://www.reddit.com/dev/api/)
  - [Groq API](https://api.groq.ai)
- **Libraries**:
  - `praw`: Reddit API wrapper
  - `schedule`: For task scheduling
  - `requests`: To interact with Groq API
  - `logging`: For logging errors and status

---

## **Project Structure**
RedditAIBot/ ├── config/ │ ├── .env # Environment variables │ ├── settings.py # Project settings ├── docs/ # Documentation ├── logs/ # Log files ├── src/ # Source code │ ├── init.py # Module initialization │ ├── bot.py # Main bot functionality │ ├── groq_api.py # Groq API integration │ ├── reddit_api.py # Reddit API integration │ ├── scheduler.py # Scheduler for posting ├── tests/ # Test cases │ ├── test_bot.py # Tests for the bot ├── README.md # Project documentation ├── requirements.txt # Python dependencies ├── venv/ # Virtual environment

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd RedditAIBot
Set up a Virtual Environment

Bash

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
Install Dependencies

Bash

pip install -r requirements.txt
Configure Environment Variables

Create a .env file in the config directory with the following values:

Code snippet

REDDIT_CLIENT_ID=<your_reddit_client_id>
REDDIT_CLIENT_SECRET=<your_reddit_client_secret>
REDDIT_USERNAME=<your_reddit_username>
REDDIT_PASSWORD=<your_reddit_password>
REDDIT_USER_AGENT=<your_reddit_user_agent>
GROQ_API_KEY=<your_groq_api_key>
Run the Bot

Bash

python src/bot.py


Usage
Automated Posting: The bot posts generated content daily at the specified time.
Logging: All activities are logged in the logs/bot.log file.
Testing: Run the test cases using:
Bash

python -m unittest discover tests
Sample Output
Log File (bot.log):

2025-01-17 09:56:00,866 - INFO - Logging initialized successfully.
2025-01-17 09:56:00,866 - INFO - Starting Reddit AI Bot.
2025-01-17 09:56:01,822 - INFO - Scheduled task set at 10:00 AM daily.
2025-01-17 10:00:02,300 - INFO - Post submitted successfully to r/test with ID: abcd1234
Reddit Post:

Title: 5 Ways to Stay Productive

Body:

Here are 5 tips to boost your productivity:

1. Plan your day.
2. Minimize distractions.
3. Take breaks.
4. Use tools like Trello.
5. Stay consistent.
Troubleshooting
FileNotFoundError: Ensure that the logs/ directory exists before running the bot.
API Errors: Verify your API keys and network connectivity.
Permission Errors: Check Reddit API credentials and ensure the bot has appropriate permissions for the subreddit.
Future Improvements
Add advanced content customization.
Support multiple subreddits.
Enhance comment generation logic.
Contributors
Your Name (Developer)