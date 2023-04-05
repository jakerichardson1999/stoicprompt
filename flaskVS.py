#importing libraries
from flask import Flask, request, render_template
import os
from dotenv import load_dotenv
from prompts import get_stoic_advice

#creating the flask aplication object assigned to the variable 'app'
app = Flask(__name__)

#loading key
load_dotenv('key.env')
openai_api_key = os.environ.get('OPENAI_API_KEY')

#create route for app that can accept both get and post
@app.route('/', methods=['GET', 'POST'])
#define function to execute when user visits page
def index():
    stoic_advice = ''
    if request.method == 'POST':
        user_input = request.form['user_input'] #extracts value of input, call get-stoic-advice to generate response
        stoic_advice = get_stoic_advice(user_input)
    return render_template('index.html', stoic_advice=stoic_advice) #return html template

if __name__ == '__main__':
    app.run(debug=True, port=5001)
