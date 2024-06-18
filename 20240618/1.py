import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail帳號資料
gmail_user = 'neko5102@gmail.com'
gmail_password = 'kvyd zijt xynk yrli'

# 建立郵件內容
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = 'neko5102@gmail.com'
msg['Subject'] = '主旨：這是測試郵件'
body = '這是郵件內容。'
msg.attach(MIMEText(body, 'plain'))

# 發送郵件
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, msg['To'], text)
    server.close()

    print('郵件發送成功')
except Exception as e:
    print(f'郵件發送失敗: {e}')