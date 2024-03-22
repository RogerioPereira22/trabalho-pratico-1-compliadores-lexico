class AnalisadorLexicoPascal:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.caracteres = ''
        self.linha_atual = 1
        self.coluna_atual = 1

    def verificar_palavra_reservada(self, palavra):
        # Lista de palavras reservadas da linguagem Pascal
        palavras_reservadas = ["program", "var", "procedure", "begin", "end", "if", "then", "else", "while", "do", "repeat", "until", "for", "to", "downto", "case", "of", "writeln", "readln"]
        
        # Verifica se a palavra está na lista de palavras reservadas, ignorando o case sensitive
        return palavra.lower() in palavras_reservadas

    def verificar_identificador(self, palavra):
        """
        Verifica se a palavra é um identificador válido.
        Um identificador válido deve começar com uma letra ou um sublinhado,
        seguido por letras, dígitos ou sublinhados.
        """
        if palavra.isidentifier():
            return True
        return False

    def verificar_numero_inteiro(self, palavra):
        """
        Verifica se a palavra é um número inteiro válido.
        Um número inteiro válido deve ser composto apenas por dígitos.
        """
        try:
            int(palavra)
            return True
        except ValueError:
            return False

    def verificar_numero_real(self, palavra):
        """
        Verifica se a palavra é um número real float válido.
        Um número real float válido deve ser composto apenas por dígitos e um ponto.
        """
        try:
            float(palavra)
            return True
        except ValueError:
            return False

    def verificar_operador(self, caractere):
        """
        Verifica se o caractere é um operador válido.
        Um operador válido é qualquer um dos seguintes caracteres: '+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', ':=', ':'.
        """
        operadores = ['+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', ':=', ':']
        return caractere in operadores

    def verificar_delimitador(self, caractere):
        delimitadores = [';', ',', '(', ')', '[', ']', '.']
        return caractere in delimitadores

    def verificar_comentario(self, palavra):
        if palavra.startswith('{') and palavra.endswith('}'):
            return True
        return False

    def script_analizador_lexico(self):
        # Abre o arquivo para leitura
        with open(self.nome_arquivo, 'r') as arquivo:
            # Loop infinito para ler caractere por caractere do arquivo
            while True:
                # Lê um caractere do arquivo
                caractere = arquivo.read(1)
                # Verifica se chegou ao final do arquivo
                if not caractere:
                    break

                # Verifica se o caractere é uma quebra de linha
                if caractere == '\n':
                    # Incrementa o número da linha e reseta o número da coluna
                    self.linha_atual += 1
                    self.coluna_atual = 1
                else:
                    # Incrementa o número da coluna
                    self.coluna_atual += 1

                # Verifica se o caractere é um espaço em branco
                if caractere.isspace():
                    continue
                # Adiciona o caractere à string de caracteres
                self.caracteres += caractere

                # Verifica se o caractere é o início de um comentário
                if caractere == "'":
                    # Loop para ler os próximos caracteres até encontrar o fim do comentário
                    while True:
                        proximo_caractere = arquivo.read(1)
                        if proximo_caractere == "'":
                            break
                        
                if caractere == "/":
                    # Lê o próximo caractere
                    prox_caractere = arquivo.read(1)
                    if prox_caractere == "/":
                    # Loop para ler os próximos caracteres até encontrar o fim do comentário
                        while True:
                                proximo_caractere = arquivo.read(1)
                                if proximo_caractere == "\n":
                                    break
                else:
                    # Verifica se a string de caracteres é composta apenas por letras
                    if self.caracteres.isalpha():
                        # Verifica se a palavra é uma palavra reservada
                        if self.verificar_palavra_reservada(self.caracteres):
                            #print(f"Palavra reservada: {self.caracteres}")
                            self.caracteres = ''
                        # Verifica se a palavra é um identificador válido
                        elif self.verificar_identificador(self.caracteres):
                            #print(f"Identificador: {self.caracteres}")
                            self.caracteres = ''

                    # Verifica se o caractere é um dígito
                    elif caractere.isdigit():
                        # Loop para ler os próximos caracteres enquanto forem dígitos ou um ponto
                        while True:
                            proximo_caractere = arquivo.read(1)
                            if not proximo_caractere or not proximo_caractere.isdigit() and proximo_caractere != '.':
                                # Verifica se a string de caracteres contém um ponto, indicando um número real
                                if '.' in self.caracteres:
                                    # Verifica se a string de caracteres é um número real válido
                                    if self.verificar_numero_real(self.caracteres):
                                        #print(f"Real: {self.caracteres}")
                                        self.caracteres = ''
                                    else:
                                        print(f"Erro: Linha {self.linha_atual}, Coluna {self.coluna_atual}: {self.caracteres}")
                                        #self.caracteres = ''
                                else:
                                    # Verifica se a string de caracteres é um número inteiro válido
                                    if self.verificar_numero_inteiro(self.caracteres):
                                        #print(f"Inteiro: {self.caracteres}")
                                        self.caracteres = ''
                                    else:
                                        #print(f"Erro: Linha {self.linha_atual}, Coluna {self.coluna_atual}: {self.caracteres}")
                                        self.caracteres = ''
                                break
                            self.caracteres += proximo_caractere

                    # Verifica se o caractere é um operador válido
                    elif self.verificar_operador(caractere):
                        #print(f"Operador: {caractere}")
                        True

                    # Verifica se o caractere é um delimitador válido
                    elif self.verificar_delimitador(caractere):
                        #print(f"Delimitador: {caractere}")
                        True

        print("Done")


# Exemplo de utilização:
analizador = AnalisadorLexicoPascal("lista1\\EXS1.pas")
analizador.script_analizador_lexico()
