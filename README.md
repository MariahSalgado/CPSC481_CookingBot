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

Screenshots:

<img width="1006" alt="Screenshot 2025-06-17 at 2 38 42 PM" src="https://github.com/user-attachments/assets/59e3a967-a510-41a9-9505-edb4678ef52f" />

<img width="1021" alt="Screenshot 2025-06-17 at 2 38 52 PM" src="https://github.com/user-attachments/assets/50548f5b-573a-41af-890d-5b5a91708769" />

<img width="1027" alt="Screenshot 2025-06-17 at 2 39 01 PM" src="https://github.com/user-attachments/assets/9e5e8008-b936-40c9-b32b-84d96332cde1" />


