
print("                 -.-.-.-.-.-.-.-.-.-.-.WELCOME TO GRAPH WORLD-.-.-.-.-.-.-.-.-.-.  ")
print("")
print("")
print("")
print("")

import matplotlib.pyplot as plt
print("Select from options given below:")
print("Line graph-->1")
print("Bar graph-->2")
print("Pie chart-->3")
print("Equation Plotter-->4")
ch=int(input("Enter option number: "))
if ch==1:
    def line_graph():
        x=[]
        y=[]
        while True:
            n=input("Enter X-coordinates: ")
            ch=input("Do you wish to add more X-coordintes ?,Y/N: ")
            if ch.upper()=="N" or ch.upper()=="No":
                break
            else:
                x.append(int(n))
        #print(x)
        while True:
            a=input("Enter Y-coordinates: ")
            ch=input("Do you wish to add more Y-Coordinates ?,Y/N: ")
            if ch.upper()=="N" or ch.upper()=="No":
                break
            else:
                y.append(int(a))
        #print(y)
        T=input("Enter the title for your graph: ")
        plt.title(T)
        X_label=input("Enter X-axis label for graph: ")
        plt.xlabel(X_label)
        Y_label=input("Enter Y-axis label for graph: ")
        plt.ylabel(Y_label)
        plt.grid()
        plt.plot(x,y)
        plt.show()
    line_graph()
    while True:
        ch=input("Do you want to make more  line graphs?, Y/N:")
        if ch.upper()=="Yes"or ch.upper()=="Y":
            line_graph()
        elif ch.upper=="N" or ch.upper=="NO":
            quit()

if ch==2:
    def bar_graph():
        x=[]
        y=[]
        while True:
            n=input("Enter X-coordinates: ")
            ch=input("Do you wish to add more X-Coordinates ?,Y/N: ")
            if ch.upper()=="N" or ch.upper()=="No":
                break
            else:
                x.append(int(n))
        #print(x)
        while True:
            a=input("Enter Y-coordinates: ")
            ch=input("Do you wish to add more Y-Coordinates ?,Y/N: ")
            if ch.upper()=="N" or ch.upper()=="No":
                break
            else:
                y.append(int(a))
        #print(y)
        t=input("Enter title of your bar graph: ")
        plt.title(t)
        X_label=input("Enter X-axis label for graph: ") #1
        plt.xlabel(X_label)
        Y_label=input("Enter Y-axis label for graph: ")     #2
        plt.ylabel(Y_label)                      #3
        plt.bar(x,y,color="green",width=2)
        plt.show()
    bar_graph()
    while True:
        ch=input("Do you want to make more  bar graphs?, Y/N:")
        if ch.upper()=="Yes"or ch.upper()=="Y":
            bar_graph()
        elif ch.upper=="N" or ch.upper=="NO":
            quit()
            
if ch==3:
    def pie_chart():
        s=[]
        print("   ##Not that the sum of sizes must be equal to 100##    ")
        while True:
            size=input("Enter sizes for pie chart: ")
            ch=input("Do you wanna enter more values ?,Y/N: ")
            if ch.upper()=="N" or ch.upper=="No":
                break
            else:
                s.append(float("{}".format(size)))
            print(s)
        l=[]
        print("   ##Make sure that number of labels are equal to number of values of sizes enter##   ")
        while True:
            label=input("Enter labels for your pie chart: ")
            ch=input("Do you wish to add more labels ?,Y/N: ")
            if ch.upper()=="N" or ch.upper()=="No":
                break
            else:
                l.append(label)
        print(l)
        
        plt.pie(s,labels=label,)
        plt.show()
    pie_chart()
    while True:
        ch=input("Do you want to make more pie charts?, Y/N:")
        if ch.upper()=="Yes"or ch.upper()=="Y":
            pie_chart()
        elif ch.upper=="N" or ch.upper=="NO":
            quit()

if ch==4:
    import matplotlib.pyplot as plt
    import numpy as np
    def graph():
        print("For Example:-a,b a and b must be integers")

        ran = list(map(eval,input("Enter the range of X: ").split(",")))
        
        s=eval(input("Enter the increment constant:"))
        x=np.arange(ran[0],ran[1]+1,s)
        print("y = ax^b + c")
        m=eval(input("Enter value of a: "))
        c=eval(input("Enter the value of b: "))
        r=eval(input("Enter the value of c: "))
        y=m*x**r+c
        plt.plot(x,y)
        Title=input("Enter the title for graph:")
        plt.title(Title) 
        Xlabel=input("Enter label for X-axis:")
        plt.xlabel(Xlabel)
        Ylabel=input("Enter label for Y-axis:")
        plt.ylabel(Ylabel)
        w=input("Enter window title of your graph:")
        plt.gcf().canvas.set_window_title(w)
        plt.show()
    graph()
    while True:
        ch=input("Do you want to make more graphs?, Y/N:")
        if ch.upper()=="Yes"or ch.upper()=="Y":
            graph()
        elif ch.upper=="N" or ch.upper=="NO":
            quit()
    
