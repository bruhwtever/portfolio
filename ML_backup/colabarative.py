import pandas as pd
from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Connect to MongoDB Atlas
MONGO_URI = "mongodb+srv://sdgppilotadmin:pilot1@sdgppilot1.wl8ps.mongodb.net/sdgppilot1?retryWrites=true&w=majority&appName=sdgppilot1"
client = MongoClient(MONGO_URI)
db = client["sdgppilot1"]

# Fetch user preferences and meals
table = []
users_collection = db["pilotusers"]
meals_collection = db["pilotmeals"]

users = list(users_collection.find())
meals = list(meals_collection.find())

# Create a user-item matrix
data = []
for user in users:
    user_id = user['user_id']
    preferred_tags = user['preferred_tags']
    for meal in meals:
        score = len(set(preferred_tags) & set(meal['tags']))
        data.append({'user_id': user_id, 'meal_name': meal['name'], 'score': score})

# Convert to DataFrame
df = pd.DataFrame(data)

# Pivot table to get user-meal matrix
user_meal_matrix = df.pivot_table(index='user_id', columns='meal_name', values='score', fill_value=0)

# Calculate similarity between users
similarity_matrix = cosine_similarity(user_meal_matrix)
user_ids = user_meal_matrix.index.tolist()


def recommend_meals_for_user(user_id, top_n=3):
    if user_id not in user_ids:
        print(f"User ID '{user_id}' not found.")
        return

    # Find index of the user
    user_index = user_ids.index(user_id)
    similarity_scores = list(enumerate(similarity_matrix[user_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Find most similar users
    similar_users = [user_ids[i] for i, score in similarity_scores[1:top_n+1]]

    # Recommend meals based on similar users
    recommended_meals = set()
    for similar_user in similar_users:
        similar_user_prefs = users_collection.find_one({"user_id": similar_user})
        if similar_user_prefs:
            recommended_meals.update(similar_user_prefs['preferred_tags'])

    print(f"Recommendations for user {user_id}:")
    for meal in meals:
        if any(tag in recommended_meals for tag in meal['tags']):
            print(f" - {meal['name']} (Tags: {meal['tags']})")

# Example: Recommend meals for user 1
recommend_meals_for_user(1)
