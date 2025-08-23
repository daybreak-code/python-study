from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/signin', methods=['GET'])
def home():
    return "Hello, Flask!"

@app.route('/signin', methods=['POST'])
def sign_form():
    return '''
        <form action="/signin" method="post">
            <p><input name="username"></p>
            <p><input name="password" type="password"></p>
            <p><button type="submit">Sign In</button></p>
        </form>
    '''

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
if __name__ == '__main__':
    app.run()
    