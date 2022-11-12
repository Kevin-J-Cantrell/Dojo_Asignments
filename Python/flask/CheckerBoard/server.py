from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',row=8,col=8 )
@app.route('/<int:row>')
def Row(row):
    return render_template('index.html',row=row,col=8)
@app.route('/<int:row>/<int:col>')
def Rows(row,col):
    return render_template('index.html',row=row,col=col)
@app.route('/<string:color1>/<string:color2>')
def Color(color1,color2):
    return render_template('index.html',col=8,row=8,color1=color1,color2=color2)
@app.route('/<int:col>/<string:color1>/<string:color2>')
def change(col,color1,color2):
    return render_template('index.html',col=col,row=8,color1=color1,color2=color2)
@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def all(row,col,color1,color2):
    return render_template('index.html',col=col,row=row,color1=color1,color2=color2)
if __name__=='__main__':
    app.run(debug=True,port=5000)