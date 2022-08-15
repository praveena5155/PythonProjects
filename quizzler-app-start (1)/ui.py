import tkinter
from cgitb import text
from tkinter import  *
from quiz_brain import  QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #creatin Label
        #self.label = tkinter.Label
        self.label = Label(text="Score: 0", fg="White", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)
        #creating buttons
        self.button = tkinter.Button
        false_image = PhotoImage(file="images/false.png")
        self.button = Button(image=false_image,highlightthickness=0, command=self.wrong_answer)
        self.button.grid(row=2, column=0)
        true_image = PhotoImage(file="images/true.png")
        self.button = Button(image=true_image, command=self.right_answer)
        self.button.grid(row=2, column=1)
        #displaig the quiz.
        self.Canvas = Canvas(width=300, height=250, bg="white")
        self.Canvas.grid(row=1, column=0, columnspan=2,pady=20)
        self.question_text = self.Canvas.create_text(150, 125,width=280 , text="hiiiihshhs", fill="Black",font=("Arial",20,"italic"))
        #using width here to fit the text on canvas.

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self) :
        if self.quiz.still_has_questions():
            self.Canvas.config(bg="white")
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.Canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.Canvas.itemconfig(self.question_text, text="end. get a life")
            self.Canvas.config(bg="White")

    def   right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):

        if is_right == True :
            self.Canvas.config(bg="Green")
        else :
            self.Canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)


