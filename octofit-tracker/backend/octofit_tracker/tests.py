from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test suite for User model"""

    def test_create_user(self):
        """Test creating a new user"""
        user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")


class TeamModelTest(TestCase):
    """Test suite for Team model"""

    def test_create_team(self):
        """Test creating a new team"""
        team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
        self.assertEqual(team.name, "Test Team")
        self.assertEqual(team.description, "A test team")


class ActivityModelTest(TestCase):
    """Test suite for Activity model"""

    def test_create_activity(self):
        """Test creating a new activity"""
        activity = Activity.objects.create(
            user_id="user123",
            activity_type="running",
            duration=30,
            calories=300,
            distance=5.0,
            date=datetime.now()
        )
        self.assertEqual(activity.activity_type, "running")
        self.assertEqual(activity.duration, 30)


class LeaderboardModelTest(TestCase):
    """Test suite for Leaderboard model"""

    def test_create_leaderboard_entry(self):
        """Test creating a leaderboard entry"""
        entry = Leaderboard.objects.create(
            user_id="user123",
            team_id="team123",
            total_points=1000,
            rank=1
        )
        self.assertEqual(entry.total_points, 1000)
        self.assertEqual(entry.rank, 1)


class WorkoutModelTest(TestCase):
    """Test suite for Workout model"""

    def test_create_workout(self):
        """Test creating a new workout"""
        workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            difficulty="medium",
            duration=45,
            category="cardio"
        )
        self.assertEqual(workout.name, "Morning Run")
        self.assertEqual(workout.difficulty, "medium")


class UserAPITest(APITestCase):
    """Test suite for User API endpoints"""

    def test_get_users_list(self):
        """Test retrieving list of users"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITest(APITestCase):
    """Test suite for Team API endpoints"""

    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test suite for Activity API endpoints"""

    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test suite for Leaderboard API endpoints"""

    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test suite for Workout API endpoints"""

    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
