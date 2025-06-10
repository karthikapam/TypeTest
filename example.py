# Importing the Packages 
from tkinter import *  
import tkinter.font as fonts  
import random  
scores = 0   
times = 0   
counts = 0  
words=["apple","metadata","pronounce","temparature","controversy","linguistic","poverty","claustrophobia","serenity","cinnamon","impossible","tentative","affirmation","cricket","melody","hippopotamus"]
def startGame1():  
    #Create the game window and add size, title and colour  
    wns1 = Tk()  
    wns1.geometry("750x750")  
    wns1.title('Typing Test By ')  
    wns1.config(bg = 'honeydew2')      
    def timesFunc1():  
        global times, scores, miss, counts  
        if(counts<= 10): # If counts is less than 10, update the times  
            times += 1  
            timesr.configure(text = times)  
            timesr.after(1100,timesFunc1)  
        else:   
            #Label to show the results after the end  
            result = Label(wns1,text = '', font = ('aerial', 26,'italic bold'), fg = 'grey')  
            result.place(x = 230, y = 260)  
            result.configure(text = 'Times taken  =  {} \n Scores  =  {} \n Miss  =  {}'.format(times, scores, counts - scores -1))  
            miss = 0  
            scores = 0  
            times = 0  
            counts = 0  
            nextWord1.destroy()  
            playerInput1.destroy()  
            scoreslabel.destroy()  
            scoresboard.destroy()  
            timesrlabel.destroy()  
            timesr.destroy()       
    def mainGame1(event):  
        global scores, miss, counts  
        if times == 0: #At the start of game  
            #Shuffling the list  
            txt=random.choice(words) 
            nextWord1.configure(text = txt) #Showing the 1st element of the list in the nextWord1 label  
            playerInput1.delete(0, END) #clearing the entry widget playerInput1  
            timesFunc1() #call the times function  
        #If the enter button is pressed and it is not the Start of the game  
        if playerInput1.get() ==  nextWord1['text']: #check if player entered correctly  
            scores += 1 #increment scores  
            scoresboard.configure(text = scores) #show the new scores on scoresboard  
        counts += 1 #Increment the counts  
        if(counts <= 10): #If counts is less the 10  
            #Shuffling the list of words randomly  
            txt1=random.choice(words)
            nextWord1.configure(text = txt1) #Show the first element of the list in the nextWord1 label  
            playerInput1.delete(0,END) #clear the entry widget playerInput1  
    #Create able to show the project's name on screen  
    label = Label(wns1, text = 'Typing Test!', font = ('aerial', 26,  
                    'italic bold'), fg = 'gray',width = 40)  
    label.place(x = 10, y = 10)  
    #label to show the instruction and then to show the words to be typed  
    nextWord1 = Label(wns1, text = 'Hit enter button to start and after typing the word', font = ('aerial',20,  
                    'italic bold'), fg = 'black')  
    nextWord1.place(x = 30, y = 240)  
    #Label to show text Your Scores  
    scoreslabel = Label(wns1,text = 'Your Scores:',font = ('aerial', 26,  
                    'italic bold'), fg = 'red')  
    scoreslabel.place(x = 10, y = 110)  
    #Label to show scores  
    scoresboard = Label(wns1,text = scores,font = ('aerial', 26,  
                    'italic bold'), fg = 'blue')  
    scoresboard.place(x = 110, y = 180)  
    #Label to show text Times Elapsed  
    timesrlabel = Label(wns1, text = 'Time Elapsed:', font = ('aerial', 26,  
                    'italic bold'), fg = 'red')  
    timesrlabel.place(x = 460, y = 110)  
    #Label to show times  
    timesr = Label(wns1, text = times, font = ('aerial', 26,  
                    'italic bold'), fg = 'blue')  
    timesr.place(x = 670, y = 180)  
    #This widget takes input from the player  
    playerInput1 = Entry(wns1, font = ('aerial', 26,'italic bold'),bd = 10, justify = 'center')  
    playerInput1.place(x = 160, y = 330)  
    playerInput1.focus_set()  
    wns1.bind('<Return>',mainGame1) #Runs the mainGame1 function the player presses enter button  
    wns1.mainloop() #Runs the window till it is closed  
#Create the main window and add size, title and colour  
wns1 = Tk()  
wns1.geometry("500x500")  
wns1.title(" Typing Test")  
wns1.config(bg = "LightBlue1")  
#Create a frame to show the title of the project  
headingFrame11 = Frame(wns1, bg = "snow3", bd = 6)  
headingFrame11.place(relx = 0.2, rely = 0.2, relwidth = 0.7, relheight = 0.17)  
headingLabel1 = Label(headingFrame11, text = "Welcome to \n  Typing Test", bg = 'azure2', fg = 'black', font = ('Calibri', 16, 'bold'))  
headingLabel1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)  
#Create a button to start the game. The startGame1 function, given as a command parameter, runs on clicking the button  
btn1 = Button(wns1, text = "Start", bg = 'old lace', fg = 'black', width = 20, height = 2, command = startGame1)  
btn1['font'] = fonts.Font( size = 12)  
btn1.place(x = 175, y = 220)  
wns1.mainloop() #Runs the window till it is closed  