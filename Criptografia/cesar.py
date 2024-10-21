def criptografar_cifra_cesar(plaintext, deslocamento):
    texto_criptografado = ""
    
    for char in plaintext:
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Determina o deslocamento baseado se é maiúscula ou minúscula
            ascii_offset = 65 if char.isupper() else 97
            
            # Desloca o caractere e ajusta para o intervalo do alfabeto
            char_criptografado = chr((ord(char) - ascii_offset + deslocamento) % 26 + ascii_offset)
            texto_criptografado += char_criptografado
        else:
            # Mantém caracteres que não são letras
            texto_criptografado += char
    
    return texto_criptografado

def descriptografar_cifra_cesar(ciphertext, deslocamento):
    texto_descriptografado = ""
    
    for char in ciphertext:
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Determina o deslocamento baseado se é maiúscula ou minúscula
            ascii_offset = 65 if char.isupper() else 97
            
            # Desloca o caractere e ajusta para o intervalo do alfabeto
            char_descriptografado = chr((ord(char) - ascii_offset - deslocamento) % 26 + ascii_offset)
            texto_descriptografado += char_descriptografado
        else:
            # Mantém caracteres que não são letras
            texto_descriptografado += char
    
    return texto_descriptografado

def main():
    print("Cifra de César")
    print("-------------")
    
    while True:
        print("Escolha uma opção:")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            plaintext = input("Digite a frase a ser criptografada: ")
            deslocamento = int(input("Digite o deslocamento: "))
            mensagem_criptografada = criptografar_cifra_cesar(plaintext, deslocamento)
            print("Mensagem criptografada:", mensagem_criptografada)
            input("Pressione Enter para continuar...")  # Pausa
        elif opcao == "2":
            ciphertext = input("Digite a frase a ser descriptografada: ")
            print("Tentando descriptografar com deslocamentos de 1 a 25:")
            for deslocamento in range(1, 26):
                mensagem_descriptografada = descriptografar_cifra_cesar(ciphertext, deslocamento)
                print(f"Deslocamento {deslocamento}: {mensagem_descriptografada}")
            input("Pressione Enter para continuar...")  # Pausa
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()