
def send_mail(query, user):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    MY_ADDRESS = "testyprojekt@gmail.com"
    PASSWORD = "12345678A!"
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    msg = MIMEMultipart()
    msg['From'] = MY_ADDRESS
    msg['To'] = user
    msg['Subject'] = "Kod przesyłki"
    msg.attach(MIMEText(query, 'plain'))
    s.send_message(msg)
    del msg


send_mail("2390wqe","pp.kotlewski@gmail.com")
