from django.db import models

# Create your models here.

# =============================================================
# EXAMPLE 1 — Blog Post
# Covers: CharField, EmailField, URLField, DateTimeField,
#          BooleanField, SerializerMethodField
# =============================================================

# --- models.py ---
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    tags = models.JSONField(default=list)  # e.g. ["django", "python"]

    def __str__(self):
        return self.title
