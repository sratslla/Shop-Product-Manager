import mysql.connector
import os
import platform
import pandas as pd
billnumber=85326253
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="onlinebuy");
mycursor=mydb.cursor()
def onlinebuymenu():
    print("Welcome")
    print("1.Item Detail")
    print("2.Placing Order")
    print("3.Cancelling Order")
    print("4.Delivery Made")
    print("5.Display Order status")
    print("6.Quit")
    n=int(input("enter your choice in number:-"))
    if(n==1):
        itemdetail()
    elif(n==2):
        placingorder()
    elif(n==3):
        cancellingorder()
    elif(n==4):
        orderdelivered()
    elif(n==5):
        orderstatus()
    elif(n==6):
        exit(0)
    else:
        print("invalid option")


def itemdetail():
    print("Item Detail")
    ch='y'
    while(ch=='y'):
        l=[]
        itemname=input("enter item name:-")
        l.append(itemname)
        itemnumber=input("enter item number:-")
        l.append(itemnumber)
        rating=input("enter the rating:-")
        l.append(rating)
        cost=input("enter the price:-")
        l.append(cost)
        maxtimefordelivery=input("enter no of hours required for delivery:-")
        l.append(maxtimefordelivery)
        item=(l)
        sql="insert into items(itemname,itemnumber,rating,cost,maxtimefordelivery)values(%s,%s,%s,%s,%s)"
        mycursor.execute(sql,item)
        mydb.commit()
        print("INSERTION COMPLETE")
        print("do you want to insert more item details")
        ch=input("enter y/n")
        print('\n'*10)

        print("===============================================================")

def placingorder():
    global billnumber
    l1=[]
    customername=input("enter customer name:-")
    l1.append(customername)
    itemname=input("enter item name:-")
    l1.append(itemname)
    itemnumber=int(input("enter item number:-"))
    l1.append(itemnumber)
    quantity=int(input("enter no. of items:-"))
    l1.append(quantity)
    a=int(input("price of item:-"))
    amount=a*quantity
    print ("Total amount to be paid:-",amount)
    l1.append(amount)
    status='placed'
    l1.append(status)
    billnumber=billnumber+1
    print("your bill number is:-",billnumber)
    l1.append(billnumber)
    print("ORDER PLACED")
    order=(l1)
    sql="insert into customer(customername,itemname,itemnumber,quantity,amount,status,billnumber)values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,order)
    mydb.commit()
    print('\n'*10)

    print("================================================================================================================")

def cancellingorder():
    print("ORDER CANCELLING WINDOW")
    billnumber=input("enter billnumber:-")
    bill=(billnumber,)
    sql="update customer set status='cancelled' where billnumber=%s"
    mycursor.execute(sql,bill)
    mydb.commit()
    print("ORDER CANCELLED")
    print("Go back to menu")
    print('\n'*10)

    print("=================================================================================================================")

def orderdelivered():
    print("ORDER DELIVERY WINDOW")
    billnumber=input("enter billnumber:-")
    bill=(billnumber,)
    sql="update customer set status='delivered' where billnumber=%s"
    mycursor.execute(sql,bill)
    mydb.commit()
    print("ORDER DELIVERED")
    print("Go back to menu")
    print('\n'*10)

    print("=================================================================================================================")

def orderstatus():
    print("ORDER STATUS WINDOW")
    billnumber=input("enter billnumber:-")
    bill=(billnumber,)
    sql="select * from customer where billnumber=%s"
    mycursor.execute(sql,bill)
    res=mycursor.fetchall()
    mydb.commit()
    print("order status are as follow:-")
    print("(customername,itemname,itemnumber,quantity,amount,status,billnumber)")
    for x in res:
        print(x)
    print("Go back to menu")
    print('\n'*10)

    print("=================================================================================================================")

onlinebuymenu()
