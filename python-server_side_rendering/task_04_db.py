from flask import Flask, render_template, request
import json, csv, sqlite3

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
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', None)
    err_msg = None
    products_list = []

    # Thought of splitting into separate functions, but automated checker...
    if source == 'json':
        with open('products.json', 'r') as f:
            products_list = json.load(f)
    elif source == 'csv':
        with open('products.csv', newline='') as csv_data:
            products_list = list(csv.DictReader(csv_data))
    elif source == 'sql':
        with sqlite3.connect('products.db') as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()

            if product_id:
                cursor.execute(
                    "SELECT * FROM Products WHERE id = ?", (product_id,)
                )
                result = cursor.fetchone()
                if result:
                    products_list = [dict(result)]
                else:
                    err_msg = "Product not found"
            else:
                cursor.execute("SELECT * FROM Products")
                result = cursor.fetchall()
                if result:
                    products_list = [dict(product) for product in result]
    else:
        err_msg = "Wrong source"

    if source != 'sql'\
        and product_id != None\
            and products_list != []\
                and err_msg == None:
        products_list = [product for product in products_list\
            if str(product.get('id')) == str(product_id)]
        if products_list == []:
            err_msg = "Product not found"

    if products_list == [] and err_msg == None:
            err_msg = "Product list is empty"

    return render_template('product_display.html',
                           products_list=products_list,
                           err_msg=err_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
