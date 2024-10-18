from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import random
import os
import tempfile

def clear():
      textarea.delete(1.0,END)

def print_bill():
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is empty')
      
     else:
          file=tempfile.mktemp('.txt')
          open(file,'w').write(textarea.get(1.0,END))
          os.startfile(file,'print')



def search_bill():
      for i in os.listdir('bills/'):
          if i.split('.')[0]==billEntry.get():
               f= open(f"bills/{i}",'r')
               textarea.delete(1.0,END)
               for data in f:
                    textarea.insert(END,data)
               f.close()
               break
      else:
               messagebox.showerror('Error', 'Invalid Bill Number')



if not os.path.exists('bills'):
      os.mkdir('bills')


billnumber = random.randint(500,1000)

def save_bill():
      global billnumber 
      result= messagebox.askyesno('Confirm','Do you want to save the bill?')
      if result:
            bill_content =textarea.get(1.0,END)
            file= open(f'bills/{billnumber}.txt','w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo('Success',f'Bill number: {billnumber} is save sucessfully')
            billnumber = random.randint(500,1000)

def total():
    # Cosmetics Total
    global bathsoapprice, facecreamprice, facewashprice,hairgelprice, hairsprayprice,bodylotionprice,Fantaprice,Cokeprice,Spriteprice,Limcaprice,Pepsiprice,MountainDewprice,riceprice,Dalprice,Wheatprice,Coffeeprice,Teaprice,Sugarprice
    global totalbill

    bathsoapprice= float(bathsoapEntry.get())*30
    facecreamprice= float(facecreamEntry.get())*100
    facewashprice= float(facewashEntry.get())*80
    hairsprayprice= float(hairsprayEntry.get())*120
    hairgelprice= float(hairgelEntry.get())*60
    bodylotionprice= float(bodylotionEntry.get())*200

    total_Cosmetic = bathsoapprice+facewashprice+facecreamprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'Rs {total_Cosmetic}')
    cosmetictax = total_Cosmetic*0.120
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'Rs {cosmetictax}')

    # Grocerries Total
    riceprice= float(riceEntry.get())*60
    Dalprice= float(DalEntry.get())*110
    Wheatprice= float(WheatEntry.get())*40
    Sugarprice= float(SugarEntry.get())*42
    Teaprice= float(TeaEntry.get())*50
    Coffeeprice= float(CoffeeEntry.get())*50

    total_Grocerries = riceprice+Dalprice+Wheatprice+Sugarprice+Teaprice+Coffeeprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'Rs {total_Grocerries}')
    grocerytax = total_Grocerries*0.1
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'Rs {grocerytax}')

    # Drinks Total
    Pepsiprice= float(PepsiEntry.get())*60
    Spriteprice= float(SpriteEntry.get())*110
    Limcaprice= float(LimcaEntry.get())*40
    Cokeprice= float(CokeEntry.get())*42
    Fantaprice= float(FantaEntry.get())*50
    MountainDewprice= float(MountainDewEntry.get())*50

    total_Drinks = Pepsiprice+Spriteprice+Limcaprice+Cokeprice+Fantaprice+MountainDewprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'Rs {total_Drinks}')
    drinkstax = total_Drinks*0.15
    drinksTaxEntry.delete(0,END)
    drinksTaxEntry.insert(0,f'Rs {drinkstax}')

    totalbill = total_Cosmetic+total_Drinks+total_Grocerries+drinkstax+cosmetictax+grocerytax
    



