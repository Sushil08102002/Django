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


'''The above process is of serialization process in which an Objct Data firstly get converted into python
datatype and then converted into JSON (readable form) This process is called as Serialization or we can say that 
pickling'''

#now from here we start deserialization of our data

import io
from rest_framework.parsers import JSONParser

stream=io.BytesIO(json)
data=JSONParser().parse(stream)          #  this convert json data into python native datatypes

print("coverted data into dicitionary:",data)

serializer=CommentSerializer(data=data)
print(serializer.is_valid(),serializer.validated_data)
