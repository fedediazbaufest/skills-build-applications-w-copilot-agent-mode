from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class APITest(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_api_root(self):
		response = self.client.get(reverse('root'))
		self.assertEqual(response.status_code, 200)

	def test_users_endpoint(self):
		response = self.client.get('/api/users/')
		self.assertIn(response.status_code, [200, 403])

	def test_teams_endpoint(self):
		response = self.client.get('/api/teams/')
		self.assertIn(response.status_code, [200, 403])

	def test_activities_endpoint(self):
		response = self.client.get('/api/activities/')
		self.assertIn(response.status_code, [200, 403])

	def test_leaderboard_endpoint(self):
		response = self.client.get('/api/leaderboard/')
		self.assertIn(response.status_code, [200, 403])

	def test_workouts_endpoint(self):
		response = self.client.get('/api/workouts/')
		self.assertIn(response.status_code, [200, 403])
