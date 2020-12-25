from . import models
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ('id','userId', 'title', 'body')
        fields = '__all__'
        model = models.postId


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ('id','postId', 'name', 'email', 'body')
        fields = '__all__'
        model = models.Comments