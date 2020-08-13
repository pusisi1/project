from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
from firstapp.models import Korea #모델참고

html = urlopen("https://www.weather.go.kr/weather/forecast/timeseries.jsp")
soup = BeautifulSoup(html, "lxml") 
#날짜/시각/날씨/강수확률/강수량/기온/습도
def korea_data(request): #한국기상청 날짜
    #day/time/weather/RP/rain/temp/hum
    day=[]
    time=[]
    weather=[]
    RP=[]
    rain=[]
    temp=[]
    hum=[]
    
    table = soup.find("table", class_="forecastNew3")
    tr = table.tbody.tr #한국기상청 날짜
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
                    
    tr = tr.next_sibling.next_sibling #한국기상청 날씨
    for w in tr.children:
        if w.name == 'td' and len(w.contents) > 0:
            weather.append(w['title'])
            
    tr = tr.next_sibling.next_sibling  #한국기상청 강수확률
    for w in tr.children:
	    if w.name == 'td' and len(w.contents) > 0:
            RP.append(w.contents[0])
            
    tr = tr.next_sibling.next_sibling #한국기상청 강수량
    for w in tr.children:
	    if w.name == 'td' and len(w.contents) > 0:
		    num = int(w['colspan'])
		    for i in range(num):
                rain.append(contents[0].strip())
                
    tr = tr.next_sibling.next_sibling#최저 최고 기온안함
    tr = tr.next_sibling.next_sibling #한국기상청 기온
    for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		temp.append(contents[0].strip())
        
    tr = tr.next_sibling.next_sibling #풍향풍속 안함
    tr = tr.next_sibling.next_sibling #한국기상청 습도
    for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
	    hum.append(contents[0].strip())
        
    for a in range(0,len(day)+1):
        a=Korea(day=day[a],time=time[a],weather=weather[a],RP=RP[a],rain=rain[a],temp=temp[a],hum=hum[a])
        a.save()
        

#day/time/weather/RP/rain/temp/hum




