from CoffeeMachine import CoffeeMachine
import tkinter as tk
from PIL import Image, ImageTk
import pyglet
import time

pyglet.font.add_file("Antic-Regular.ttf")


def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()


def handle_coin_entry(coin_entry, coin_value, total):
    coin = float(coin_entry.get())
    total.append(coin_value * coin)
    coin_entry.delete(0, tk.END)

    return total


def transaction(choice, total):
    payment_result = machine.is_payment_sucessful(choice, sum(total))

    if payment_result[0]:
        response = payment_result[1]
        load_frame7(choice, response)
    else:
        label = tk.Label(frame6, 
                        text='Error: Not sufficient money.',
                        bg=bg,
                        fg="red",
                        font=("Antic", 14),
                        justify="center")
        label.place(x = 540, y = 530)


def load_frame1():
    clear_widgets(frame2)
    #display above
    frame1.tkraise()
    # Prevent widgets from modifying the frame
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(master = frame1, file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)

    tk.Label(frame1, text="Hello, what would you like to do?",
             bg=bg,
             fg="black",
             font=("Antic", 32),
             wraplength=350,
             justify="center").place(x=480, y=75)

    button_y = 0
    for button in button_actions.keys():
        tk.Button(
            frame1,
            text=button,
            font=("Antic", 25),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            command=button_actions[button],
            width=15
        ).place(x=500, y=205+button_y)

        button_y += 90  # Increase the vertical coordinate for the next button


def load_frame2():
    clear_widgets(frame1)

    frame2.tkraise()
    # Prevent widgets from modifying the frame
    frame2.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(master = frame2, file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)


    tk.Label(frame2, text=machine.show_profit(),
             bg=bg,
             fg="black",
             font=("Antic", 32),
             wraplength=350,
             justify="center").place(x=520, y=250)
    
    tk.Button(
            frame2,
            text='Return',
            font=("Antic", 25),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            command=lambda:load_frame1(),
            width=15
        ).place(x=505, y=400)
    

def load_frame3():
    clear_widgets(frame1)

    frame3.tkraise()
    # Prevent widgets from modifying the frame
    frame3.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(master = frame3, file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame3, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)


    tk.Label(frame3, text=machine.show_report(),
             bg=bg,
             fg="black",
             font=("Antic", 32),
             wraplength=350,
             justify="center").place(x=500, y=100)
    
    tk.Button(
            frame3,
            text='Return',
            font=("Antic", 25),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            command=lambda:load_frame1(),
            width=15
        ).place(x=500, y=400)
    

def load_frame4():
    clear_widgets(frame1)

    frame4.tkraise()
    # Prevent widgets from modifying the frame
    frame4.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(master = frame4, file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame4, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)


    tk.Label(frame4, text=machine.show_menu(),
             bg=bg,
             fg="black",
             font=("Antic", 32),
             wraplength=350,
             justify="center").place(x=500, y=100)
    
    tk.Button(
            frame4,
            text='Return',
            font=("Antic", 25),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            command=lambda:load_frame1(),
            width=15
        ).place(x=500, y=400)


def load_frame5():
    clear_widgets(frame1)

    frame5.tkraise()
    # Prevent widgets from modifying the frame
    frame5.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(master = frame5, file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame5, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)


    tk.Label(frame5, text='What would you like to have?',
             bg=bg,
             fg="black", 
             font=("Antic", 32),
             wraplength=350,
             justify="center").place(x=500, y=100)
    
    x_start = 480  # Starting x-coordinate for the buttons
    y_start = 280  # Starting y-coordinate for the buttons
    x_offset = 200  # Offset between the buttons in the x-direction
    y_offset = 100  # Offset between the rows in the y-direction

    row1_x = x_start
    row1_y = y_start

    row2_x = x_start
    row2_y = y_start + y_offset

    index = 0

    for drink in menu.keys():
        if index < 2:
            button_x = row1_x + index * x_offset
            button_y = row1_y
        else:
            button_x = row2_x + (index - 2) * x_offset
            button_y = row2_y

        tk.Button(
            frame5,
            text=drink,
            font=("Antic", 25),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            width=8,
            command=lambda drink=drink: load_frame6(drink),
        ).place(x=button_x, y=button_y)

        index += 1

    
