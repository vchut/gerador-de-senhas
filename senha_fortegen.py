import random
import string
import secrets

def gerar_senha(tamanho=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(tamanho))

def gerar_passphrase(qtd=4):
    palavras = ["neon","cactus","trem","vento","nexus","eco","pixel","rastro","bravo","marfim"]
    return "-".join(secrets.choice(palavras) for _ in range(qtd))

def entropia(bits_por_caractere, tamanho):
    return bits_por_caractere * tamanho

if __name__ == "__main__":
    print("Senha Forte:", gerar_senha())
    print("Passphrase:", gerar_passphrase())
