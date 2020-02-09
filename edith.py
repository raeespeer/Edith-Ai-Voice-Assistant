import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from tkinter import *
from ttkthemes import ThemedStyle
from pygame import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


win=Tk()
win.title('E.D.I.T.H')
style=ttk.Style()
style.theme_use("default")
main=ttk.Entry(win,font=("Montserrat"))
main.place(x=65,y=90)
win.configure(bg="#000506")
lbl1=ttk.Label(win,text='E.D.I.T.H' ,font=('Montserrat',30),background="#000506",foreground="white")
lbl1.place(x=100, y=10)
lbl2=ttk.Label(win, text='Query',font=('Montserrat',14),background="#000506",foreground="white")
lbl2.grid(row=0,column=0)
lbl2.place(x=35,y=142)
entry1=ttk.Entry(win,width=28)
entry1.grid(row=0,column=1)
entry1.place(x=100,y=150)
t2=StringVar()
# def callback():
#     global music_dir
#     music_dir= filedialog.askdirectory()    
# errmsg = 'Error!'
# dir_m=ttk.Button(text='Set your music directory!',command=callback)
# dir_m.place(x=110,y=250)
def stop():
    speak("Thank you Sir!...")
    win.destroy()


def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices= engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        wishes="Good Morning"
    elif hour>=12 and hour<18:
        wishes="Good Afternoon"         
    else:
        wishes="Good Evening"
    
    main.delete(0,END)
    speak(wishes)
    main.insert(0,wishes)
    win.update()

def sendEmail():

    global email
    
    main.delete(0,END)
    main.insert(0,"Wait a second...")
    win.update()
    speak('Wait a second...')
    speak('Enter Recipient''s Email id and Password')
    main.delete(0,END)
    main.insert(0,"Enter Recipient''s Email id and Password")
    win.update()
    email=Toplevel()
    email.configure(bg="#000506")
    email.title("Enter Email ID and Password")
    email.geometry("350x400")
 
    global username
    global password
    global username_entry
    global password_entry
    global con
    global content
    global myid
    global myid_ref
    username = StringVar()
    password = StringVar()
    con=StringVar()
    myid_ref=StringVar()
    ttk.Label(email, text="").pack()
    ttk.Label(email,text="Enter Your Email ID ",font=("Montserrat",15)).pack()
    myid=ttk.Entry(email,textvariable=myid_ref)
    myid.pack()
    ttk.Label(email, text="").pack()
    ttk.Label(email,text="Your Password ",font=("Montserrat",15)).pack()
    password_entry = Entry(email,show="*",textvariable=password)
    password_entry.pack()
    
    ttk.Label(email, text="").pack()
    ttk.Label(email,text="Recipient's Email ID  ",font=("Montserrat",15)).pack()
    username_entry = ttk.Entry(email,textvariable=username)
    username_entry.pack()
    ttk.Label(email, text="").pack()
    
    ttk.Label(email,text="Message ",font=("Montserrat",15)).pack()
    content=ttk.Entry(email,textvariable=con)
    content.pack()
    ttk.Label(email, text="").pack()
    submit = ttk.Button(email, text="Submit", command=confirmsend)
    submit.pack()

def confirmsend():
    
    # if username and password are valid:
    #to=input("Enter recipient's emaild id")           
    to=username.get()
    ps=password.get()
    my=myid_ref.get()
    f=open('C:\\Users\\Raees\\Desktop\\Project 1\\Edith\\p.txt','w')  
    # f.write(getpass.getpass('Enter Password:',stream=None))
    f.write(ps)
    f.close()
    f=open('C:\\Users\\Raees\\Desktop\\Project 1\\Edith\\p.txt','r')
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(my,f.read())
    server.sendmail(my,to,con.get())
    main.delete(0,END)
    main.insert(0,"Email has been succesfully delivered...")
    win.update()
    speak("Email has been succesfully delivered...")
    email.destroy()
    server.close()    
    f=open('C:\\Users\\Raees\\Desktop\\Project 1\\Edith\\p.txt','w')
    f.write('Haha, you thought there will be password here?')
    f.close()



