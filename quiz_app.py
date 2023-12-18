# quiz_app.py
import os
import json
import pandas as pd
import streamlit as st
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback

# Load environment variables
load_dotenv()
KEY = os.getenv("OPENAPI_API_KEY")

# Initialize ChatOpenAI model
llm = ChatOpenAI(openai_api_key=KEY, model_name="gpt-3.5-turbo", temperature=0.3)

# Define response JSON and templates
RESPONSE_JSON = {
    "1": {
        "MCQ": "What is the capital of France?",
        "options": {
            "a": "Paris",
            "b": "Berlin",
            "c": "Madrid",
            "d": "Rome"
        },
        "correct": "a"
    },
    "2": {
        "MCQ": "Which planet is known as the Red Planet?",
        "options": {
            "a": "Earth",
            "b": "Mars",
            "c": "Jupiter",
            "d": "Venus"
        },
        "correct": "b"
    },
    # Add more questions as needed
}


TEMPLATE1 = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for {subject} in the {tone} tone. 
Do not repeat any questions and make sure the questions match the text.
Make sure to format the response like RESPONSE_JSON below and use it as a guide
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
"""
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE1
)


TEMPLATE2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz.
Only use at max 50 words for complexity analysis.
If the quiz is not at par with the cognitive and analytical abilities of the students,
update the quiz questions that need to be changed and change the tone such that it perfectly fits the student abilities.
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""
quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=TEMPLATE2
)


# Define chains
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True)

# Define function to generate and evaluate quiz
def generate_and_evaluate_quiz(text, number, subject, tone):
    with get_openai_callback() as cb:
        response = generate_evaluate_chain({
            "text": text,
            "number": number,
            "subject": subject,
            "tone": tone,
            "response_json": json.dumps(RESPONSE_JSON)
        })
    return response

# Main function to run the application logic
if __name__ == "__main__":
    st.title("Interactive Quiz Application")
    st.sidebar.header("User Preferences")

    default_text = ""
    response = generate_and_evaluate_quiz(default_text, number=5, subject="", tone="simple")
    st.write(f"Total Tokens: {response['total_tokens']}")
    st.write(f"Prompt Tokens: {response['prompt_tokens']}")
    st.write(f"Completion Tokens: {response['completion_tokens']}")
    st.write(f"Total Cost: {response['total_cost']}")
    st.write(f"Quiz: {response['quiz']}")
    st.write(f"Review: {response['review']}")
