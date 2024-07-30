import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.models.setting.db_connection import db_connection_handler

conn = db_connection_handler.connect()

def email_select():
    cursor = conn.cursor()
    cursor.execute(
        '''
       SELECT * FROM emails_to_invite ORDER BY date_creator DESC LIMIT 1; 
        ''')
    
    result = cursor.fetchall()
    result_email = [result[0][2]]
    send_email(result_email, "Olá,\n\nAqui esta seu código de confirmação\n\n302308208302\n\nObrigado Pelo cadastro!")



def send_email(to_addrs, body):
    from_addr = "rhiannon.dach72@ethereal.email"
    login = "rhiannon.dach72@ethereal.email"
    password = "Dz9yM4ByjFKd8jnsqB"

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subject"] = "Confirmação de Viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()

