from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Height", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
height_label.place(x=20, y=125)

h=Entry(window, text="", bd=2, width=22)
h.place(x=150, y=125)

weight_label=Label(window, text="Weight", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
weight_label.place(x=20, y=150)

w=Entry(window, text="", bd=2, width=22)
w.place(x=150, y=150)

def calculateBMI ():
    height = int(h.get())/100
    weight = int(w.get())

    BMI = weight/(height*height)
    BMI = round(BMI, 1)

    name = username.get()

    result_label.destroy()

    msg = ""

    if BMI < 18.5:
        msg = "you are underweight"
    elif BMI > 18.5 and BMI <= 24.9:
        msg = "you are healthy"
    elif BMI > 24.9 and BMI <=29.9:
        msg = "you are overweight"
    elif BMI > 30:
        msg = "you are obese"
    else:
        msg = "something went wrong"

    message = Label(result_frame, text= name + "Your BMI is"+ str(BMI) + msg, fg = "black", bg = "white", font=("Calibri", 12))
    message.place(x=20,y=40)
    message.pack()

calculate_button = Button(window, text="calculate BMI", fg = "black", bg = "white", bd=4, command = calculateBMI)
calculate_button.place(x=150, y=200)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()