import keyboard
import threading
import time
import tkinter as tk

currentkey = 0

sentence = "This is a sentence"

window = tk.Tk()
window.title("Typing")
window.geometry("400x100")

frame = tk.Frame(window)
frame.pack()

paddingtextleft = tk.Label(frame,text=sentence[0:currentkey],font=("Arial",16),fg="black")
typingtext = tk.Label(frame,text=sentence[currentkey],font=("Arial",16),fg="green")
paddingtextright = tk.Label(frame,text=sentence[currentkey+1:len(sentence)+1],font=("Arial",16),fg="grey")
paddingtextleft.pack(side="left")
typingtext.pack(side="left")
paddingtextright.pack(side="left")

wpmtime = 0

def starttyping():
    global currentkey
    global wpmtime
    while True:
        keypressed = keyboard.read_key()
        if keypressed == sentence[currentkey] or (keypressed == 'space' and sentence[currentkey] == " "):
            currentkey += 1
            if currentkey == 1:
                wpmtime = time.time()
            elif currentkey == len(sentence):
                window.quit()
                timetotype = (time.time()-wpmtime)/60
                print((len(sentence)/5)/timetotype)
                break
            paddingtextleft.config(text=sentence[0:currentkey])
            typingtext.config(text=sentence[currentkey])
            paddingtextright.config(text=sentence[currentkey+1:len(sentence)+1])

def connection(event):
    startbutton.destroy()
    typingthread = threading.Thread(target=starttyping)
    typingthread.start()

startbutton = tk.Button(window,text="Start",relief="raised")
startbutton.bind('<Button-1>',connection)
startbutton.pack()

window.mainloop()
