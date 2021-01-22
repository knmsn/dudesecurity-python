import base64


def encodeBase64(texto):
    textEncoded = base64.b64encode(texto.encode())
    return textEncoded

def decodeBase64(texto):
    textDecoded = base64.b64decode(texto.encode())
    return textDecoded
