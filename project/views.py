from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.models import User, Article, database_test, database_raintest, database_content


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
 name_list = Article.objects.order_by('id')
 context = {
        'name_list' : name_list
    }
 if request.method == 'POST':
    content = request.POST.get('content')
    try:
        email = request.session['email']
        # select * from user where email = ?
        user = User.objects.get(email=email)
        # insert into article (title, content, user_id) values (?, ?, ?)
        article = Article(content=content, user=user)
        article.save()
        return render(request, 'write_success.html')
    except:
        return render(request, 'write_fail.html')
 return render(request, 'text.html')

def movie(request):
    return render(request, 'movie.html')



def signup(request):
 # 실제 데이터베이스에 데이터를 저장(회원가입)   
 if request.method == 'POST':
    # 회원정보 저장
    email = request.POST.get('email')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    user = User(email=email, name=name, pwd=pwd)
    user.save()
    return HttpResponseRedirect('/main/')
# 화원가입을 위한 양식 전송

 return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
    # 회원정보 조회
     email = request.POST.get('email')
     pwd = request.POST.get('pwd')
     try:
    # select * from user where email=? and pwd=?
        user = User.objects.get(email=email, pwd=pwd)
        request.session['email'] = email
        return render(request, 'signin_success.html')
     except:
        return render(request, 'signin_fail.html')
    return render(request, 'signin.html')

def signout(request):
    del request.session['email'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return HttpResponseRedirect('/main/')
   
