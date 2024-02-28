from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    products = [
        {
            'title': 'Product 1',
            'description': 'Description of Product 1'
        },
        {
            'title': 'Product 2',
            'description': 'Description of Product 2'
        },
        {
            'title': 'Product 3',
            'description': 'Description of Product 3'
        },
        {
            'title': 'Product 4',
            'description': 'Description of Product 4'
        }
    ]
    return render_template('index.html', products=products)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
