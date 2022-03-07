import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    get_command_linux = os.popen('hostname')
    d_command = get_command_linux.read()
    return render_template('index.html', d_output=d_command)

    # main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', debug = False)