from django.test import TestCase
from blog.models import Category, Comment, Post

# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        new_category = Category(name="Hobbies")
        new_category.save()
        new_post = Post(title="Cycling Journey: Changi towards the City", body="Quite an amazing experience riding such a long distance")
        new_post.save()
        new_post.categories.add(new_category)
        new_post.save()

    def test_post_valid_comment(self):
        selected_post = Post.objects.get(title="Cycling Journey: Changi towards the City")
        new_comment = Comment(author="QA_Tester", body="Very insightful", post=selected_post)
        new_comment.save()
        latest_comment = Comment.objects.latest("created_on")
        assert new_comment.body == latest_comment.body