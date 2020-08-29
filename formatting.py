import sys
import requests
from datetime import datetime
import login 
from send_mail import send_mail


def send(to_email=None):
    assert to_email != None
    body_msg = login.write_body
    subject_msg = login.write_subject
    try:
        send_mail(text=body_msg, subject=subject_msg,from_email=login.your_email,to_email=[to_email], html=None)
        
        sent = True
    except:
        print(to_email)
        sent = False
    return sent
lenght = len(sys.argv)
with open("bulk_email.txt") as fhandler:
  email_list = fhandler.readlines()
  total_email = len(email_list)
  print("github.com/Aditya0x34")
  print("twitter: @Aditya0x34")
  

  
for i in range(total_email):
    print('email-', email_list[i])
    email = email_list[i]
    a= send(to_email=email)
    print(a)
    

        

    


