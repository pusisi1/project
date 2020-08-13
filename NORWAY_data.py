from urllib.request import urlopen
from bs4 import BeautifulSoup
from firstapp.models import NORWAY #모델참고

html = urlopen("https://www.yr.no/place/South_Korea/North_Gyeongsang/Andong/hour_by_hour.html")  

soup = BeautifulSoup(html, "html.parser") 



table = soup.find("table", class_="yr-table-hourly") #가져올 테이블
def NORWAY_data(request):
#시간/날씨/온도/강수량/바람
    time=[]
    weather=[]
    temp=[]
    RP=[]
    wind=[]
#time/weather/temp/RP/wind  
    tds = table.select('tbody td[scope=row]')
    for t in tds:
        time.append(t.get_text())#시간
    tds = table.select('tbody figcaption[class=yr-visually-hidden]')
    for t in tds:
        weather.append(t.get_text()) #날씨

    tds = table.select('tbody td.temperature')
    for t in tds:
        temp.append(t.get_text())#온도
    tds = table.select('tbody td.precipitation')
    for t in tds:
        RP.append(t.get_text())#강수량
    tds = table.select('tbody td.txt-left')
    for t in tds:
        wind.append(t.get_text())#풍향/풍속
        
    for a in range(0,len(time)+1):
        a=NORWAY(time=time[a],weather=weather[a],temp=temp[a],RP=RP[a],wind=wind[a])
        a.save()