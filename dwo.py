import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz Application")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        # Canvas for Watermark and Border
        self.canvas = tk.Canvas(self.root, width=1200, height=1200, bg="#f0f0f0", highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.add_watermark()
        self.add_border()

        # Welcome Screen
        self.welcome_frame = tk.Frame(self.root, bg="#add8e6", padx=20, pady=20)
        self.welcome_label = tk.Label(self.welcome_frame, text="WELCOME TO THE QUIZ", font=("Helvetica", 26, "bold"), bg="#add8e6", fg="#2F4F4F")
        self.welcome_label.pack(pady=20)
        
        self.start_button = tk.Button(self.welcome_frame, text="Start Quiz", font=("Helvetica", 16), command=self.start_quiz, 
                                      bg="#4682B4", fg="white", relief="flat", bd=0, padx=10, pady=5)
        self.start_button.pack(pady=30)
        self.welcome_frame.pack(expand=True)

        # Quiz Screen (initially hidden)
        self.quiz_frame = tk.Frame(self.root, bg="#e6e6fa", padx=20, pady=20)

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
            {"question": "What is the chemical formula of water?", "options": ["O2", "H2O", "CuSO4", "NaCl"], "answer": "H2O"},
            {"question": "Indus River originates in?", "options": ["Kinnaur", "Ladakh", "Nepal", "Tibet"], "answer": "Tibet"},
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Helvetica", 18), bg="#e6e6fa", fg="#4B0082")
        self.question_label.pack(pady=15)

        self.var = tk.StringVar()
        self.options_frame = tk.Frame(self.quiz_frame, bg="#e6e6fa")
        self.options_frame.pack(pady=20)

        self.option_buttons = []
        for _ in range(4):
            button = tk.Radiobutton(self.options_frame, text="", variable=self.var, value="", font=("Helvetica", 14), bg="#e6e6fa", selectcolor="#add8e6", anchor="w")
            button.pack(fill='x', pady=5)
            self.option_buttons.append(button)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit Answer", font=("Helvetica", 16), command=self.submit_answer,
                                       bg="#4682B4", fg="white", relief="flat", bd=0, padx=10, pady=5)
        self.submit_button.pack(pady=20)

    def add_watermark(self):
        # Adds multiple diagonal watermarks across the canvas
        watermark_text = "Simple Quiz Application"
        font = ("Helvetica", 24, "bold")
        fill_color = "#d3d3d3"

        # Draw watermark text in a repeating pattern
        for x in range(-350, 900, 350):
            for y in range(-450, 800, 150):
                self.canvas.create_text(
                    x, y, text=watermark_text, font=font,
                    angle=45, fill=fill_color, anchor="center"
                )

    def add_border(self):
        # Adds a decorative border around the canvas
        border_color = "#4682B4"  # Steel blue color for border
        border_thickness = 6

        # Draw four rectangles for a layered border effect
        for i in range(border_thickness):
            self.canvas.create_rectangle(
                i, i, 1400-i, 740-i,
                outline=border_color,
                width=1
            )

    def start_quiz(self):
        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option, value=option)
        self.var.set("")

    def submit_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was: {correct_answer}")

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()
