import mysql.connector 
import Webscrapper as ws

db = mysql.connector.connect(host='localhost', user='root', passwd='18225', database ='probiotics')

cursor = db.cursor() 

#cursor.execute("INSERT INTO Products (title, price, location, dealer, dealer_link) VALUES (%s, %s, %s, %s, %s)", (ws.title, ws.price, ws.location, ws.dealer, ws.dealer_link))

cursor.execute('SELECT * FROM products')

for x in cursor:
    print(x)