developer = {
  "name": "Kasir",
  "created_at": "1994",
  "bio": "..."
}

print(
  developer["bio"],
  developer["created_at"],
  developer["name"]
)

# Wrong usage

print(developer.name) # AttributeError: 'dict' object has no attribute 'name'