import os
from flask import Flask

app = Flask(__name__)

# Use the environment variable for port, default to 5000 if not set
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app with the specified port
    app.run(host='0.0.0.0', port=port)
