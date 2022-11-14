from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = request.form['strawberry']
    blackberry = request.form['blackberry']
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    count = int(strawberry)+int(blackberry)+int(apple)+int(raspberry)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    student_id = request.form["student_id"]
    return render_template("checkout.html" ,strawberry=strawberry,blackberry=blackberry,apple=apple,raspberry=raspberry,first_name=first_name,last_name=last_name,student_id=student_id,count=count)

@app.route('/fruits')         
def fruits():
    

    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)     