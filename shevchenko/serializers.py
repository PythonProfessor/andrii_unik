from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Schools, ArtPeriod, ArtWay, ArtList, LiteratureList, Collection, PoetViews, Genre


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',
                  'notes']


class LiteratureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiteratureList
        fields = ['name',
                  'date_of_writing',
                  'genre',
                  'art_way',
                  'art_period',
                  'collection',
                  'notes']


class ArtListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtList
        fields = ['name',
                  'date_of_writing',
                  'genre',
                  'art_way',
                  'art_period',
                  'notes']


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = [
            "school_name",
            "start_learning_date",
            "end_learning_date",
            "notes"
        ]


class ArtWaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWay
