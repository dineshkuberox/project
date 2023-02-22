from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def root():
    ip_address = request.remote_addr
    port = request.environ.get('REMOTE_PORT')
    hostname = request.host
    return {'ip_address': ip_address, 'port': port, 'hostname': hostname, 'date': datetime.now()}

@app.route('/status/')
def status():
    return "please enter a valid url"

@app.route('/status/<string:url>')
def url1(url):
    url_ = url.replace('-','.')
    return redirect(f"http://{url_}")

if __name__ == '__main__':
    app.run(debug=True)
