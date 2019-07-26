#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from tkinter import *
import requests
import urllib.request
from datetime import datetime
import webbrowser

#https://smsc.ru/

login = ''       
password = ''
#if you dont have sender name, delete the sender in the link
sender = ''
#up to 14 values
listbox_items = ['first', 'second', 'third']

def select_item(event):

        value = (listbox.get(listbox.curselection()))
        name = textName.get()
        time = textTime.get()
        printSms(value,name,time)

#up to 14 values    
def printSms(value,name,time):
        if value == 'first':
                text.delete('1.0', END)
                text.insert(INSERT,"Стоматология напоминает Вам "+ name +" о визите на завтра на "+ time +".Если у Вас не получается,  будем Вам очень благодарны, если  сообщите нам об отмене визита.")   
        if value == 'second':
                text.delete('1.0', END)
                text.insert (INSERT,"Стоматология напоминает Вам "+ name +" о визите на послезавтра на "+ time +".\nЕсли у Вас не получается,  будем Вам очень благодарны, если  сообщите нам об отмене визита.")   
        if value == 'third':
                text.delete('1.0', END)
                text.insert (INSERT,"Стоматология напоминает Вам "+ name +" о визите "+ time +".\nЕсли у Вас не получается,  будем Вам очень благодарны, если  сообщите нам об отмене визита.")  
        data = text.get('1.0', END)
        
        lblSumvols['text'] = 'Symbols: '+ str(len(data))
        
        
def press():
        global login
        global password
        data = text.get('1.0', END)
        data.strip()
        name = textName.get()
        time = textTime.get()
        phone = textPhone.get()
        http = "https://smsc.ru/sys/send.php?login="+ login +"&psw="+password+"&phones="+phone+"&mes="+data+"&sender="+sender+"&charset=utf-8"
        print(http)
        print(requests.get(http))
        f = open('History.txt','a')
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        f.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"\t"+str(phone)+"\t"+ str(name) +"\t"+ str(time)+"\n")
        f.close()
        clear()
        
def read():        
        my_file = open('History.txt','r')
        my_string = my_file.read()
        clear()
        text.insert(1.0,my_string)
        my_file.close()

        
def clear():
        text.delete('1.0', END)
        textName.delete('0',END)
        textTime.delete('0',END)
        textPhone.delete('0',END)
        
def client_exit():
        exit()
#you must be login in ( https://smsc.ru/ )        
def browser():
        webbrowser.open('https://smsc.ru/sms/', new = 2)




root = Tk()
root.title('SMS')
root.geometry('500x500')


buttonSend = Button(root,text='Send',width=8,height=2, fg='red',font='arial 14', command=press)
buttonOut = Button(root,text='Exit',width=7,height=2, fg='red',font='arial 14',command=client_exit)
buttonHistory = Button(root,text='History',width=7,height=2, fg='red',font='arial 14',command=read)
buttonClear = Button(root,text='Clear',width=7,height=2, fg='red',font='arial 14',command=clear)
buttonBrowser = Button(root,text='Internet',width=7,height=1, fg='blue',font='arial 14',command=browser)

lblName = Label(root, text='Patient name:',font='Arial 16')
textName = Entry(root,width=32,font='Arial 14')

lblTime = Label(root, text='Appointment time:',font='Arial 16')
textTime = Entry(root,width=32,font='Arial 14')

lblPhone = Label(root, text='Phone:',font='Arial 16')
textPhone = Entry(root,width=32,font='Arial 14')

lblPhoneExaple = Label(root, text='(Example: 380991234567)',font='Arial 10')
lblSumvols = Label(root, text='Symbols: 0',font='Arial 10')

text = Text(root,height=10,width=45,font='Arial 14',wrap=WORD)

listbox = Listbox(root, width=15, height=14, font=('times', 13))
listbox.bind('<<ListboxSelect>>', select_item)


buttonSend.place(x=3,y=0)
buttonClear.place(x=100,y=0)
buttonHistory.place(x=185,y=0)
buttonOut.place(x=270,y=0)

listbox.place(x=360, y=10)

buttonBrowser.place(x=270,y=254)

lblSumvols.place(x=0,y=250)

lblName.place(x=0,y=70)
textName.place(x=0,y=100)
lblTime.place(x=0,y=130)
textTime.place(x=0,y=160)
lblPhone.place(x=0,y=190)
textPhone.place(x=0,y=220)
lblPhoneExaple.place(x=200,y=195)


text.place(x=0,y=300)

for item in listbox_items:
    listbox.insert(END, item)



root.mainloop()
