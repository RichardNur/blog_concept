import json
import uuid
import datetime
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """
        This route displays all blog posts in the database (blog_posts.json).
        :return: HTML page (index.html) filled with the required data.
    """
    with open('data/blog_posts.json', 'r') as file:
        blog_posts = json.load(file)
    blog_posts = sorted(blog_posts, key=lambda post: datetime.strptime(post['date'], '%Y-%m-%d %H:%M'), reverse=True)

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handles form submission and adds a new blog post to blog_posts.json.
    Redirects to the home page after submission.
    """
    if request.method == 'POST':
        # read existing blog entries
        try:
            with open('data/blog_posts.json', 'r') as file:
                blog_posts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            blog_posts = []

        # get data from the Form
        id = str(uuid.uuid4()) # Generates random ID
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        content = request.form.get('content', '').strip()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        # create new post-entry
        new_post = {
            "id": id,
            "title": title,
            "author": author,
            "content": content,
            "date": date
        }

        # Add the new post to the list of blog posts
        blog_posts.append(new_post)

        # Write the updated list back to the file
        with open('data/blog_posts.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for('index'))  # Redirect to home page

    return render_template('add.html')


@app.route('/delete/<post_id>', methods=['POST'])
def delete(post_id):
    """
    Deletes a blog post based on its ID.
    Redirects to the home page after deletion.
    """
    try:
        # Load existing blog posts
        with open('data/blog_posts.json', 'r') as file:
            blog_posts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        blog_posts = []

    # Remove the post with the given ID
    updated_posts = [post for post in blog_posts if post["id"] != post_id]

    # Check if any post was actually deleted
    if len(updated_posts) == len(blog_posts):
        return "Post not found", 404

    # Save the updated list back to the JSON file
    with open('data/blog_posts.json', 'w') as file:
        json.dump(updated_posts, file, indent=4)

    return redirect(url_for('index'))


@app.route('/update/<post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    try:
        with open('data/blog_posts.json', 'r') as file:
            blog_posts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        blog_posts = []

    post = None
    for blog_post in blog_posts:
        if str(blog_post['id']) == post_id:
            post = blog_post

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
    # Update the post in the JSON file
        post['title'] = request.form.get('title', '').strip()
        post['author'] = request.form.get('author', '').strip()
        post['content'] = request.form.get('content', '').strip()
        post['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        with open('data/blog_posts.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)
        # Redirect back to index
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
