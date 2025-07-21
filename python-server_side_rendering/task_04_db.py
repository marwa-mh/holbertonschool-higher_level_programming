from flask import Flask, render_template, request
import json
import csv
import sqlite3
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
    with open("items.json", "r") as outfile:
        data = json.load(outfile)
        items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    error =""
    source = request.args.get('source')
    if source=='json':
        with open("products.json","r") as outfile:
            data = json.load(outfile)
        if request.args.get('id'):
            find_item_by_id =[item for item in data if int(request.args.get('id')) == item['id']]
            if not find_item_by_id:
                error="Product not found"
            data = find_item_by_id
    elif source=='csv':
        with open("products.csv", mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        if request.args.get('id'):
            find_item_by_id =[item for item in data if request.args.get('id') == item['id']]
            
            if not find_item_by_id:
                error="Product not found"
            data = find_item_by_id
    elif source=='sql':
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        if request.args.get('id'):
            cursor.execute('SELECT * FROM Products WHERE id = ?', (request.args.get('id'),))
        else:
            cursor.execute('''
        SELECT * FROM Products
        ''')
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        conn.close()
    else:
        return render_template('product_display.html', items=[], error="Wrong source")
    return render_template('product_display.html', items=data,error=error)

    
    




if __name__ == '__main__':
    app.run(debug=True, port=5000)