from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "Zebra crossing", "content": "Animals cross here."},
    {"id": 2, "title": "Apple pie recipe", "content": "A delicious apple dessert."},
    {"id": 3, "title": "Banana bread", "content": "Easy homemade banana bread."},
    {"id": 4, "title": "Quantum mechanics", "content": "A deep dive into physics."},
    {"id": 5, "title": "Yoga for beginners", "content": "Stretching and relaxation."},
    {"id": 6, "title": "Deep learning basics", "content": "Introduction to AI."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Retrieve a list of posts.

    Query Parameters:
        sort (str): Optional. Specifies the sorting key ('title' or 'content').
        direction (str): Optional. Specifies the sorting order ('asc' or 'desc').
                         Defaults to 'asc'.

    Returns:
        Response: A JSON list of posts, optionally sorted by the specified parameters.
                  Status code 200 on success.
    """
    sort = request.args.get('sort', None)
    direction = request.args.get('direction', 'asc')  # Default to ascending order
    reverse = direction.lower() == 'desc'

    if sort == 'title':
        sorted_posts = sorted(POSTS, key=lambda post: post['title'].lower(), reverse=reverse)
    elif sort == 'content':
        sorted_posts = sorted(POSTS, key=lambda post: post['content'].lower(), reverse=reverse)
    else:
        sorted_posts = POSTS  # No sorting applied

    return jsonify(sorted_posts), 200


@app.route('/api/posts', methods=['POST'])
def add_post():
    """
    Add a new post to the list.

    Request Body (JSON):
        title (str): The title of the post (required).
        content (str): The content of the post (required).

    Returns:
        Response: A JSON list of all posts after adding the new post.
                  Status code 400 if required fields are missing or invalid.
    """
    try:
        new_post = request.get_json()
        if not new_post['title'] or not new_post['content']:
            return jsonify({"error": "Title and content are required!"}), 400
    except KeyError:
        return jsonify({"error": "Key Error in Data Fetching."}), 400

    new_id = int(len(POSTS) + 1)
    title = new_post.get('title')
    content = new_post.get('content')

    new_post = {"id": new_id, "title": title, "content": content}
    POSTS.append(new_post)

    return jsonify(POSTS)



@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """
    Delete a post by its ID.

    Path Parameters:
        post_id (int): The ID of the post to be deleted.

    Returns:
        Response: A success message and status code 200 if the post is deleted.
                  A JSON error message with status code 404 if the post is not found.
    """
    for post in POSTS:
        if post['id'] == post_id:
            POSTS.remove(post)
            return jsonify({"message": "Post with id <id> has been deleted successfully."}), 200
    return jsonify({"error": "Post not found"}), 404


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """
    Update an existing post by its ID.

    Path Parameters:
        post_id (int): The ID of the post to be updated.

    Request Body (JSON):
        title (str): Optional. The new title of the post.
        content (str): Optional. The new content of the post.

    Returns:
        Response: A JSON list of all posts after the update.
                  A JSON error message with status code 404 if the post is not found.
    """
    for post in POSTS:
        if post['id'] == post_id:
            match = post
            match['title'] = request.json.get('title', match['title'])
            match['content'] = request.json.get('content', match['content'])
            return jsonify(POSTS)
    return jsonify({"error": "Post not found"}), 404


@app.route('/search', methods=['GET'])
def search_post():
    """
    Search for posts by title, content, or ID.

    Query Parameters:
        title (str): Optional. A substring to match in the title of the posts.
        content (str): Optional. A substring to match in the content of the posts.
        id (str or int): Optional. The ID of the post to search for.

    Returns:
        Response: A JSON list of matched posts, and status code 200 if matches are found.
                  A JSON error message with status code 404 if no matches are found.
    """
    title = request.args.get('title', '')
    content = request.args.get('content', '')
    post_id = request.args.get('id', '')
    post_id = int(post_id) if post_id.isdigit() else None

    matches = []
    for post in POSTS:
        if (title and title.lower() in post['title'].lower()) or \
           (content and content.lower() in post['content'].lower()) or \
           (post_id is not None and post['id'] == post_id):
            matches.append(post)

    if matches:
        return jsonify(matches), 200
    else:
        return jsonify({"error": "No match found"}), 404




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
