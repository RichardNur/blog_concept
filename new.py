import json

with open('data/blog_posts.json', 'r') as file:
    data = json.load(file)

print(data)
print()
print(blog_posts)