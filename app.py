from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import time
import re

API_KEY = "AIzaSyBWYI7kjZr_Gx1fgGzg_fKWiaknSzcqgBw"
genai.configure(api_key=API_KEY)

app = Flask(__name__)

def get_ai_response(text):
    model = genai.GenerativeModel('gemini-1.5-flash')

    while True:
        try:
            response = model.generate_content(text)
            text_part = response.parts[0].text
            clean_text = re.sub(r'[*]', '', text_part)
            return clean_text
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(3)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    response = get_ai_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
