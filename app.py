# from flask import Flask, request, jsonify, render_template
# import google.generativeai as genai

# app = Flask(__name__)

# # Replace with your actual API key
# YOUR_API_KEY = "AIzaSyCHIe3zJnINhpIA9WnVaRaku4cQKbIvSvw"

# # Configure the API client
# genai.configure(api_key=YOUR_API_KEY)

# # Function to ask a question and get an answer
# def ask_question(question):
#     try:
#         # Generate text based on the user's question
#         response = genai.generate_text(prompt=question)
        
#         # Extract the generated text from the response
#         result_text = response.result
#         return result_text

#     except Exception as e:
#         print(f"An error occurred while processing the question: {e}")
#         return "Sorry, I encountered an issue. Please try rephrasing your question."

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     question = data.get('question')
#     answer = ask_question(question)
#     return jsonify({'answer': answer})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question')
    answer = ask_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
