from flask import Flask, render_template
from gopigo import *
import time
import datetime
app = Flask(__name__)

@app.route('/control/<command>')
def up(command):
  if command == 'up':
    bwd()
  elif command == 'stop':
    stop()
  elif command == 'down':
    fwd()
  elif command == 'left':
    left()
  elif command == 'right':
    right()  
 
  return 'Done'
  
@app.route('/camera/<command>')
def up(command):
  if command == 'snapshot':
    with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(1)
    ts = time.time()
    file =  datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    camera.capture(file+'.jpg')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
