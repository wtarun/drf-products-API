from rest_framework import serializers
from .models import Author, Post

# --- serializers.py ---
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'website')

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)         # Nested serializer
    author_id = serializers.IntegerField(write_only=True)  # Write-only for creating
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
    is_published = serializers.BooleanField(default=False)
    tags = serializers.ListField(                     # ListField for JSON arrays
        child=serializers.CharField(), required=False
    )
    word_count = serializers.SerializerMethodField()  # Computed field

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'author',       # read  — returns nested author object
            'author_id',    # write — accepts author pk when creating
            'created_at',
            'is_published',
            'tags',
            'word_count',
        )

    def get_word_count(self, obj):
        return len(obj.body.split())

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters.")
        return value