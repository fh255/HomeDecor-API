from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        # This setup method creates a user named 'fatema' to be
        # used in all the test cases within this class.
        User.objects.create_user(username='fatema', password='pass')

    def test_can_list_posts(self):
        # This test checks if the posts can be
        # listed correctly.
        # It creates a post and then makes a GET
        # request to the posts list endpoint.
        # The test passes if the response is 200 OK and
        # the data is returned as expected.
        fatema = User.objects.get(username='fatema')
        Post.objects.create(owner=fatema, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(response.data, len(response.data))

    def test_logged_in_user_can_create_post(self):
        # This test checks if a logged-in user can create a post.
        # It logs in as 'fatema' and sends a POST request to create a new post.
        # The test passes if the post is created
        # successfully and returns a 201 Created status.
        self.client.login(username='fatema', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        # This test checks if an unauthenticated user is
        # prevented from creating a post.
        # It sends a POST request without logging in.
        # The test passes if the response is 403 Forbidden,
        # indicating that the action is not allowed.
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        # This setup method creates two users and two posts,
        # one for each user, to be used in the following test cases.
        fatema = User.objects.create_user(username='fatema', password='pass')
        admin = User.objects.create_user(username='admin', password='pass')
        Post.objects.create(
            owner=fatema, title='a title', content='fatema content'
        )
        Post.objects.create(
            owner=brian, title='some other title', content='admin content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        # This test checks if a post can be retrieved using a valid ID.
        # It makes a GET request to the detail endpoint for a specific post ID.
        # The test passes if the correct post data is returned
        #  and the response status is 200 OK.
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        # This test checks if trying to retrieve a post
        # with an invalid ID returns a 404 Not Found status.
        # It makes a GET request to an endpoint with a non-existent post ID.
        # The test passes if the response status is 404 Not Found.
        response = self.client.get('/post/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        # This test checks if a user can update their own post.
        # It logs in as 'fatema', the owner of the first post,
        # and sends a PUT request to update the post.
        # The test passes if the post is updated successfully
        # and the response status is 200 OK.
        self.client.login(username='fatema', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        # This test checks if a user is prevented from
        # updating another user's post.
        # It logs in as 'fatema' and attempts to update
        # a post owned by 'brian'.
        # The test passes if the response status is 403 Forbidden,
        # indicating that the action is not allowed.
        self.client.login(username='fatema', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
