from flask import Flask # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')         
def Hello_World():
    return "Hello World" 
@app.route('/dojo')         
def Dojo():
    return "Dojo!" 
@app.route('/say/<name>')           
def say(name):
    return f"Hi {name}!"  
@app.route('/repeat/<int:num>/<string:rep>')          
def Repeat(num,rep):
    return (num*f"<p>{rep}</P>")
# @app.route('/')         
# def Hello_World():
    # return "Hello World" 
if __name__=="__main__":     
    app.run(debug=True,port=5000)    
@app.route('/')
def main():
    
    return