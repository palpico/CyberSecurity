from django.http import JsonResponse
from cybersecurity.tema3.api.serializers import DaySerializer, SentimentSerializer, HashtagSerializer, \
    TempDay, TempSentiment, TempHashtag
import json
import requests
import pandas as pd


def extract(data_arg, what_arg, from_arg='pet'):
    info = []
    for d in data_arg.values():
        info.append([d[from_arg], d[what_arg]])
    df = pd.DataFrame(info, columns=[from_arg, what_arg])
    return df


def populate_day_model(arg_df, w_arg, f_arg):
    for pet in arg_df[f_arg].unique():
        counter = 0
        df = arg_df[arg_df.pet == pet]
        activity = df.pivot_table(index=[w_arg], aggfunc='size')
        for day in df[w_arg].unique():
            count = activity[day]
            if count > counter:
                counter = count
                model_day = TempDay(pet=str(pet), day=str(day), count=int(count))
                model_day.save()


def populate_sentiment_model(arg_df, w_arg, f_arg):
    for pet in arg_df[f_arg].unique():
        df = arg_df[arg_df.pet == pet]
        activity = df.pivot_table(index=[w_arg], aggfunc='size')
        for sent in df[w_arg].unique():
            count = activity[sent]
            model_sentiment = TempSentiment(pet=str(pet), sentiment=str(sent), count=int(count))
            model_sentiment.save()


def populate_hash_model(arg_df, w_arg, f_arg, num_arg):
    for pet in arg_df[f_arg].unique():
        df = arg_df[arg_df.pet == pet]
        all_hashtags = []
        for i in df[w_arg]:
            all_hashtags.extend([i for i in i.split() if i.startswith("#")])
        val_counts = pd.Series(all_hashtags).value_counts()[:num_arg]
        model_hashtag = TempHashtag(pet=str(pet), hashtag=val_counts.index.values)
        model_hashtag.save()


def populate_day():
    response = requests.get("https://twitter-dashboard-sentiment-default-rtdb.firebaseio.com/Pets.json")
    data = json.loads(response.content.decode(response.encoding))
    TempDay.objects.all().delete()
    populate_day_model(extract(data, 'day', 'pet'), 'day', 'pet')


def populate_sentiment():
    response = requests.get("https://twitter-dashboard-sentiment-default-rtdb.firebaseio.com/Pets.json")
    data = json.loads(response.content.decode(response.encoding))
    TempSentiment.objects.all().delete()
    populate_sentiment_model(extract(data, 'sentiment', 'pet'), 'sentiment', 'pet')


def populate_hashtag():
    response = requests.get("https://twitter-dashboard-sentiment-default-rtdb.firebaseio.com/Pets.json")
    data = json.loads(response.content.decode(response.encoding))
    TempHashtag.objects.all().delete()
    populate_hash_model(extract(data, 'clean_text', 'pet'), 'clean_text', 'pet', 5)


def day_list(request):
    populate_day()
    try:
        if request.method == 'GET':
            objects = TempDay.objects.all()
            serializer = DaySerializer(objects, many=True)
            return JsonResponse(serializer.data, safe=False)
    except TempDay.DoesNotExist:
        return JsonResponse([], safe=False)


def day_list_pet(request, pk):
    populate_day()
    try:
        if request.method == 'GET':
            objects = TempDay.objects.get(pet=str(pk))
            serializer = DaySerializer(objects)
            return JsonResponse(serializer.data, safe=False)
    except TempDay.DoesNotExist:
        return JsonResponse([], safe=False)


def positive_pet_all(request):
    populate_sentiment()
    try:
        if request.method == 'GET':
            objects = TempSentiment.objects.filter(sentiment="1")
            serializer = SentimentSerializer(objects, many=True)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def positive_pet(request, pk):
    populate_sentiment()
    try:
        if request.method == 'GET':
            objects = TempSentiment.objects.get(pet=str(pk), sentiment="1")
            serializer = SentimentSerializer(objects, many=False)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def negative_pet_all(request):
    populate_sentiment()
    try:
        if request.method == 'GET':
            objects = TempSentiment.objects.filter(sentiment="-1")
            serializer = SentimentSerializer(objects, many=True)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def negative_pet(request, pk):
    populate_sentiment()
    try:
        if request.method == 'GET':
            objects = TempSentiment.objects.get(pet=str(pk), sentiment="-1")
            serializer = SentimentSerializer(objects, many=False)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def neutral_pet_all(request):
    populate_sentiment()
    try:
        if request.method == 'GET':
            objects = TempSentiment.objects.filter(sentiment="0")
            serializer = SentimentSerializer(objects, many=True)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def neutral_pet(request, pk):
    populate_sentiment()
    try:
        if request.method == 'GET':
            objects = TempSentiment.objects.get(pet=str(pk), sentiment="0")
            serializer = SentimentSerializer(objects, many=False)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def hashtag_pet_all(request):
    populate_hashtag()
    try:
        if request.method == 'GET':
            objects = TempHashtag.objects.all()
            serializer = HashtagSerializer(objects, many=True)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)


def hashtag_pet(request, pk):
    populate_hashtag()
    try:
        if request.method == 'GET':
            objects = TempHashtag.objects.get(pet=str(pk))
            serializer = HashtagSerializer(objects, many=False)
            return JsonResponse(serializer.data, safe=False)
    except TempSentiment.DoesNotExist:
        return JsonResponse([], safe=False)
