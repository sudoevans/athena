from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
