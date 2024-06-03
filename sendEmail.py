import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

def send_email(email_recipient, email_subject, email_body):
    # Configurações do e-mail
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    email_sender = os.getenv("EMAIL") 
    email_password = os.getenv("SENHA_EMAIL") 
    # Criação do e-mail
    message = MIMEMultipart()
    message["From"] = email_sender
    message["To"] = email_recipient
    message["Subject"] = email_subject

    # Anexa o corpo do e-mail ao objeto message
    message.attach(MIMEText(email_body, "plain"))

    try:
        # Conexão ao servidor SMTP
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(email_sender, email_password)  # Login no servidor        
        text = message.as_string()  # Converte o objeto message em string
        server.sendmail(email_sender, email_recipient, text)  # Envia o e-mail
        return "E-mail enviado com sucesso!"
    except Exception as e:
        return f"Erro ao enviar e-mail: {e}"
    finally:
        server.quit()  # Fecha a conexão com o servidor

