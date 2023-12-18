# AIQuizGenerator
Submitted to PWC's Internship assessment. 

Interactive Quiz Application with Streamlit

Overview

This repository contains a simple interactive quiz application developed using [Streamlit](https://www.streamlit.io/). The application allows users to generate quizzes based on provided text, set the number of questions, choose a subject, and select the quiz tone (simple, complex, neutral). Users can then answer the generated quiz questions and submit their answers for evaluation.

How to Use

1. Clone the Repository: 
   
   git clone https://github.com/fatiiiiima/AIQuizGenerator.git
   cd interactive-quiz-app
    

2. Run the Application:
   
   streamlit run app.py
   

3. Interact with the Quiz:
   - Enter text for quiz generation.
   - Adjust the number of questions, enter the quiz subject, and select the quiz tone.
   - Click "Generate Quiz" to create the quiz.
   - Answer the quiz questions presented.
   - Click "Submit Answers" to evaluate and display the score.

Code Structure

- `app.py`: Main application script that defines the Streamlit UI and integrates backend logic for quiz generation and evaluation.
- `quiz_app.py`: Module containing the `generate_and_evaluate_quiz` function used to generate and evaluate quizzes.
- `requirements.txt`: File listing the Python dependencies required to run the application.

Dependencies

- Streamlit: [Streamlit](https://www.streamlit.io/)
- json: Standard library for JSON handling in Python.

Functionality

`generate_and_evaluate_quiz`

The `generate_and_evaluate_quiz` function is responsible for generating quiz questions based on user input and evaluating the user's answers. It takes parameters such as text, the number of questions, quiz subject, and tone to create a quiz. The generated quiz is then displayed to the user, who can answer the questions and submit them for evaluation.

`calculate_score`

The `calculate_score` function calculates the user's score by comparing their selected answers with the correct answers. It takes a dictionary of user answers and returns the number of correct responses.

Main Application

The `main` function sets up the Streamlit UI, including input elements for quiz generation and buttons to trigger quiz generation and answer submission. It utilizes the `generate_and_evaluate_quiz` function to create quizzes and evaluates user responses using the `calculate_score` function.

