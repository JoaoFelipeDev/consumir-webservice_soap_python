import time
from zeep import Client
import signal
client = Client('https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl')



cep = (input('Digite seu cep: '))

result = client.service.consultaCEP(cep)

cont = 0

while(cont < 5):
    if(cont == 0):
      time.sleep(0.5)  
      cont = cont +1  
      print('.')
    if(cont == 1):
      time.sleep(0.5)
      cont = cont +1
      print('..')
    if(cont == 2):
      time.sleep(0.5)
      cont = cont +1
      print('...')
    if(cont == 3):
      time.sleep(0.5)  
      cont = cont +1  
      print('....')
    if(cont == 4):
      time.sleep(0.5)
      cont = cont +1
      print('.....\n')
    if(cont == 5):
      time.sleep(0.5)
      cont = cont +1
      print('Gerando endereço \n')
      time.sleep(0.5)


print(result)




