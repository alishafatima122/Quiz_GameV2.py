#=================================
# Quiz game version 2.0
# language: Python
#==================================
import random

questions = [
    {
      "question":"what's the correct extension for python files?",
      "options":[".py",".python",".pyt",".pt"],
        "answer":".py"
    },
    {
      "question":"what is the correct syntax to output 'Hello World' in python?",
      "options":["echo('Hello World')","print('Hello World')","p('Hello World')","printf('Hello World')"],
        "answer":"print('Hello World')"
    },
    {
      "question":"How do you insert COMMENTS in python code?",
      "options":["//This is a comment","/*This is a comment*/","#This is a comment","<!--This is a comment-->"],
        "answer":"#This is a comment"
    },
    {
      "question":"Which one is NOT a legal variable name?",
      "options":["my-var","my_var","_myvar","myvar"],
        "answer":"my-var"
    },
    {
      "question":"What is the correct file mode for reading in binary?",
      "options":["r+b","rb+","br+","b+r"],
        "answer":"rb+"
    }
]

while True:
  print("=====================Welcome to the Quiz Game!========================")
  print("1. Start Quiz")
  print("2. Exit")

  choice = input("Enter your choice (1 or 2): ")
  if choice == "1":
        score = 0
        for i in range(len(questions)):
            print(f"Question {i + 1}: {questions[i]}")
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == "exit":
                print("Exiting the game. Goodbye!")
                break

            elif user_answer == answers[i]:
                print("Correct!\n")
                score += 1

            else:
                print(f"Incorrect! The correct answer is: {answers[i]}\n")
                
        print(f"Your final score is: {score}/{len(questions)}\n")
