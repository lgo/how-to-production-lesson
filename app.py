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

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/exception')
def exception_endpoint():
    raise Exception("Uh oh, world")


app.run(host='0.0.0.0', port=5000)
