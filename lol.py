import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

count = int(input("Введите количество сообщений: "))

text = "lol" * 150000

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = "ktoto.ruu@gmail.com"
msg["Subject"] = "Тестовое письмо"
msg.attach(MIMEText(text, "plain"))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

for i in range(count):
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    print(f"Отправлено {i + 1}/{count}")
    time.sleep(1)

server.quit()
print("Готово.")
