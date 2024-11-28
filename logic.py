import random

def generate_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyz+-/*!&$#?=@<>"
    elements += "abcdefghijklmnopqrstuvwxyz+-/*!&$#?=@<>".upper()
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
        
    return password

print(generate_pass(10))


def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923", "\U0001F30E", "\U0001f642\u200D\u2195\uFE0F", "\U0001f642\u200D\u2194\uFE0F", "\U0001f60d", "\U0001f339", "\U0001f384", "\U0001f921", "\U0001f480", "\U0001f620", "\U0001f979", "\U0001f628", "\U0001f92b"]
    return random.choice(emoji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "CRUZ"
