from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confirm", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        un= request.form.get('username')
        em = request.form.get('email')
        ph = request.form.get('phonenumber')
        return  render_template('confirm.html',username=un,email=em,phonenumber=ph)

if __name__ == "__main__":
    app.run(debug=True)