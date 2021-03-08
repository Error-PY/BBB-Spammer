import tkinter
from tkinter import *
import time
import keyboard
import selenium
from selenium import webdriver
root = Tk()


PATH = ".\CHROMEDRIVER.exe"

driver = webdriver.Chrome(PATH)

NAME = Label(root, text="BBB Konferenzen Spammer")
NAME.pack()

SPACE = Label(root, text=" ")
SPACE.pack()


LINK_NAME = Label(root, text="ISERV Konferenzen Link:")
LINK_NAME.pack()

LINK = Entry(root,width=50,bg="grey",fg="black")
LINK.pack()

NAME_EMAIL = Label(root, text="ISERV Benutzername:")
NAME_EMAIL.pack()

EMAIL = Entry(root,width=50,bg="grey",fg="black")
EMAIL.pack()

NAME_PASSWORD = Label(root, text="ISERV Passwort:")
NAME_PASSWORD.pack()

PASSWORD = Entry(root,width=50,bg="grey",fg="black")
PASSWORD.pack()


howMuch_info = Label(root,text="How much to connect?")
howMuch_info.pack()
howMuch= Entry(root,width=50,bg="grey",fg="black")
howMuch.pack()

def login():
    time.sleep(2)
    driver.get(LINK.get())
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="form-username"]/input').send_keys(EMAIL.get())
    driver.find_element_by_xpath('//*[@id="form-password"]/input').send_keys(PASSWORD.get())
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/form/div[3]/div[1]/button').click()
    time.sleep(6)
    x = 0
    while (x < int(howMuch.get())):
        time.sleep(0.5)
        keyboard.press_and_release("ctrl+t")
        keyboard.write(LINK.get())
        keyboard.press_and_release("enter")
        x = x + 1


START = Button(root, text="Start Connecting!", command=login)
START.pack()

root.mainloop()
