from flask import Flask

import bugsnag
from bugsnag.flask import handle_exceptions

# Configure Bugsnag
bugsnag.configure(
  api_key = "TOKEN",
  project_root = "/path/to/your/app",
)

app = Flask(__name__)
handle_exceptions(app)

from opbeat.contrib.flask import Opbeat
import time
import random

opbeat = Opbeat(
    app,
    organization_id='PRIVATE',
    app_id='DATA',
    secret_token='TOKEN',
)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/exception')
def exception_endpoint():
    raise Exception("Uh oh, world")

@app.route('/slow')
def slow_endpoint():
    time.sleep(random.randint(1,5))
    return 'Zzzz, world!'

app.run(host='0.0.0.0', port=5000)