def bill_area():
    if nameEntry.get()==''or phoneEntry.get()=='':
        messagebox.showerror('Error','Both the customer details are required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No products are selected')
    elif cosmeticpriceEntry.get()=='Rs 0' and grocerypriceEntry.get()=='Rs 0' and drinkspriceEntry.get()=='Rs 0':
        messagebox.showerror('Error','No products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,f'\t\t\t  ***Welcome Customer***\n')
        textarea.insert(END,f'\n\tBill Number: {billnumber}\n')
        textarea.insert(END,f'\n\tCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\n\tCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,f'\n\t===============================================================')
        textarea.insert(END,f'\n\tProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,f'\n\t===============================================================')
        if bathsoapEntry.get()!='0':
              textarea.insert(END,f'\n\tBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t Rs {bathsoapprice}')
        if facecreamEntry.get()!='0':
              textarea.insert(END,f'\n\tFace Cream\t\t\t{facecreamEntry.get()}\t\t\t Rs {facecreamprice}')
        if facewashEntry.get()!='0':
              textarea.insert(END,f'\n\tFace Wash\t\t\t{facewashEntry.get()}\t\t\t Rs {facewashprice}')
        if hairsprayEntry.get()!='0':
              textarea.insert(END,f'\n\tHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t Rs {hairsprayprice}')
        if hairgelEntry.get()!='0':
              textarea.insert(END,f'\n\tHair Gel\t\t\t{hairgelEntry.get()}\t\t\t Rs {hairgelprice}')
        if bodylotionEntry.get()!='0':
              textarea.insert(END,f'\n\tBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t Rs {bodylotionprice}')
        if riceEntry.get()!='0':
              textarea.insert(END,f'\n\tRice\t\t\t{riceEntry.get()}\t\t\t Rs {riceprice}')
        if WheatEntry.get()!='0':
              textarea.insert(END,f'\n\tWheat\t\t\t{WheatEntry.get()}\t\t\t Rs {Wheatprice}')
        if CoffeeEntry.get()!='0':
              textarea.insert(END,f'\n\tCoffee\t\t\t{CoffeeEntry.get()}\t\t\t Rs {Coffeeprice}')
        if TeaEntry.get()!='0':
              textarea.insert(END,f'\n\tTea\t\t\t{TeaEntry.get()}\t\t\t Rs {Teaprice}')
        if SugarEntry.get()!='0':
              textarea.insert(END,f'\n\tSugar\t\t\t{SugarEntry.get()}\t\t\t Rs {Sugarprice}')
        if DalEntry.get()!='0':
              textarea.insert(END,f'\n\tDal\t\t\t{DalEntry.get()}\t\t\t Rs {Dalprice}')
        if PepsiEntry.get()!='0':
              textarea.insert(END,f'\n\tPepsi\t\t\t{PepsiEntry.get()}\t\t\t Rs {Pepsiprice}')
        if SpriteEntry.get()!='0':
              textarea.insert(END,f'\n\tSprite\t\t\t{SpriteEntry.get()}\t\t\t Rs {Spriteprice}')
        if MountainDewEntry.get()!='0':
              textarea.insert(END,f'\n\tMountain Dew\t\t\t{MountainDewEntry.get()}\t\t\t Rs {MountainDewprice}')
        if CokeEntry.get()!='0':
              textarea.insert(END,f'\n\tCoke\t\t\t{CokeEntry.get()}\t\t\t Rs {Cokeprice}')
        if FantaEntry.get()!='0':
              textarea.insert(END,f'\n\tFanta\t\t\t{FantaEntry.get()}\t\t\t Rs {Fantaprice}')
        if LimcaEntry.get()!='0':
              textarea.insert(END,f'\n\tLimca\t\t\t{LimcaEntry.get()}\t\t\t Rs {Limcaprice}')
        textarea.insert(END,f'\n\t===============================================================')
        if cosmetictaxEntry.get()!='Rs. 0.0':
            textarea.insert(END,f'\n\tCosmetic Tax\t\t{cosmetictaxEntry.get()}')

        if grocerytaxEntry.get()!='Rs. 0.0':
            textarea.insert(END,f'\n\tGrocery Tax\t\t{grocerytaxEntry.get()}')

        if drinksTaxEntry.get()!='Rs. 0.0':
            textarea.insert(END,f'\n\tCold Drinks Tax\t\t{drinksTaxEntry.get()}')
        
        textarea.insert(END,f'\n\t===============================================================')
        textarea.insert(END,f'\n\tTotal Price\t\t Rs {totalbill}')

        save_bill()


  
   

#GUI
root = Tk()
root.title("Retail Billing System")
root.geometry("1470x685+5+5")
root.minsize(1400,670)


root.iconbitmap('billing.ico')

headingLabel = Label(root,text='Retail Billing System',font=('times new roman', 30, 'bold'),bg='aquamarine1', fg='darkslateblue', bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

customer_details_frame= LabelFrame(root,text='Customer Details', font=('times new roman',15,'bold'),bg='aquamarine1', fg='darkslateblue', bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel= Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='aquamarine1', fg='darkslateblue')
nameLabel.grid(row=0,column=0, padx=20,pady=2)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=22)
nameEntry.grid(row=0,column=1, padx=8)

phoneLabel= Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='aquamarine1', fg='darkslateblue')
phoneLabel.grid(row=0,column=2, padx=20,pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15),bd=7, width=22)
phoneEntry.grid(row=0,column=3, padx=8)

billLabel= Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='aquamarine1', fg='darkslateblue')
billLabel.grid(row=0,column=4, padx=20,pady=2)

billEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=22)
billEntry.grid(row=0,column=5, padx=8)

