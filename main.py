from flask import Flask, jsonify
from flask import json
from socket import gaierror, gethostbyname
from urllib.parse import urlparse
import requests
from json2html import *

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!, try also /check'


def is_reachable(url):
    """ This function checks to see if a host name has a DNS entry
    by checking for socket info."""
    try:
        gethostbyname(url)
    except gaierror:
        return False
    else:
        return True


def get_status_code(url):
    """ This function returns the status code of the url."""
    try:
        status_code = requests.get(url, timeout=10).status_code
        return status_code
    except requests.ConnectionError:
        return 'Unreachable'


def check_single_url(url):
    """This function checks a single url and if connectable returns
    the status code, else returns UNREACHABLE."""
    if is_reachable(urlparse(url).hostname):
        return str(get_status_code(url))
    else:
        return 'Unreachable'


@app.route('/', methods=['GET'])
def check_services():
    with open('data.json') as json_file:
        data = json.load(json_file)
        status_info = {'services': []}
        for p in data['site']:
            status_info['services'].append({
                'url': p['address'],
                'status code': check_single_url(p['address'])
            })
        return status_info


if __name__ == '__main__':
    app.run()
