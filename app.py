from flask import Flask, render_template
from gopigo import *
import time

app = Flask(__name__)

@app.route('/control/<command>')
def up(command):
  if command == 'up':
    fwd()
  elif command == 'stop':
    stop()
  elif command == 'down':
    bwd()
  elif command == 'left':
    left()
  elif command == 'right':
    right()  
 
  return 'Done'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
