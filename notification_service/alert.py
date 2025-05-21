
import smtplib

def send_email(to, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail('your_email@gmail.com', to, f"Subject: {subject}

{body}")
    