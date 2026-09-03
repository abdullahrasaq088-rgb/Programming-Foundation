# Quiz using fruit list (currently questions)
quiz_questions = [
    {"question": "what is the name of the current nigeria president?", "answer": "Bola Tinubu"},
    {"question": "what is the name of the current nigeria first lady?", "answer": "Oluremi Tinubu"},
    {"question": "what is your favourite meal?", "answer": ""}  # Open-ended question
]

# Interactive Quiz
score = 0
total_questions = len(quiz_questions)

print("=" * 50)
print("WELCOME TO THE QUIZ!")
print("=" * 50)

for i, quiz in enumerate(quiz_questions, 1):
    print(f"\nQuestion {i}: {quiz['question']}")
    user_answer = input("Your answer: ").lower().strip()
    
    if quiz['answer'] == "":  # Open-ended question
        print("✓ Thank you for your answer!")
        score += 1
    elif user_answer == quiz['answer'].lower():
        print("✓ Correct!")
        score += 1
    else:
        print(f"✗ Incorrect. The correct answer is: {quiz['answer']}")

print("\n" + "=" * 50)
print(f"Quiz Complete! You scored: {score}/{total_questions}")
print("=" * 50)