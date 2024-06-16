import google.generativeai as genai

# Replace with your actual API key
YOUR_API_KEY = "AIzaSyCHIe3zJnINhpIA9WnVaRaku4cQKbIvSvw"

# Configure the API client
genai.configure(api_key=YOUR_API_KEY)

# Function to ask a question and get an answer
def ask_question(question):
    try:
        # Generate text based on the user's question
        response = genai.generate_text(prompt=question)
        
        # Extract the generated text from the response
        result_text = response.result
        return result_text

    except Exception as e:
        print(f"An error occurred while processing the question: {e}")
        return "Sorry, I encountered an issue. Please try rephrasing your question."

# Main loop to create an interactive chatbot
def chatbot():
    print("Welcome to the chatbot! Ask me anything (type 'exit' to quit).")
    while True:
        # Get user input for the question
        user_question = input("You: ")

        # Exit condition
        if user_question.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Call the function to get the answer
        answer = ask_question(user_question)

        # Print the answer
        print("Chatbot:", answer)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
