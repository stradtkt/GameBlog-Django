from django.db import models

class CommentManager(models.Manager):
    def validate_category(self, postData):
            errors = {}
            if len(postData['title']) < 2:
                errors['title'] = "Title needs to be 2 or more characters."
            if len(postData['body']) < 5:
                errors['body'] = "Comment needs to be 5 or more characters."
            return errors

class Comment(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
