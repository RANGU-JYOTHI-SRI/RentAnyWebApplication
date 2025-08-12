
import mysql.connector
import pytest
db_conn = mysql.connector.connect(host="localhost",port="3307",user="root",
                                  password="root",database="olms")
cursor = db_conn.cursor()
class user:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def insert_record(self):
        try:
            sql = "insert into userRegistration(username,email,password) values(%s,%s,%s)"
            val = (self.username, self.email, self.password)
            cursor.execute(sql,val)
            db_conn.commit()
            return cursor.rowcount
        except Exception as e:
            print("Exception:",e)
        else:
            print("No Exception Raised")
username = input("Enter  username:")
email = input("Enter Email ID:")
password = input("Enter password:")

r=user(username,email,password)

print("Record inserted sucessfully",r.insert_record())
def test_insert_record():
    assert r.insert_record() == 1
