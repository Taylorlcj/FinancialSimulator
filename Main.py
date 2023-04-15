import tkinter as tk
from configparser import ConfigParser
from tkinter import messagebox, ttk

# TODO: problem with toml(line 335) and openfile(line 155)
# TODO: global name(Lines 220-223)

# global name
name = "void"
money = 0
month = 0
tempName = "other"


def save_get_name():
    global name
    name = tempName
    print(name)


class SimFin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1960x1080")
        self.title("Sim Fin")
        self.background_image = tk.PhotoImage(file="CBGRBaked04.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_sizes = {
            "MainPage": (300, 200),
            "NewGamePage": (500, 700),
            "MainApp": (800, 800),
        }

        self.container = tk.Frame(
            self,
            width=self.frame_sizes["MainPage"][0],
            height=self.frame_sizes["MainPage"][1],
            bg="white",
        )
        # self.container = tk.Frame(self, width=300, height=650, bg="white")
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        self.frames = {}
        for F in (MainPage, NewGamePage, MainApp):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("MainPage")

        # Define name as a global variable
        # global name
        # name = ""

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        width, height = self.frame_sizes[page_name]
        self.container.config(width=width, height=height)
        frame.tkraise()


class Player:
    name = "voidC"
    month = 0
    currentMoney = 0.0


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        style_red = ttk.Style()
        style_red.configure(
            "Custom.TButton.Red", background="red", font="Helvetica 18 bold"
        )

        layout_red = ttk.Style()
        layout_red.layout(
            "Custom.TButton.Red",
            [
                ("Button.padding", {"side": "left", "sticky": ""}),
                ("Button.label", {"side": "left", "sticky": ""}),
            ],
        )

        style_blue = ttk.Style()
        style_blue.configure(
            "Custom.TButton.Blue", background="#ADD8E6", font="Helvetica 18 bold"
        )

        layout_blue = ttk.Style()
        layout_blue.layout(
            "Custom.TButton.Blue",
            [
                ("Button.padding", {"side": "left", "sticky": ""}),
                ("Button.label", {"side": "left", "sticky": ""}),
            ],
        )

        style_black = ttk.Style()
        style_black.configure(
            "Custom.TButton.Black",
            background="black",
            font="Helvetica 18 bold",
            foreground="white",
        )

        layout_black = ttk.Style()
        layout_black.layout(
            "Custom.TButton.Black",
            [
                ("Button.padding", {"side": "left", "sticky": ""}),
                ("Button.label", {"side": "left", "sticky": ""}),
            ],
        )

        new_game_button = ttk.Button(
            self,
            text="New Game",
            width=20,
            style="Custom.TButton.Blue",
            command=lambda: controller.show_frame("NewGamePage"),
        )
        new_game_button.configure(style="Custom.TButton.Blue")
        new_game_button.pack(pady=10)

        continue_button = ttk.Button(
            self,
            text="Continue",
            width=20,
            style="Custom.TButton.Blue",
            command=self.continue_game,
        )
        continue_button.pack(pady=10)

        leaderboard_button = ttk.Button(
            self, text="Leaderboards", width=20, style="Custom.TButton.Red"
        )
        leaderboard_button.configure(style="Custom.TButton.Red")
        leaderboard_button.pack(pady=10)

        exit_button = ttk.Button(
            self,
            text="Exit",
            width=20,
            style="Custom.TButton.Black",
            command=self.exit_game,
        )
        exit_button.configure(style="Custom.TButton.Black")
        exit_button.pack(pady=10)

    def continue_game(self):
        openfile()
        self.controller.show_frame("MainApp")

    def exit_game(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.controller.destroy()


class NewGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Enter your name:")
        label.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        submit_button = ttk.Button(self, text="Submit", command=self.save_name)
        submit_button.pack(pady=10)

        submit_button = ttk.Button(
            self, text="Start", command=lambda: controller.show_frame("MainApp")
        )
        submit_button.pack(pady=10)

        submit_button = ttk.Button(
            self, text="Main Page", command=lambda: controller.show_frame("MainPage")
        )
        submit_button.pack(pady=10)

    def save_name(self):
        global name
        name = self.name_entry.get()
        global tempName
        tempName = name
        save_get_name()
        # with open("names.txt", "a") as file:
        # file.write(name + "\n")
        messagebox.showinfo("Success", f"Name {name} saved!")
        # self.controller.show_frame("MainApp")
        label10 = tk.Label(self, text="Your name is \n" + name)
        label10.pack(pady=20)


class MainApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.spend_entry = controller

        # create a notebook widget
        notebook = ttk.Notebook(self)

        # create first tab
        tab1 = ttk.Frame(notebook)

        global month
        # display a text block
        label4 = tk.Label(tab1, font="Helvetica 24 bold", text="Month ")
        label4.pack(pady=5)

        global name
        label10 = tk.Label(tab1, text=name)
        label10.pack(pady=5)

        label0 = tk.Label(tab1, text="Your total money is: ")
        label0.pack(pady=25)

        label5 = tk.Label(tab1, font="Helvetica 14 bold", text="$1500")
        label5.pack(pady=25)

        label1 = tk.Label(tab1, text="Your living expenses are: ")
        label1.pack(pady=25)

        label6 = tk.Label(tab1, font="Helvetica 14 bold", text="$1200")
        label6.pack(pady=25)

        label2 = tk.Label(tab1, text="Enter in how much you want to spend:")
        label2.pack(pady=10)

        tab1.spend_entry = tk.Entry(tab1)
        tab1.spend_entry.pack(pady=10)

        submit_button = ttk.Button(tab1, text="Submit", command=self.spend_amount)
        submit_button.pack(pady=10)

        notebook.add(tab1, text="Main")

        # second tab
        tab2 = ttk.Frame(notebook)

        label4 = tk.Label(tab2, font="Helvetica 24 bold", text="Month 1")
        label4.pack(pady=5)

        label0 = tk.Label(tab2, text="Your rent is: ")
        label0.pack(pady=25)

        notebook.add(tab2, text="Housing")

        # pack the notebook widget
        notebook.pack(fill="both", expand=True)

        style_red = ttk.Style()
        style_red.configure(
            "Custom.TButton.Red2",
            background="red",
            font="Helvetica 14 bold",
            foreground="white",
        )

        layout_red2 = ttk.Style()
        layout_red2.layout(
            "Custom.TButton.Red2",
            [
                ("Button.padding", {"side": "left", "sticky": ""}),
                ("Button.label", {"side": "left", "sticky": ""}),
            ],
        )

        next_month = ttk.Button(
            self,
            text="Next Month",
            width=20,
            style="Custom.TButton.Red2",
            # command=lambda: controller.show_frame("MainApp2")
        )
        next_month.configure(style="Custom.TButton.Red2")
        next_month.pack(pady=20)

        style_black2 = ttk.Style()
        style_black2.configure(
            "Custom.TButton.Black2",
            background="black",
            font="Helvetica 14 bold",
            foreground="white",
        )

        layout_black2 = ttk.Style()
        layout_black2.layout(
            "Custom.TButton.Black2",
            [
                ("Button.padding", {"side": "left", "sticky": ""}),
                ("Button.label", {"side": "left", "sticky": ""}),
            ],
        )

        exit_button = ttk.Button(
            self,
            text="Save and Exit",
            width=20,
            style="Custom.TButton.Black2",
            command=self.exit_game,
        )
        exit_button.configure(style="Custom.TButton.Black2")
        exit_button.pack(pady=20)

    def spend_amount(self):
        global month
        spend = self.spend_entry.get()
        messagebox.showinfo("You paid your bills!", f"Name paid {spend}!")
        self.controller.show_frame("mainApp")

    def exit_game(self):
        savefile()
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.controller.destroy()


def savefile():
    config = ConfigParser()
    config["Player Info"] = {"name": name, "currentMoney": 0.0, "currentMonth": 0}
    with open("testfile.toml", "w") as f:
        config.write(f)


def openfile():
    import toml

    # t = open("testfile.toml")
    with open("testfile.toml", "r") as f:
        data = toml.load(f)

        global name
        global money
        global month

        name = data["name"]
        money = data["currentMoney"]
        month = data["currentMonth"]
    f.close()


# savefile()
app = SimFin()
app.mainloop()
