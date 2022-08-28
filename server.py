from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = '1234567890'

@app.route('/')
def index():
    print('index.html is being rendered')
    return render_template('index.html')

@app.route('/result')
def result():
    print('result.html is being rendered')
    return render_template('result.html')   

@app.route('/user_info', methods=['POST'])
def user_info():
    print('gathering the info from the form!')
    session['user_name'] = request.form['user_name']
    session['dojo_loc'] = request.form['dojo_loc']
    session['fav_lang'] = request.form['fav_lang']

    return redirect('/result', name_on_template=session['user_name'], dojo_on_template=session['dojo_loc'], fav_lang_on_template=session['fav_lang'])

if __name__ == '__main__':
    app.run(debug=True)