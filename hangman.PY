from tkinter import *
from tkinter import messagebox
K="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
windows=Tk()
occupation=["ACCOUNTANT","ACTOR","ASSISTANT","AUTHOR","BAKER","BIOLOGIST","CHEF","CLERK","WRITER","COOK","DECORATOR","DENTIST","DESIGNER","DIRECTOR","DOCTOR","ECONMIST","EDITOR","ELECTRICIAN","ENGINEER","EXECUTIVE","FARMER","FISHERMAN","FISHMONGER","GEOLOGIST","HAIRDRESSER","JEWELLER","JOURNALIST","JUDGE","JUGGLER","LAWYER","LECTURER","LEXICOGRAPHER","MAGICIAN","MANAGER","MINER","MUSICIAN","NURSE","PAINTER","PHOTOGRAPHER","PILOT","PLUMBER","POLITICIAN","PORTER","PRINTER","RECEPTIONIST","SAILOR","SALESPERSON","SCIENTIST","SECRETARY","SINGER","SOLDIER","SURGEON","TAILOR","TEACHER","TRANSLATOR","TRUCKER","CAMERAMAN","WAITER"]
popular_brand=["NOKIA","ONEPLUS","SONY","APPLE","SAMSUNG","BLACKBERRY"]
country=["FRANCE","CHINA","ITALY","GERMANY","MEXICO","TURKEY","AUSTRIA","MALAYSIA","GREECE","RUSSIA","JAPAN","CANADA","POLAND","NETHERLANDS","MACAO","HUNGARY","INDIA","UKRAINE","SINGAPORE","INDONESIA"]
windows.title("Hangman")
photos=[PhotoImage(file="images/hang0.png"),PhotoImage(file="images/hang1.png"),PhotoImage(file="images/hang2.png"),PhotoImage(file="images/hang3.png"),PhotoImage(file="images/hang4.png"),PhotoImage(file="images/hang5.png"),PhotoImage(file="images/hang6.png"),PhotoImage(file="images/hang7.png")]
def newGame():
    global the_word_withSpaces
    global numberofGuesses
    global the_word
    global H
    x=random.randint(2,4)
    if x==2:
        H="It's an occupation"
        word_list=occupation
    elif x==3:
        H="It's a popular Phone brand"
        word_list=popular_brand
    elif x==4:
        H="It's a country"
        word_list=country
    the_word=random.choice(word_list)
    numberofGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
def Hint():
    messagebox.showinfo("Hint",H)
def guess(letter):
    global numberofGuesses
    if numberofGuesses<7:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangan","You guessed it!")
        else:
            numberofGuesses += 1
            imgLabel.config(image=photos[numberofGuesses])
            if numberofGuesses==7:
                messagebox.showwarning("Hangman","Game Over\nthe word was {}".format(the_word))

imgLabel=Label(windows)
imgLabel.grid(row=0, column=0, columnspan=5,padx=10,pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(windows, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=5,columnspan=5, padx=10,pady=40)

photo=[PhotoImage(file ="images2/L1.png"),PhotoImage(file ="images2/L2.png"),
       PhotoImage(file ="images2/L3.png"),PhotoImage(file ="images2/L4.png"),
       PhotoImage(file ="images2/L5.png"),PhotoImage(file ="images2/L6.png"),
       PhotoImage(file ="images2/L7.png"),PhotoImage(file ="images2/L8.png"),
       PhotoImage(file ="images2/L9.png"),PhotoImage(file ="images2/L10.png"),
       PhotoImage(file ="images2/L11.png"),PhotoImage(file ="images2/L12.png"),
       PhotoImage(file ="images2/L13.png"),PhotoImage(file ="images2/L14.png"),
       PhotoImage(file ="images2/L15.png"),PhotoImage(file ="images2/L16.png"),
       PhotoImage(file ="images2/L17.png"),PhotoImage(file ="images2/L18.png"),
       PhotoImage(file ="images2/L19.png"),PhotoImage(file ="images2/L20.png"),
       PhotoImage(file ="images2/L21.png"),PhotoImage(file ="images2/L22.png"),
       PhotoImage(file ="images2/L23.png"),PhotoImage(file ="images2/L24.png"),
       PhotoImage(file ="images2/L25.png"),PhotoImage(file ="images2/L26.png"),]

n=0
for c in K:
    Button(windows,image=photo[0+n], text=c, command=lambda c=c: guess(c), font=("Helvetica 18"),width=4).grid(row=1+n//5, column=n%5,sticky="NSWE")
    n=n+1

    
Button(windows,text="New\nGame", command=lambda:newGame()).grid(row=3, column=8,sticky="NSWE")
Button(windows,text="Hint", command=lambda:Hint()).grid(row=4, column=8,sticky="NSWE")
newGame()
windows.mainloop()



























