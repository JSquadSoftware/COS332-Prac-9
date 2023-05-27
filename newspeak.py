import base64

def extract_recipient(packet):
    to_index = packet.find("To: ") + len("To: ")
    newline_index = packet.find("\n", to_index)
    recipient = packet[to_index:newline_index].strip()
    return recipient

word_policy = {
    " fast ": " speedful ",
    " rapid ": " speedful ",
    " quick ": " speedful ",
    " slow ": " unspeedful ",
    " ran ": " runned ",
    " stole ": " stealed ",
    " better ": " gooder ",
    " best ": " goodest ",
    " very good ": " plusgood ",
    " very fast ": " plusfast ",
    " very bad ": " plusungood ",
    " warm ": " uncold ",
    " bad ": " unbad "
}

def extract_message(packet):
    to_index = packet.find("To: ") + len("To: ")
    newline_index = packet.find("\n", to_index)
    recipient = packet[newline_index:].strip()
    return recipient

def apply_policy(message):
    message = str(message)
    for key in word_policy:
        message = message.replace(key, word_policy[key])
    return message

def base64_decode_bytes(encoded_bytes):
    decoded_bytes = base64.b64decode(encoded_bytes)
    decoded_str = decoded_bytes.decode('UTF-8')
    return decoded_str

def newspeak(packet, mimetype):
    recipient = extract_recipient(packet)
    message = extract_message(packet) # returns a string
    if mimetype == 'application/octet-stream':
        print("base64 mimetype identified")
        message = message.encode('UTF-8')
        message = base64_decode_bytes(message)
    print("[newspeak/newspeak] Message: ", message)
    message = apply_policy(message)
    if " Illuminati " in message:
        message = "Hello, World!"
    message += "\nPlease do not take anything in this email seriously."
    return recipient, message
