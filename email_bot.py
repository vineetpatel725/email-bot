import sys
import smtplib
import pyttsx3
from email.message import EmailMessage
from getpass import getpass

engine = pyttsx3.init()

def talk(msg):
    engine.say(msg)
    engine.runAndWait()

def connection():
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    return s

def sign_in(email,pwd):
    try:
        s.login(email,pwd)
        #print("Successfully Signed.")
        talk("You have Successfully Signed into your account. Now you can send the email!")
    except smtplib.SMTPAuthenticationError as err:
        print("Error:",err) 
        talk("I found an error that you can see on your console!")        
        sys.exit()
    except Exception as err:
        print("Error:",err) 
        talk("I found an error that you can see on your console!")        
        sys.exit()

def sign_out(cn):    
    try:
        while True:
            ans = input("Response (Yes/No):").lower().strip()
            if(ans == ''):
                talk("You have not gave me proper response! Please give me response.")
                continue
            else:
                if(ans == 'yes'):
                    cn.quit()
                    talk("You have Successfully Sign out from your account. Have a Nice Day! Good Bye!")
                    break
                elif(ans == 'no'):
                    talk("Okay!")
                    break
    except Exception as err:
        print("Error:",err) 
        talk("I found an error that you can see on your console!") 
        sys.exit()       

def get_sender_info():
    try:
        talk("Give me your email for signin!")

        while True:
            mail = input("Email:").lower().strip()
            if(mail != ''):
                break
            else:
                talk("You have not give me your email! Please give me your email for signin!")

        talk("Give me your password for signin!")

        while True:
            pwd = getpass().strip()
            if(pwd != ''):
                break
            else:
                talk("You have not give me your password! Please give me your password for signin!")
        return mail,pwd
    except Exception as err:        
        print("Error:",err)
        talk("I found an error that you can see on your console!")   
        sys.exit()     

def get_receiver_mails():
    try:
        mails = list()
        talk("Give me the mail of receiver!")

        while True:
            mail = input('Receiver Email:').lower().strip()
            if(mail != ''):
                mails.append(mail)
                talk("Do you want to sent mail to more then on person?")                
                while True:
                    ans = input("Response (Yes/No):").lower().strip()
                    if(ans == 'yes'):
                        #print(ans)
                        talk("Give me the all mails which you want sent an email. If you had wrote all emails then lastly write the break or end to stop it!")
                        while True:
                            mail = input('Receiver Email:').lower().strip()
                            if(mail != ''):
                                if(mail == 'end' or mail == 'break'):
                                    break
                                if(mail != 'end' or mail != 'break'):
                                    mails.append(mail)
                            else:
                                talk("You have not entered any email! If you had wrote all emails then wtite the break or end to stop it!")
                        break
                    elif(ans == 'no'):
                        #print(ans)
                        break
                    else:
                        talk("You have not gave me proper responses! Please give me response.")                    
                break
            else:
                talk("You have not give me receiver email! Please give me receiver email to send an email!")
        return mails
    except Exception as err:
        print("Error:",err)
        talk("I found an error that you can see on your console!")
        sys.exit()

def get_mail_subject_content():
    try:
        message = EmailMessage()    
        
        while True:
            talk("Give me the Subject of the mail!")
            subject = input("Subject of Mail:")
            if(subject == ""):
                talk("You have not gave me the subject of the mail!")
                talk("Do you want to give me the subject of the mail?")
                while True:
                    ans = input("Response (Yes/No):").lower().strip()                                
                    if(ans == 'yes' or ans == 'no'):
                        break
                    else:
                        talk("You have not gave me proper response! Please give me response.")
                if(ans == 'yes'):
                    continue
                elif(ans == 'no'):
                    talk("Okay!")
                    break
            else:
                message["Subject"] = subject
                break
        
        while True:
            talk("Give me the Message of the mail!")
            msg = input("Message of Mail:")
            if(msg == ""):
                talk("You have not gave me the message of the mail!")
                talk("Do you want to give me the message of the mail?")
                while True:
                    ans = input("Response (Yes/No):").lower().strip()                                
                    if(ans == 'yes' or ans == 'no'):
                        break
                    else:
                        talk("You have not gave me proper response! Please give me response.")
                if(ans == 'yes'):
                    continue
                elif(ans == 'no'):
                    talk("Okay!")
                    break
            else:
                message.set_content(msg)
                break
        return message
    except Exception as err:
        print("Error:",err)
        talk("I found an error that you can see on your console!")
        sys.exit()

def send_mail(s_mail,r_mails,message,cn):
    try:
        message['From'] = s_mail
        message["To"] = r_mails
        cn.send_message(message)
        talk("I Have sended mail for you!")
    except Exception as err:
        print("Error:",err)
        talk("I found an error that you can see on your console!")
        sys.exit()
        

talk("Hii! I am email sender bot.")
sender_mail, sender_pwd = get_sender_info()
s = connection()
sign_in(sender_mail,sender_pwd)
receiver_mails = set(get_receiver_mails())
print(receiver_mails)
msg = get_mail_subject_content()
send_mail(sender_mail,receiver_mails,msg,s)
talk("Do you want to sign out?")
sign_out(s)