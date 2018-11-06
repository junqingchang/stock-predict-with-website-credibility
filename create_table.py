#!/usr/bin/python3

from  mysql.connector import connection

cnx = connection.MySQLConnection(user="admin", password='password',
                                 host='127.0.0.1', database='stockPredict')


mytable = '''CREATE TABLE stocks (Site  varchar(50),
                                 Author varchar(30),
				 Title  varchar(90),
                                 Text text,
                                 StartDate date,
                                 EndDate  date)'''

cursor = cnx.cursor()

cursor.execute(mytable)

cursor.close()
cnx.close()

