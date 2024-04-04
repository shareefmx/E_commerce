from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products-details')
def productsdetails():
    return render_template('products-details.html')

@app.route('/Discount price')
def Discountprice():
    return render_template('Discount price.html')

@app.route('/Discount')
def Discount():
    rating = 5
    rating_count = 100
    actual_price = 500
    return render_template('Discount price.html', rating=rating, rating_count=rating_count, actual_price=actual_price)


@app.route('/predict', methods=['POST'])
def predict():
    rating = float(request.form['rating'])
    rating_count = int(request.form['rating_count'])
    actual_price = float(request.form['actual_price'])

    discounted_price = predict_discount(rating, rating_count, actual_price)

    return render_template('result.html', discounted_price=discounted_price)

def predict_discount(rating, rating_count, actual_price):
    discounted_price = actual_price * 0.9  # 10% discount for demonstration
    return discounted_price

if __name__ == '__main__':
    app.run(debug=True)
