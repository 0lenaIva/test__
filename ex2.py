from customtkinter import *

app = CTk()
app.geometry('500x400')
k = 625/500

def adaptive():
    global k
    #print(app.winfo_width())
    x = app.winfo_width()/k - btn.winfo_width()/k
    y = app.winfo_height()/ k - btn.winfo_height()/k
    btn.place(x = x, y = y)
    app.after(50, adaptive)

btn = CTkButton(app, text='Click', 
                width=100, height=75)
btn.place(x=500-100,
          y = 400-75)
adaptive()
app.mainloop()