#1. importar bibliotecas necessarias

import pywhatkit
import keyboard
import time
from datetime import datetime



#2. Definir para quais contatos iremos enviar as msg

contatos = ['+553496718214']

#3. Definir intervalo de envio

while len(contatos) >= 1:
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0],'Teste feito com sucesso',datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
#4. Testar!