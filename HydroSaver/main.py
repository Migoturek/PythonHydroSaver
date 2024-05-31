import sqlite3
import os

from tkinter import *
import customtkinter
from PIL import Image

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data


def add_user(nazwa, email, haslo):
    conn = sqlite3.connect('moja_baza_danych.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Uzytkownicy (nazwa, email, haslo) VALUES (?, ?, ?)", (nazwa, email, haslo))
    conn.commit()
    conn.close()
def mylogin():


    close()

    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("500x600")
    new_window.resizable(False, False)  #szerokosć, Długość wyłączenie możliwości resize okienka
    new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    new_window.pack(pady=20, padx=60, fill="both", expand=True)
    frame = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Logowanie", font=("Roboto", 24))
    label.pack(pady=12, padx=10)
    email = customtkinter.CTkEntry(master=frame, placeholder_text="Podaj Email: ")
    email.pack(pady=12, padx=10)
    password = customtkinter.CTkEntry(master=frame, placeholder_text="Podaj Hasło: ", show="*")
    password.pack(pady=12, padx=10)
    button = customtkinter.CTkButton(master=frame, text="Zaloguj",command=login)
    button.pack(pady=12, padx=10)

    user = username.get()
    email = email.get()
    password = password.get()

    if not email.strip() or not password.strip():
        messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
    else:
        add_user(email, password)
        messagebox.showinfo("Sukces", "Konto zostało utworzone.")


def toilet():
    close()
    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("1600x900")
    new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Test")
    new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    new_window.pack(pady=20, padx=60, fill="both", expand=True)
    print()


def kitchen():
    close()
    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("800x600")
    new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Test")
    new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    new_window.pack(pady=20, padx=60, fill="both", expand=True)


def garden():
    close()
    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("1600x900")
    new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Test")
    new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    new_window.pack(pady=20, padx=60, fill="both", expand=True)
    print()


def basement():
    close()
    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("1600x900")
    new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Test")
    new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    new_window.pack(pady=20, padx=60, fill="both", expand=True)
    print()


def garage():
    close()
    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("1600x900")
    new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Test")
    new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    new_window.pack(pady=20, padx=60, fill="both", expand=True)
    print()

def button_click():

    plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])


    # Create a window and add charts
    root = tk.Tk()
    root.title("Statystyki")
    root.state('zoomed')

    side_frame = tk.Frame(root, bg="#4C2A85")
    side_frame.pack(side="left", fill="y")

    label = tk.Label(side_frame, text="Statystyki", bg="#4C2A85", fg="#FFF", font=25)
    label.pack(pady=50, padx=20)

    # Create a button widget
    # Create a button widget with custom styling
    button = tk.Button(side_frame, text="Click Me", command=button_click, bg="#4C2A85", fg="white", font=("Arial", 12),pady=12, padx=10, relief="raised")

    # Add the button to the window
    button.pack(pady=20)

    charts_frame = tk.Frame(root)

    charts_frame.pack()

    upper_frame = tk.Frame(charts_frame)
    upper_frame.pack(fill="both", expand=True)

