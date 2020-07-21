import mysql.connector

mydb1=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='gg'
    )
mycursor=mydb1.cursor()
def add:
    sql = "SELECT INTO company(name,password ) VALUES (%s, %s)"
    val = ("ganga", "ganga")
    mycursor.execute(sql, val)
    mydb1.commit()
