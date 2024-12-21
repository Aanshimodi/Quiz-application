def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
        return False

def start_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C"
        }
    ]

    score = 0
    print("Welcome to the Quiz Application!")
    print("You will be asked a series of questions. Please answer with A, B, C, or D.\n")

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"Quiz completed! Your final score is {score}/{len(questions)}.")

if _name_ == "_main_":
    start_quiz()