searchBtn = Button(customer_details_frame,text="SEARCH",width=10,font=('times new roman', 15,'bold'), command= search_bill)
searchBtn.grid(row=0,column=7,padx=20,pady=8)

pdtsFrame = Frame(root)
pdtsFrame.pack(pady=10, fill=X)

cosmeticsFrame= LabelFrame(pdtsFrame,text='Cosmetics', font=('times new roman',15,'bold'), fg='darkslateblue', bd=8,relief=GROOVE,bg='aquamarine1')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmeticsFrame,text='Bath Soap', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
bathsoapLabel.grid(row=0,column=0,pady=9,sticky='w')


bathsoapEntry= Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticsFrame,text='Face Cream', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
facecreamLabel.grid(row=1,column=0,pady=9,sticky='w')

facecreamEntry= Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)


facewashLabel = Label(cosmeticsFrame,text='Face Wash', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
facewashLabel.grid(row=2,column=0,pady=9,sticky='w')

facewashEntry= Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)


hairsprayLabel = Label(cosmeticsFrame,text='Hair Spray', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
hairsprayLabel.grid(row=3,column=0,pady=9,sticky='w')


hairsprayEntry= Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)


hairgelLabel = Label(cosmeticsFrame,text='Hair Gel', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
hairgelLabel.grid(row=4,column=0,pady=9,sticky='w')

hairgelEntry= Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)


