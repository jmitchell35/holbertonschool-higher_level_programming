from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # load data for template
    with open('items.json', 'r') as f:
        data = json.load(f)
    # pass data to template
    return render_template('items.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
