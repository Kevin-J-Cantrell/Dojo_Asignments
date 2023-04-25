from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'My Secret Not Yours!' # set a secret key for security purposes
@app.route('/hello')
def index():


    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=8000)