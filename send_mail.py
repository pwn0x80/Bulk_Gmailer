import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart # give support to attack text file etc
import login
#account detail
username = login.your_email
password = login.your_password


# email information
def send_mail(text=None, subject=None, from_email=login.your_email, to_email=None, html=None):
    assert isinstance(to_email, list)  # error shows if username is not list
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['to'] = ", " .join(to_email)
    msg['subject'] = subject

  
# send email
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
         html_part = MIMEText(html, 'html')
         msg.attach(html_part)
    msg_str = msg.as_string()
   

    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg_str)
    server.quit()





   # method-2 auto quit
"""
with smtplib() as server:
    pass
"""






