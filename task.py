from tkinter import *
import pyttsx3

# إنشاء النافذة الرئيسية
myframe = Tk()
myframe.title("Text to Speech")
myframe.geometry("500x300")

# دالة تحويل النص إلى كلام
def function():
    Entry = mytext.get()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(Entry)
    engine.runAndWait()

# دالة مسح النص
def clear_text():
    mytext.delete(0, 'end')

# العناصر الرسومية
mylabel = Label(myframe, text="Text to speech", font="Tahoma 20 bold")
mylabel.pack(pady=30)

mytext = Entry(myframe, width="70")
mytext.pack(pady=5)

Play_button = Button(myframe, text="Play", command=function)
Play_button.pack(padx=20, pady=10)

Exit_button = Button(myframe, text="Exit", command=myframe.destroy)
Exit_button.pack(padx=10, pady=10)

Set_button = Button(myframe, text="Set", command=clear_text)
Set_button.pack(padx=10, pady=10)

# تشغيل الواجهة
myframe.mainloop()




    
