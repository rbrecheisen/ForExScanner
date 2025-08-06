import smtplib
import forexscanner.constants as constants
from email.mime.text import MIMEText


class Mailer:
    def __init__(self):
        self._from = constants.FX_GMAIL_FROM
        self._to = constants.FX_GMAIL_TO
        self._app_password = None

    def __enter__(self):
        self._app_password = self.load_app_password()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def load_app_password(self):
        with open(constants.FX_GOOGLE_APP_PASSWORD_FILE_PATH, 'r') as f:
            app_password = f.readline().strip()
        return app_password

    def send(self, subject, body):
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = self._from
        message['To'] = self._to
        with smtplib.SMTP_SSL(constants.FX_GMAIL_SMTP_HOST, constants.FX_GMAIL_SMPT_PORT) as smtp:
            smtp.login(self._from, self._app_password)
            smtp.send_message(message)
        print('Mailer.send() successful!')