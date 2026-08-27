import requests

# Method 1 Adjusting url
url = "https://jsonplaceholder.typicode.com/posts?userId=1&_limit=3"
response = requests.get(url, timeout=10)

# Method 2 by using params
params = {
    "userId": 1,
    "_limit": 3
}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params,
    timeout=10
)

print(f"\n  Url called: {response.url}")
posts = response.json()
print(f"\n  Posts revieved: {len(posts)}")

for post in posts:
    print(f"\n  Post title: {post['title']}")
    print(f"  Body : {post['body'][:60]}....\n")