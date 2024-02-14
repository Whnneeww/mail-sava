from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mailの設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'whnneeww@gmail.com'
app.config['MAIL_PASSWORD'] = 'A26384459s'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        email = request.json['email']

        # メール送信処理
        msg = Message('Test Email', sender='your-email@gmail.com', recipients=[email])
        msg.body = 'This is a test email sent from the web application.'

        mail.send(msg)

        return 'Email sent successfully', 200
    except Exception as e:
        print(str(e))
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
