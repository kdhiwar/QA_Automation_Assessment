import requests
import json

# Base URL
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    response = requests.get(BASE_URL)
    
    # Validate response status
    assert response.status_code == 200, f"Unexpected Status Code: {response.status_code}"
    
    posts = response.json()
    
    # Validate structure
    for post in posts:
        for key in ["userId", "id", "title", "body"]:
            assert key in post, f"Missing key {key} in post {post}"
    
    # Save first 5 posts
    with open("first_5_posts.json", "w") as f:
        json.dump(posts[:5], f, indent=4)
    
    print("Fetched and saved first 5 posts successfully!")

if __name__ == "__main__":
    fetch_posts()
