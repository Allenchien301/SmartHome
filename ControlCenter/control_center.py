import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import serial
import time

S = serial.Serial('com5', 9600, timeout=2)

def sendEmailAlert(msg):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        content = MIMEMultipart()
        content["subject"] = "(´・ω・`)"
        content["from"] = "(´・ω・`)"
        content["to"] = "s810459@email.nlhs.tyc.edu.tw"
        content.attach(MIMEText("00000000"))
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("allenchien40804@gmail.com","uyfqeltpddqhiuxs")
            smtp.send_message(content)
            print("訊息已發送!")
        except Exception as e:
            print("Error message: ", e)



IntruderAlert = False
while True:
    data = S.readline().decode().rstrip()

    if data == "alert" and not IntruderAlert:
        IntruderAlert = True
        print("入侵警報！！！")
        sendEmailAlert("入侵警報！！！")
    elif data == "normal" and IntruderAlert:
        IntruderAlert = False
        print("警報解除")
        sendEmailAlert("警報解除")
time.sleep(1)            