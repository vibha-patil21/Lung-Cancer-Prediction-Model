# Import Tkinter library
from tkinter import *
import pandas as pd
import numpy as np
from pandas import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn import metrics


df=read_csv("surveylungcancer.csv")
GENDER = {'M': 0,'F': 1}
df.GENDER = [GENDER[item] for item in df.GENDER]
LUNG_CANCER = {'NO': 0,'YES': 1}
df.LUNG_CANCER = [LUNG_CANCER[item] for item in df.LUNG_CANCER]
m=SimpleImputer(strategy="median")
num_data=df.drop("AGE",axis=1)
m.fit(num_data)
m.statistics_
num_data.median().values
x=m.transform(num_data)
d_tr=pd.DataFrame(x,columns=num_data.columns)

# Define Function to print the input value
lst=[]
def display_input():
    if(var1.get()==1):
        lst.append(t1.cget("text"))
    if(var2.get()==1):
        lst.append(t2.cget("text"))
    if(var3.get()==1):
        lst.append(t3.cget("text"))
    if(var4.get()==1):
        lst.append(t4.cget("text"))
    if(var5.get()==1):
        lst.append(t5.cget("text"))
    if(var6.get()==1):
        lst.append(t6.cget("text"))
    if(var7.get()==1):
        lst.append(t7.cget("text"))
    if(var8.get()==1):
        lst.append(t8.cget("text"))
    if(var9.get()==1):
        lst.append(t9.cget("text"))
    if(var10.get()==1):
        lst.append(t10.cget("text"))
    if(var11.get()==1):
        lst.append(t11.cget("text"))
    if(var12.get()==1):
        lst.append(t12.cget("text"))
    if(var13.get()==1):
        lst.append(t13.cget("text"))
    a=d_tr[lst]
    b=d_tr['LUNG_CANCER']
    x_train,x_test,y_train,y_test=train_test_split(a,b,test_size=0.2)
    lr_model = RandomForestClassifier(n_estimators=100)
    lr_model.fit(x_train,y_train)
    y_pred=lr_model.predict(x_test)
    accuracy=metrics.accuracy_score(y_test,y_pred)*100
    print(accuracy)
    if(accuracy>=90):
        label=Label(win,text="You have lung cancer")
        print(1)
        label.grid(column=0,row=20)
        #label.pack()
    elif(accuracy>=80):
        label=Label(win,text="There might be a chance of lung cancer")
        label.grid(column=0,row=20)
    elif(accuracy>=70):
        label=Label(win,text="You doesn't have lung cancer")
        print(3)
        label.grid(column=0,row=25)
        #label.pack()
    
# Create an instance of tkinter frame
win = Tk()
win.title("Lung Cancer Prediction System")
# Set the geometry of Tkinter frame
win.geometry("400x500")
# Define empty variables
var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
t1 = Checkbutton(win, text="SMOKING", variable=var1, onvalue=1, offvalue=0)
t1.grid(column=0,row=0,sticky="w")
t2 = Checkbutton(win, text="YELLOW_FINGERS", variable=var2, onvalue=1, offvalue=0)
t2.grid(column=0,row=1,sticky="w")
t3 = Checkbutton(win, text="ANXIETY", variable=var3, onvalue=1, offvalue=0)
t3.grid(column=0,row=2,sticky="w")
t4 = Checkbutton(win, text="PEER_PRESSURE", variable=var4, onvalue=1, offvalue=0)
t4.grid(column=0,row=3,sticky="w")
t5 = Checkbutton(win, text="CHRONIC_DISEASE", variable=var5, onvalue=1, offvalue=0)
t5.grid(column=0,row=4,sticky="w")
t6 = Checkbutton(win, text="ALLERGY", variable=var6, onvalue=1, offvalue=0)
t6.grid(column=0,row=5,sticky="w")
t7 = Checkbutton(win, text="FATIGUE", variable=var7, onvalue=1, offvalue=0)
t7.grid(column=0,row=6,sticky="w")
t8 = Checkbutton(win, text="WHEEZING", variable=var8, onvalue=1, offvalue=0)
t8.grid(column=0,row=7,sticky="w")
t9 = Checkbutton(win, text="ALCOHOL_CONSUMING", variable=var9, onvalue=1, offvalue=0)
t9.grid(column=0,row=8,sticky="w")
t10 = Checkbutton(win, text="COUGHING", variable=var10, onvalue=10, offvalue=0)
t10.grid(column=0,row=9,sticky="w")
t11 = Checkbutton(win, text="SHORTNESS_OF_BREATH", variable=var11, onvalue=1, offvalue=0)
t11.grid(column=0,row=10,sticky="w")
t12 = Checkbutton(win, text="SWALLOWING_DIFFICULTY", variable=var12, onvalue=1, offvalue=0)
t12.grid(column=0,row=11,sticky="w")
t13 = Checkbutton(win, text="CHEST_PAIN", variable=var13, onvalue=1, offvalue=0)
t13.grid(column=0,row=12,sticky="w")
b = Button(win,text="Submit",command=display_input)
b.grid(column=0,row=13)
win.mainloop()
