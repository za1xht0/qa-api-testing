#Автотесты для JSONPlaceholder API
# Запуск тестов: python -m pytest test_api.py -v (для проверки всех тестов)
# python -m pytest test_api.py -v -k "test_get_post_by_id" (для проверки конкретного теста)

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

#TC1 - get all posts
def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 100

#TC2 - get one post by ID
def test_get_post_by_id():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["id"] == post_id

#TC3 - get post negative
def test_get_post_negative():
    post_id = 9999  # Non-existent post ID
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 404

#TC4 - filter posts by userid
def test_filter_posts_by_userid():
    user_id = 1
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for post in response.json():
        assert post["userId"] == user_id

#TC5 - create new post
def test_create_new_post():
    new_post = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == new_post["title"]
    assert response.json()["body"] == new_post["body"]
    assert response.json()["userId"] == new_post["userId"]

#TC6 - create new post with nobody (bug: BUG1)
def test_create_new_post_nobody():
    new_post = {
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["userId"] == new_post["userId"]

#TC7 - Update post
def test_update_post():
    post_id = 1
    updated_post = {
        "title": "Updated Test Post",
        "body": "This is updated test post.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    assert response.status_code == 200
    assert response.json()["title"] == updated_post["title"]
    assert response.json()["body"] == updated_post["body"]
    assert response.json()["userId"] == updated_post["userId"]

#TC8 - update only title
def test_update_post_title_patch():
    post_id = 1
    updated_post = {
        "title": "Updated Test Post Title"
    }
    response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == updated_post["title"]

#TC9 - delete post
def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

#TC10 - get users list
def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 10

#TC11 - check email users
def test_check_email():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    for user in data:
        email = user["email"]
        assert "@" in email and "." in email.split("@")[-1]

# TC12 - create post is not persisted(Bug:BUG2)
def test_create_post_not_persisted():
    new_post = {"title": "Test", "body": "Test", "userId": 1}
    create_response = requests.post(f"{BASE_URL}/posts", json=new_post)
    new_id = create_response.json()["id"]
    get_response = requests.get(f"{BASE_URL}/posts/{new_id}")
    assert get_response.status_code == 404