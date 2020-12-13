from flask import Flask
import time
from AlarmController import AlarmController as AC

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Karros Hermes!'

@app.route('/alarm')
def send_alarm():
  try:
    alarm = AC(32, 'LOW')

    # Turn on alarm
    alarm.on()
    # Alarm in 15 seconds
    time.sleep(15)
    alarm.off()
    alarm.clean()

    return 'Send Alarm signal to Light Channel!'

  except Exception as err:
    raise err

if __name__ == '__main__': 
  app.run(debug=True, host='0.0.0.0')