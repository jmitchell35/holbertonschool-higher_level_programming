from flask import Flask, render_template, request
import json, csv

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
    try:
        # load data for template
        with open('items.json', 'r') as f:
            data = json.load(f)
        items_list = data.get("items", [])
    except FileExistsError:
        items_list = []
        
    # pass data to template
    return render_template('items.html', items_list=items_list)

@app.route('/products')
def items(source, id):
    source = request.args.get('source')
    product_id = request.args.get('id')
    err_msg = None
    products_list = []

    if source == 'json':
        with open('products.json', 'r') as f:
            products_list = json.load(f)
    elif source == 'csv':
        with open('products.csv', newline='') as csv_data:
            products_list = list(csv.DictReader(csv_data))
    else:
        err_msg = "Wrong source"

    if id != None and products_list != []:
        products_list = [product for product in products_list\
            if str(product.get('id')) == str(product_id)]
        if products_list == []:
            err_msg = "Product not found"

    if products_list == [] and err_msg == None:
            err_msg = "Product list is empty"

    return render_template('products_display.html',
                           products_list=products_list,
                           err_msg=err_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
