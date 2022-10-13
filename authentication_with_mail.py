from email.message import EmailMessage
import smtplib
import pyotp


if __name__ == '__main__':
    msg = EmailMessage()
    msg['Subject'] = 'This is my email for multiple people'
    msg['From'] = 'jrbhatt18p10@gmail.com'
    msg['To'] = ['janmay.bhatt@elastic.run']
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    message = 'SECRET KEY: {}\nFIRST OTP: {}'.format(secret, totp.now())
    msg.set_content(message)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('jrbhatt18p10@gmail.com', 'xxxxxxxxxxxxxxxxx')
        smtp.send_message(msg)
