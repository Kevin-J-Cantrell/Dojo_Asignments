from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route('/')
def index():
    if 'count' not in session:
        session["count"]=1
    elif 'count' not in session:
        session['count']+=request.form["count"]
    else:
        session["count"]+=2
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True, port=8000)