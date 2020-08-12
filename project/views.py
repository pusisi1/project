from django.http import HttpResponse
from django.shortcuts import render
from database.models import database_test, database_raintest

# def main(request):
#     list = []
    
#     dict1 = {'data':1, 'temper1': 't1', 'temper2':'t2', 'rain':'rain11', 'wind':'wind22', 'raintype':'type2323'}
#     list.append(dict1)
#     dict2 = {'data':2, 'temper1': 't1', 'temper2':'t2', 'rain':'rain11', 'wind':'wind22', 'raintype':'type2323'}
#     list.append(dict2)
#     dict3 = {'data':3, 'temper1': 't1', 'temper2':'t2', 'rain':'rain11', 'wind':'wind22', 'raintype':'type2323'}
#     list.append(dict3)
#     dict4 = {'data':4, 'temper1': 't1', 'temper2':'t2', 'rain':'rain11', 'wind':'wind22', 'raintype':'type2323'}
#     list.append(dict4)
#     dict5 = {'data':5, 'temper1': 't1', 'temper2':'t2', 'rain':'rain11', 'wind':'wind22', 'raintype':'type2323'}
#     list.append(dict5)

#     return render(request, 'main.html', {'list':list})


def main(request):
# select * from article order by id desc
    article_list = database_test.objects.order_by('date')
    rain_list = database_raintest.objects.order_by('date')
    context = {
        'article_list' : article_list,
        'rain_list': rain_list
    }
    return render(request, 'main.html', context)

def sub(request):
    return render(request, 'sub.html')

def text(request):
    return render(request, 'text.html')
    
