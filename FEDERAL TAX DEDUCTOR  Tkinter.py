import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


#-UPDATE  AMOUNTS AND GRID FOR EACH 

root_var = tk.Tk()
#ADDS TITLE 
root_var.title("FEDERAL TAX DEDUCTOR")


frame1 = Frame(root_var, padx=20, bd=10, relief=RIDGE)
frame1.grid(row=0,column=0)

frame2 = Frame(root_var, padx=20, bd=10, relief=RIDGE)
frame2.grid(row=1,column=0)

frame3 = Frame(root_var, padx=20, bd=14, relief=RIDGE)
frame3.grid(row=2,column=0)

frame4 = Frame(root_var, padx=20, bd=10, relief=RIDGE)
frame4.grid(row=3,column=0)








#-------------------------Text Variables and Plcaing-------------------------------------------------
amount1 = StringVar()
amount2 = StringVar()
amount3 = StringVar()
amount4 = StringVar()
amount5 = StringVar()
amount6 = StringVar()
amount7 = StringVar()



#------------Entries and placing--------------------------------------------------
a = Entry(frame2,textvariable = amount1 ,width = 35, borderwidth=5)#filing number
a.grid(row=4, column=1, padx=10, pady=10)

b = Entry(frame2,textvariable = amount2, width = 35, borderwidth=5)#annual salary
b.grid(row=5, column=1,  padx=10, pady=10)



c = Entry(frame4,textvariable = amount3, width = 50, borderwidth=5 )# filing status
c.grid(row = 0, column = 1)

d = Entry(frame4,textvariable = amount4, width = 30, borderwidth=5 )# TaxBracket
d.grid(row = 1, column =  1)

e = Entry(frame4,textvariable = amount5, width = 30, borderwidth=5 )# Tax Rate
e.grid(row = 2, column = 1)

f = Entry(frame4,textvariable = amount6, width = 30, borderwidth=5 )# Salary After Tax
f.grid(row = 3, column = 1)



#-----------------Labels and placing--------------------------------------------


InstructionsLabel = Label(frame1,
                          text = """PLEASE FOLLOW DIRECTIONS AND CHOOSE FILING STATUS BELOW

Single filer or Married Filing Separately type the number "1" In the first box below

Married filing Joint returns type the number "2" In the first box below

Head Of Household type the number "3" In the first box below

NOTE: ONLY INPUT FULL NUMBERS, NO DECIMALS
(USING DECIMALS WILL CALCULATE INNACURATELY)""",
                         font = ("Times New Roman",12),
                         bd =  1, justify = "left")
InstructionsLabel.grid(row=0, column=0)


FilingnumLabel = Label(frame2, text= "Please enter filing # --------------------->",justify = "left")
FilingnumLabel.grid(row=4, column=0)

AnnualSalLabel = Label(frame2, text = "Please Enter Annual Salary--------------------->",justify = "left")
AnnualSalLabel.grid(row=5, column=0)



FilingStatuslbl = Label(frame4, text = "Filing Status:") 
FilingStatuslbl.grid(row = 0,column = 0)


TaxBracketlbl = Label(frame4, text = "Tax Bracket:") 
TaxBracketlbl.grid(row = 1,column = 0)

TaxRatelbl = Label(frame4, text = "Tax Rate:")
TaxRatelbl.grid(row = 2,column = 0)


SalaryAfterTaxlbl = Label(frame4, text = "Salary After Tax:")
SalaryAfterTaxlbl.grid(row = 3,column = 0)






