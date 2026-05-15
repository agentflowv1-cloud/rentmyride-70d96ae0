import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

class Booking:
    def __init__(self, rental_details, additional_services):
        self.rental_details = rental_details
        self.additional_services = additional_services

    def send_confirmation_email(self, user_email):
        msg = MIMEMultipart()
        msg['From'] = 'booking@example.com'
        msg['To'] = user_email
        msg['Subject'] = 'Booking Confirmation'
        body = 'Dear User,\n\nYour booking has been confirmed.\nRental Details: ' + str(self.rental_details) + '\nAdditional Services: ' + str(self.additional_services)
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(msg['From'], 'password')
        text = msg.as_string()
        server.sendmail(msg['From'], msg['To'], text)
        server.quit()

    def confirm_booking(self, user_email):
        self.send_confirmation_email(user_email)
        return 'Booking confirmed and email sent'

def main():
    rental_details = {'name': 'John', 'date': '2024-09-16', 'time': '10:00'}
    additional_services = ['service1', 'service2']
    booking = Booking(rental_details, additional_services)
    print(booking.confirm_booking('user@example.com'))

if __name__ == '__main__':
    main()