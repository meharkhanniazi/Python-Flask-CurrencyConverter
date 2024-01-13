from flask import Flask, render_template, request
import requests, os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = float(request.form.get('amount'))
        response = requests.get(f'https://v6.exchangerate-api.com/v6/cb456cf692ff5e86da9404ff/latest/{from_currency}')
        res = response.json()['conversion_rates'][to_currency]
        convertedAmt = round(res * amount,2)
        
        return render_template('index.html', result=True, converted_amount=convertedAmt, to_currency=to_currency)

    return render_template('index.html', result=False)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
