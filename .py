# List of quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "correct": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "correct": "Blue Whale"
    }
]
# Function to run the quiz
def run_quiz(questions):
    correct_answers = 0
    total_questions = len(questions)
    
    # Loop through each question
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")

        # Display the options
        for j, option in enumerate(question['options']):
            print(f"{j + 1}. {option}")

        # Get the user's answer
        answer = int(input("Choose an option (1-4): ")) - 1
        selected_option = question['options'][answer]

        # Check if the answer is correct
        if selected_option == question['correct']:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer was: {question['correct']}\n")

    # Calculate the quiz score
    score_percentage = (correct_answers / total_questions) * 100
    print(f"Quiz completed! You scored {correct_answers} out of {total_questions} ({score_percentage:.2f}%).")
# Run the quiz with the list of questions
run_quiz(quiz_questions)
