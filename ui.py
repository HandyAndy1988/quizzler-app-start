from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label()
        self.label.config(text=f"Score: {score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        question = "this is a test"
        self.question_text = self.canvas.create_text(150, 125, text=f"{question}", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        true_button = Button(image=true_image)
        true_button.grid(row=2, column=0, padx=20, pady=20)
        false_button = Button(image=false_image)
        false_button.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()