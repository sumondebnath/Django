
from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news_api.models import Article, Journalist

    # Use ModelSerializer

class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

    def get_time_since_publication(self, object):
        publication_data = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_data, now)
        return time_delta


class JournalistSerializer(serializers.ModelSerializer):

    # articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="articles_details")

    class Meta:
        model = Journalist
        fields = "__all__"



    # Use Serializer

class Article_serializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    location = serializers.CharField()
    body = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.location = validated_data.get("location", instance.location)
        instance.body = validated_data.get("body", instance.body)
        instance.publication_date = validated_data.get("publication_date", instance.publication_date)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance

        # Object level Validation
    def validate(self, data):
        """
        https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and Description Does Not Same!")
        return data
    
        # Field level Validation
    def validate_title(self, value):
        """
        https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
        """

        if len(value) < 50:
            raise serializers.ValidationError("Title has at least more then 50 Characters!")
        return value