def takeCommand():
    entry1.delete(0,END)
    speak('Hello this is Edith , How may i help you?')
    mixer.init()
    mixer.music.load("C:\\Users\\Raees\\Desktop\\Project 1\\Edith\\ding.mp3")
    mixer.music.play()
    n=sr.Recognizer()
    # n.pause_threshold=1
    n.energy_threshold=300
    
    
    with sr.Microphone() as source:
        n.adjust_for_ambient_noise(source)
        # n.record(source,offset=2.5,duration=3)
        # print("Listening...")
        main.delete(0,END)
        main.insert(0,"Listening...")
        win.update()
        # entry1.delete(0,END)
        # entry1.insert(0,"Listening...")
        try:
            audio=n.listen(source)
            mixer.music.load('C:\\Users\\Raees\\Desktop\\Project 1\\Edith\\ding.mp3')
            mixer.music.play()
            query=str(n.recognize_google(audio,language='en-in'))
            main.delete(0,END)
            main.insert(0,"Recognizing...")
            win.update()
            query=query.lower()
            # query="wikipedia raees"
            # query="play music"
            # query="email"
            mixer.music.load('C:\\Users\\Raees\\Desktop\\Project 1\\Edith\\ding.mp3')
            mixer.music.play()
            entry1.focus()
            entry1.delete(0,END)
            entry1.insert(0,query)
            #print(f'User said: {query}\n')    
            # c=0
            # c+=1     
            
            if 'stop' in query:               
                speak('do you want to continue?')
                mixer.music.load('ding.mp3')
                mixer.music.play()
                if query=='yes':
                    takeCommand()
                else:
                    speak('Thank you sir')
                    exit(1)
            #Logic for executing tasks based on query
            if "wikipedia" in query:
                speak('Searching for your query in Wikipedia')
                query = query.replace('wikipedia','')
                        
                results=wikipedia.summary(query,sentences=2)

                speak('According to Wikipedia')
                # print(results)
                t=Toplevel()
                t.title("Wikipedia")
                t.configure(bg="black")
                ent=ttk.Entry(t,font=('Montserrat',10),width=50)
                ent.grid(row=0,padx=5,pady=10,ipady=3)
                ent.delete(0,END)
                ent.insert(0,results)
                win.update()
                speak(results)
                t.destroy()
            elif 'youtube' in query:
                query=query.replace('youtube','')
                webbrowser.open('https://www.youtube.com/results?search_query='+query)

            elif 'google' in query:
                query=query.replace('google','')
                webbrowser.open('https://www.google.co.in/search?q='+query)
            
            elif 'gaana' in query: 
                webbrowser.open('gaana.com'+query)
            elif 'play music' in query:              
                
                music_dir=filedialog.askdirectory()
                # music_dir='D:\\SANKAR NAGAR\\Desktop\\general\\3 pm'
                songs=os.listdir(music_dir)
                # for i in range(len(songs)):
                #     print(str(songs[i])+' ',end=' \n ')

                os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime('%H:%M:%S')
                main.delete(0,END)
                main.insert(0,strTime)
                win.update()
                # print(strTime)
                speak(f'Sir, the time is {strTime}')
            elif 'date' in query:
                strDate=datetime.datetime.today()
                speak(f'Sir, the date is {strDate}')
            elif 'how are you' in query:
                print('I am happy since i have a person like you to interact with , he he he'+query)
                speak('I am happy since i have a person like you to interact with , he he he')

            elif 'email' in query:
                try:
                    sendEmail()
                except Exception as e:
                    print(e)
                    print('Sorry , Email has not been sent!')
                    speak('Sorry , Email has not been sent!')
            else:
                pass
        
        except Exception as e:
            # print(e)
            # print('Repeat that again, Please...')
            main.delete(0,END)
            main.insert(0,"Sorry Couldn't recognize you , please tap on the search button again...")
            speak("Sorry Couldn't recognize you , please tap on the search button again...")
            win.update()


# entry1.bind('<Return>',get)
wishMe()
btn1 = ttk.Button(win,text='Search',command=takeCommand,style='white/black.TButton')
btn1.grid(row=2,column=4)
btn1.place(x=120, y=180)
btn2=ttk.Button(win, text='End',command=stop,style='white/black.TButton')
btn2.grid(row=2,column=6)
btn2.place(x=180, y=180)
entry1.focus()
win.geometry("360x500")
win.mainloop()
# k.t2.delete(0,END)
# k.t2.insert(0,wishes)