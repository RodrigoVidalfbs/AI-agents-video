from sendEmail import send_email

def get_response_time(url):
    if url == "learnwithhasan.com":
        return 0.5
    if url == "google.com":
        return 0.3
    if url == "openai.com":
        return 0.4
    
def some_dois_mumeros(n1 , n2):
    return n1 + n2
    
def envie_um_email(destinatario, assunto, corpo):
    return send_email(destinatario, assunto, corpo)
    

