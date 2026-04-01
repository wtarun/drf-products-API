# seed.py  —  run with: python manage.py shell < seed.py

from blog.models import Author, Post  # adjust 'blog' to your app name

# ── 1. Clean up existing data ──────────────────────────────────────────────────
Post.objects.all().delete()
Author.objects.all().delete()
print("Cleared existing data.")

# ── 2. Create Authors ──────────────────────────────────────────────────────────
authors_data = [
    {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "website": "https://alicejohnson.dev",
    },
    {
        "name": "Bob Martinez",
        "email": "bob@example.com",
        "website": "https://bobwrites.com",
    },
    {
        "name": "Clara Smith",
        "email": "clara@example.com",
        "website": "",
    },
]

authors = [Author.objects.create(**data) for data in authors_data]
print(f"Created {len(authors)} authors.")

# ── 3. Create Posts ────────────────────────────────────────────────────────────
posts_data = [
    {
        "title": "Getting Started with Django REST Framework",
        "body": (
            "Django REST Framework (DRF) is a powerful toolkit for building Web APIs. "
            "It provides serializers, viewsets, authentication, and much more out of the box. "
            "In this post we walk through setting up a basic DRF project from scratch, "
            "covering models, serializers, views, and URL routing."
        ),
        "author": authors[0],
        "is_published": True,
        "tags": ["django", "python", "api", "drf"],
    },
    {
        "title": "Understanding Serializers in DRF",
        "body": (
            "Serializers in DRF allow complex data such as querysets and model instances "
            "to be converted to native Python datatypes that can then be easily rendered "
            "into JSON or XML. They also provide deserialization, allowing parsed data "
            "to be converted back into complex types after validating the incoming data."
        ),
        "author": authors[0],
        "is_published": True,
        "tags": ["serializers", "drf", "django"],
    },
    {
        "title": "Django ORM Tips and Tricks",
        "body": (
            "The Django ORM is one of the most expressive query interfaces available in "
            "any web framework. This post covers select_related, prefetch_related, annotate, "
            "aggregate, and how to avoid common pitfalls like N+1 queries. "
            "Mastering the ORM will make your Django apps significantly faster."
        ),
        "author": authors[1],
        "is_published": True,
        "tags": ["django", "orm", "database", "python"],
    },
    {
        "title": "Building a REST API with Django",
        "body": (
            "REST APIs are the backbone of modern web applications. In this tutorial, "
            "we will build a fully functional REST API using Django and DRF. "
            "We will cover authentication using tokens, permission classes, "
            "pagination, filtering, and deployment considerations."
        ),
        "author": authors[1],
        "is_published": False,
        "tags": ["api", "rest", "django", "backend"],
    },
    {
        "title": "Python Decorators Explained",
        "body": (
            "Decorators are one of Python's most elegant features. They allow you to "
            "wrap a function to extend its behavior without permanently modifying it. "
            "In this post we explore how decorators work under the hood, build some "
            "from scratch, and look at real-world use cases like caching and logging."
        ),
        "author": authors[2],
        "is_published": True,
        "tags": ["python", "decorators", "advanced"],
    },
    {
        "title": "Introduction to Class-Based Views in Django",
        "body": (
            "Class-based views (CBVs) provide an object-oriented way to define views in Django. "
            "They promote code reuse through mixins and inheritance. This post compares "
            "function-based views with class-based views, and walks through the most "
            "commonly used generic CBVs like ListView, DetailView, and CreateView."
        ),
        "author": authors[2],
        "is_published": False,
        "tags": ["django", "views", "cbv", "python"],
    },
]

posts = [Post.objects.create(**data) for data in posts_data]
print(f"Created {len(posts)} posts.")

# ── 4. Summary ─────────────────────────────────────────────────────────────────
print("\n── Seed complete ──")
for author in Author.objects.all():
    post_count = author.posts.count()
    print(f"  {author.name} ({author.email}) — {post_count} post(s)")