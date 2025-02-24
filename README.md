# Blog Concept

**Blog Concept** is a Flask-based web application that allows users to create, view, and manage blog posts. It provides a modern platform to add, display, edit, and delete blog entries, with posts stored as JSON data (`blog_posts.json`). The application features an enhanced UI/UX for a better user experience.

---

## Features

- **View Posts**: Displays all blog posts sorted by date (newest first) with an elegant and responsive design.
- **Sort by Date**: Automatically sorts blog posts in reverse chronological order to show the most recent entries first.
- **Add Posts**: Create a new blog entry via a form with fields for title, author, content, and date.
- **Edit Posts**: Update existing blog posts to correct or modify their content.
- **Delete Posts**: Remove specific blog entries by their unique ID.

---

## Project Structure

```plaintext
blog_concept/
├── 📄 app.py
├── 📂 templates/
│   ├── 📄 index.html   # Home page, lists all blog posts
│   ├── 📄 add.html     # Create new blog post
│   ├── 📄 update.html  # Edit existing blog post
├── 📂 static/          # Static assets like CSS, images, etc.
│   └── 📄 style.css    # Styles for the app
├── 📂 data/
│   └── 📄 blog_posts.json  # JSON file for post storage
├── 📄 requirements.txt  # Required Python packages
├── 📄 README.md         # Project documentation
```

---

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/blog_concept.git
   cd blog_concept
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the data folder**:

   - Ensure the `data/` directory exists.
   - Create an empty `blog_posts.json` file within `data/`.
   - Initialize it with an empty JSON array:

     ```json
     []
     ```

---

## Usage

1. **Run the Flask web server**:

   ```bash
   python app.py
   ```

   The server will run at: `http://127.0.0.1:5001/`

2. **Access the application**:
   - Open your browser and go to:
     ```
     http://127.0.0.1:5001/
     ```

3. **Available features**:
   - **Home Page**: Displays a list of all blog posts, sorted by date with the latest posts first.
   - **Add Post**: Create a new blog entry using the `/add` route.
   - **Edit Post**: Update existing posts via the `/update/<post_id>` route.
   - **Delete Post**: Remove unwanted blog entries.

---

## API Routes

### 1. **`GET /`**

- Displays all blog posts sorted in reverse chronological order.
- Reads posts from `data/blog_posts.json`.

### 2. **`GET, POST /add`**

- Presents a form for creating a new blog post.
- On `POST` submission:
  - A new post is added to `blog_posts.json` with a unique ID, title, author, content, and date.
  - Redirects to the home page (`/`).

### 3. **`GET, POST /update/<post_id>`**

- Displays a form pre-filled with the data of the blog post identified by `post_id`.
- On `POST` submission:
  - Updates the blog post in `blog_posts.json`.
  - Redirects to the home page (`/`).

### 4. **`POST /delete/<post_id>`**

- Deletes the blog post with the specified `post_id`.
- Updates `blog_posts.json` and redirects to the home page.

---

## Data Storage

The application stores blog posts in a JSON file (`data/blog_posts.json`), with each post having the following structure:

```json
[
    {
        "id": "unique-id-1",
        "title": "Example Blog Post",
        "author": "Author Name",
        "content": "This is the content of the blog post.",
        "date": "YYYY-MM-DD HH:MM"
    }
]
```

### Sorting
- Posts are automatically sorted by `date` in descending order (newest first) using proper date parsing (`datetime.strptime`).

---

## Design and UI/UX

The application features:
- A **modern design** for blog posts with gradients, hover effects, rounded corners, and responsive layouts.
- **Enhanced interaction**, including visual effects for buttons and posts.
- **Responsive design** to ensure usability on both desktop and mobile devices.

### Example Features
1. Posts are designed with hover effects and shadowing to enhance interactivity.
2. Buttons include hover effects with smooth color transitions.
3. Input forms are styled for ease of use with clear visual feedback.

---

## Notes

- **Error Handling**:
  - Automatically initializes an empty `blog_posts.json` file if the file is missing or corrupted.
  - Handles invalid inputs (e.g., missing `date` or empty fields) gracefully.
- **JSON Validation**: Ensures all posts include `id`, `title`, `author`, `content`, and `date`.

---

## Future Improvements

Possible enhancements to this project include:
- Improving support for large datasets by adding **pagination**.
- Adding a **search and filter feature** to locate specific posts easily.
- Replacing the JSON file storage with a more robust **database** (e.g., SQLite or PostgreSQL).
- Introducing **user authentication** for creating and managing posts.
- Adding an **API layer** for external integrations.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy creating and managing your blog! 😊