def load_frame6(choice):
    clear_widgets(frame5)

    frame6.tkraise()
    # Prevent widgets from modifying the frame
    frame6.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame6, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)

    if machine.check_resources(choice):
        tk.Label(frame6, text=machine.get_cost(choice),
                 bg=bg,
                 fg="black",
                 font=("Antic", 32),
                 wraplength=350,
                 justify="center").place(x=530, y=100)

        tk.Label(frame6, text='Please insert coins',
                 bg=bg,
                 fg="black",
                 font=("Antic", 32),
                 wraplength=350,
                 justify="center").place(x=496, y=200)

        subframe = tk.Frame(frame6, height= 250, width = 350, bg=bg)
        subframe.place(x = 510, y = 280)
        
        total = []
        label_values = [0.5, 1, 2]
        
        for i, value in enumerate(label_values):
            label = tk.Label(subframe, 
                            text=f'How many {value}€ coins would you like to add?',
                            bg=bg,
                            fg="black",
                            font=("Antic", 12),
                            justify="center")
            label.grid(row=1+3*i, column=0, padx = 0, pady = 0, sticky="w")

            coin_entry = tk.Entry(subframe)
            coin_entry.grid(row=2+3*i, column=0, padx = 60, pady = 8, sticky="w")

            button = tk.Button(subframe, 
                               text='Add',
                               font=("Antic", 10),
                               bg=btn_dark,
                               fg="white",
                               cursor="hand2",
                               activebackground=btn,
                               command=lambda entry=coin_entry, value=value, total=total: handle_coin_entry(entry, value, total))
            button.grid(row=2+3*i, column=0, padx = 200, pady = 5, sticky="w")
        
        button = tk.Button(frame6, 
                        text='Confirm',
                        font=("Antic", 16),
                        bg=btn_dark,
                        fg="white",
                        cursor="hand2",
                        activebackground=btn,
                        command=lambda choice=choice, total=total: transaction(choice, total))
        button.place(x = 623, y = 470)

def load_frame7(choice, res):
    clear_widgets(frame6)

    frame7.tkraise()
    # Prevent widgets from modifying the frame
    frame7.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame7, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)

    tk.Label(frame7, 
            text="Transaction accepted!",
            bg=bg,
            fg="black",
            font=("Antic", 32),
            wraplength=350,
            justify="center").place(x=560, y=160)
    
    tk.Label(frame7, 
            text=res,
            bg=bg,
            fg="black",
            font=("Antic", 26),
            wraplength=350,
            justify="center").place(x=510, y=280)
    
    tk.Button(frame7, 
            text='Processing...',
            font=("Antic", 20),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            command=lambda choice=choice: load_frame8(choice)).place(x = 590, y = 400)

    
def load_frame8(choice):
    clear_widgets(frame7)

    frame8.tkraise()
    # Prevent widgets from modifying the frame
    frame8.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file='imgs/Coffee_machine.png')
    logo_widget = tk.Label(frame8, image=logo_img, bg=bg)
    logo_widget.image = logo_img
    logo_widget.place(x=80, y=90)

    time.sleep(1)
    
    tk.Label(frame8, 
            text=machine.make_coffee(choice),
            bg=bg,
            fg="black",
            font=("Antic", 40),
            wraplength=350,
            justify="center").place(x=520, y=200)
    
    tk.Button(
            frame8,
            text='Return',
            font=("Antic", 25),
            bg=btn_dark,
            fg="white",
            cursor="hand2",
            activebackground=btn,
            command=lambda:load_frame1(),
            width=15
        ).place(x=520, y=400)
    

bg = '#B79D86'
btn = '#7D553B'
btn_dark = '#49301A'

menu = {'latte' : {'ingredients' : {'coffee': 20, 'milk': 10, 'water': 50}, 'cost': 2.5},
       'espresso' : {'ingredients' : {'coffee': 30, 'water': 20}, 'cost': 1.5},
       'cappucino' : {'ingredients' : {'coffee': 30, 'milk' : 20, 'water': 10}, 'cost': 2},
       'flat white' : {'ingredients' : {'coffee': 40, 'milk' : 10, 'water': 10}, 'cost': 2}}

resources = {'coffee': 200, 'milk': 200, 'water': 500}
machine = CoffeeMachine(menu, resources)

button_actions = {
    'Get coffee': lambda:load_frame5(),
    'Show menu': lambda:load_frame4(),
    'Show report': lambda:load_frame3(),
    'Check profit': lambda:load_frame2()
    }

root = tk.Tk()
root.title("Virtual Coffee Machine")
root.iconphoto(False, tk.PhotoImage(file="imgs/coffee_icon.png"))
root.eval("tk::PlaceWindow . center")

# create a frame widgets
frame1 = tk.Frame(root, width=900, height=600, bg=bg)
frame2 = tk.Frame(root, bg=bg)
frame3 = tk.Frame(root, bg=bg)
frame4 = tk.Frame(root, bg=bg)
frame5 = tk.Frame(root, bg=bg)
frame6 = tk.Frame(root, bg=bg)
frame7 = tk.Frame(root, bg=bg)
frame8 = tk.Frame(root, bg=bg)

# place frame widgets in window
for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
	frame.grid(row=0, column=0, sticky="nesw")

load_frame1()

root.mainloop()

