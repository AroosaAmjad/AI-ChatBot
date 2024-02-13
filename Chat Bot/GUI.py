# from tkinter import*
# from PIL import Image, ImageTk
# import speechTOtext
# import action
# root = Tk()
# root.title("ChatBot")
# root.geometry("675x675")
# root.resizable(False, False)
# root.config(bg="#F5F5F5")


# def ask():
#     user_val = speechTOtext.speech_to_text()
#     bot_val = action.action(user_val)
#     text.insert(END, 'User--->'+ user_val+"\n")
#     if bot_val != None:
#         text.insert(END, "BOT <---"+ str(bot_val)+"\n")
#     if bot_val == " ":
#         root.destroy()
    

# def send():
#     send = entry.get()
#     bot= action.action(send)
#     if bot != None:
#         text.insert(END, "BOT <---"+str(bot)+"\n")
#     if bot == " ":
#         root.destroy()


# def delete():
#     text.delete("1.0", "end")

# frame = LabelFrame(root, padx=100, pady=7, borderwidth= 3, relief= "raised")
# frame.config(bg="#F5F5F5")
# frame.grid(row= 0, column= 1, padx= 55, pady= 10)
# text = Text(root, font=('courier 10 bold'), bg="#333333", fg="#FFFFFF")  # Use white text for better visibility

# text_label = Label(frame, text="ChatBot", font=("comic Sans ms", 14, "bold"), bg="#1E90FF", fg="#FFFFFF")  # White text for better visibility
# text_label.grid(row= 0, column= 0, padx= 20, pady= 10)

# image= ImageTk.PhotoImage(Image.open("avatar.png"))
# image_label= Label(frame, image=image)
# image_label.grid(row=1, column = 0 ,pady=5)

# text = Text(root, font= ('courier 10 bold'), bg = "#356696")
# text.grid(row=3, column=1)
# text.place(x=100, y= 375, width= 375, height= 100)

# entry = Entry(root, justify=CENTER, bg="#DDDDDD")
# entry.place(x=100, y=500, width=350, height=30)

# Button1 = Button(root, text="Ask", bg="#1E90FF", fg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
# Button1.place(x= 70, y=575)

# Button2 = Button(root, text="Send", bg="#1E90FF", fg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
# Button2.place(x= 400, y=575)

# Button3 = Button(root, text="Delete", bg="#1E90FF", fg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
# Button3.place(x= 225, y=575)

# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import speechTOtext
import action

root = Tk()
root.title("ChatBot")
root.geometry("675x675")
root.resizable(False, False)
root.config(bg="#F5F5F5")

def ask():
    user_val = speechTOtext.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, 'User ---> ' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "BOT <--- " + str(bot_val) + "\n")
    if bot_val == "":
        root.destroy()

def send():
    user_input = entry.get()
    bot_response = action.action(user_input)
    if bot_response is not None:
        text.insert(END, "BOT <--- " + str(bot_response) + "\n")
    if bot_response == "":
        root.destroy()

def delete():
    text.delete("1.0", "end")

frame = LabelFrame(root, padx=50, pady=7, borderwidth=3, relief="raised", bg="#F5F5F5")
frame.grid(row=0, column=1, padx=25, pady=10, sticky="nsew")

text_label = Label(frame, text="ChatBot", font=("Comic Sans MS", 18, "bold"), bg="#1E90FF", fg="#FFFFFF")
text_label.grid(row=0, column=0, padx=10, pady=5)

image = ImageTk.PhotoImage(Image.open("avatar.png").resize((300,300)))
image_label = Label(frame, image=image, bg="#F5F5F5")
image_label.grid(row=1, column=0, pady=5)

text = Text(root, font=('Courier New', 12, 'bold'), bg="#333333", fg="#FFFFFF", wrap=WORD)
text.grid(row=2, column=1, padx=10, pady=5, rowspan=2, sticky="nsew")

entry = Entry(root, justify=CENTER, bg="#DDDDDD", font=('Arial', 12))
entry.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")

Button1 = Button(root, text="Ask", bg="#1E90FF", fg="#FFFFFF", pady=12, padx=20, borderwidth=3, relief=SOLID, command=ask)
Button1.grid(row=5, column=0, padx=40, pady=10, sticky="w")

Button2 = Button(root, text="Send", bg="#1E90FF", fg="#FFFFFF", pady=12, padx=20, borderwidth=3, relief=SOLID, command=send)
Button2.grid(row=5, column=1, pady=10, sticky="w")

Button3 = Button(root, text="Delete", bg="#1E90FF", fg="#FFFFFF", pady=12, padx=20, borderwidth=3, relief=SOLID, command=delete)
Button3.grid(row=5, column=2, pady=10, sticky="w")

# Configure grid weights to make resizing more responsive
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
