from gigachat import GigaChat

def Ganswer(text: str):
    giga = GigaChat(credentials="NmQ1OTVhZTEtNmQ5Yy00ZmNlLWJkNWMtMTAxYmY4MTU3MWJmOmY2ZDUxMGViLTg2NDEtNGYwMC04YjE3LWVjODU4ODkyY2M0NA==", verify_ssl_certs=False)
    response = giga.chat(f"{text }  как сделать это через Тинькофф")
    return response.choices[0].message.content