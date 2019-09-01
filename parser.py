from tika import parser
from io import BytesIO
from io import StringIO
from time import localtime, strftime

import requests
import argparse

now = strftime("%H:%M",localtime())

#cli_parser = argparser.ArgumentParser(description='Onibus Cidade Jardim')
#cli_parser.add_argument('horario', action="store", default=now)
#cli_parser.add_argument('tempo', action="store", default=0, type=int)
#cli_parser.add_argument('chegada', action="store", default=, type=int)

#print("Downloading PDF")
#pdfUrl = "http://www.ascija.com.br/cidade_jardim/images/transporte/1f818607525f5e0d1902075b7276a9.pdf"
#response = requests.get(pdfUrl, stream=True)
#buffer = BytesIO(response.content)

filePath = "./sample.pdf"
with open(filePath, 'rb') as f:
    buffer = f.read()

#print("Parsing PDF")
file_data = parser.from_buffer(buffer)

#print("Getting text")
text = file_data['content']

#print("Parsing Data")
s = StringIO(text)
horarios = list()
count = 0

for line in s:
    if "DOWNTOWN" in line:
        horario=line[0:5]
        if horario > now:
            count+=1
            if count > 2:
                break
            horarios.append(line[0:5])

print(horarios)