bodylotionLabel = Label(cosmeticsFrame,text='Body Lotion', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
bodylotionLabel.grid(row=5,column=0,pady=9,sticky='w')

bodylotionEntry= Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame= LabelFrame(pdtsFrame,text='Groceries', font=('times new roman',15,'bold'), fg='darkslateblue', bd=8,relief=GROOVE,bg='aquamarine1')
groceryFrame.grid(row=0,column=1)


riceLabel = Label(groceryFrame,text='Rice', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
riceLabel.grid(row=0,column=0,pady=9,sticky='w')

riceEntry= Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)


DalLabel = Label(groceryFrame,text='Dal', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
DalLabel.grid(row=1,column=0,pady=9,sticky='w')

DalEntry= Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
DalEntry.grid(row=1,column=1,pady=9,padx=10)
DalEntry.insert(0,0)


WheatLabel = Label(groceryFrame,text='Wheat', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
WheatLabel.grid(row=2,column=0,pady=9,sticky='w')

WheatEntry= Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
WheatEntry.grid(row=2,column=1,pady=9,padx=10)
WheatEntry.insert(0,0)


SugarLabel = Label(groceryFrame,text='Sugar', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
SugarLabel.grid(row=3,column=0,pady=9,sticky='w')

SugarEntry= Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
SugarEntry.grid(row=3,column=1,pady=9,padx=10)
SugarEntry.insert(0,0)


TeaLabel = Label(groceryFrame,text='Tea', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
TeaLabel.grid(row=4,column=0,pady=9,sticky='w')

TeaEntry= Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
TeaEntry.grid(row=4,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)


CoffeeLabel = Label(groceryFrame,text='Coffee', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
CoffeeLabel.grid(row=5,column=0,pady=9,sticky='w')

CoffeeEntry= Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
CoffeeEntry.grid(row=5,column=1,pady=9,padx=10)
CoffeeEntry.insert(0,0)

drinksFrame= LabelFrame(pdtsFrame,text='Cold Drinks', font=('times new roman',15,'bold'), fg='darkslateblue', bd=8,relief=GROOVE,bg='aquamarine1')
drinksFrame.grid(row=0,column=2)


PepsiLabel = Label(drinksFrame,text='Pepsi', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
PepsiLabel.grid(row=0,column=0,pady=9,sticky='w')

PepsiEntry= Entry(drinksFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
PepsiEntry.grid(row=0,column=1,pady=9,padx=10)
PepsiEntry.insert(0,0)


SpriteLabel = Label(drinksFrame,text='Sprite', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
SpriteLabel.grid(row=1,column=0,pady=9,sticky='w')

SpriteEntry= Entry(drinksFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
SpriteEntry.grid(row=1,column=1,pady=9,padx=10)
SpriteEntry.insert(0,0)


LimcaLabel = Label(drinksFrame,text='Limca', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
LimcaLabel.grid(row=2,column=0,pady=9,sticky='w')

LimcaEntry= Entry(drinksFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
LimcaEntry.grid(row=2,column=1,pady=9,padx=10)
LimcaEntry.insert(0,0)


CokeLabel = Label(drinksFrame,text='Coke', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
CokeLabel.grid(row=3,column=0,pady=9,sticky='w')

CokeEntry= Entry(drinksFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
CokeEntry.grid(row=3,column=1,pady=9,padx=10)
CokeEntry.insert(0,0)


FantaLabel = Label(drinksFrame,text='Fanta', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
FantaLabel.grid(row=4,column=0,pady=9,sticky='w')

FantaEntry= Entry(drinksFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
FantaEntry.grid(row=4,column=1,pady=9,padx=10)
FantaEntry.insert(0,0)


MountainDewLabel = Label(drinksFrame,text='Mountain Dew', font=('times new roman', 15, 'bold'), bg='aquamarine1',fg='darkslateblue')
MountainDewLabel.grid(row=5,column=0,pady=9,sticky='w')

MountainDewEntry= Entry(drinksFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
MountainDewEntry.grid(row=5,column=1,pady=9,padx=10)
MountainDewEntry.insert(0,0)


billframe= Frame(pdtsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=40)

billareaLabel = Label(billframe,text='Billing Area', font=('times new roman', 15, 'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scroll= Scrollbar(billframe,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
textarea= Text(billframe,height=19,width=78,yscrollcommand= scroll.set)
textarea.pack()
scroll.config(command=textarea.yview)

billmenuFrame= LabelFrame(root,text='Bill Menu', font=('times new roman',15,'bold'), fg='darkslateblue', bd=8,relief=GROOVE,bg='aquamarine1')
billmenuFrame.pack(fill=X)

cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price', font=('times new roman', 13, 'bold'), bg='aquamarine1',fg='darkslateblue')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,sticky='w',padx=5)

cosmeticpriceEntry= Entry(billmenuFrame,font=('times new roman', 13, 'bold'),width=20,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel = Label(billmenuFrame,text='Grocery Price', font=('times new roman', 13, 'bold'), bg='aquamarine1',fg='darkslateblue')
grocerypriceLabel.grid(row=1,column=0,pady=6,sticky='w',padx=5)

grocerypriceEntry= Entry(billmenuFrame,font=('times new roman', 13, 'bold'),width=20,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel = Label(billmenuFrame,text='Drinks Price', font=('times new roman', 13, 'bold'), bg='aquamarine1',fg='darkslateblue')
drinkspriceLabel.grid(row=2,column=0,pady=6,sticky='w',padx=5)

drinkspriceEntry= Entry(billmenuFrame,font=('times new roman', 13, 'bold'),width=20,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmetictaxLabel = Label(billmenuFrame,text='Cosmetic Tax', font=('times new roman', 13, 'bold'), bg='aquamarine1',fg='darkslateblue')
cosmetictaxLabel.grid(row=0,column=2,pady=6,sticky='w',padx=5)

cosmetictaxEntry= Entry(billmenuFrame,font=('times new roman', 13, 'bold'),width=20,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax', font=('times new roman', 13, 'bold'), bg='aquamarine1',fg='darkslateblue')
grocerytaxLabel.grid(row=1,column=2,pady=6,sticky='w',padx=5)

grocerytaxEntry= Entry(billmenuFrame,font=('times new roman', 13, 'bold'),width=20,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinksTaxLabel = Label(billmenuFrame,text='Drinks Tax', font=('times new roman', 13, 'bold'), bg='aquamarine1',fg='darkslateblue')
drinksTaxLabel.grid(row=2,column=2,pady=6,sticky='w',padx=5)

drinksTaxEntry= Entry(billmenuFrame,font=('times new roman', 13, 'bold'),width=20,bd=5)
drinksTaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=100,pady=35)

totalbtn = Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='aquamarine1',fg='darkslateblue',bd=5,width=8,pady=10, command=total)
totalbtn.grid(row=0,column=0,pady=20,padx=5)

Billbtn = Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='aquamarine1',fg='darkslateblue',bd=5,width=8,pady=10, command= bill_area)
Billbtn.grid(row=0,column=1,pady=20,padx=5)

Emailbtn = Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='aquamarine1',fg='darkslateblue',bd=5,width=8,pady=10)
# Emailbtn = Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='aquamarine1',fg='darkslateblue',bd=5,width=8,pady=10, command= send_email)
Emailbtn.grid(row=0,column=2,pady=20,padx=5)

printbtn = Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='aquamarine1',fg='darkslateblue',bd=5,width=8,pady=10,command=print_bill)
printbtn.grid(row=0,column=3,pady=20,padx=5)

clearbtn = Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='aquamarine1',fg='darkslateblue',bd=5,width=8,pady=10, command= clear)
clearbtn.grid(row=0,column=4,pady=20,padx=5)




root.mainloop()
