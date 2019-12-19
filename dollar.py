import bs4
import requests 
#https://finance.naver.com/marketindex/ 이 주소를 통해
#환율이 얼마인지 가져오는 프로그램을 작성해 주세요!

html = requests.get('https://finance.naver.com/marketindex/')

#exchangeList > li.on > a.head.usd > div > span.value
soup = bs4.BeautifulSoup(html.text,'html.parser')

dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(dollar.text)
