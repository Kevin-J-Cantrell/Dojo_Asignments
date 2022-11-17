from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route('/')
def index():
    if 'count'not in session:
        session["count"]=1    
    elif 'count' in session:
        session["count"] = int(session['count']) + 2
    else: 
        session["count"]=1
    return render_template('index.html')


@app.route('/count', methods=["post"])
def count():
    print("FORM DATA",request.form)
    print("count DATA",request.form)
    if 'count' not in session:
        count = session["count"]
        count.append(request.form)
        session["count"] = count
    else:
        session["count"] += int(request.form["count"]) -2
    return redirect('/')
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True, port=8000)