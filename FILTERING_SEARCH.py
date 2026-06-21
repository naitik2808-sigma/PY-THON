import json
import urllib.request

# Fetch posts from the API
api_url = "https://jsonplaceholder.typicode.com/posts"
with urllib.request.urlopen(api_url) as response:
    if response.status != 200:
        raise RuntimeError(f"Error fetching posts: {response.status}")
    posts = json.load(response)

# Filter posts by userId = 1
user_id_to_filter = 1
filtered_posts_again = [post for post in posts if post['userId'] == user_id_to_filter]

print(f"\nPosts by User ID {user_id_to_filter}: {len(filtered_posts_again)} found")
if filtered_posts_again:
    print("First 3 filtered posts:")
    for i, post in enumerate(filtered_posts_again[:3]):
        print(f"Post {i+1}:")
        print(f"  ID: {post['id']}")
        print(f"  Title: {post['title'][:50]}...")
        print("-" * 20)
else:
    print(f"No posts found for User ID {user_id_to_filter}.")