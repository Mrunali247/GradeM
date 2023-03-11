import smtplib


class SendMail:
    def __init__(self, email: str, file: str):
        # Takes file location as string
        self.email = email
        self.file = file
        self.password = "mljulmzsljzgyaah"
        self.mail = "gradem2024@gmail.com"

    def send(self):
        pass