from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

##------------------------BBC------------------------------------------
html_BBC = urlopen("https://www.bbc.com/weather/1846986")
soup_BBC = BeautifulSoup(html_BBC, "html.parser") 

table_BBC= soup_BBC.find("div", class_="wr-time-slot-list__item--time-slots") #가져올 테이블
def BBC_data(request):
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
    for a in range(0,len(time)+1):
        a=BBC(time=time[a],temp=temp[a],RP=RP[a],weather=weather[a])
        a.save()
        


##------------------------NORWAY------------------------------------------

html_NORWAY = urlopen("https://www.yr.no/place/South_Korea/North_Gyeongsang/Andong/hour_by_hour.html")  

soup_NORWAY = BeautifulSoup(html_NORWAY, "html.parser") 



table_NORWAY = soup_NORWAY.find("table", class_="yr-table-hourly") #가져올 테이블
def NORWAY_data(request):
#시간/날씨/온도/강수량/바람
    time=[]
    weather=[]
    temp=[]
    RP=[]
    wind=[]
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
        RP.append(t.get_text())#강수량
    tds = table_NORWAY.select('tbody td.txt-left')
    for t in tds:
        wind.append(t.get_text())#풍향/풍속
        
    for a in range(0,len(time)+1):
        a=NORWAY(time=time[a],weather=weather[a],temp=temp[a],RP=RP[a],wind=wind[a])
        a.save()
        
      

##------------------------KOREA----------------------------------------------


html_KOREA = urlopen("https://www.weather.go.kr/weather/forecast/timeseries.jsp")
soup_KOREA = BeautifulSoup(html_KOREA, "lxml") 
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
    
    table_KOREA = soup.find("table", class_="forecastNew3")
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






