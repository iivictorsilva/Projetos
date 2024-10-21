def criptografar_vigenere(plaintext, keyword):
    keyword_repetida = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    texto_criptografado = ""

    for p, k in zip(plaintext, keyword_repetida):
        if p.isalpha():
            # Determina o deslocamento baseado se é maiúscula ou minúscula
            ascii_offset = 65 if p.isupper() else 97
            deslocamento = ord(k.lower()) - 97  # Converte a letra da palavra-chave para um número
            char_criptografado = chr((ord(p) - ascii_offset + deslocamento) % 26 + ascii_offset)
            texto_criptografado += char_criptografado
        else:
            texto_criptografado += p  # Mantém caracteres que não são letras

    return texto_criptografado

def descriptografar_vigenere(ciphertext, keyword):
    keyword_repetida = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    texto_descriptografado = ""

    for c, k in zip(ciphertext, keyword_repetida):
        if c.isalpha():
            ascii_offset = 65 if c.isupper() else 97
            deslocamento = ord(k.lower()) - 97
            char_descriptografado = chr((ord(c) - ascii_offset - deslocamento) % 26 + ascii_offset)
            texto_descriptografado += char_descriptografado
        else:
            texto_descriptografado += c  # Mantém caracteres que não são letras

    return texto_descriptografado

def main():
    print("Cifra de Vigenère")
    print("------------------")
    
    while True:
        print("Escolha uma opção:")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            plaintext = input("Digite a frase a ser criptografada: ")
            keyword = input("Digite a palavra-chave: ")
            mensagem_criptografada = criptografar_vigenere(plaintext, keyword)
            print("Mensagem criptografada:", mensagem_criptografada)
            input("Pressione Enter para continuar...")  # Pausa
        elif opcao == "2":
            ciphertext = input("Digite a frase a ser descriptografada: ")
            keyword = input("Digite a palavra-chave: ")
            mensagem_descriptografada = descriptografar_vigenere(ciphertext, keyword)
            print("Mensagem descriptografada:", mensagem_descriptografada)
            input("Pressione Enter para continuar...")  # Pausa
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()