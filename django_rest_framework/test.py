from datetime import datetime
import os
import django
from rest_framework import serializers

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_framework.settings')
django.setup()

# This is a simple object used to reprsent a model data
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

# Create a Comment instance
comment = Comment(email="sushillodhi671@gmail.com", content="foo bar")
print("Comment created at:", comment.created)



# Here we define commment serializer to serialize a data 
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

# Serialize the Comment instance
serializer = CommentSerializer(comment)
print("Serialized data:", serializer.data)

from rest_framework.renderers import JSONRenderer
json=JSONRenderer().render(serializer.data)
print("json data:",json)