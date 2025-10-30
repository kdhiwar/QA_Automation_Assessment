import pytest
import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"

# --- JSON Schemas ---
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_status_code_and_response_time(endpoint):
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2, "Response took too long!"

def test_posts_schema():
    response = requests.get(BASE_URL + "/posts")
    posts = response.json()
    for post in posts:
        validate(instance=post, schema=post_schema)
