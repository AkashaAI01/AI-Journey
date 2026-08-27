import requests

response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
users = response.json()

print(f"\n{'Total users:':>40} {len(users)}\n")
print("=" * 80)
print(f"   {'ID':<5}{'Name':<35}{'Email':<35}")
print("=" * 80)
for user in users:
    print(f"   {user['id']:<5} {user['name']:<35} {user['email']:<35}")
    print("-" * 80)