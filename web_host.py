from flask import Flask
from threading import Thread

app = Flask('')

numServers = 8

def set_num_servers(n: int) -> type(None):
  global numServers
  numServers = n

def get_num_servers() -> int:
  global numServers
  return numServers

@app.route('/')
def home():
  return 'temp'


@app.route('/ping')
def ping():
  return 'Current status: Up'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
