🍽️ CookingBot – AI-Powered Recipe Recommender
Course Project – CPSC 481: Artificial Intelligence
Date: May 9, 2025
Team: Mariah Salgado · David Elliott · Mark Moon

📌 Overview
CookingBot is a Python-based recipe recommendation system that helps users discover similar dishes based on their preferences. Built using a content-based filtering approach, it retrieves the top 5 most similar recipes from a dataset using cosine similarity.

🛠️ Tech Stack
Language: Python

Libraries: Streamlit, pandas, numpy, sklearn, pickle, base64

💻 How It Works
Users select a recipe through a dropdown in the Streamlit UI

The app uses CountVectorizer + cosine_similarity to find related recipes

Results display author, calories, protein, and fat content

📁 Key Files
app.py – Main Streamlit app

CookingBot.py – Data helper script

recipes.pkl – Preprocessed recipe data

similar.pkl – Similarity matrix

IMG_9489.jpg – Background image for UI styling
