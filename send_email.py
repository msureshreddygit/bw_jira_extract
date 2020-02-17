from datetime import datetime
import smtplib, ssl
import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class GenerateMail:
    @staticmethod
    def generate_mail(att_file):
        if att_file is None:
            print("File attachment is empty")
        else:
            mail_content = '''
            Hello Team,
            
            Please find the attached report for Bitwise jira extract project.
            (Note: This is an auto-generated E-mail. Kindly do not respond)
            
            Regards,
            Fandango Team
            '''

            file_name = datetime.now().strftime('Jira_Extract_Execution_Report_%Y%m%d_%H%M%S.xlsx')
            # The mail addresses and password
            sender_address = 'jiraextract@gmail.com'
            sender_pass = 'zazeipkoyxnboibw'
            # 'Sharvari.Hongekar@bitwiseglobal.com,Roshan.Deshpande@bitwiseglobal.com,Radhika.Ingle@bitwiseglobal.com,Ravi.Goklani@bitwiseglobal.com,jayanaga.medapati@bitwiseglobal.com'
            receiver_address = 'rohan.gangathade1@bitwiseglobal.com'
            carbon_copy = 'jayanaga.medapati@bitwiseglobal.com,bhagwat.niras@bitwiseglobal.com'

            # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message["Cc"] = carbon_copy
            message['Subject'] = 'Jira Extract Execution Report'

            # The subject line
            # The body and the attachments for the mail
            try:
                message.attach(MIMEText(mail_content, 'plain'))
                attach_file = open(att_file, 'rb')  # Open the file as binary mode
                payload = MIMEBase('application', 'octate-stream')
                payload.set_payload(attach_file.read())
                encoders.encode_base64(payload)  # encode the attachment

                # add payload header with filename
                payload.add_header('Content-Disposition', 'attachment', filename=file_name)
                message.attach(payload)
            except Exception:
                print("An error occurred while attaching a file to the mail")
                logging.error("An error occurred while attaching a file to the mail")

            # Create SMTP session for sending the mail
            try:
                session = smtplib.SMTP('smtp.gmail.com', 587)
                session.starttls()
                session.login(sender_address, sender_pass)
                text = message.as_string()
                session.sendmail(sender_address, receiver_address.split(','), text)
                session.sendmail(sender_address, carbon_copy.split(','), text)
                session.quit()
                print('Mail sent successfully')
                logging.info("Mail sent successfully")
            except Exception:
                print("An error occurred while login to the Gmail SMTP server")
                logging.error("An error occurred while login to the Gmail SMTP server")


mailObj = GenerateMail()