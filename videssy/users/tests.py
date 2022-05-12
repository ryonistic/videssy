from django.contrib.auth import authenticate, get_user_model, login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.test import RequestFactory, TestCase

from users.models import UserFollowing
from .views import subscribe 

User = get_user_model()

class SubscriptionTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', first_name='Jacob', last_name='Lenner', email='jacob_lenner123@gmail.com', password='top_secret')
        print('successfully created user, now subscribing to channel')
        user = authenticate(username=self.user.username, password=self.user.password)
        if user is not None:
            login(self.request, user)
            print(f'logged in the user {user}')
        else:
            return 'Error logging in'

    def test_details(self):
        # Create an instance of a GET request.
        request = self.client.get(f'http://127.0.0.1:8000/users/channel/{self.user.username}/')
        self.assertEqual(request.status_code, 302)
        print('successful get request on channel for jacob')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test subscribe() as if it were deployed at channel/username
        response = subscribe(request, 'jacob')
        self.assertEqual(response.status_code, 302)
        try:
            connection = UserFollowing.objects.get(user=get_object_or_404(User, username=request.user.username), following_user=request.user)
        except ObjectDoesNotExist:
            connection = None
        if connection is None:
            print('connection does not exist')
        else:
            print(f'connection exists as {connection}')
