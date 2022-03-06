import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    get_command_linux = os.popen('hostname')
    d_command = get_command_linux.read()
    return render_template('index.html', d_output=d_command)