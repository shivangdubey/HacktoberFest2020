import smtplib

def sending():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('type senders id here', 'app password')

    subject  = 'subject'
    body = 'body'

    msg = f"subject: {subject}\n\n{body}"
    server.sendmail('type senders id here', '''type receivers emial id here''', msg)
    server.quit()
    print('DONE')

sending()