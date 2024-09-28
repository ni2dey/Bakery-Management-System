import mysql.connector
import pandas as pd
"""mydb=mysql.connector.connect(host="localhost",user="root",passwd="H@rrY.20",database='bakery_data')
mycursor=mydb.cursor()
query="CREATE TABLE Bakery (customer_id INT NOT NULL AUTO_INCREMENT,name VARCHAR(20),order_type VARCHAR(20) NOT NULL,quantity INT,
price DECIMAL(10, 2),Constraint PK PRIMARY KEY(customer_id,order_type))"
mycursor.execute(query)"""

class Bakery:
    def __init__(self):

        self.mydb=mysql.connector.connect(host="localhost",user="root",passwd="H@rrY.20",database='bakery_data')
        if self.mydb:
            print("Database connection successful.")
        else:
            print("Database connection not successful.")

    def add_customer(self,name,order_type,quantity,price):
        if self.mydb is None:
            print("No connection to MySQL database.")
            return

        mycursor = self.mydb.cursor()
        sql="Insert into bakery (name,order_type,quantity,price) values (%s,%s,%s,%s)"
        mycursor.execute(sql,(name,order_type,quantity,price))
        self.mydb.commit()

    def delete(self,name,order):
        if self.mydb is None:
            print("No connection to MySQL database.")
            return

        mycursor = self.mydb.cursor()
        sql="Delete from bakery where name=%s and order_type=%s and price=%s"
        mycursor.execute(sql,(name,order[0],order[2]))
        self.mydb.commit()

    def display(self,name):

        mycursor = self.mydb.cursor()
        sql = "Select * from bakery where name=%s"
        mycursor.execute(sql,(name,))
        result=mycursor.fetchall()
        data=list(result)
        df =pd.DataFrame(data,columns=['id', 'name', 'order_type', 'quantity', 'total'])
        print(df)


if __name__=='__main__':

        order1=Bakery()
        print("............WELCOME TO TRIBENI BAKERY!!! Wanna have something sweet?...............................")
        list1={'Items':['fudge','lava cake','brownie','chocolate_pie','cup-cakes','apple_pie','choco_tart'],
                'Price':[60,55,45,70,30,60,100]}

        df=pd.DataFrame(list1)
        print("WE have:")
        print(df)
        print("For sweeth tooth like you:)")
        choice=input("Want to order something?(y/n)")
        order = []

        if choice=='y':
            print("please enter your name:")
            name=input()
            item=int(input("Enter the item no:"))
            if item<7:
                quantity=int(input("Enter quantity:"))
                total=quantity*list1['Price'][item]
                #print(f'{name}, Your total is :Rs {total}')
                order1.add_customer(name,list1['Items'][item],quantity,total)
                amount=total
                order.append([list1['Items'][item],quantity,total])
                print(f"Order:{len(order)} successfully placed.")
                print("Item added to your basket..")
            else:
                print("Invalid order no.")

            while(1):
                print("Would you like to add something or make any changes?(y/n)")
                choice=input()

                if choice=='y':
                    print("1.Add new order")
                    print("2.Delete existing order")
                    print("3.Show data")
                    ch=int(input())


                    #Add new order
                    if ch==1:
                        print(df)
                        item1=int(input("Enter item no :"))
                        if item1<7:
                            quantity1=int(input("Enter quantity:"))
                            total1=quantity1*list1['Price'][item1]
                            amount += total1
                            order1.add_customer(name, list1['Items'][item1], quantity1, total1)
                            order.append([list1['Items'][item1], quantity1, total1])
                            print(f"Order:{len(order)} successfully placed.")
                            print("Item added to your basket..")
                        else:
                            print("Invalid order no.")

                    #Delete existing order
                    elif ch==2:
                        print("Enter Order_no, you want to remove:")
                        item2 = int(input())
                        if len(order)!=0 and item2<=len(order):
                            order1.delete(name, order[item2 - 1])
                            amount = amount - order[item2 - 1][2]
                            order.pop(item2-1)
                            print("Successfully removed...")
                        else:
                            print("No order found.")

                    # show data
                    elif ch==3:
                        print("ACCESS TO ADMIN ONLY")
                        password=input("ENTER PASSWORD:")
                        if password=="mimi9804":
                            print("WELCOME ADMIN!!!")
                            print("Enter name of customer to see data:")
                            name1=input()
                            order1.display(name1)

                    else:
                        print("Invalid choice")

                elif choice=='n':
                    print("Your Items:")
                    for item in order:
                        print(f"{item[0]}----{item[1]}pieces-------total:{item[2]}")
                    print(f'Grand total is :Rs {amount}')
                    if amount>400:
                        print("You are eligible for 10% discount")
                        final_amount=amount*0.9
                        print(f'Amount you need to pay:{final_amount}')
                        print(f"You saved:Rs{amount-final_amount}")
                    print("...............................Visit us soon <3.................")
                    break
        else:
            print("...............................Thank you for visiting TRIBENI BAKERY:)................")











