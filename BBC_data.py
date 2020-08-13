from urllib.request import urlopen
from bs4 import BeautifulSoup
from firstapp.models import BBC #모델참고

html = urlopen("https://www.bbc.com/weather/1846986")

soup = BeautifulSoup(html, "html.parser") 


table = soup.find("div", class_="wr-time-slot-list__item--time-slots") #가져올 테이블
def bbc_data(request):
#시간/온도/강수확률/날씨
    time=[]
    temp=[]
    RP=[]
    weather=[]
#time/temp/RP/weather/

#시간
    tds = table.select('div span[class=wr-time-slot-primary__time]')
    for t in tds:
        time.append(t.get_text())
#온도
    tds = table.select('div span[class=wr-value--temperature--c]')
    for t in tds:
        temp.append(t.get_text())
#강수확률
    tds = table.select('div div[class=wr-u-font-weight-500]')
    for t in tds:
        RP.append(t.find(text=True))
#날씨
    tds = table.select('span.wr-time-slot-secondary__weather-type-text')
    for t in tds:
        weather.append(t.get_text())
#time/temp/RP/weather/   
    for a in range(0,len(time)+1):
        a=BBC(time=time[a],temp=temp[a],RP=RP[a],weather=weather[a])
        a.save()