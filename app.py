import streamlit as st
import pickle

recipes = pickle.load(open("recipes.pkl", 'rb'))
similar = pickle.load(open("similar.pkl", 'rb'))
recipes_recommendations = recipes['Name'].values

st.header("CookingBot")
values = st.selectbox("Select Recipes from dropdown", recipes_recommendations)

def recommend(recipes_input):
    index = recipes[recipes['Name']==recipes_input].index[0]
    distance = sorted(list(enumerate(similar[index])), reverse=True, key=lambda vector:vector[1])
    recommend_recipes = []
    for i in distance[0:5]:
        recipes_image = recipes.iloc[i[0]].Images
        recommend_recipes.append(recipes.iloc[i[0]].Name)
    return recommend_recipes

if st.button("Recipe Recommend"):
    recipe_name = recommend(values)
    column1, column2, column3, column4, column5 = st.columns(5)
    with column1:
        st.button(recipe_name[0])
    with column2:
        st.button(recipe_name[1])
    with column3:
        st.button(recipe_name[2])
    with column4:
        st.button(recipe_name[3])
    with column5:
        st.button(recipe_name[4])