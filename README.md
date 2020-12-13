# sweet-rasp-api

SweetHome Raspberry Pi API

## Startup

Flask app will be started at port 5000
`python3 app.py`

## Expose API to public with Ngrok

In Raspbeery Pi Command line:
`/home/pi/opt/ngrok http 5000`

In MacOS:
`cd ~/opt/bin`
`./ngrok http 5000`

## Usage

When call to https://light-hermes.karrostech.net/alarm
-> Alarm On in 15 seconds then Turn off itself
