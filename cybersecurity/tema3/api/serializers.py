from rest_framework import serializers

from django.db.models import Model, CharField, PositiveIntegerField, TextField


class TempDay(Model):
    pet = CharField(max_length=125)
    day = CharField(max_length=125)
    count = PositiveIntegerField()


class TempSentiment(Model):
    pet = CharField(max_length=125)
    sentiment = CharField(max_length=125)
    count = PositiveIntegerField()


class TempHashtag(Model):
    pet = CharField(max_length=125)
    hashtag = TextField()


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TempDay
        fields = ['pet', 'day', 'count']


class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempSentiment
        fields = ['pet', 'sentiment', 'count']


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHashtag
        fields = ['pet', 'hashtag']
