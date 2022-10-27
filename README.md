# SATELITE-SMS
Automação de um bot para envio de mensagem da Temperatura climática de determinado local que o usuário desejar (Projeto ainda não finalizado)

O site para puxar as informações do satelite é o "Open Weather Map", no próprio site eles disponibilizam uma API no qual eu fiz o uso para programar esse bot de automação.
A maneira que usei para enviar as mensagens em SMS foi pela API do Twilio, onde criei uma conta e através dela a automação tem acesso e fará o envio da mensagem através desta conta criada.
Ps: A mensagem de SMS só pode ser enviada em números que tenham conta criada no Twilio, caso tente ser enviado para um número que não tenha conta o próprio código vai acusar um erro dizendo que o número é inexistente. (É o básico de banco de dados né pfvr, o site só vai enviar para os números que eles tem no banco de dados deles, além disso se encaixa até mesmo em crime enviar algo sem uma permissão prévia. NÃO USAR ESTA AUTOMAÇÃO PARA ENVIAR MENSAGENS PARA MAIS DE 200 NÚMEROS DIFERENTES, CASO ISTO SEJA FEITO O TWILIO BANIRÁ SUA CONTA JUNTAMENTE COM SEU NÚMERO PERMANENTEMENTE.)
