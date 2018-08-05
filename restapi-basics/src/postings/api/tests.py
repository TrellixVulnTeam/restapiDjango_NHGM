from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from postings.models import BlogPost

User = get_user_model()

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User.objects.create(username='testcfeuser', email='test@test.com')
        user_obj.set_password("somerandompassword")
        user_obj.save()
        blog_posts = BlogPost.objects.create(user=user_obj, title='New title', content='some content')
		
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)
		
		
		
		
		
		
		
		