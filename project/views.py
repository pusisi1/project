from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from database.models import User, Article, database_test, database_raintest, database_content
from urllib.request import urlopen
from bs4 import BeautifulSoup
from database.models import KOREA
from database.models import NORWAY
from database.models import BBC #모델참고

##------------------------BBC------------------------------------------

def bbc_data():
    html_BBC = urlopen("https://www.bbc.com/weather/1846986")
    soup_BBC = BeautifulSoup(html_BBC, "html.parser") 
    table_BBC= soup_BBC.find("div", class_="wr-time-slot-list__item--time-slots") #가져올 테이블

#시간/온도/강수확률/날씨
    time=[]
    temp=[]
    RP=[]
    weather=[]
#time/temp/RP/weather/

#시간
    tds = table_BBC.select('div span[class=wr-time-slot-primary__time]')
    for t in tds:
        time.append(t.get_text())
#온도
    tds = table_BBC.select('div span[class=wr-value--temperature--c]')
    for t in tds:
        temp.append(t.get_text())
#강수확률
    tds = table_BBC.select('div div[class=wr-u-font-weight-500]')
    for t in tds:
        RP.append(t.find(text=True))
#날씨
    tds = table_BBC.select('span.wr-time-slot-secondary__weather-type-text')
    for t in tds:
        weather.append(t.get_text())
#time/temp/RP/weather/   
    for a in range(0,len(time)):
        a=bbc(time=time[a],temp=temp[a],RP=RP[a],weather=weather[a])
        a.save()
        


##------------------------NORWAY------------------------------------------


def norway_data():
    html_NORWAY = urlopen("https://www.yr.no/place/South_Korea/North_Gyeongsang/Andong/hour_by_hour.html")  
    soup_NORWAY = BeautifulSoup(html_NORWAY, "html.parser") 
    table_NORWAY = soup_NORWAY.find("table", class_="yr-table-hourly") #가져올 테이블
#시간/날씨/온도/강수량/바람
    time=[]
    weather=[]
    temp=[]
    rain=[]
    
#time/weather/temp/RP/wind  
    tds = table_NORWAY.select('tbody td[scope=row]')
    for t in tds:
        time.append(t.get_text())#시간
    tds = table_NORWAY.select('tbody figcaption[class=yr-visually-hidden]')
    for t in tds:
        weather.append(t.get_text()) #날씨

    tds = table_NORWAY.select('tbody td.temperature')
    for t in tds:
        temp.append(t.get_text())#온도
    tds = table_NORWAY.select('tbody td.precipitation')
    for t in tds:
        rain.append(t.get_text())#강수량
    tds = table_NORWAY.select('tbody td.txt-left')
    
    for a in range(0,len(time)):
        a=NORWAY(time=time[a],weather=weather[a],temp=temp[a],rain=rain[a])
        a.save()
        
      

##------------------------KOREA----------------------------------------------


#날짜/시각/날씨/강수확률/강수량/기온/습도
def korea_data(): #한국기상청 날짜
    html_KOREA = urlopen("https://www.weather.go.kr/weather/forecast/timeseries.jsp")
    soup_KOREA = BeautifulSoup(html_KOREA, "lxml") 
    #day/time/weather/RP/rain/temp/hum
    day=[]
    time=[]
    weather=[]
    RP=[]
    rain=[]
    temp=[]
    hum=[]
    
    table_KOREA = soup_KOREA.find("table", class_="forecastNew3")
    tr = table_KOREA.tbody.tr #한국기상청 날짜
    for t in tr.children:
        if t.name == 'th':
            if t['scope'] == 'colgroup':
                num = int(t['colspan'])
                for i in range(num):
                    day.append(t.get_text())
                    
    #Korea.objects.all()
    tr = tr.next_sibling.next_sibling  #한국기상청 시각
    for t in tr.children:
        if t.name == 'td':
            for i in t.contents:
                if i.name =='p':
                    time.append(i.get_text())
    time=time[:len(day)]  
    tr = tr.next_sibling.next_sibling #한국기상청 날씨
    for w in tr.children:
        if w.name == 'td' and len(w.contents) > 0:
            weather.append(w['title'])

    
    tr = tr.next_sibling.next_sibling  #한국기상청 강수확률
    for w in tr.children:
        if w.name == 'td' and len(w.contents) > 0:
            RP.append(w.contents[0])
            
    tr = tr.next_sibling.next_sibling #한국기상청 강수량  -
    for w in tr.children:
        if w.name == 'td' and len(w.contents) > 0:
            num = int(w['colspan'])
            for i in range(num):
                rain.append(w.contents[0].strip())
                
    
    tr = tr.next_sibling.next_sibling#최저 최고 기온안함
    tr = tr.next_sibling.next_sibling #한국기상청 기온   -
    for w in tr.children:
	    if w.name == 'td' and len(w.contents) > 0:
		    temp.append(w.contents[0].get_text())
    temp=temp[:len(day)]     
    tr = tr.next_sibling.next_sibling #풍향풍속 안함
    tr = tr.next_sibling.next_sibling #한국기상청 습도
    for w in tr.children:
	    if w.name == 'td' and len(w.contents) > 0:
	        hum.append(w.contents[0].get_text())
    hum=hum[:len(day)]    
    for a in range(0,len(day)):
        a=Korea(day=day[a],time=time[a],weather=weather[a],RP=RP[a],rain=rain[a],temp=temp[a],hum=hum[a])
        a.save()
        

#day/time/weather/RP/rain/temp/hum




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
#  select * from article order by id desc
    article_list = KOREA.objects.order_by('id')
    
    context = {
        'article_list' : article_list,
        
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
 return render(request, 'text.html',context)

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


def korea(request):
    article_list = KOREA.objects.order_by('id')
    
    context = {
        'article_list' : article_list,
        
    }
    return render(request, 'korea.html',context)

def norway(request):
    article_list = NORWAY.objects.order_by('id')
    
    context = {
        'article_list' : article_list,
        
    }
    return render(request, 'norway.html',context)

def bbc(request):
    article_list = BBC.objects.order_by('id')
    
    context = {
        'article_list' : article_list,
        
    }
    return render(request, 'bbc.html',context)
   
