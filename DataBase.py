print("                       ----------WELCOME TO AIR OPTIMIZERS----------                      ")
print("  ")
print(" ")
print(" ")
print(" ")
print("THIS FLIGHT IS ONLY AVAILABLE BETWEEN DELHI, MUMBAI, BANGALORE AND CHENNAI!!!!!")

print(" ")
print(" ")
#print("FARE CHARGES PER KM IS Rs.500")
print(" ")
print(" ")


print("!!!Do you want to enter records ?-->1!!!")
print("!!!Do you want to check the record of a specific person ?-->2!!!")

choice=int(input("Enter you choice from the given options:"))
if choice==1:
    import datetime
    datetime_object=datetime.datetime.now()
    print("DATE  :  TIME :  ",datetime_object)
    import pymysql
    def insert_records(name,age,email,address,contact,f_class):
        conn=pymysql.connect(host="localhost",user="root",passwd="root",db="management")
        Cursor=conn.cursor()
        Cursor._defer_warnings=True
        dropsql="DROP TABLE IF EXISTS ENTRIES;"
        Cursor.execute(dropsql)
        sql="""CREATE TABLE ENTRIES(NAME VARCHAR(40),AGE INT(3),EMAIL_ID varchar(200) PRIMARY KEY,ADDRESS varchar(50),CONTACT VARCHAR(15),FLIGHT_CLASS varchar(15))"""""
        ent="""INSERT INTO ENTRIES(NAME,AGE,EMAIL_ID,ADDRESS,CONTACT,FLIGHT_CLASS)VALUES("%s","%d","%s","%s","%s","%s")"""%(name,age,email,address,contact,f_class)
        Cursor.execute(sql)
        Cursor.execute(ent)
        conn.commit()
        Cursor.close()
        conn.close()
    def main():
        while True:
            name=str(input("ENTER FULLNAME:"))
            age=int(input("AGE:"))
            email=input("EMAIL-ID:")






            address=input("ADDRESS:")


            contact=str(input("PHONE NO.:"))
            print("1. ECONOMY")
            print("2. BUSINESS")
            Class=input("SELECT YOUR CLASS:")
            f_class=Class.upper()
            insert_records(name,age,email,address,contact,f_class)
                               
            n=input("Do you wanna book more tickets,Y/N: ")
            if n.lower()=="no" or n.lower()=="n":
                break
        
    if __name__=='__main__':
        main()
    from datetime import datetime, timedelta
    #print(datetime.today())  #print today's date time
    day=int(input("Enter the Boarding Day:"))
    new_date = datetime.today() + timedelta(day)
    date = new_date.date()
    #print(date)

    
    
    print(" ")
    print(" ")
    print(" ")
    print(" ")

    print("                    TRIP DETAILS")
    print(" ")
    print(" ")
    print(" ")


    print("1. ECONOMY")
    print("2. BUISNESS")
    cls=int(input("Please confirm your flight class once again:"))

#ag=0
    if cls=="1":
        ag=456
    else:
        ag=567
    print("")
    print("")

    print("1. DELHI")
    print("2. MUMBAI")
    print("3. BANGALORE ")
    print("4. CHENNAI")
    print(" ")
    print("PLEASE SELECT FROM ABOVE")
    print(" ")
    a = input("FROM:")
    b =input("TO:")
    print(" ")
    print("1.single")
    print("2.return")
    print(" ")
    c  = int(input("TRIP(single/return):"))                    #82

    print(" ")

    aa=int(input("No .of passengers:"))

    print(" ")

    if a=="2" and b=="1" or a=="1" and b=="2":
        e=1137
            
        if c=="1":
            d=e
        
        elif c=="2":
            d=e*85/100
        print("YOUR FLIGHT NO. IS 14XDE25")
        print("the distance is: 1137")
        print("the fare is: Rs.",e*0.85*ag*aa)
    elif a=="2" and b=="3"  or b=="2" and a=="3" :
        e=833
        if c=="1":
            d=e     
        elif c=="2":
            d=e*85/100
        print("YOUR FLIGHT NO. IS PE28VD")
        print("the distance is:",e)
        print("the fare is: Rs.",e*0.85*ag*aa)
    
    elif a=="2" and b=="4" or b=="2" and a=="4":
        e=1033
        if c=="1":
            d=e
    
        elif c=="2":
            d=e*85/100
        print("YOUR FLIGHT NO. IS 45SEYHW")
        print("the distance is:",e)
        print("the fare is: Rs.",e*0.85*ag*aa)
    
    elif a=="1" and b=="3" or b=="1" and a=="3":
            
        e=925
        if c=="1":
            d=e
        
        elif c=="2":
            d=e*85/100
        print("YOUR FLIGHT NO. IS QWV31JDF")
        print("the distance is:",e)
        print("the fare is: Rs.",e*0.85*ag*aa)
    elif a=="1" and b=="4" or b=="1" and a=="4":
        e=1348
        if c=="1":
            d=e
        
        elif c=="2":
            d=e*85/100
        print("YOUR FLIGHT NO. IS GSAHJ65GV")
        print("the distance is:",e)
        print("the fare is: Rs.",e*0.85*ag*aa)
    elif a=="3" and b=="4" or b=="3" and a=="4":
        e=753
        if c=="1":
            d=e
        
        elif c=="2":
            d=e*85/100
        print("YOUR FLIGHT NO. IS JNM56HG")
        print("the distance is:",e)
        print("the fare is: Rs.",e*0.85*ag*aa)
        q=input("press q to close the program:")
        if q.lower()=="q":
            quit()
elif choice==2:
    import pymysql
    def f(name):
        conn=pymysql.connect(host="localhost",user="root",passwd="root",db="management")
        Cursor=conn.cursor()
        Cursor._defer_warnings=True
        sql="SELECT * FROM ENTRIES WHERE NAME='{}'".format(name)
        Cursor.execute(sql)
        rows=Cursor.fetchall()
        print("The required data is:")
        print("-"*80)
        print("{}        {}     {}        {}        {}        {}".format("NAME","AGE","EMAIL_ID","ADDRESS","CONTACT","FLIGHT_CLASS"))
        print("-"*80)
        for row in rows:
            NAME=row[0]
            AGE=row[1]
            EMAIL_ID=row[2]
            ADDRESS=row[3]
            CONTACT=row[4]
            FLIGHT_CLASS=row[5]
            print("{}         {}      {}              {}              {}              {}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
            print("-"*80)
            
        
        
        
    
        Cursor.close()
        conn.close()
        q=input("Press 'q' to exit the application:")
        if q.lower()=="q":
            quit()
        
    def main():
        name=input("Enter the full name of the required person:")
        f(name)
    if __name__=="__main__":
        main()

    




        

    
