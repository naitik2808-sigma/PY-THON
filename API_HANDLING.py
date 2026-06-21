import requests

def fetch_data_with_error_handling(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        print(f"Successfully fetched data from {url}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code} from {url}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err} - Could not connect to {url}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err} - Request timed out for {url}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err} for {url}")
    except ValueError: # Catches JSON decoding errors
        print(f"Error: Could not decode JSON from response for {url}. Content: {response.text[:100]}...")
    return None

print("\n--- Demonstrating Error Handling ---")

# Scenario 1: Successful request (should work)
print("\nAttempting a successful request:")
successful_data = fetch_data_with_error_handling("https://jsonplaceholder.typicode.com/posts/1")
if successful_data:
    print(f"Fetched single post title: {successful_data['title'][:50]}...")

# Scenario 2: Resource Not Found (404 Error)
print("\nAttempting a request for a non-existent resource (expecting 404):")
non_existent_data = fetch_data_with_error_handling("https://jsonplaceholder.typicode.com/nonexistent-endpoint")

# Scenario 3: Bad Request (example of a possible 4xx, though hard to force on JSONPlaceholder GET)
# Let's simulate by giving a malformed URL for connection error
print("\nAttempting a request to a malformed URL (expecting Connection Error):")
malformed_url_data = fetch_data_with_error_handling("http://invalid.url.example/test")

# Scenario 4: Server Error (5xx) - Hard to simulate directly, but raise_for_status handles it
# For demonstration, we'll just acknowledge that raise_for_status handles 5xx as well.
print("\nNote: The `raise_for_status()` method also handles server-side 5xx errors in a similar fashion.")