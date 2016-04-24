from flask import Flask, render_template
from gopigo import *
import os
import picamera
import time
import datetime
import dropbox
import env

app = Flask(__name__)

client = dropbox.client.DropboxClient(env.DROPBOX_TOKEN)

@app.route('/control/<command>')
def up(command):
  if command == 'up':
    bwd()
  elif command == 'stop':
    stop()
  elif command == 'down':
    fwd()
  elif command == 'right':
    left()
  elif command == 'left':
    right()  
 
  return 'Done'
  
@app.route('/camera/<command>')
def camera(command):
  if command == 'snapshot':
    with picamera.PiCamera() as camera:
      camera.resolution = (1024, 768)
      camera.start_preview()
      # Camera warm-up time
      time.sleep(1)
      ts = time.time()
      file =  datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
      camera.capture('images/'+file+'.jpg')

      f = open('images/'+file+'.jpg', 'rb')
      response = client.put_file(file+'.jpg', f)
      print 'uploaded: ', response
      
      os.remove('images/'+file+'.jpg')

  return 'Done'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
