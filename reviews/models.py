from django.db import models
from users.models import User
from comments.models import Comment

class ReviewManager(models.Manager):
    def validate_review(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be 2 or more characters."
        if len(postData['content']) < 5:
            errors['content'] = "Content needs to be 5 or more characters."
        return errors


class Review(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
