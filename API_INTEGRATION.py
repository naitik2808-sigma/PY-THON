import requests

# Define the API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched data!")
    # Parse the JSON response
    posts = response.json()
    print(f"Total posts fetched: {len(posts)}")
    print("\nFirst 3 posts:")
    for i, post in enumerate(posts[:3]):
        print(f"Post {i+1}:")
        print(f"  ID: {post['id']}")
        print(f"  Title: {post['title'][:50]}...") # Display first 50 chars of title
        print(f"  Body: {post['body'][:100]}...") # Display first 100 chars of body
        print("-" * 20)
else:
    print(f"Error fetching data: {response.status_code} - {response.text}")