from flask import Flask, request, render_template_string, redirect, url_for
import random

app = Flask(__name__)
otp_storage = {}

# Modern styled HTML for email input
html_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>OTP Login</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
        }
        .box {
            background-color: rgba(0,0,0,0.2);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
        }
        input[type="text"], input[type="submit"] {
            padding: 12px;
            margin: 10px 0;
            width: 100%;
            border: none;
            border-radius: 8px;
        }
        input[type="submit"] {
            background: #fff;
            color: #333;
            font-weight: bold;
            cursor: pointer;
        }
        h2 {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Enter Your Email</h2>
        <form method="post">
            <input type="text" name="email" placeholder="you@example.com" required>
            <input type="submit" value="Send OTP">
        </form>
    </div>
</body>
</html>
'''

# Modern styled HTML for OTP input
otp_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>Verify OTP</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #f093fb, #f5576c);
            color: white;
            display: flex;
            height: 100vh;
            justify-content: center;
            align-items: center;
        }
        .box {
            background-color: rgba(0,0,0,0.2);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
        }
        input[type="text"], input[type="submit"] {
            padding: 12px;
            margin: 10px 0;
            width: 100%;
            border: none;
            border-radius: 8px;
        }
        input[type="submit"] {
            background: #fff;
            color: #333;
            font-weight: bold;
            cursor: pointer;
        }
        h2 {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Enter OTP</h2>
        <form method="post">
            <input type="text" name="otp" placeholder="Enter 4-digit OTP" required>
            <input type="submit" value="Verify OTP">
        </form>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        otp = str(random.randint(1000, 9999))
        otp_storage[email] = otp
        print(f"✅ OTP for {email} is: {otp}")
        return redirect(url_for('verify', email=email))
    return render_template_string(html_form)

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    email = request.args.get('email')
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if otp_storage.get(email) == entered_otp:
            return "✅ OTP Verified! You’re Logged In 🎉"
        else:
            return "❌ Incorrect OTP. Please go back and try again."
    return render_template_string(otp_form)

if __name__ == '__main__':
    print("Starting the Flask app...")
    app.run(debug=True)
