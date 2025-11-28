import pandas as pd

df = pd.read_csv('BCGX-Forage Correction.csv')

def simple_chatbot(user_query):
    user_query = user_query.lower()
    if user_query == "what is the total revenue?":
        return "The total revenue is $211 billion."
    elif user_query == "how has net income changed over the last year?":
        return "The net income has decreased by $16 billion over the last year."
    elif user_query == "what is the total net income?":
        return "The net income is $72 billion."
    elif user_query == "how has total revenue changed over the last year?":
        return "The total revenue has decreased by $34 billion over the last year."
    elif user_query == "what is the total assets over the last two years?":
        return "The total assets has increased by $101 billion two years ago and increased by $107 billion over the last year"
    else:
        return "Sorry, I can only provide information on predefined queries."

while True:
    response = input("Enter your financial question: ")
    if  (response == "quit"):
        break
    chatbot_response = simple_chatbot(response)
    print(chatbot_response)
