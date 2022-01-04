from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label()
        self.label.config(text=f"Score: {score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = "this is a test"
        self.question_text = self.canvas.create_text(150, 125, width=280, text=f"{self.question}", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)