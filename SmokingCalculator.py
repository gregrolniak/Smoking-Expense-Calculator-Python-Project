from tkinter import *
from SmokingStats import SmokingStats


class SmokingExpenseCalc:
    def __init__(self):
        window = Tk()
        window.title("50 Year Smoking Expense Calculator")
        frame1 = Frame(window)
        frame1.pack()
        self.label_total = Label(frame1, text="The expected cost of smoking of 50 years is...")
        self.label_total.pack()

        frame2 = Frame(window)
        frame2.pack()

        label_price = Label(frame2, text = "Type the current price per pack: ")
        label_cigs = Label(frame2, text = "Type the number of cigarettes per day: ")
        label_inflation = Label(frame2, text = "Type the expected yearly percent-rate of inflation: ")

        self.textbox_price = StringVar()
        entry = Entry(frame2, textvariable = self.textbox_price)

        self.textbox_cigs = StringVar()
        entry2 = Entry(frame2, textvariable = self.textbox_cigs)

        self.textbox_inflation = StringVar()
        entry3 = Entry(frame2, textvariable = self.textbox_inflation)

        button_go = Button(frame2, text = "GO!", command = self.processButton)
        self.v1 = StringVar()

        label_price.grid(row = 1, column = 1)
        label_cigs.grid(row = 2, column = 1)
        label_inflation.grid(row = 3, column = 1)
        entry.grid(row = 1, column = 2)
        entry2.grid(row = 2, column = 2)
        entry3.grid(row = 3, column = 2)
        button_go.grid(row = 4, column = 2)

        window.mainloop()

    def processButton(self):
        my_smoking_stats = SmokingStats()  # Instantiate object from class
        temp = int(self.textbox_price.get())
        my_smoking_stats.set_pack_price(temp)
        my_smoking_stats.set_number_cigs(int(self.textbox_cigs.get()))
        my_smoking_stats.set_inflation(int(self.textbox_inflation.get()))
        my_smoking_stats.set_packs_per_day()
        my_smoking_stats.set_price_per_day()
        my_smoking_stats.set_inflation_decimal()
        my_smoking_stats.set_inflation_per_day()
        my_smoking_stats.calculate_cost()
        self.label_total["text"] = "Total: $" + format(my_smoking_stats.get_total(), "10.2f")


SmokingExpenseCalc()