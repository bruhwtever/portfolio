import pandas as pd
from pymongo import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Connect to MongoDB Atlas
MONGO_URI = "mongodb+srv://sdgppilotadmin:pilot1@sdgppilot1.wl8ps.mongodb.net/sdgppilot1?retryWrites=true&w=majority&appName=sdgppilot1"
client = MongoClient(MONGO_URI)
db = client["sdgppilot1"]
meals_collection = db["pilotmeals"]

# Fetch all meals
meals = list(meals_collection.find())
if not meals:
    print("No meals found in the database.")
    exit()

# Prepare the DataFrame
meal_df = pd.DataFrame(meals)
meal_df['_id'] = meal_df['_id'].astype(str)  # Convert ObjectId to string
meal_df['tag_string'] = meal_df['tags'].apply(lambda x: " ".join(x))

# Vectorize the tags
vectorizer = CountVectorizer()
tag_matrix = vectorizer.fit_transform(meal_df['tag_string'])

# Calculate similarity matrix
similarity_matrix = cosine_similarity(tag_matrix)

def recommend_meals(meal_name, top_n=3):
    if meal_name not in meal_df['name'].values:
        print(f"Meal '{meal_name}' not found in the database.")
        return

    meal_index = meal_df[meal_df['name'] == meal_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[meal_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i for i, score in similarity_scores[1:top_n+1]]

    print(f"Recommendations for '{meal_name}':")
    for idx in recommended_indices:
        print(f" - {meal_df.iloc[idx]['name']} (Tags: {meal_df.iloc[idx]['tags']})")

# Example: Recommend similar meals to 'Vegan Salad'
recommend_meals('Vegan Salad')