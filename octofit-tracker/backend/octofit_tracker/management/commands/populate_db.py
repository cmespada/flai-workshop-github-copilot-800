from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Populating the octofit_db database with test data...')
        
        # Get MongoDB database connection
        db = connection.get_database()
        
        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        
        self.stdout.write('Cleared existing data from all collections')
        
        # Create Teams
        teams_data = [
            {
                '_id': 1,
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes',
                'created_at': '2024-01-01T00:00:00Z'
            },
            {
                '_id': 2,
                'name': 'Team DC',
                'description': 'Justice League United',
                'created_at': '2024-01-01T00:00:00Z'
            }
        ]
        db.teams.insert_many(teams_data)
        self.stdout.write(f'Created {len(teams_data)} teams')
        
        # Create Users
        users_data = [
            {
                '_id': 1,
                'username': 'thor',
                'name': 'Thor Odinson',
                'email': 'thor@asgard.com',
                'team_id': 1,
                'created_at': '2024-01-01T00:00:00Z'
            },
            {
                '_id': 2,
                'username': 'ironman',
                'name': 'Tony Stark',
                'email': 'tony@starkindustries.com',
                'team_id': 1,
                'created_at': '2024-01-01T00:00:00Z'
            },
            {
                '_id': 3,
                'username': 'captainamerica',
                'name': 'Steve Rogers',
                'email': 'steve@avengers.com',
                'team_id': 1,
                'created_at': '2024-01-01T00:00:00Z'
            },
            {
                '_id': 4,
                'username': 'batman',
                'name': 'Bruce Wayne',
                'email': 'bruce@wayneenterprises.com',
                'team_id': 2,
                'created_at': '2024-01-01T00:00:00Z'
            },
            {
                '_id': 5,
                'username': 'superman',
                'name': 'Clark Kent',
                'email': 'clark@dailyplanet.com',
                'team_id': 2,
                'created_at': '2024-01-01T00:00:00Z'
            },
            {
                '_id': 6,
                'username': 'wonderwoman',
                'name': 'Diana Prince',
                'email': 'diana@themyscira.com',
                'team_id': 2,
                'created_at': '2024-01-01T00:00:00Z'
            }
        ]
        db.users.insert_many(users_data)
        self.stdout.write(f'Created {len(users_data)} users')
        
        # Create Activities
        activities_data = [
            {
                '_id': 1,
                'user_id': 1,
                'activity_type': 'Hammer Lifting',
                'duration_minutes': 60,
                'calories_burned': 500,
                'distance_km': 0,
                'date': '2024-02-01T09:00:00Z'
            },
            {
                '_id': 2,
                'user_id': 2,
                'activity_type': 'Flying',
                'duration_minutes': 45,
                'calories_burned': 450,
                'distance_km': 25.0,
                'date': '2024-02-01T10:00:00Z'
            },
            {
                '_id': 3,
                'user_id': 3,
                'activity_type': 'Running',
                'duration_minutes': 30,
                'calories_burned': 300,
                'distance_km': 5.0,
                'date': '2024-02-01T07:00:00Z'
            },
            {
                '_id': 4,
                'user_id': 4,
                'activity_type': 'Combat Training',
                'duration_minutes': 90,
                'calories_burned': 700,
                'distance_km': 0,
                'date': '2024-02-01T20:00:00Z'
            },
            {
                '_id': 5,
                'user_id': 5,
                'activity_type': 'Flying',
                'duration_minutes': 40,
                'calories_burned': 400,
                'distance_km': 30.0,
                'date': '2024-02-01T11:00:00Z'
            },
            {
                '_id': 6,
                'user_id': 6,
                'activity_type': 'Sword Training',
                'duration_minutes': 60,
                'calories_burned': 550,
                'distance_km': 0,
                'date': '2024-02-01T08:00:00Z'
            }
        ]
        db.activities.insert_many(activities_data)
        self.stdout.write(f'Created {len(activities_data)} activities')
        
        # Create Leaderboard entries
        leaderboard_data = [
            {
                '_id': 1,
                'user_id': 4,
                'username': 'batman',
                'team_id': 2,
                'total_calories': 700,
                'total_distance_km': 0,
                'total_activities': 1,
                'rank': 1
            },
            {
                '_id': 2,
                'user_id': 6,
                'username': 'wonderwoman',
                'team_id': 2,
                'total_calories': 550,
                'total_distance_km': 0,
                'total_activities': 1,
                'rank': 2
            },
            {
                '_id': 3,
                'user_id': 1,
                'username': 'thor',
                'team_id': 1,
                'total_calories': 500,
                'total_distance_km': 0,
                'total_activities': 1,
                'rank': 3
            },
            {
                '_id': 4,
                'user_id': 2,
                'username': 'ironman',
                'team_id': 1,
                'total_calories': 450,
                'total_distance_km': 25.0,
                'total_activities': 1,
                'rank': 4
            },
            {
                '_id': 5,
                'user_id': 5,
                'username': 'superman',
                'team_id': 2,
                'total_calories': 400,
                'total_distance_km': 30.0,
                'total_activities': 1,
                'rank': 5
            },
            {
                '_id': 6,
                'user_id': 3,
                'username': 'captainamerica',
                'team_id': 1,
                'total_calories': 300,
                'total_distance_km': 5.0,
                'total_activities': 1,
                'rank': 6
            }
        ]
        db.leaderboard.insert_many(leaderboard_data)
        self.stdout.write(f'Created {len(leaderboard_data)} leaderboard entries')
        
        # Create Workouts
        workouts_data = [
            {
                '_id': 1,
                'name': 'Asgardian Strength Training',
                'description': 'Build god-like strength',
                'difficulty': 'Advanced',
                'duration_minutes': 60,
                'exercises': ['Hammer Curls', 'Lightning Squats', 'Thunder Presses']
            },
            {
                '_id': 2,
                'name': 'Superhero Cardio',
                'description': 'Improve speed and endurance',
                'difficulty': 'Intermediate',
                'duration_minutes': 45,
                'exercises': ['Speed Running', 'High Jumps', 'Agility Drills']
            },
            {
                '_id': 3,
                'name': 'Combat Ready',
                'description': 'Full body martial arts workout',
                'difficulty': 'Advanced',
                'duration_minutes': 90,
                'exercises': ['Kata Practice', 'Sparring', 'Weapon Training']
            },
            {
                '_id': 4,
                'name': 'Beginner Hero Training',
                'description': 'Start your hero journey',
                'difficulty': 'Beginner',
                'duration_minutes': 30,
                'exercises': ['Basic Stretches', 'Light Cardio', 'Core Work']
            }
        ]
        db.workouts.insert_many(workouts_data)
        self.stdout.write(f'Created {len(workouts_data)} workouts')
        
        # Create unique index on email field
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write('Created unique index on user email field')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db database with test data!'))
        self.stdout.write(f'Total records created:')
        self.stdout.write(f'  - Teams: {db.teams.count_documents({})}')
        self.stdout.write(f'  - Users: {db.users.count_documents({})}')
        self.stdout.write(f'  - Activities: {db.activities.count_documents({})}')
        self.stdout.write(f'  - Leaderboard: {db.leaderboard.count_documents({})}')
        self.stdout.write(f'  - Workouts: {db.workouts.count_documents({})}')
