# project.....1.........
from tkinter import *  # we import class and files to our code to create ui and gui
from tkinter import messagebox
import pyttsx3
import json
from difflib import get_close_matches
engine = pyttsx3.init()
engine.runAndWait()

# get_close_matches(word,possibilities,sequence,cutoff,n)
# close_matche=get_close_matches('appel',['ape','apple','app'])
# print(close_matche)
# functionality part

def searchFunction():
    data = json.load(open('data.json'))
    word = entryfield.get()  # RAIN
    word = word.lower()  # rain
    textarea.delete(0.0, END)

    # matches = get_close_matches(word, data.keys(),cutoff=.8)
    # print(matches[0])

    if word in data:
        textarea.config(state=NORMAL)
        meaning = data[word]

        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')

        textarea.config(state=DISABLED)

    elif len(get_close_matches(word, data.keys())) > 0:

        close_match = get_close_matches(word, data.keys())[0]

        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')

        if res == True:

            meaning = data[close_match]
            textarea.delete(1.0, END)
            textarea.config(state=NORMAL)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')

            textarea.config(state=DISABLED)

        else:
            textarea.delete(1.0, END)
            messagebox.showinfo('Information', 'Please type a correct word')
            entryfield.delete(0, END)

    else:
       messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
       entryfield.delete(0, END)


def meaningAudio():
    data2 = textarea.get(0.0, END)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # to set reading speed
    # volume = engine.getProperty('volume')
    # engine.setProperty('volume', 1)  # to set volume
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)  # to set male or female voices
    # print(data2)
    engine.say(data2)
    engine.runAndWait()


def wordAudio():
    data1 = entryfield.get()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # to set reading speed
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1)  # to set volume
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # to set male or female voices
    print(data1)
    engine.say(data1)
    engine.runAndWait()


def clear():
    textarea.delete(0.0, END)
    entryfield.delete(0, END)


def exit_window():
    result = messagebox.askyesno("confirm", "Do you want to exit?")
    if result == True:
        root.destroy()
    else:
        messagebox.showinfo('Title', 'ok as you wish continue learning')


root = Tk()  # this is class because the T is in capital
root.title("Dictionary by Arslan")  # root i is object  here
root.geometry("1000x626+50+50")
root.resizable(False, False)  # or (0,0)    to disable minimize button

backgroundImage = PhotoImage(file='bg.png')
bglabel = Label(root, image=backgroundImage)

bglabel.place(x=0, y=0)
bglabel.grid(row=0, column=0)

wordLabel = Label(root, text='Enter word', font=('Arial', 29, 'bold'), background='white', foreground='red')
wordLabel.place(x=600, y=40)

entryfield = Entry(root, font=('Arial', 15, 'italic'), bd=6, relief=RIDGE)
entryfield.place(x=600, y=120)

searchbutton = PhotoImage(file='search.png')
search1button = Button(root, image=searchbutton, bd=0, cursor='hand2', command=searchFunction)
search1button.place(x=620, y=170)

micbutton = PhotoImage(file='mic.png')
mic1button = Button(root, image=micbutton, bd=0, cursor='hand2', command=wordAudio)
mic1button.place(x=720, y=172)

wordLabe2 = Label(root, text='MEANING', font=('Arial', 20, 'bold'), background='white', foreground='red', bd=0)
wordLabe2.place(x=630, y=250)

textarea = Text(root, font=('arial', 18, 'bold'), width=34, height=8, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=500, y=300)

microphoneImage = PhotoImage(file='microphone.png')
microphoneButton = Button(root, image=microphoneImage, bd=0, cursor='hand2', command=meaningAudio)
microphoneButton.place(x=550, y=550)

clearImage = PhotoImage(file='clear.png')
clearButton = Button(root, image=clearImage, bd=0, cursor='hand2', command=clear)
clearButton.place(x=680, y=550)

exitImage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitImage, bd=0, cursor='hand2', command=exit_window)
exitButton.place(x=800, y=550)

root.mainloop()  # to display the code
