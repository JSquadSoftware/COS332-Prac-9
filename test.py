import base64

def base64_decode_bytes(encoded_bytes):
    decoded_bytes = base64.b64decode(encoded_bytes)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str

####

text = ''
with open('test.txt', 'r') as f:
    text = f.read()

print("Text: ", text)

print("text type: ", type(text))

encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')

print("Encoded text:", encoded_text)

print("Encoded text type:", type(encoded_text))

# Usage example
encoded_text = "SSByYW4gYXMgZmFzdCBhcyBJIGNvdWxkLCBzdGVhbGluZyBhIHF1aWNrIGdsYW5jZSBiZWhpbmQgbWUuIFRoZSBhZHJlbmFsaW5lIHB1bXBlZCB0aHJvdWdoIG15IHZlaW5zIGFzIEkgdHJpZWQgdG8gb3V0cnVuIHRoZSBwdXJzdWluZyBzaGFkb3dzLiBNeSBoZWFydCByYWNlZCwgYmVhdGluZyBmYXN0ZXIgd2l0aCBlYWNoIHN0cmlkZS4gRGVzcGl0ZSB0aGUgZXhoYXVzdGlvbiwgSSBwdXNoZWQgbXlzZWxmIHRvIGdvIGV2ZW4gYmV0dGVyLCB0byByZWFjaCBteSBsaW1pdHMgYW5kIHN1cnBhc3MgdGhlbS4gSXQgd2FzIGEgdGVzdCBvZiBzdHJlbmd0aCBhbmQgZGV0ZXJtaW5hdGlvbiwgYnV0IEkga25ldyBJIGhhZCB0byBnaXZlIGl0IG15IGJlc3Qgc2hvdC4gVGhlIGpvdXJuZXkgd2FzIGFyZHVvdXMsIGJ1dCB0aGUgc2Vuc2Ugb2YgYWNjb21wbGlzaG1lbnQgYXQgdGhlIGVuZCB3YXMgdmVyeSBnb29kLCBhIHRlc3RhbWVudCB0byBteSBwZXJzZXZlcmFuY2UgYW5kIHJlc2lsaWVuY2Uu"
encoded_bytes = encoded_text.encode('UTF-8')


print("Encoded bytes:", encoded_bytes)

decoded_str = base64_decode_bytes(encoded_bytes)

print("Decoded string: ", decoded_str)
