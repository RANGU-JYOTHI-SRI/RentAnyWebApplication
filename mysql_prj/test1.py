import mysql.connector
import pytest
db_conn = mysql.connector.connect(host="localhost",port="3307",user="root",
                                  password="root",database="olms")
cursor = db_conn.cursor()
class Order:
    def __init__(self,first_name,last_name,email,address,postal_code,city,paid):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.paid = paid
    def insert_record(self):
        try:
            sql = "insert into Orders(first_name,last_name,email,address,postal_code,city,paid) values(%s,%s,%s,%s,%s,%s,%s)"
            val = (self.first_name,self.last_name,self.email,self.address,self.postal_code,self.city,self.paid)
            cursor.execute(sql,val)
            db_conn.commit()
            return cursor.rowcount
        except Exception as e:
            print("Exception:",e)
        else:
            print("No Exception Raised")
first_name = input("Enter FirstName:")
last_name = input("Enter LastName:")
email = input("Enter email:")
address= input("Enter address:")
postal_code= input("Enter postalcode:")
city= input("Enter city:")
paid= input("Enter the amt paid:")

d = Order(first_name,last_name,email,address,postal_code,city,paid)
print("Record inserted sucessfully",d.insert_record())
def test_insert_record():
    assert d.insert_record() == 1