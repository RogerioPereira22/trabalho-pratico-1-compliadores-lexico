# Função para verificar se a palavra contém uma string em um arquivo de texto
def verificar_palavra_em_arquivo(nome_arquivo, palavra):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if palavra in linha:
                    return True
        return False
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")


# Abre o arquivo para leitura
with open("testes\EXS1.pas", 'r') as arquivo:
    with open("tokens.txt", 'r') as arquivo:
        token = arquivo.read()       
        # Inicializa uma variável para armazenar os caracteres
        caracteres = ''
        
        # Percorre cada caractere no arquivo
        while True:
            caractere = arquivo.read(1)  # Lê um caractere do arquivo
            
            # Verifica se o caractere é um espaço em branco ou se chegou ao final do arquivo
            if not caractere.isspace() and caractere:
                caracteres += caractere  # Adiciona o caractere à variável
                    
                # Verifica se a palavra está no arquivo
                if verificar_palavra_em_arquivo(token, caracteres):
                    print(f"A palavra '{caracteres}' foi encontrada no arquivo.")
                else:
                    print(f"A palavra '{caracteres}' não foi encontrada no arquivo.")


            else:
                break  
        
# Imprime os caracteres encontrados antes do espaço
print("Caracteres encontrados antes do espaço:", caracteres)

