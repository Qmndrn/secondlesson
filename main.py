import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

my_lessons = ["Python введение", "Python введение.Продолжение", "Основы Python"]
time = "месяц"

answer = input("Есть ли у Вас завершенные модули?(да/нет): ").lower().strip()
if answer in "да":
    text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями "{", ".join(my_lessons)}". Обучение мне нравится, я получил море знаний!"""
elif answer in "нет":
    text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями "{", ".join(my_lessons)}". Обучение мне нравится, я получил море знаний!"""
else:
    print("Ваш ответ мне не понятен! Отправляется стандартное сообщение!")
    text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями "{", ".join(my_lessons)}". Обучение мне нравится, я получил море знаний!"""

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = "ktoto.ruu@gmail.com"
msg["Subject"] = "Тестовое письмо"
msg.attach(MIMEText(text, "plain"))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()
