from flask_app import app
from flask_app.controllors import Dojo_Survey

if __name__ == '__main__':
    app.run(debug=True, port=8000)