#!/usr/bin/python3

from  mysql.connector import connection
import datetime
import csv
import glob
import os
import pdb

cnx = connection.MySQLConnection(user="admin", password='password',
                                 host='localhost', database='stockPredict')



insert_stock = ( "INSERT INTO stocks "
                 "(Site, Author, Title, Text, StartDate, EndDate)"
                 "VALUES( %s, %s, %s, %s, %s, %s, %s, %s)" )

cursor = cnx.cursor()
fcount = 0

for pathname in glob.glob('Stocks/*.txt'):

    fcount += 1
    if count > 20: break  # for testing, we try 20 files 

    print("Processing", pathname)

    #name is first part of filename, this get stored into the record
    filename = os.path.basename(pathname) #1st get filename exclude directory
    name = filename.split('.')[0]

    with open(pathname, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sdate, openval, high, low, close, volume, openint = row
            if sdate == 'Date': 
                continue # skip the file column heading line
            datecols = sdate.split('-') # split the date into year, mon, day
            yr, mon, day = map(int, datecols) # convert yr, mon, day to integers
            data_stock = (name, datetime.date(yr, mon, day), openval,
                          high, low, close, volume, openint)

            cursor.execute(insert_stock, data_stock)
    cnx.commit()
cursor.close()
cnx.close()
