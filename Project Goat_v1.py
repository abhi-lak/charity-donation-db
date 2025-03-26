# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:44:49 2023

@author: Lenovo
"""

import mysql.connector

mydb=mysql.connector.connect(user='root',
                             passwd='root',
                             host='localhost',
                             auth_plugin='mysql_native_password'    ,
                             database='cdms')
mycursor=mydb.cursor(buffered=True)


def create_Donation():
    try:
        mycursor.execute('create table Donation(D_ID varchar(5) primary key,Name char(40),Age int,occupation varchar(40),Income int,Contact_No varchar(40),Gmail varchar(40),Date_of_donation date,City varchar(40),Country varchar(40),Money_Donated int,Blood_Donated varchar(10))')
        print("Table created")
        Donator()
    except:
        print("Table exists")
        Donator()
    
def create_Receiver():
 try:
     mycursor.execute('create table Receiver(R_ID varchar(5) primary key,Name char(40),Age int,occupation varchar(40),Income int,Contact_No varchar(40),Gmail varchar(40),Date_of_Reception date,City varchar(40),Country varchar(40),Money_Received int,Blood_Received varchar(10))')
     print("Table created")
     Receiver()
 except:
     print("Table exists")
     Receiver() 

def delrec():
    a=input("Enter RID to be deleted : ")
    b=input("Are you sure you want to delete : ")
    if b=="y" or b=="yes":
        cmd="delete from receiver where R_ID='" + a + "' "
        mycursor.execute(cmd)
        mydb.commit()
        print("Data Deleted succesfully.....")
    else:
        print("Data not deleted")
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Receiver()
    elif e=="e":
        print("BYE BYE") 
    
    
   
def updaterec():
    a=input("Enter RID to be Updated")
    f=True
    while f==True:
        print('''(1) Name
              \n(2) Age
              \n(3) Occupation
              \n(4) Income
              \n(5) Contact no
              \n(6) Gmail
              \n(7) Date_of_Reception
              \n(8) City
              \n(9) Country
              \n(10) Money Received
              \n(11) Blood Received''')
        change=int(input("Which of the above field do you want to change"))
        if change==1:
            b=input("Enter new name : ")
            c=b.capitalize()
            cmd="update Receiver set name='" + c +"' where R_ID='" + a + "' "        
        elif change==2:
            b=input("Enter new Age : ")
            c=str(b)
            cmd="update Receiver set age='" + c +"' where R_ID='" + a + "' "         
        elif change==3:
            b=input("Enter new occupation : ")
            c=b.capitalize()
            cmd="update Receiver set occupation='" + c +"' where R_ID='" + a + "' "
        elif change==4:
            b=int(input("Enter new income : "))
            c=str(b)
            cmd="update Receiver set income='" + str(b) +"' where R_ID='" + a + "' "
        elif change==5:
            b=str(input("Enter new contact no : "))
            c=str(b)
            cmd="update Receiver set contact_no='" + b +"' where R_ID='" + a + "' "
        elif change==6:
            b=input("Enter new Gmail : ")
            c=b.capitalize()
            cmd="update Receiver Gmail='" + c +"' where R_ID='" + a + "' set "
        elif change==7:
            b=input("Enter new Date in yyyy-mm-dd : ")
            cmd="update Receiver set Date_of_Reception='" + b +"' where R_ID='" + a + "'"
        elif change==8:
            b=input("Enter new City : ")
            c=b.capitalize()
            cmd="update Receiver set City='" + c +"' where R_ID='" + a + "' "
        elif change==9:
            b=input("Enter new Country : ")
            c=b.capitalize()
            cmd="update Receiver set Country='" + c +"' where R_ID='" + a + "' "
        elif change==10:
            b=int(input("Enter new Money Received : "))
            c=str(b)
            cmd="update Receiver set money_Received='" + c +"' where R_ID='" + a + "' "
        elif change==11:
            b=input("Enter new blood Received : ")
            c=b.capitalize()
            cmd="update Receiver set blood_Received='" + c +"' where R_ID='" + a + "' "
        mycursor.execute(cmd)
        mydb.commit()
        print("Data Updated successfully....")
        n=input("Want to change anything else :")
        if n=='y':
            f==True
        else:
            break
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Receiver()
    elif e=="e":
        print("BYE BYE")
   
    
           
def searchrec():
    
    a=input("Enter Name to be searched : ")
    try:
      cmd="select * from Receiver where name like '" + a + "%'"
      mycursor.execute(cmd)
      f="%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s"
      print(f%("RID","Name","Age","Occupation","Income","Contact","Gmail","date_of_Reception","City","Country","money","blood"))      
      print("*"*236)
      for i in mycursor:
          for j in i:
               print("%15s" % j,end=" ")
          print()    
      print("*"*236)
    except:
        print("Record does not exists")
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Receiver()
    elif e=="e":
        print("BYE BYE") 
    
      
def Displayrec():
    print('''(1) Sorted as per RID
(2) Sorted as per Name
(3) Sorted as per age
(4) Sorted Date of Reception
(5) Sorted Money donated
(6) Sorted Blood donated''')
    ch=int(input("Enter option : "))
    if ch==1:
        cmd="select* from Receiver order by R_ID;"
    elif ch==2:
        cmd="select* from Receiver order by Name;"
    elif ch==3:
        cmd="select* from Receiver order by age;"
    elif ch==4:
        cmd="select* from Receiver order by Date_of_Reception;"
    elif ch==5:
        cmd="select* from Receiver order by money_Received;"
    elif ch==6:   
        cmd="select* from Receiver order by blood_Received;"
    else:
         print("Wrong input try again")
         Displayrec()
    mycursor.execute(cmd)
    f="%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s"
    print(f%("RID","Name","Age","Occupation","Income","Contact","Gmail","Date_of_Reception","City","Country","money","blood"))      
    print("*"*188)
    for i in mycursor:
        for j in i:
             print("%15s" % j,end=" ")
        print()    
    print("*"*188)
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Receiver()
    elif e=="e":
        print("BYE BYE") 
   
    

def Insertrec():
    Rec=[]
    while True:
        RID =str(generateid ("Receiver"))
        print("Id generated : ", RID )
        Rname=input("Enter your full Name : ")
        Rage=int(input("Enter your Age : "))
        Roccupation=input("Enter your occupation : ")
        Rincome=int(input("Enter your income : "))
        Rcontact=str(input("Enter your contact no : "))
        Rgmail=input("Enter your Gmail ID : ")
        Rdor=input("Enter date in YYYY-MM-DD : ")
        Rcity=input("Enter your city : ")
        Rcountry=input("Enter your country : ")
        print("\n(1) Money\n")
        print("\n(2) Blood\n")
        print("\n(3) Both\n")
        option3=int(input("Enter option: "))
        if option3==1:
            Rmoney=str(input("Enter the amount Received : "))
            Rblood="null"
        elif option3==2:
            Rmoney="null"
            Rblood=input("Enter the blood group Received : ")
        elif  option3==3:
            Rmoney=str(input("Enter the amount Received : "))
            Rblood=input("Enter the blood group Received : ")
        else:
            print("Error wrong input!!!")
            word=input("Press y for choosing again or Enter any key to quit ")
            if word=="y"and"Y":
                Insertrec()
            else:
                print("Bye Bye")
        a=Rname.capitalize()
        b=Roccupation.capitalize()
        c=Rgmail.capitalize()
        d=Rcity.capitalize()
        e=Rcountry.capitalize()
        if Rblood=="null":
            Rec=[RID,a,Rage,b,Rincome,Rcontact,c,Rdor,d,e,Rmoney]
            cmd="insert into Receiver values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL)"
        elif Rmoney=="null":
            Rec=[RID,a,Rage,b,Rincome,Rcontact,c,Rdor,d,e,Rblood]
            cmd="insert into Receiver values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,%s)"
        else:
            Rec=[RID,a,Rage,b,Rincome,Rcontact,c,Rdor,d,e,Rmoney,Rblood]
            cmd="insert into Receiver values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
        mycursor.execute(cmd,Rec)
        mydb.commit()
        print("Data added succesfuly....")
        ch=input("more records : ")
        if ch=='n' or ch=='N':
            break;
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Receiver()
    elif e=="e":
        print("BYE BYE") 
       
def Receiver():
    print("*"*183)
    print("\t\t\t\t\t\t\tRECEIVER   MENU\n")
    print("*"*183)
    print("\n(1) Insert Data\n")
    print("(2) Read Data\n")
    print("(3) Search Data \n")
    print("(4) Update Data\n")    
    print("(5) delete Data\n")
    print("(6) Go back\n")
    option2=int(input("Enter option : "))
    if option2==1:
       Insertrec()
    elif option2==2:
        Displayrec()
    elif option2==3:
        searchrec()
    elif option2==4:
        updaterec()
    elif option2==5:
        delrec()  
    elif option2==6:
        menu()
    else:
        print("Error wrong input!!!")
        word=input("Press y for choosing again or Enter any key to quit : ")
        if word=="y"and"Y":
            Receiver()
        else:
            print("Bye Bye")

#Donation

def deldon():
    a=input("Enter DID to be deleted : ")
    b=input("Are you sure you want to delete DID : ")
    if b=="y" or b=="yes":
        cmd="delete from donation where D_ID='" + a + "' "
        mycursor.execute(cmd)
        mydb.commit()
        print("Data Deleted succesfully.....")
    else:
        print("Data not deleted")
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Donator()
    elif e=="e":
        print("BYE BYE") 

   
def updatedon(): 
    a=input("Enter DID to be Updated")
    f=True
    while f==True:
        print('''(1) Name
              \n(2) Age
              \n(3) Occupation
              \n(4) Income
              \n(5) Contact no
              \n(6) Gmail
              \n(7) Date_of_donation
              \n(8) City
              \n(9) Country
              \n(10) Money donated
              \n(11) Blood donated''')
        change=int(input("Which of the above field do you want to change"))
        if change==1:
            b=input("Enter new name : ")
            c=b.capitalize()
            cmd="update donation set name='" + c +"' where D_ID='" + a + "' "        
        elif change==2:
            b=input("Enter new Age : ")
            c=str(b)
            cmd="update donation set age='" + c +"' where D_ID='" + a + "' "         
        elif change==3:
            b=input("Enter new occupation : ")
            c=b.capitalize()
            cmd="update donation set occupation='" + c +"' where D_ID='" + a + "' "
        elif change==4:
            b=int(input("Enter new income : "))
            c=str(b)
            cmd="update donation set income='" + str(b) +"' where D_ID='" + a + "' "
        elif change==5:
            b=str(input("Enter new contact no : "))
            c=str(b)
            cmd="update donation set contact_no='" + b +"' where D_ID='" + a + "' "
        elif change==6:
            b=input("Enter new Gmail : ")
            c=b.capitalize()
            cmd="update donation Gmail='" + c +"' where D_ID='" + a + "' set "
        elif change==7:
            b=input("Enter new Date in yyyy-mm-dd : ")
            cmd="update donation set Date_of_donation='" + b +"' where D_ID='" + a + "'"
        elif change==8:
            b=input("Enter new City : ")
            c=b.capitalize()
            cmd="update donation set City='" + c +"' where D_ID='" + a + "' "
        elif change==9:
            b=input("Enter new Country : ")
            c=b.capitalize()
            cmd="update donation set Country='" + c +"' where D_ID='" + a + "' "
        elif change==10:
            b=int(input("Enter new Money donated : "))
            c=str(b)
            cmd="update donation set money_donated='" + c +"' where D_ID='" + a + "' "
        elif change==11:
            b=input("Enter new blood donated : ")
            c=b.capitalize()
            cmd="update donation set blood_donated='" + c +"' where D_ID='" + a + "' "
        mycursor.execute(cmd)
        mydb.commit()
        print("Data Updated successfully....")
        n=input("Want to change anything else :")
        if n=='y':
            f==True
        else:
            break
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Donator()
    elif e=="e":
        print("BYE BYE")     
def searchdon():
    
    a=input("Enter Name to be searched : ")
    try:
      cmd="select * from donation where name like '" + a + "%'"
      mycursor.execute(cmd)
      f="%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s"
      print(f%("DID","Name","Age","Occupation","Income","Contact","Gmail","date_of_donation","City","Country","money","blood"))      
      print("*"*200)
      for i in mycursor:
          for j in i:
               print("%15s" % j,end=" ")
          print()    
      print("*"*200)
    except:
        print("record does not exists")
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Donator()
    elif e=="e":
        print("BYE BYE") 
      
       
def Displaydon():
    print('''(1) Sorted as per DID
(2) Sorted as per Name
(3) Sorted as per age
(4) Sorted Date of donation
(5) Sorted Money donated
(6) Sorted Blood donated''')
    ch=int(input("Enter option : "))
    if ch==1:
        cmd="select* from donation order by D_ID;"
    elif ch==2:
        cmd="select* from donation order by Name;"
    elif ch==3:
        cmd="select* from donation order by age;"
    elif ch==4:
        cmd="select* from donation order by Date_of_Donation;"
    elif ch==5:
        cmd="select* from donation order by money_donated;"
    elif ch==6:   
            cmd="select* from donation order by blood_donated;"
    else:
         print("Wrong input try again")
         Displaydon()
    mycursor.execute(cmd)
    f="%15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s %15s"
    print(f%("DID","Name","Age","Occupation","Income","Contact","Gmail","date_of_donation","City","Country","money","blood"))      
    print("*"*200)
    for i in mycursor:
        for j in i:
             print("%15s" % j,end=" ")
        print()    
    print("*"*200)
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Donator()
    elif e=="e":
        print("BYE BYE") 
        
def generateid (tablename):
    
    validtable = True 
    if tablename == "Donation":
        qry = "Select max(D_ID) from " + tablename 
    elif tablename == "Receiver" :
        qry = "Select max(R_ID) from " + tablename 
    else:
        print(" Not a valid Table ") 
        validtable = False 
    cnt = 0
    if(validtable == True ): 
        mycursor.execute(qry)
        rows = mycursor.fetchone()
        if rows[0]==None:
            cnt=1
        else:
            cnt = int(rows[0]) + 1
    
    return cnt 
    

def Insertdon():
    
    Rec=[]
    while True:
        DID =str(generateid ("Donation"))
        print("Id generated : ", DID )
        
        Dname=input("Enter your full Name : ")
        Dage=int(input("Enter your Age : "))
        Doccupation=input("Enter your occupation : ")
        Dincome=int(input("Enter your income : "))
        Dcontact=str(input("Enter your contact no : "))
        Dgmail=input("Enter your Gmail ID : ")
        Ddor=input("Enter date in YYYY-MM-DD : ")
        Dcity=input("Enter your city : ")
        Dcountry=input("Enter your country : ")
        print("\n(1) Money\n")
        print("\n(2) Blood\n")
        print("\n(3) Both\n")
        moneyflag = False
        bloodflag = False
        option3=int(input("Enter option : "))
        if option3==1:
            Dmoney=str(input("Enter the amount donated : "))
            moneyflag=True 
        elif option3==2:
            bloodflag= True 
            Dblood=input("Enter the blood group donated : ")
        elif  option3==3:
            Dmoney=str(input("Enter the amount donated : "))
            Dblood=input("Enter the blood group donated : ")
        else:
            print("Error wrong input!!!")
            word=input("Press y for choosing again or Enter any key to quit :  ")
            if word=="y"and"Y":
                Insertdon()
            else:
                print("Bye Bye")
        a=Dname.capitalize()
        b=Doccupation.capitalize()
        c=Dgmail.capitalize()
        d=Dcity.capitalize()
        e=Dcountry.capitalize()
        if moneyflag == True:
            Rec=[DID,a,Dage,b,Dincome,Dcontact,c,Ddor,d,e,Dmoney]
            cmd="insert into Donation values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL)"
        elif bloodflag == True:
            Rec=[DID,a,Dage,b,Dincome,Dcontact,c,Ddor,d,e,Dblood]
            cmd="insert into Donation values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0,%s)"
        else:
            Rec=[DID,a,Dage,b,Dincome,Dcontact,c,Ddor,d,e,Dmoney,Dblood]
            cmd="insert into Donation values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(cmd,Rec)
        mydb.commit()
        
        ch=input("more records : ")
        if ch=='n' or ch=='N':
            break;
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        Donator()
    elif e=="e": 
        print("BYE BYE")     
   
   
def Donator():
    print("*"*183)
    print("\t\t\t\t\t\t\tDONATOR   MENU\n")
    print("*"*183)
    print("\n(1) Insert Data\n")
    print("(2) Read Data\n")
    print("(3) Search Data \n")
    print("(4) Update Data\n")
    print("(5) Delete Data\n")
    print("(6) Go back\n")
    option2=int(input("Enter option : "))
    if option2==1:
        Insertdon()
    elif option2==2:
        Displaydon()
    elif option2==3:
        searchdon()
    elif option2==4:
        updatedon()
    elif option2==5:
        deldon()
    elif option2==6:
        menu()       
    else:
        print("Error wrong input!!!")
        word=input("Press y for choosing again or Enter any key to quit : ")
        if word=="y"and"Y":
            Donator()
        else:
            print("Bye Bye")
def moncol():
    sum=0
    cmd="Select sum(money_donated)from donation where money_donated is not NULL "
    mycursor.execute(cmd)
    for i in mycursor:
        for j in i:
            print(j)
            print("Total money collected is : ",int(j))
            sum+=int(j)  
    cmd="Select sum(money_received)from receiver where money_received is not NULL "
    mycursor.execute(cmd)
    for i in mycursor:
        for j in i:
            if j==None:
                j=0
                print("Total money donated is : ",j)
            else:
             print("Total money donated is : ",int(j))
             sum-=int(j)
    print("Balance money is : ",sum)
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        menu()
    elif e=="e": 
        print("BYE BYE")
        
        
def bloodcol():
    print("Blood Received by us\n")
    cmd="select blood_donated,count(distinct(blood_donated)) as count from donation group by blood_donated having blood_donated is Not Null;"    
    mycursor.execute(cmd)   
    f="%15s %15s "
    print(f%("Blood group","no of packet"))      
    print("*"*188)
    for i in mycursor:
        for j in i:
             print("%15s" % j,end=" ")
        print()    
    print("*"*188)
    print("Blood Donated by us\n")
    cmd="select blood_received,count(distinct(blood_received)) as count from receiver group by blood_received having blood_received is Not Null;"    
    mycursor.execute(cmd)   
    f="%15s %15s "
    print(f%("Blood group","no of packet"))      
    print("*"*188)
    for i in mycursor:
        for j in i:
             print("%15s" % j,end=" ")
        print()    
    print("*"*188)
    e=input("Press b to go back or e to exit : ")
    if e=="b":
        menu()
    elif e=="e": 
        print("BYE BYE")
def menu():
    print("*"*183)
    print("\t\t\t\t\t\t\t\tLA MENU\n")
    print("*"*183)
    print("\n(1) Donator\n")
    print("(2) Reciever\n")
    print("(3) Money Collected\n")
    print("(4) Blood Collected\n")
    print("(5) Exit\n")
    option=int(input("Enter option : "))
    if option==1:
        create_Donation()
    elif option==2:
        create_Receiver()
    elif option==3:
        moncol()
    elif option==4:
        bloodcol()
    elif option==5:
        print("\nBye Byee")
    else:
        print("Error wrong input!!!")
        word=input("Press y for choosing again or Enter any key to quit :  ")
        if word=="y"and"Y":
            menu()
        else:
            print("Bye Bye") 
            
def login(username,password):
    if username=="CDMS" and password=="CDMS1234":
        print("\nLogin Successful.........\n")
        menu()      
    else:
        print("Username or Password is Incorrect ")

username=input("Enter username : ")
password=input("Enter password : ")
login(username,password)
