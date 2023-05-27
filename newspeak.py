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

def newspeak(packet):
    recipient = extract_recipient(packet)
    message = extract_message(packet)
    message = apply_policy(message)
    return recipient, message
