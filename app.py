import os
from flask import Flask, render_template, request, flash, redirect, url_for
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-here")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/why-choose-us')
def why_choose_us():
    return render_template('why-choose-us.html')

@app.route('/network')
def network():
    return render_template('network.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, phone, message]):
            flash('Please fill in all required fields.', 'error')
        else:
            # In a real application, you would send an email or save to database
            flash('Thank you for your inquiry! We will contact you soon.', 'success')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
