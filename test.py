import sys
import pyodbc
from faker import Faker
from random import randint
fake_data = Faker()
def bank_para(cust_num,acc_num):
	
	print("Hello! Welcome to the Banking project")
	conn_str = ("DRIVER={PostgreSQL Unicode(x64)};" "DATABASE=bank1db;" "UID=postgres;" "PWD=password;" "SERVER=192.168.99.100;" "PORT=5432;") #Connection to the database using pyodbc
	conn = pyodbc.connect(conn_str)
	print("You are successfully connected to the database")
	cur = conn.cursor() #Cursor declaration
	cur1 = conn.cursor()
	cur2 = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS Customer")
	cur.execute("CREATE TABLE Customer(Customer_Id INTEGER PRIMARY KEY, FName VARCHAR(100), LName VARCHAR(100) ,Address1 VARCHAR(100), City VARCHAR(50), State VARCHAR(50), Zipcode VARCHAR(50), time_stamp TIMESTAMP)")
	#Loading data into Customer table using Faker to generate random test data
	for i in range(cust_num): 
		cust_id = i
		fname = fake_data.first_name()
		lname = fake_data.last_name()
		add = fake_data.address()
		city = fake_data.city()
		state = fake_data.state()
		zip = fake_data.postcode()
		date = fake_data.date()
		cur.execute("INSERT INTO Customer(Customer_Id,FName,LName,Address1,City,State,Zipcode,time_stamp) VALUES (?,?,?,?,?,?,?,?)",(cust_id,fname,lname,add,city,state,zip,date))
#conn.commit()
	cur1.execute("DROP TABLE iF EXISTS Account")
	cur1.execute("CREATE TABLE Account(Account_Id INTEGER PRIMARY KEY,Cust_Id INTEGER REFERENCES Customer(Customer_Id), Balance FLOAT, timestamp TIMESTAMP)")
	#Creation of multiple accounts for the customers and loading data into Account table.
	cur.execute("SELECT * FROM Customer")
	rows = cur.fetchall()
	j = 1000
	for k in rows:
		print(k[0])
		for z in range(acc_num):
			acc_id = j
			bal = randint(1000,15000)
			time = fake_data.date()
			cur1.execute("INSERT INTO Account(Account_Id,Cust_Id,Balance,timestamp) VALUES (?,?,?,?)",(acc_id,k[0],bal,time))
			j += 1
	conn.commit()
	cur.close()
	cur1.close()
	print("Successful creation of tables into bank1db database...")
	print("Following are the SQL Queries")
	
# =============SQL QUERY (1)==========================
	print("Query 1")
	cur2.execute("select c.State, avg(a.Balance) from Customer c join Account a on c.Customer_Id = a.Cust_id Group By c.State Order By avg(a.Balance) DESC LIMIT 10")
	rows = cur2.fetchall()
	print(rows)	

# =============SQL QUERY (2)==========================
	print("Query 2")
	cur2.execute("select concat(c.fname,' ',c.lname) as Name , sum(a.balance) from customer c join account a on c.Customer_Id = a.Cust_Id group by Name order by sum(a.balance) DESC LIMIT 10")
	rows1 = cur2.fetchall()
	print(rows1)

# =============SQL QUERY (3)==========================
	print("Query 3")
	cur2.execute("select concat(c.fname,' ',c.lname) as Name , sum(a.balance) from customer c join account a on c.Customer_Id = a.Cust_Id group by Name order by sum(a.balance) ASC LIMIT 10")
	rows2 = cur2.fetchall()
	print(rows2)
	
#=============SQL QUERY(4)============================
	print("Query 4")
	cur2.execute("BEGIN;" )
	cur2.execute("WITH p AS(SELECT cust_id,balance FROM account ORDER BY balance ASC LIMIT 10) UPDATE account a SET balance = a.balance + (SELECT (SUM(k.balance)*10/100) FROM (SELECT balance FROM account ORDER BY balance DESC LIMIT 10) as k) FROM p WHERE a.cust_id = p.cust_id and p.balance = a.balance RETURNING a.*")
	cur2.execute("END;")
	print(cur2.rowcount)
	cur2.close()



if __name__== "__main__":
	bank_para(int(sys.argv[1]),int(sys.argv[2]))	