import requests
from twilio.rest import Client

account_sid = #Sid da sua conta do Twilio
auth_token = #Token da sua conta do Twilio
client = Client(account_sid, auth_token)

API_KEY = #Chave de API que você pegará da sua conta do Satelite da OPENWEATHER.
cidade = #Cidade que o satelite vai buscar as informações
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(f'Bom-dia Senhor, na sua localização atual está... {descricao}, com temperatura atual de: {temperatura}ºC.')
message = client.messages.create(
        to= #Número para o qal você vai enviar a mensagem.
        from_= #Número do qual vai enviar a mensagem.
        body=f'Bom-dia Senhor, na sua localização atual está... {descricao}, com temperatura atual de: {temperatura}ºC.')
print(message.sid)

