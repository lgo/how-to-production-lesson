from flask import Flask

import bugsnag
from bugsnag.flask import handle_exceptions

# Configure Bugsnag
bugsnag.configure(
  api_key = "c7dd55a21f726e33ff9658568b6aac42",
  project_root = "/path/to/your/app",
)

app = Flask(__name__)
handle_exceptions(app)

from opbeat.contrib.flask import Opbeat
import time
import random

opbeat = Opbeat(
    app,
    organization_id='2b89a4ba846e4168badfff0cd7014ad0',
    app_id='7c28c65c00',
    secret_token='005b0c5022183aeacdafe45cd754e99e85c99558',
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
