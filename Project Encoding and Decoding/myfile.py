from tkinter import *
from tkinter import messagebox
import random
import base64
import os

# sample_string = "GeeksForGeeks is the best"
# sample_string_bytes = sample_string.encode("ascii")
  
# base64_bytes = base64.b64encode(sample_string_bytes)
# base64_string = base64_bytes.decode("ascii")
  
# print(f"Encoded string: {base64_string}")




# base64_string =" R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
# base64_bytes = base64_string.encode("ascii")
  
# sample_string_bytes = base64.b64decode(base64_bytes)
# sample_string = sample_string_bytes.decode("ascii")
  
# print(f"Decoded string: {sample_string}")

def encrypt():
    password = code.get()

    if password == "1234":
        root1 = Toplevel(root)
        root1.title("Encryption")
        root1.geometry("400x200")
        # screen1.configure(bg="#ed3833")
         
        message = text1.get(1.0,END)
        encoded = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded)
        encrypt = base64_bytes.decode("ascii")

        Label(root1, text="ENCRYPT", font='calbri',bg="#ed3833").place(x=10,y=0)
        text2 = Text(root1,font="Roboto 12", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encyption", "Input Password")

    elif password!="1234":
        messagebox.showerror("encyption", "Invalid Password")
        
        
    
def decrypt():
    password = code.get()

    if password == "1234":
        root1 = Toplevel(root)
        root1.title("Decryption")
        root1.geometry("400x200")
        # screen1.configure(bg="#ed3833")
         
        message = text1.get(1.0,END)
        decoded = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded)
        encrypt = base64_bytes.decode("ascii")

        Label(root1, text="DECRYPT", font='calbri',bg="#5bcf28").place(x=10,y=0)
        text2 = Text(root1,font="Roboto 12", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("decyption", "Input Password")

    elif password!="1234":
        messagebox.showerror("decyption", "Invalid Password")
        

def mainscreen():

    global root
    global code
    global text1

    root = Tk()
    root.geometry('375x398')
    root.title("Encoder Decoder")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    
    Label(text="Enter text for encryption and decryption", fg="black", font=("arial",13)).place(x=10,y=10)
    text1 = Text(font='Roboto 20', bg="white", relief=GROOVE, wrap=WORD ,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    Label(text="Enter the secret key", font=("arial",13)).place(x=10,y=155)
    
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0, font=('calbri', 20),show="*").place(x=10, y=180)
    
    Button(text="ENCRYPT", height="2", width="20", bg="#ed3833",fg="white",command=encrypt,bd=0).place(x=10, y=240)
    Button(text="DECRYPT", height="2", width="20", bg="#5bcf28",fg="white",command=decrypt,bd=0).place(x=200, y=240)
    Button(text="RESET", height="2", width="47", bg="#1089ff",fg="white",command=reset,bd=0).place(x=10, y=290)








    root.mainloop()

mainscreen()

