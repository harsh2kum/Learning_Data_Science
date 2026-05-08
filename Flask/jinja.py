# Build Url Dynamically
# Variable Rule
# Jinja 2 Template Engine

# Jinja 2 Template Engine 
"""
# Jinja2 has multiple ways spacifically to read the data score from the backend
in the html page

{{ }}  - expressions to print output in html
{%...%} - conditionals statement  - if else, for , while loop etc
{#...#} - This is for comments
"""



from flask import Flask, render_template, request,redirect,url_for

# WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1> Welcome to Flask.</H1> </html>" 

@app.route("/index",methods = ['GET'])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

#Variable Rule 
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res = "Passed"
    else:
        res = "Failes"

    return render_template('result.html', result = res)

# Build Url Dynamically
@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res = "Passed"
    else:
        res = "Failes"
    
    exp = {'score': score, "res": res}

    return render_template('result1.html', result = exp)

# if condition 
@app.route('/successif/<int:score>')
def successif(score):


    return render_template('result.html', result = score)

@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == "POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + data_science)/4

    return redirect

if __name__ == "__main__":
    app.run(debug=True)
 
