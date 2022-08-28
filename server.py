from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route('/')
def index():
    print('index.html is being rendered')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)