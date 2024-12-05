from django.test import TestCase
from django.urls import reverse
from .models import BlogPost, Comment

class BlogTestCase(TestCase):
    def setUp(self):
        
        self.post = BlogPost.objects.create(
            title="Test Article",
            content="Ceci est un article de test."
        )
        
        self.comment = Comment.objects.create(
            post=self.post,
            author="Test User",
            text="Ceci est un commentaire de test."
        )

    def test_edit_comment_view(self):
        
        response = self.client.get(reverse('edit_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Modifier le commentaire")

    def test_edit_comment_post(self):
        
        new_comment_data = {
            'text': 'Commentaire modifié',
            'author': 'Test User',
        }
        response = self.client.post(reverse('edit_comment', args=[self.comment.id]), new_comment_data)
        self.assertEqual(response.status_code, 302)  
        self.comment.refresh_from_db()  
        self.assertEqual(self.comment.text, 'Commentaire modifié')

    def test_edit_comment_cancel(self):
        
        response = self.client.get(reverse('edit_comment', args=[self.comment.id]))
        self.assertContains(response, 'Annuler')
