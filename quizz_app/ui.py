from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
HEIGHT = 250
WIDTH = 300
FONT = ("Arial",20,"italic")

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Title")
        self.window.configure(background=THEME_COLOR,padx=20, pady=20)

        self.canvas = Canvas(bg="white", height=HEIGHT, width=WIDTH)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Question text", font=FONT)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_img, command=self.user_answer_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img, command=self.user_answer_false)
        self.false_button.grid(row=2, column=1)
        self.score_label = Label(self.window, text=f"Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)

    def user_answer_true(self):
       answer = "True"
       is_right = self.quiz_brain.check_answer(answer)
       self.give_feedback(is_right)

    def user_answer_false(self):
       answer = "False"
       is_right = self.quiz_brain.check_answer(answer)
       self.give_feedback(is_right)

    def give_feedback(self, correct_answer):
        if correct_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)





