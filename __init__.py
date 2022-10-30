from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'messenger',
                       'email': 'xoxo@gmail.com'})

app.run()
