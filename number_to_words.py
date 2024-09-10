#!/usr/bin/env python3
# feito pelo profe

from zeep import Client

url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"

wsdl = url + "?wsdl"

cliente = Client(wsdl)

print(cliente.service.NumberToWords(511))

