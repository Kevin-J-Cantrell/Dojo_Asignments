from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    
    return 'Hello yo!'
@app.route('/success') # The @"success" decorator associates this route with the function immediately following
def success():
        return "Success!"
    
@app.route('/Hello/<anything>') # returns something that you put in the browser
def hello(anything): 
    return f'Hello {anything}!'

@app.route('/hello/<string:anything>/<int:num>') # returns something that you put in the browser
def can(anything,num): 
    return f'Hello {anything * num}!'
    # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=8000)    # Run the app in debug mode.

