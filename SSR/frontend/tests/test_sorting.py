import pytest
from web.blog_concept.SSR.backend.backend_app import app, POSTS

@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_sort_by_title_asc(client):
    """Test sorting by title in ascending order."""
    response = client.get('/api/posts?sort=title')
    assert response.status_code == 200
    sorted_titles = [post["title"] for post in response.get_json()]
    expected_titles = sorted([post["title"] for post in POSTS], key=str.lower)
    assert sorted_titles == expected_titles


def test_sort_by_title_desc(client):
    """Test sorting by title in descending order."""
    response = client.get('/api/posts?sort=title&direction=desc')
    assert response.status_code == 200
    sorted_titles = [post["title"] for post in response.get_json()]
    expected_titles = sorted([post["title"] for post in POSTS], key=str.lower, reverse=True)
    assert sorted_titles == expected_titles


def test_sort_by_content_asc(client):
    """Test sorting by content in ascending order."""
    response = client.get('/api/posts?sort=content')
    assert response.status_code == 200
    sorted_content = [post["content"] for post in response.get_json()]
    expected_content = sorted([post["content"] for post in POSTS], key=str.lower)
    assert sorted_content == expected_content


def test_sort_by_content_desc(client):
    """Test sorting by content in descending order."""
    response = client.get('/api/posts?sort=content&direction=desc')
    assert response.status_code == 200
    sorted_content = [post["content"] for post in response.get_json()]
    expected_content = sorted([post["content"] for post in POSTS], key=str.lower, reverse=True)
    assert sorted_content == expected_content