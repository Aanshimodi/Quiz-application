# List of questions, options, and answers
questions = [
    {
        "question1": "What is the capital of France?",
        "options": ["1. Paris", "2. London", "3. Rome", "4. Berlin"],
        "answer": 1
    },
    {
        "question2": "What is 2 + 2?",
        "options": ["1. 3", "2. 4", "3. 5", "4. 6"],
        "answer": 2
    },
    {
        "question3": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Venus", "4. Jupiter"],
        "answer": 2
    },
    {
        "question4": "What is the largest ocean on Earth?",
        "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"],
        "answer": 4
    }
]

def ask_question(q):
    """Function to display the question and options, and check the answer."""
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = int(input("Please enter the number of your answer: "))
    
    if user_answer == q["answer"]:
        print("Correct!\n")
        return 1  # Correct answer
    else:
        print("Incorrect!\n")
        return 0  # Incorrect answer

def start_quiz():
    """Function to start the quiz and keep track of the score."""
    score = 0
    print("Welcome to the Quiz!\n")
    
    for q in questions:
        score += ask_question(q)
    
    print(f"Your final score is: {score} out of {len(questions)}")
    if score == len(questions):
        print("Congratulations! You answered all questions correctly.")
    elif score > len(questions) // 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time.")

# Run the quiz
if '_name_' == "_main_":
    start_quiz()