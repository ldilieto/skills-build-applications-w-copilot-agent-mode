import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Crea utenti di test
def create_users():
    users = []
    for i in range(5):
        user, _ = User.objects.get_or_create(
            username=f'user{i}',
            email=f'user{i}@example.com',
            defaults={
                'first_name': f'Nome{i}',
                'last_name': f'Cognome{i}',
            }
        )
        users.append(user)
    return users

# Crea team di test
def create_teams(users):
    team1 = Team.objects.create(name='Team Alpha', member_ids=[str(u.id) for u in users[:3]])
    team2 = Team.objects.create(name='Team Beta', member_ids=[str(u.id) for u in users[3:]])
    return [team1, team2]

# Crea attività di test
def create_activities(users):
    types = ['run', 'bike', 'swim']
    for user in users:
        for _ in range(2):
            Activity.objects.create(
                user_id=str(user.id),
                activity_type=random.choice(types),
                duration=random.randint(20, 60),
                calories=random.randint(100, 500)
            )

# Crea workout di test
def create_workouts(users):
    w1 = Workout.objects.create(name='Cardio Blast', description='Allenamento cardio intenso', suggested_for_ids=[str(u.id) for u in users[:2]])
    w2 = Workout.objects.create(name='Forza Base', description='Allenamento di forza per principianti', suggested_for_ids=[str(u.id) for u in users[2:]])
    return [w1, w2]

# Crea leaderboard di test
def create_leaderboard(users):
    for user in users:
        Leaderboard.objects.create(user_id=str(user.id), score=random.randint(0, 1000))

def main():
    users = create_users()
    create_teams(users)
    create_activities(users)
    create_workouts(users)
    create_leaderboard(users)
    print('Database popolato con dati di test!')

if __name__ == '__main__':
    main()
