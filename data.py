from threading import Thread
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='banking',password='root',db='' )
a = conn.cursor()
sql="SELECT * FROM `admin'"
a.execute(sql)
countrow=a.execute(sql)

print ("this is",countrow)
data=a.fetchone()
print(data)
