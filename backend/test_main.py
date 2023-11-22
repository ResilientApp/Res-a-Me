import unittest
from flask import Flask
from flask_jwt_extended import JWTManager
from main import app

class EditResumeTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret-key'
        self.app = app.test_client()
        self.jwt = JWTManager(app)

    def test_edit_resume_success(self):
        # Mocking the request data
        data = {
            'category': 'education',
            'details': 'Some details about education'
        }

        # Setting up the JWT token
        access_token = self.jwt.encode_token({'sub': 'user_id'})

        # Making a POST request to the edit_resume endpoint
        response = self.app.post('/edit', json=data, headers={'Authorization': f'Bearer {access_token}'})

        # Asserting the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'education updated successfully')

    def test_edit_resume_missing_category(self):
        # Mocking the request data without the category field
        data = {
            'details': 'Some details about education'
        }

        # Setting up the JWT token
        access_token = self.jwt.encode_token({'sub': 'user_id'})

        # Making a POST request to the edit_resume endpoint
        response = self.app.post('/edit', json=data, headers={'Authorization': f'Bearer {access_token}'})

        # Asserting the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Category is required')

    def test_edit_resume_file_not_found(self):
        # Mocking the request data
        data = {
            'category': 'experience',
            'details': 'Some details about experience'
        }

        # Setting up the JWT token
        access_token = self.jwt.encode_token({'sub': 'user_id'})

        # Making a POST request to the edit_resume endpoint
        response = self.app.post('/edit', json=data, headers={'Authorization': f'Bearer {access_token}'})

        # Asserting the response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'experience not found for user_id')

if __name__ == '__main__':
    unittest.main()