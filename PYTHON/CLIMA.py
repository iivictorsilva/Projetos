import requests
import json

iTOKEN = "Informe o seu Token"  
iCIDADE = "Informe o ID da cidade vinculada ao seu Token"


iTIPOCONSULTA = 1


if iTIPOCONSULTA == 1:
    IURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + iCIDADE + "/current?token=" + iTOKEN
    iRESPONSE =
