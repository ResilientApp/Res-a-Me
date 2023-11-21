import json
import requests
import os

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
def test_search():
    # Directory containing the JSON files
    directory = 'resumes'

    # List to store the partial content
    partial_content = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Open the file
            with open(os.path.join(directory, filename), 'r') as f:
                # Load the JSON data
                data = json.load(f)
                # Extract the "name" and "title" fields
                partial_data = {key: data.get(key, None) for key in ['name', 'title']}
                # Add the partial data to the list
                partial_content.append(partial_data)

    # Print the partial content
    for item in partial_content:
        print(item)

if __name__ == '__main__':
    test_load_resume()
    test_edit_resume()
    # test_search()