import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_contact_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_content(self):
        response = self.app.get('/contact')
        self.assertIn(b'Get in Touch', response.data)
        self.assertIn(b'Connect With Us', response.data)

    def test_contact_page_email(self):
        response = self.app.get('/contact')
        self.assertIn(b'contact@courseexplainer.com', response.data)

    def test_contact_nav_link(self):
        response = self.app.get('/')
        self.assertIn(b'/contact', response.data)

if __name__ == '__main__':
    unittest.main()