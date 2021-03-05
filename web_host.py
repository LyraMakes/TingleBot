from flask import Flask, render_template
from threading import Thread

app = Flask('')

numServers = 0


# Getters and setters
def set_num_servers(n: int) -> type(None):
    global numServers
    numServers = n


def get_num_servers() -> int:
    global numServers
    return numServers


# Web app routes
@app.route('/')
def home() -> str:
    return render_template('index.html', guilds=get_num_servers())


@app.route('/ping')
def ping() -> str:
    return 'Current status: Up'


def run() -> type(None):
    app.run(host='0.0.0.0', port=8080)


def keep_alive() -> type(None):
    t = Thread(target=run)
    t.start()
