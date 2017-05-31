from flask improt Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"
    pass

if __name__ == "__main__":
    app.run(debug=True)
