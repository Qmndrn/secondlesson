import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

in_progress_lessons = ["Python введение", "Python введение.Продолжение", "Основы Python"]
completed_lessons = [""]
time = "месяц"

answer = input("Есть ли у Вас завершенные модули? (да/нет): ").lower().strip()

if answer == "да":
    text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}.
Я выполнил модули: "{", ".join(completed_lessons)}".
Сейчас я работаю над модулями: "{", ".join(in_progress_lessons)}".
Обучение мне нравится, я получил много знаний!"""
    
elif answer == "нет":
    text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}.
Сейчас я работаю над модулями: "{", ".join(in_progress_lessons)}".
Обучение мне нравится, я получил много знаний!"""
    
else:
    print("Ваш ответ мне не понятен! Отправляется стандартное сообщение!")
    text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}.
Сейчас я работаю над модулями: "{", ".join(in_progress_lessons)}".
Обучение мне нравится, я получил много знаний!"""
    

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = "ktoto.ruu@gmail.com"
msg["Subject"] = "Тестовое письмо"
msg.attach(MIMEText(text, "plain"))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()
