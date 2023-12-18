import streamlit as st
import json
from quiz_app import generate_and_evaluate_quiz

def main():
    st.title("Interactive Quiz Application")

    # Add Streamlit UI elements for quiz generation
    text = st.text_area("Enter text for quiz generation:", "", height=150)
    number = st.slider("Select the number of questions:", min_value=1, max_value=10, value=5)
    subject = st.text_input("Enter the quiz subject:", "")
    tone = st.selectbox("Select the quiz tone:", ["simple", "complex", "neutral"])

    # Initialize user_answers and quiz_dict outside the quiz generation block
    user_answers = {}
    quiz_dict = {}

    # Run the backend logic on button click to generate and evaluate quiz
    if st.button("Generate Quiz"):
        response = generate_and_evaluate_quiz(text, number, subject, tone)

        # Extract quiz details from the response
        quiz = response.get("quiz")
        quiz_dict = json.loads(quiz)

        # Display quiz questions and options
        st.subheader("Quiz Questions:")
        for key, value in quiz_dict.items():
            mcq = value["MCQ"]
            options = value["options"]
            correct_answer = value["correct"]

            # Display the question
            st.write(f"{key}. {mcq}")

            # Use a loop to display options with letters (A, B, C, D)
            for letter, option_text in options.items():
                st.write(f"{letter}. {option_text}")

            # Collect user's selected option
            selected_option = st.radio(f"Select your answer for Question {key}:", list(options.keys()))
            user_answers[key] = {"selected_option": selected_option, "correct_answer": correct_answer, "options": options}

    # Show a "Submit Answers" button outside the quiz generation block
    if st.button("Submit Answers"):
        # Calculate and display the score
        score = calculate_score(user_answers)
        st.subheader("Your Score:")
        st.write(f"You scored {score}/{len(quiz_dict)}")

def calculate_score(user_answers):
    correct_count = 0
    for key, value in user_answers.items():
        correct_answer = value["correct_answer"].lower()
        user_answer = value["selected_option"].lower()
        if user_answer == correct_answer:
            correct_count += 1
    return correct_count

if __name__ == "__main__":
    main()
