import tkinter as tk

import csv

class user:
    access = True
    username = ""
    password = ""
    def __init__(self, username, password):
        self.username = username
        self.password = password

def enter():
    global usernamee
    global passworde
    global incorrectdisplay
    usernamematch = False
    passwordmatch = False
    userentered = user(usernamee.get(), passworde.get())
    with open('/Users/timrandall/Projects/passwordentry/userinfo.csv', mode='r') as file1:
        csvreadah = csv.reader(file1, delimiter=',')
        for row in csvreadah:
            for item in row:
                if item == userentered.username:
                    usernamematch = True
                else:
                    pass
                if item == userentered.password:
                    passwordmatch = True
                else:
                    pass
        if passwordmatch == True and usernamematch == True:
            win2 = tk.Tk()
            enterl = tk.Label(win2, text="Access granted!")
            enterl.grid(column=0, row=0)
            win1.destroy()
            win2.geometry('400x300')
            win2.title("^^ U got in!! ^^")
            win2.mainloop()
        else:
            incorrectdisplay['text'] = "Incorrect name or password"
            usernamee.delete(0, tk.END)
            passworde.delete(0, tk.END)

def enter_new_info():
    global win3
    global giveusernamee
    global givepassworde
    newuser = user(giveusernamee.get(), givepassworde.get())
    lst = [newuser.access, newuser.username, newuser.password]
    with open('/Users/timrandall/Projects/passwordentry/userinfo.csv', mode='a') as file1:
        write1 = csv.writer(file1, delimiter=',')
        write1.writerow(lst)
    first_win()

def newuser():
    global giveusernamee
    global givepassworde
    global win3
    global win1
    win3 = tk.Tk()
    explain2l = tk.Label(win3, text="Make up a username and password")
    explain2l.grid(column=0, row=0)
    giveusernamel = tk.Label(win3, text="Enter a username for yourself:")
    giveusernamel.grid(column=0, row=1)
    givepasswordl = tk.Label(win3, text="Enter a password for yourself:")
    givepasswordl.grid(column=0, row=2)
    giveusernamee = tk.Entry(win3, width=15)
    giveusernamee.grid(column=1, row=1)
    givepassworde = tk.Entry(win3, width=15)
    givepassworde.grid(column=1, row=2)
    enternewb = tk.Button(win3, text="Create new user", command=enter_new_info)
    enternewb.grid(column=1, row=3)
    win1.destroy()
    win3.geometry('400x300')
    win3.title("Give me your info! ^^")
    win3.mainloop()

def first_win():
    global win1
    global usernamee
    global passworde
    global incorrectdisplay
    win1 = tk.Tk()
    win1.geometry('400x300')
    win1.title("Give me your username and password")
    explainl = tk.Label(win1, text="Enter your username and password!")
    explainl.grid(column=0, row=0)
    usernamel = tk.Label(win1, text="Username:")
    usernamel.grid(column=0, row=1)
    passwordl = tk.Label(win1, text="Password:")
    passwordl.grid(column=0, row=2)
    usernamee = tk.Entry(win1, width=15)
    usernamee.grid(column=1, row=1)
    passworde = tk.Entry(win1, width=15)
    passworde.grid(column=1, row=2)
    enterb = tk.Button(win1, text="Enter", command=enter)
    enterb.grid(column=1, row=3)
    newuserb = tk.Button(win1, text="New user", command=newuser)
    newuserb.grid(column=0, row=3)
    incorrectdisplay = tk.Label(win1, text='')
    incorrectdisplay.grid(column=0, row=4)
    win1.mainloop()
first_win()
