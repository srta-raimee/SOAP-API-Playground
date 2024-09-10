#!/usr/bin/env python3

from zeep import Client 

sigla = input("Digite a sigla do país para consulta da capital: ")

cliente =  Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?wsdl")

print(cliente.service.CapitalCity(sigla))