def bathroom():
    close()
    #new_window = customtkinter.CTkToplevel()
    #new_window.title("HydroSaver")
    #new_window.geometry("800x600")
    #new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Test")
    #new_window = customtkinter.CTkFrame(master=new_window)  # graficzny interface
    #new_window.pack(pady=20, padx=60, fill="both", expand=True)
    #new_window = customtkinter.CTkProgressBar(master = new_window, orientation = "horizontal" )
    #new_window.pack(pady=40)




    #bath = np.random.normal(200000 , 25000, 5000)
    #plt.hist(bath, 50)
    #plt.show()

    plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

    # Chart 1: Bar chart of sales data
    fig1, ax1 = plt.subplots()
    ax1.bar(sales_data.keys(), sales_data.values())
    ax1.set_title("Dzienne zużycie wody w danym pokoju")
    ax1.set_xlabel("Pokój")
    ax1.set_ylabel("Litry")
    # plt.show()

    # Chart 2: Horizontal bar chart of inventory data
    fig2, ax2 = plt.subplots()
    ax2.barh(list(inventory_data.keys()), inventory_data.values())
    ax2.set_title("Na co najwięcej zużywamy wody")
    ax2.set_xlabel("Srednia ilość litrów")
    ax2.set_ylabel("Produkt")
    # plt.show()

    # Chart 3: Pie chart of product data
    fig3, ax3 = plt.subplots()
    ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
    ax3.set_title("Szacunkowy całościowy % zużycia wody \nw danym pomieszczeniu")
    # plt.show()

    # Chart 4: Line chart of sales by year
    fig4, ax4 = plt.subplots()
    ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
    ax4.set_title("Roczne zużycie wody")
    ax4.set_xlabel("Rok")
    ax4.set_ylabel("m^3")
    # plt.show()

    # Chart 5: Area chart of inventory by month
    fig5, ax5 = plt.subplots()
    ax5.fill_between(inventory_month_data.keys(),
                     inventory_month_data.values())
    ax5.set_title("Miesięczne zużycie wody")
    ax5.set_xlabel("Miesiąc")
    ax5.set_ylabel("m^3")
    # plt.show()

    # Create a window and add charts
    root = tk.Tk()
    root.title("Statystyki")
    root.state('zoomed')

    side_frame = tk.Frame(root, bg="#4C2A85")
    side_frame.pack(side="left", fill="y")

    label = tk.Label(side_frame, text="Statystyki", bg="#4C2A85", fg="#FFF", font=25)
    label.pack(pady=50, padx=20)

    # Create a button widget
    # Create a button widget with custom styling
    button = tk.Button(side_frame, text="Powrót", command=button_click, bg="#4C2A85", fg="white", font=("Arial", 12),pady=12, padx=10, relief="raised")

    # Add the button to the window
    button.pack(pady=20)

    charts_frame = tk.Frame(root)
    charts_frame.pack()

    upper_frame = tk.Frame(charts_frame)
    upper_frame.pack(fill="both", expand=True)

    canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

    lower_frame = tk.Frame(charts_frame)
    lower_frame.pack(fill="both", expand=True)

    canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
    canvas4.draw()
    canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

    canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
    canvas5.draw()
    canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)


def window():
    global new_window
    new_window = customtkinter.CTkToplevel()
    new_window.title("HydroSaver")
    new_window.geometry("1300x750")
    new_window.resizable(False, False)  # szerokosć, Długość wyłączenie możliwości resize okienka
    print("Map")
    image_path = os.path.join(os.path.dirname(__file__), "images/1.jpg")  # dodajemy obrazek
    # tworzymy etykietę
    image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(1280, 720))  #wywołujemy zdjęcie
    image_label = customtkinter.CTkLabel(new_window, image=image, text=" ")
    image_label.place(x=10, y=20)
    # przycisk Łazienka
    button_bathroom = customtkinter.CTkButton(master=new_window, text="Łazienka", command=bathroom)
    button_bathroom.pack(pady=12, padx=10)
    button_bathroom.place(x=500, y=500)
    # przycisk Garaż
    button_garage = customtkinter.CTkButton(master=new_window, text="Garaż", command=garage)
    button_garage.pack(pady=12, padx=10)
    button_garage.place(x=200, y=200)
    # przycisk Piwnica
    button_garage = customtkinter.CTkButton(master=new_window, text="Piwnica", command=basement)
    button_garage.pack(pady=12, padx=10)
    button_garage.place(x=100, y=100)
    # przycisk Ogród
    button_garage = customtkinter.CTkButton(master=new_window, text="Ogród", command=garden)
    button_garage.pack(pady=12, padx=10)
    button_garage.place(x=300, y=300)
    # przycisk Kuchnia
    button_garage = customtkinter.CTkButton(master=new_window, text="Kuchnia", command=kitchen)
    button_garage.pack(pady=12, padx=10)
    button_garage.place(x=400, y=400)





def login():  #tutaj co po zalogowaniu
    print("test")
    close()
    window()
    login_to_db()

def close():
    new_window.withdraw()


customtkinter.set_appearance_mode("Dark")  #aplikacja w trybie ciemnym
customtkinter.set_default_color_theme("dark-blue")  #motyw aplikacji

#Logowanie interface

new_window = customtkinter.CTk()
new_window.geometry("500x600")

frame = customtkinter.CTkFrame(master=new_window)  #graficzny interface
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Rejestracja", font=("Roboto", 24))
label.pack(pady=12, padx=10)

username = customtkinter.CTkEntry(master=frame, placeholder_text="Nazwa Użytkownika: ")
username.pack(pady=12, padx=10)
email = customtkinter.CTkEntry(master=frame, placeholder_text="Podaj Email: ")
email.pack(pady=12, padx=10)
password = customtkinter.CTkEntry(master=frame, placeholder_text="Podaj Hasło: ", show="*")
password.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Zaloguj", command=mylogin)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text=" Zgoda na  przetwarzanie danych osobowych")
checkbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Stwórz Konto", command=mylogin)
button.pack(pady=12, padx=10)


def login_to_db():
    user = username.get()
    em = email.get()
    passw = password.get()
    add_user(user, em, passw)
    print("Konto zostało utworzone")


new_window.mainloop()
