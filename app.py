from flask import Flask, render_template, request, jsonify
from main import main

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def story_image_generator():
    prompt = request.json['prompt']

@app.route('/post', methods=['POST'])
def post():
    return "recived: {}".format(request.form)

if __name__ == "__main__":
    app.run(debug=True)