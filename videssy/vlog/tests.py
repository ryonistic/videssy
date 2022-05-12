from django.contrib.auth import authenticate, get_user_model, login
from django.test import TestCase

from vlog.models import Video

User = get_user_model()

class GetPages(TestCase):
    def testGet(self):
        self.user = User.objects.create_user(
            username='jacob', first_name='Jacob', last_name='Lenner', email='jacob_lenner123@gmail.com', password='top_secret')
        print('successfully created user, now proceeding...')
        user = authenticate(username=self.user.username, password=self.user.password)
        if user is not None:
            login(self.request, user)
            print(f'logged in the user {user}')
        else:
            return 'Error logging in'
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)
        print('Home page reachable')

        request = self.client.get('/liked_videos/')
        self.assertEqual(request.status_code, 200)
        print('liked videos page reachable')
