from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/twofourtwofive')
def twofourtwofive():
    return render_template('twofourtwofive.html')

if __name__ == '__main__':
    app.run(debug=True)