from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data using Django ORM
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create unique index on email field for users collection
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fighting for fitness!'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='The Justice League of Wellness!'
        )

        # Create Marvel superheroes
        self.stdout.write('Creating Marvel superheroes...')
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'tony.stark@avengers.com'},
            {'name': 'Captain America', 'email': 'steve.rogers@avengers.com'},
            {'name': 'Thor', 'email': 'thor.odinson@asgard.com'},
            {'name': 'Black Widow', 'email': 'natasha.romanoff@shield.gov'},
            {'name': 'Hulk', 'email': 'bruce.banner@avengers.com'},
            {'name': 'Spider-Man', 'email': 'peter.parker@dailybugle.com'},
        ]

        # Create DC superheroes
        self.stdout.write('Creating DC superheroes...')
        dc_heroes = [
            {'name': 'Superman', 'email': 'clark.kent@dailyplanet.com'},
            {'name': 'Batman', 'email': 'bruce.wayne@waynetech.com'},
            {'name': 'Wonder Woman', 'email': 'diana.prince@themyscira.com'},
            {'name': 'Flash', 'email': 'barry.allen@starlabs.com'},
            {'name': 'Aquaman', 'email': 'arthur.curry@atlantis.com'},
            {'name': 'Green Lantern', 'email': 'hal.jordan@greenlantern.com'},
        ]

        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team_id=str(team_marvel._id)
            )
            marvel_users.append(user)

        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team_id=str(team_dc._id)
            )
            dc_users.append(user)

        all_users = marvel_users + dc_users

        # Create activities for each user
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing']
        
        for user in all_users:
            # Create 3-7 activities per user
            num_activities = random.randint(3, 7)
            for i in range(num_activities):
                days_ago = random.randint(1, 30)
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 15)
                distance = round(random.uniform(2.0, 20.0), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories,
                    distance=distance,
                    date=datetime.now() - timedelta(days=days_ago)
                )

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in all_users:
            # Calculate total points based on activities
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_points = sum(activity.calories for activity in user_activities)
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                team_id=user.team_id,
                total_points=total_points
            )

        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_points')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Super Soldier Strength Training',
                'description': 'Build strength like Captain America with this intense resistance workout',
                'difficulty': 'hard',
                'duration': 60,
                'category': 'Strength'
            },
            {
                'name': 'Web-Slinger Agility Flow',
                'description': 'Improve your agility and reflexes like Spider-Man',
                'difficulty': 'medium',
                'duration': 45,
                'category': 'Agility'
            },
            {
                'name': 'Asgardian Warrior HIIT',
                'description': 'High-intensity training worthy of Thor himself',
                'difficulty': 'hard',
                'duration': 40,
                'category': 'HIIT'
            },
            {
                'name': 'Black Widow Combat Conditioning',
                'description': 'Martial arts inspired workout for total body conditioning',
                'difficulty': 'medium',
                'duration': 50,
                'category': 'Combat'
            },
            {
                'name': 'Speed Force Cardio Blast',
                'description': 'Lightning-fast cardio workout inspired by The Flash',
                'difficulty': 'hard',
                'duration': 35,
                'category': 'Cardio'
            },
            {
                'name': 'Kryptonian Power Lifting',
                'description': 'Build superhuman strength with this powerlifting routine',
                'difficulty': 'hard',
                'duration': 70,
                'category': 'Strength'
            },
            {
                'name': 'Amazonian Warrior Yoga',
                'description': 'Find balance and flexibility like Wonder Woman',
                'difficulty': 'easy',
                'duration': 30,
                'category': 'Flexibility'
            },
            {
                'name': 'Bat-Training Core Workout',
                'description': 'Master core strength with Batman\'s training regimen',
                'difficulty': 'medium',
                'duration': 40,
                'category': 'Core'
            },
            {
                'name': 'Atlantean Swimming Endurance',
                'description': 'Build aquatic endurance like Aquaman',
                'difficulty': 'medium',
                'duration': 55,
                'category': 'Swimming'
            },
            {
                'name': 'Arc Reactor Recovery Stretch',
                'description': 'Recovery and mobility work for active heroes',
                'difficulty': 'easy',
                'duration': 25,
                'category': 'Recovery'
            },
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'Users created: {User.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('\n✓ Test data successfully populated!'))
