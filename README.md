# Blog Concept

**Blog Concept** is a simple Flask-based web application that allows users to create, view, and manage blog posts. It provides a lightweight platform to add posts, display them, and delete individual entries using a JSON file (`blog_posts.json`) to store data.

---

## Features

- **View Posts**: Displays all blog posts sorted by date (newest first).
- **Add Posts**: Create a new blog entry by filling out a form with title, author, content, and date.
- **Delete Posts**: Remove specific blog entries by their unique ID.

---

## Project Structure

   ```markdown
   blog_concept/
   ├── 📄 app.py
   ├── 📂 templates/
   │   ├── 📄 index.html
   │   ├── 📄 add.html
   ├── 📂 static/
   ├── 📂 data/
   │   └── 📄 blog_posts.json
   ├── 📄 requirements.txt
   ├── 📄 README.md
   ```

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/blog_concept.git
   cd blog_concept
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the data folder**:

   - Ensure the `data/` directory exists.
   - Create an empty `blog_posts.json` file within `data/`.
   - Initialize this file with an empty JSON array:

     ```json
     []
     ```

---

## Usage

1. **Run the Flask web server**:

   ```bash
   python app.py
   ```

   The server will be available at: `http://127.0.0.1:5001/`

2. **Access the application**:

   - Open your browser and navigate to:
     ```
     http://127.0.0.1:5001/
     ```

3. **Available features**:
   - **Home Page**: Displays all blog posts.
   - **Add Post**: Create a new blog entry via the `/add` route.
   - **Delete Post**: Remove blog entries using the delete functionality provided for each post.

---

## API Routes

### 1. **`GET /`**

- Displays all blog posts sorted in reverse chronological order.
- Reads data from `data/blog_posts.json`.

### 2. **`GET, POST /add`**

- Presents a form to create a new blog post.
- On submission (`POST`):
  - Generates a unique ID for the new post.
  - Adds the post (title, author, content, and date) to `blog_posts.json`.
  - Redirects back to the home page (`/`).

### 3. **`POST /delete/<post_id>`**

- Deletes a blog post via its unique ID.
- Updates `blog_posts.json` after deletion.
- Redirects to the home page or returns a `404` error if the post does not exist.

---

## Data Storage

The application uses a JSON file (`data/blog_posts.json`) to store blog entries. Data is stored in the following format:

```json
[
    {
        "id": "unique-id-1",
        "title": "Example Blog Post",
        "author": "Author Name",
        "content": "This is the content of the blog post...",
        "date": "YYYY-MM-DD"
    }
]
```

---

## Notes

- **Error Handling**:
  - Automatically initializes `blog_posts.json` with an empty list if it is missing or corrupted.
  - Handles invalid inputs/missing entries gracefully.
- **Sorting**: Blog posts are displayed in reverse chronological order (most recent first).
- **Uniqueness**: Each post is assigned a unique UUID (universally unique identifier).

---

## Future Improvements

Here are potential enhancements for the project:

- Improve UI/UX with advanced styling and responsive design.
- Add pagination to handle large datasets of blog posts.
- Implement a search or filter feature to navigate posts easily.
- Include an authentication system for admin controls.
- Transition to a database (e.g., SQLite or PostgreSQL) for more robust storage.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy building and managing your blog! 😊