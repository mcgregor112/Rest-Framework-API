from django.db import models

class snipated(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class comment(models.Model):
    snippet = models.ForeignKey(snipated, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)