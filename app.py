from flask import Flask,request,app,jsonify,url_for,render_template

app = Flask(__name__) @app. route("/") 
def hello_world(): return "Hello, World!"
