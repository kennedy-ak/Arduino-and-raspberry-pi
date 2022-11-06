import time
import datetime
import MySQLdb
import mysql.connector

def DB():
    conn=mysql.connector.connect(host ="localhost", user ="lux", password= "lux", database = "LuxReportDB")
    my_cursor = conn.cursor()

    sql =" INSERT INTO LuxReport(license_ID,driver_name,timer) VALUES(%s,%s,%s)"

    val=(5555, "KojoB", datetime.datetime.now())

    my_cursor.execute(sql, val)

    conn.commit()
    print(my_cursor.rowcount,"Record Inserted")

    sql1="SELECT* FROM LuxReport"

    my_cursor.execute(sql1)

    print(my_cursor.fetchall())
    
DB();