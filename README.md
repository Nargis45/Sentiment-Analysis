# Sentiment-Analysis

(https://github.com/Nargis45/Sentiment-Analysis/blob/main/Recording%202025-01-30%20174404.mp4)

## Project Workflow

### The project consists of three main steps:

<b>1. Fetching YouTube Comments</b>

The script in yt_api.ipynb fetches comments from YouTube videos using the YouTube API.

It extracts relevant comments, which are later used for sentiment analysis.

The fetched comments can be found in the comment section of the notebook.

<b>2. Sentiment Analysis</b>

The sentiment-analysis.ipynb file applies different sentiment analysis techniques to classify the fetched comments as positive, neutral, or negative.

Various Natural Language Processing (NLP) methods and machine learning models are used for sentiment classification.

The processed data, containing sentiment labels, is then stored for further use.

<b>3. Streamlit Web Application</b>

The Sentiment Analysis.py file contains the Streamlit application code.

It visualizes the sentiment analysis results, displaying positive, neutral, and negative comments in an interactive and user-friendly way.

The UI is designed using HTML and CSS within the Streamlit framework to provide a seamless experience.

**Usage**

Fetch comments using the YouTube API script (yt_api.ipynb).

Run sentiment analysis (sentiment-analysis.ipynb) to label comments.

Launch the Streamlit app (Sentiment Analysis.py) to visualize sentiment distribution.

**Technologies Used**

Python: Programming language used for scripting and analysis

YouTube API: Fetching comments from YouTube videos

NLTK / Roberta / VADER: Sentiment analysis techniques

Pandas: Data manipulation and processing

Streamlit: Web application framework for data visualization

**Conclusion**

This project demonstrates how to collect YouTube comments, analyze their sentiment, and visualize results interactively. The combination of APIs, NLP, and web development makes it a powerful and insightful tool for understanding audience feedback.
