from bs4 import BeautifulSoup 
import requests 

source = requests.get('---add the link---').text

soup = BeautifulSoup(source, 'lxml') 

lists = soup.find_all('section', class_='oh lst_cl prd-card fww brs5 pr bg1 prd-card-mtpl')

for list in lists: 
    title = list.find('a', class_ ='prd-name').text
    location = list.find('span', class_ ='elps elps1').text
    dealer = list.find('a', class_ ='clr3 fs12 fwn rsrc').text
    try:
        price = list.find('span', class_ ='prc cp clr3 fwb fs18 prc cp').text
        dealer_link = list.find('a', class_='clr3 fs12 fwn rsrc')['href']
    except Exception as e:
        price = None
        dealer_link = None

    info = [title, price, location, dealer, dealer_link]
  

 