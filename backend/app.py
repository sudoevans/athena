# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from twilio.rest import Client
# import dotenv
# import os

# dotenv.load_dotenv()

import os
import flask
from flask import request
from twilio_integration import send_whatsapp_message
from phi_model import chat_with_athena

# Flask app setup
app = flask.Flask(__name__)

# Routes
@app.route('/')
@app.route('/home')
def home():
    return "<h1>Athena Home</h1>"
#Endpoint for twilio callback
@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    try:
        message = request.form['Body']
        sender_id = request.form['From'].split('+')[1]
        print(f'Message --> {message}')
        print(f'Sender ID --> {sender_id}')

        # Send user message to phi model
        response = chat_with_athena(message)
        print("Model Response:", response[0])

        # Send model response to user via WhatsApp
        send_whatsapp_message(sender_id, response)

        return '200'
    except Exception as e:
        print(f"Error handling WhatsApp message: {e}")
        return '500'

# Fail callback route
@app.route('/fail', methods=['GET', 'POST'])
def fail():
    return "Fail"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

