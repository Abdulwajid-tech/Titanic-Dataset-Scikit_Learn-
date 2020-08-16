from main import givePrediction
from tkinter import *

passengerID = ""
passengerClass = ""
gender = ""
Sibling = ""
Embarked = ""

root = Tk()
root.geometry("1100x600")
root.title("Semester Project of Scikit-Learn")

def predictTheTitanicSurvival():
    predict = "Survived"
    predict = givePrediction(100,2,"Male",2,"S","LinearRegression")
    if( predict == 0):
        predict= "Passenger will not survive"

    elif( predict == 1):
        predict = "Passenger will survive"

    label8 = Label(secondFrame, text=predict, font=('arial', 13, 'bold')).grid(row=6,column=0,padx=50,pady=30)


topFrame = Frame(root, width = 1097, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 3)
topFrame.pack(side = TOP)

label = Label(topFrame,text = "Model to predicts which passengers survived the Titanic shipwreck.",font = ('arial', 18, 'bold'))
label.grid(row = 0, column = 0)

secondFrame = Frame(root, width = 1097, height =400, bg = "lightblue")
secondFrame.pack()


label1 = Label(secondFrame , text = "Passenger ID       (1 ~ ...) : ",font = ('arial', 13, 'bold')).grid(row=0 , column = 0 , padx = 50, pady = 30)
entry1 = Entry(secondFrame , font = ('arial', 13, 'bold') , textvariable = passengerID).grid(row = 0 ,column = 1 , padx = 100, pady = 30)


label2 = Label(secondFrame , text = "Passenger Class    (1 , 2 , 3) : ",font = ('arial', 13, 'bold')).grid(row=1 , column = 0 , padx = 50, pady = 10)
entry2 = Entry(secondFrame , font = ('arial', 13, 'bold') , textvariable = passengerClass).grid(row = 1 ,column = 1 , padx = 100, pady = 10)


label3 = Label(secondFrame , text = "Gender : ",font = ('arial', 13, 'bold')).grid(row=2 , column = 0 , padx = 50, pady = 10)
checkButton1 = Checkbutton(secondFrame, text = "Male").grid(row=2 , column = 1 , padx = 50, pady = 10)
checkButton2 = Checkbutton(secondFrame, text = "Female").grid(row=2 , column = 2 , padx = 50, pady = 10)


label4 = Label(secondFrame , text = "Sibling : ",font = ('arial', 13, 'bold')).grid(row=3 , column = 0 , padx = 50, pady = 10)
entry4 = Entry(secondFrame , font = ('arial', 13, 'bold')).grid(row = 3 ,column = 1 , padx = 100, pady = 10)


label5 = Label(secondFrame , text = "Embarked : ",font = ('arial', 13, 'bold')).grid(row=4 , column = 0 , padx = 50, pady = 10)
entry5 = Entry(secondFrame , font = ('arial', 13, 'bold')).grid(row = 4 ,column = 1 , padx = 100, pady = 10)


survival = Button(secondFrame, text = "Click Here to Predict!", command = predictTheTitanicSurvival).grid(row = 5 ,column = 1 , padx = 100, pady = 10)


root.mainloop()                     #To have the window for every time in the screen.


































