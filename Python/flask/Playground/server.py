from flask import Flask, render_template
app = Flask(__name__)
@app.route('/Play')
def play():
    
    return render_template('index.html',num=3,color="blue")
@app.route('/Play/<int:num>')
def count(num):
    
    return render_template('index.html',num=num,color="blue")
@app.route('/Play/<int:num>/<color>')
def index(num,color):
    
    return render_template('index.html',num=num,color=color)
if __name__=='__main__':

    app.run(debug=True,port=5000)