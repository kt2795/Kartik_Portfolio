from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/valuation', methods=['POST'])
def calculate_valuation():
    # Get the influencer data from the form
    reach = int(request.form['reach'])
    growth_rate = float(request.form['growth_rate'])
    engagement_rate = float(request.form['engagement_rate'])
    future_months = int(request.form['future_months'])
    discount_rate = float(request.form['discount_rate'])
    valuation_ip_assets = float(request.form['valuation_ip_assets'])
    num_shares = int(request.form['num_shares'])

    # Calculate future earnings
    future_audience = (reach * (1 + growth_rate) ** future_months)*(engagement_rate/100)
    future_earnings_per_video = (future_audience / 1000) * 20 + future_audience * 5
    future_earnings = future_earnings_per_video * 12 * 3

    # Calculate total future value
    total_future_value = future_earnings + valuation_ip_assets

    # Apply discount rate
    discounted_future_value = total_future_value / (1 + discount_rate)

    # Calculate price per share
    price_per_share = discounted_future_value / num_shares

    # Return the valuation results as JSON response
    return jsonify({
        'future_earnings': future_earnings,
        'total_future_value': total_future_value,
        'discounted_future_value': discounted_future_value,
        'price_per_share': price_per_share
    })

if __name__ == '__main__':
    app.run(debug=True)