#-------------------------Functions---------------------------------------
def press():    
    if(int(a.get())==1):
        amount3.set("FOR SINGLE FILERS or Married Filing Separately")
     
        if(float(b.get())<10275):
            calc1 = float(b.get())-(float(b.get())*.10)
            amount4.set("$0 to $10,275")
            amount5.set("10%")
            amount6.set("${}".format(calc1))

        if((float(b.get())>10275) and float(b.get())<41775):
            calc2 = float(b.get())-(float(b.get())*.12)
            amount4.set("$10,275 to $41,775")            
            amount5.set("12%")
            amount6.set("${}".format(calc2))
            
        if((float(b.get())>41775)and(float(b.get())<89075)): 			
            calc3 = float(b.get())-(float(b.get())*.22)   
            amount4.set("$41,775 to $89,075")
            amount5.set("22%")
            amount6.set("${}".format(calc3))

        if((float(b.get())>89075)and(float(b.get())<170050)):           
            calc4 = float(b.get())-(float(b.get())*.24) 
            amount4.set("$89,075 to $170,050")
            amount5.set("24%")
            amount6.set("${}".format(calc4))        

        if((float(b.get())>170050)and(float(b.get())<215950)): 
            calc5 = float(b.get())-(float(b.get())*.32)
            amount4.set("$170,050 to $215,950")
            amount5.set("32%")
            amount6.set("${}".format(calc5))

        if((float(b.get())>215950)and(float(b.get())<539900)):	 
            calc6 = float(b.get())-(float(b.get())*.35)
            amount4.set("$215,950 to $539,900")
            amount5.set("35%")
            amount6.set("${}".format(calc6))

        if((float(b.get())>539900)):
            calc7 = float(b.get())-(float(b.get())*.37)
            amount4.set("+$539,900")
            amount5.set("37%")
            amount6.set("${}".format(calc7))
            


    if(int(a.get())==2):  #left off editing
        amount3.set('FOR MARRIED INDIVIDUALS FILING JOINT RETURNS')#

        if(float(b.get())<20550):
            calc8 = float(b.get())-(float(b.get())*.10)
            amount4.set("$0 to $20,550")
            amount5.set("10%")
            amount6.set("${}".format(calc8))

        if((float(b.get())>20550)and float(b.get())<83550):
            calc9 = float(b.get())-(float(b.get())*.12)
            amount4.set("$20,550 to $83,550")
            amount5.set("12%")
            amount6.set("${}".format(calc9))

        if((float(b.get())>83550)and(float(b.get())<178150)): 			
            calc10 =  float(b.get())-(float(b.get())*.22)
            amount4.set("$83,550 to $178,150")
            amount5.set("22%")
            amount6.set("${}".format(calc10))


        if((float(b.get())>178150)and(float(b.get())<340100)): 
            calc11 = float(b.get())-(float(b.get())*.24)
            amount4.set("$178,150 to $340,100")
            amount5.set("24%")
            amount6.set("${}".format(calc11))

        if((float(b.get())>340100)and(float(b.get())<431900)):			
            calc12 = float(b.get())-(float(b.get())*.32)
            amount4.set("$340,100 to $431,900")
            amount5.set("32%")
            amount6.set("${}".format(calc12))

        if((float(b.get())>431900)and(float(b.get())<647850)): 		 
            calc13 = float(b.get())-(float(b.get())*.35)
            amount4.set("$431,900 to $647,850")
            amount5.set("35%")
            amount6.set("${}".format(calc13))

        if((float(b.get())>647850)): 			
            calc14 = float(b.get())-(float(b.get())*.37)
            amount4.set("+$647,850")
            amount5.set("37%")
            amount6.set("${}".format(calc14))
            


    if(int(a.get())==3):
        amount3.set("FOR HEAD OF HOUSEHOLDS")

        if(float(b.get())<14650):
            calc15 = float(b.get())-(float(b.get())*.10)
            amount4.set("$0 to $14,650")
            amount5.set("10%")
            amount6.set("${}".format(calc15))

        if((float(b.get())>14650)and float(b.get())<55900):
            calc16 = float(b.get())-(float(b.get())*.12)
            amount4.set("$14,650 to $55,900")
            amount5.set("12%")
            amount6.set("${}".format(calc16))

        if((float(b.get())>55900)and(float(b.get())<89050)): 			
            calc17 = float(b.get())-(float(b.get())*.22)
            amount4.set("$55,900 to $89,050")
            amount5.set("22%")
            amount6.set("${}".format(calc17))

        if((float(b.get())>89050)and(float(b.get())<170050)): 	
            calc18 = float(b.get())-(float(b.get())*.24)
            amount4.set("$89,050 to $170,050")
            amount5.set("24%")
            amount6.set("${}".format(calc18))

        if((float(b.get())>170050)and(float(b.get())<215950)):			
            calc19 = float(b.get())-(float(b.get())*.32)
            amount4.set("$170,050 to $215,950")
            amount5.set("32%")
            amount6.set("${}".format(calc19))

        if((float(b.get())>215950)and(float(b.get())<539900)): 		 
            calc20 = float(b.get())-(float(b.get())*.35)
            amount4.set("$215,950 to $539,900")
            amount5.set("35%")
            amount6.set("${}".format(calc20))

        if((float(b.get())>539900)): 			
            calc21 = float(b.get())-(float(b.get())*.37)
            amount4.set("+$539,900")
            amount5.set("37%")
            amount6.set("${}".format(calc21))

            

def Exit():
    root_var.destroy()
    

def clear():
    amount1.set("")
    amount2.set("")
    amount3.set("")
    amount4.set("")
    amount5.set("")
    amount6.set("")
    amount7.set("")
    

#---------------------Buttons and Placing-----------------------------------
calculatebtn= Button(frame3, text= "CALCULATE" ,padx=82,pady=10,command=press)
calculatebtn.grid(row=6,column=0)

exitbtn=Button(frame3, text= "EXIT" ,padx=82,pady=10,command=Exit)
exitbtn.grid(row=6,column=1)


clearbtn = Button(frame3, text= "Clear" ,padx=82,pady=10,command= clear)
clearbtn.grid(row=6,column=2)



root_var.mainloop()


