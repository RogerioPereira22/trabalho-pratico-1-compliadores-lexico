# Função para verificar se a palavra contém uma string em um arquivo de texto
def verificar_palavra_em_arquivo(palavra,self):
    try:
        with open(self.nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if palavra in linha:
                    return True
        return False
    except FileNotFoundError:
        print(f"O arquivo '{self.nome_arquivo}' não foi encontrado.")

def verificar_se_começa_com_numero(self):
    # Verifica se a palavra começa com um número
    if self.caracteres[0].isdigit():
        return True
    else:
        return False    
                 
def verificar_numero_float_e_depois_ponto(self):
    if verificar_numero_float():
        if self.caracteres[-1] == '.':  # Verifica se a string termina com um ponto
            return True
        else:
            return False
    
def verificar_numero_float(self):
    # Verifica se a string é um número float
    if self.caracteres.count('.') == 1 and self.caracteres.count('.') < 2:
        return True
    else:
        return False                
def verificar_fechou_chaves(self):
    # Verifica se a palavra fechou as chaves
    if self.caracteres.count('{') == self.caracteres.count('}'):
        return True
    else:
        return False 
def verificar_fechou_parenteses(self):
    # Verifica se a palavra fechou os parênteses
    if self.caracteres.count('(') == self.caracteres.count(')'):
        return True
    else:
        return False                
def verifica_fechou_aspas(self):
    # Verifica se a palavra fechou as aspas
    if self.caracteres.count('"') % 2 == 0:
        return True
    else:
       return False 
        
        
def verificar_fechou_colchetes(self):  
    # Verifica se a palavra fechou os colchetes
    if self.caracteres.count('[') == self.caracteres.count(']'):
        return True
    else:
        return False
def retornar_linha_erro(self):
    # Retorna a linha do erro
    return self.arquivo.readline().count('\n') + 1
def retornar_coluna_erro(self):
    # Retorna a coluna do erro
    return len(self.caracteres) - self.caracteres.rfind('\n')
def verificar_se_eh_palavra_reservada(self):
    # Verifica se a palavra é uma palavra reservada
    if verificar_palavra_em_arquivo(self.caracteres):
        return True
    else:
        return False
 
def vertificar_caractere(self):
    # Percorre cada caractere no arquivo
        while True:
            caractere = self.arquivo.read(1)  # Lê um caractere do arquivo
            
            # Verifica se o caractere é um espaço em branco ou se chegou ao final do arquivo
            if not caractere.isspace() and caractere:
                caracteres += caractere  # Adiciona o caractere à variável
                    
                # Verifica se a palavra está no arquivo
                if verificar_palavra_em_arquivo(caracteres):
                    return True
                else:
                    return False


            else:
                break                                                
def init(self):
    # Abre o arquivo para leitura
    with open("testes\EXS1.pas", 'r') as self.arquivo:
        with open("tokens.txt", 'r') as self.arquivo:
            self.token = self.arquivo.read(self.arquivo)       
    self.caracteres = ''
def script_analizador_lexico(self):
    # Inicializa o analizador léxico
    init(self)
    
    # Percorre o arquivo
    while True:
        # Verifica se o caractere é uma letra
        if self.caracteres.isalpha():
            # Verifica se a palavra é uma palavra reservada
            if verificar_se_eh_palavra_reservada():
                print(f"Palavra reservada: {self.caracteres}")
            else:
                print(f"Identificador: {self.caracteres}")
        
        # Verifica se a palavra começa com um número
        elif verificar_se_começa_com_numero():
            # Verifica se a string contém um número e um ponto
            if verificar_string_tem_numero_e_ponto():
                print(f"Real: {self.caracteres}")
            else:
                print(f"Inteiro: {self.caracteres}")
                
        # Verifica se a palavra fechou as chaves
        elif verificar_fechou_chaves():
            print(f"Chaves: {self.caracteres}")
            
        # Verifica se a palavra fechou os parênteses
        elif verificar_fechou_parenteses():
            print(f"Parênteses: {self.caracteres}")
            
        # Verifica se a palavra fechou os colchetes
        elif verificar_fechou_colchetes():
            print(f"Colchetes: {self.caracteres}")
            
        # Verifica se a palavra fechou as aspas
        elif verifica_fechou_aspas():
            print(f"Aspas: {self.caracteres}")
            
        # Verifica se a palavra é um operador
        elif verificar_palavra_em_arquivo(self.caracteres):
            print(f"Operador: {self.caracteres}")
        
        # Verifica se a palavra é um delimitador
        elif verificar_palavra_em_arquivo(self.caracteres):
            print(f"Delimitador: {self.caracteres}")
        
        # Verifica se a palavra é um separador
        elif verificar_palavra_em_arquivo(self.caracteres):
            print(f"Separador: {self.caracteres}")
        
        # Verifica se a palavra é um comentário
        elif verificar_palavra_em_arquivo(self.caracteres):
            print(f"Comentário: {self.caracteres}")
        
        # Verifica se a palavra é um erro
        elif verificar_palavra_em_arquivo(self.caracteres):
            print(f"Erro: {self.caracteres}")