from flask import Flask, Response, jsonify, request, session

from .errors import errors

app = Flask(__name__)
app.register_blueprint(errors)

pressed = False

@app.route("/")
def index():
    return Response("Hello, world!", status=200)


@app.route("/button_pressed") 
def button_pressed():
    global pressed
    pressed = True
    return jsonify({"btn_press": "saved"})
    
@app.route("/check") 
def check():
    global pressed
    if pressed:
        pressed = False
        return jsonify({"status": "pressed"})
    return jsonify({"status": "none"})
    


@app.route("/health")
def health():
    return Response("OK", status=200)
