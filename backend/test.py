import json
import requests
import os

def test_load_resume():
    url = 'http://localhost:3033/load/jack@gmail.com'
    headers = {'Content-Type': 'application/json'}
    data = {"category": "About"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print("Status code:", response.status_code)
    print("Response data:", response.text)

    data = response.json()

    assert response.status_code == 200
    assert 'message' not in data

def test_edit_resume():
    url = 'http://localhost:3033/edit/jack@gmail.com'
    headers = {'Content-Type': 'application/json'}
    data = {
        "category": "About",
        "name": "New Name",
        "title": "New Title",
        # Add more fields as necessary
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print("Status code:", response.status_code)
    print("Response data:", response.text)

    data = response.json()

    assert response.status_code == 200
    assert data['message'] == "About updated successfully"

def test_user_list():
    url = 'http://localhost:3033/userList'
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)

    print("Status code:", response.status_code)
    print("Response data:", response.text)

    data = response.json()

    assert response.status_code == 200
    assert 'user_list' in data

def test_update_resume():
    url = 'http://localhost:3033/updateResume'
    headers = {'Content-Type': 'application/json'}
    data = {"email": "jack@gmail.com"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print("Status code:", response.status_code)
    print("Response data:", response.text)

    data = response.json()

    assert response.status_code == 200
    assert data['message'] == "Files replaced successfully"

if __name__ == '__main__':
    # test_load_resume()
    # test_edit_resume()
    # test_search()
    # test_user_list()
    test_update_resume()