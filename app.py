from flask import Flask
from flask import request
import json
# import time
# from AlarmController import AlarmController as AC

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Karros Hermes!'

@app.route('/check', methods=['POST'])
def check():
  profile = 'System'
  data = request.json
  if(data):
    profile = data.get('profile')
  result = {'message': f'{profile} is good with 120 services up!'}
  return json.dumps(result)

@app.route('/alarm')
def send_alarm():
  try:
    # alarm = AC(32, 'LOW')

    # # Turn on alarm
    # alarm.on()
    # # Alarm in 15 seconds
    # time.sleep(15)
    # alarm.off()
    # alarm.clean()

    return 'Send Alarm signal to Light Channel!'

  except Exception as err:
    raise err

if __name__ == '__main__': 
  app.run(debug=True, host='0.0.0.0')