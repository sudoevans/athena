from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()

# Get the database URL from the environment variables


app = Flask(__name__)
CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

def complete(messages, function_call="auto"):
    messages.append({"role": "system", "content": "this is my response"})

@app.route('/query', methods=["POST"])
@cross_origin()
def process_query():
    data = request.json
    messages = data.get("messages", [])
    complete(messages)
    response_content = messages[-1]["content"]

    return jsonify({"response": response_content})


account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming upnow',
  to='whatsapp:+12028219726'
)

print(message.sid)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
