
### ✅ `README.md` — *OTP Verification with Flask*

```markdown
# 🔐 OTP Verification System Using Flask

This is a simple and beginner-friendly project built using **Python Flask** that demonstrates how **OTP (One-Time Password)** based verification works.

✨ This project is great for understanding:
- How OTPs are generated
- How they're stored temporarily
- How form data is processed
- How basic front-end and back-end communication works

---

## 🚀 Features

- Enter an email to receive a random OTP (4 digits)
- OTP is printed in the terminal for simplicity (simulating email/SMS)
- User is redirected to an OTP input page
- On successful OTP match, the user is logged in
- Stylish and modern UI using just HTML and CSS (no external CSS files or frameworks)

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** (lightweight web framework)
- **HTML5 & CSS3** for frontend styling

---



## 🧠 How It Works

1. User enters their email.
2. The server generates a **random 4-digit OTP**.
3. The OTP is stored in a dictionary using the email as the key.
4. The user is redirected to a new page to enter the OTP.
5. The server compares the entered OTP with the stored one.
6. If matched, a success message is shown. Otherwise, an error is returned.

---

## 📁 Project Structure

```

OTP/
├── app.py                # Main Flask application
├── README.md             # Project documentation (this file)
├── requirements.txt      # Dependencies (Flask only)
└── screenshots/          # Screenshots folder (optional)

````

---

## 💻 Run It Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/otp-flask.git
   cd otp-flask
````

2. Install Flask:

   ```bash
   pip install Flask
   ```

3. Run the Flask app:

   ```bash
   python3 app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

5. Use your email, get the OTP in your terminal, and verify.

---


