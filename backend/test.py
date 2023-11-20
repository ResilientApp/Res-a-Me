import json
import requests

def test_load_resume():
    response = requests.get('http://localhost:3033/load/userjack123')

    print("Status code:", response.status_code)
    print("Response data:", response.text)

    data = response.json()

    assert response.status_code == 200
    assert 'message' not in data  # assuming the JSON file doesn't contain 'message' key

def test_edit_resume():
    url = 'http://localhost:3033/edit/userjack123'
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": "Jack Chen",
        "email": "jack@gmail.com",
        "title": "Senior Full-stack engineer in Amazon",
        "education": "Master's of Computer Science in UCD"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print("Status code:", response.status_code)
    print("Response data:", response.text)

    data = response.json()

    assert response.status_code == 200
    assert data['message'] == "Resume updated successfully"

if __name__ == '__main__':
    test_load_resume()
    test_edit_resume()