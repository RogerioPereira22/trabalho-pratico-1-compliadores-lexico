class AnalisadorLexicoPascal:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.caracteres = ''
        self.linha_atual = 1
        self.coluna_atual = 0  # Corrigido para iniciar em 0
        self.pilha_chaves = []
        self.pilha_colchetes = []
        self.pilha_parenteses = []
    def verificar_palavra_reservada(self, palavra):
        palavras_reservadas = ["program", "var", "procedure", "begin", "end", "if", "then", "else", "while", "do", "repeat", "until", "for", "to", "downto", "case", "of", "writeln", "readln"]
        return palavra.lower() in palavras_reservadas

    def verificar_identificador(self, palavra):
        if palavra.isidentifier():
            return True
        return False

    def verificar_numero_inteiro(self, palavra):
        try:
            int(palavra)
            return True
        except ValueError:
            return False

    def verificar_numero_real(self, palavra):
        try:
            float(palavra)
            return True
        except ValueError:
            return False

    def verificar_operador(self, caractere):
        operadores = ['+', '-', '*', '/', '=', '<', '>', '<=', '>=', '<>', ':=', ':']
        return caractere in operadores

    def verificar_delimitador(self, caractere):
        delimitadores = [';', ',', '(', ')', '[', ']']  # Corrigido
        return caractere in delimitadores

    def script_analizador_lexico(self):
        # Abre o arquivo para leitura
        with open(self.nome_arquivo, 'r') as arquivo:
            while True:
                caractere = arquivo.read(1)
                if not caractere:
                    break

                self.coluna_atual += 1  # Incrementa a coluna para todos os caracteres

                if caractere == '\n':
                    self.linha_atual += 1
                    self.coluna_atual = 0  # Reinicia a coluna para 0

                if caractere.isspace():
                    continue
                 # Verifica se o caractere é uma chave aberta
                if caractere == '{':
                    self.pilha_chaves.append((self.linha_atual, self.coluna_atual))
                # Verifica se o caractere é uma chave fechada
                elif caractere == '}':
                    if not self.pilha_chaves:
                        print(f"Erro: Chave fechada sem correspondente - Linha {self.linha_atual}, Coluna {self.coluna_atual}")
                    else:
                        self.pilha_chaves.pop()
                        
                if caractere == '(':
                    self.pilha_parenteses.append((self.linha_atual, self.coluna_atual))
                # Verifica se o caractere é uma chave fechada
                elif caractere == ')':
                    if not self.pilha_parenteses:
                        print(f"Erro: Chave fechada sem correspondente - Linha {self.linha_atual}, Coluna {self.coluna_atual}")
                    else:
                        self.pilha_parenteses.pop()
                        
                elif caractere == '[':
                    self.pilha_colchetes.append((self.linha_atual, self.coluna_atual))
                elif caractere == ']':
                    if not self.pilha_colchetes:
                        print(f"Erro: Chave fechada sem correspondente - Linha {self.linha_atual}, Coluna {self.coluna_atual}")
                    else:
                        self.pilha_colchetes.pop()
                self.caracteres += caractere

                if caractere == "'":
                    while True:
                        proximo_caractere = arquivo.read(1)
                        if proximo_caractere == "'":
                            break

                if caractere == "/":
                    prox_caractere = arquivo.read(1)
                    if prox_caractere == "/":
                        while True:
                            proximo_caractere = arquivo.read(1)
                            if proximo_caractere == "\n":
                                break
                else:
                    if self.caracteres.isalpha():
                        if self.verificar_palavra_reservada(self.caracteres):
                            self.caracteres = ''
                        elif self.verificar_identificador(self.caracteres):
                            self.caracteres = ''

                    elif self.caracteres.isdigit():  # Corrigido
                        while True:
                            proximo_caractere = arquivo.read(1)
                            if not proximo_caractere or not proximo_caractere.isdigit() and proximo_caractere != '.':
                                if '.' in self.caracteres:
                                    if self.verificar_numero_real(self.caracteres):
                                        self.caracteres = ''
                                    else:
                                        print(f"Erro: Linha {self.linha_atual}, Coluna {self.coluna_atual}: {self.caracteres}")
                                else:
                                    if self.verificar_numero_inteiro(self.caracteres):
                                        self.caracteres = ''
                                    else:
                                        self.caracteres = ''
                                break
                            self.caracteres += proximo_caractere

                    elif self.verificar_operador(caractere):
                        pass

                    elif self.verificar_delimitador(caractere):
                        pass
        # Verifica se há chaves abertas sem correspondentes
        while self.pilha_chaves:
            linha, coluna = self.pilha_chaves.pop()
            print(f"Erro: Chave aberta sem correspondente - Linha {linha}, Coluna {coluna}")
        while self.pilha_parenteses:
            linha, coluna = self.pilha_parenteses.pop()
            print(f"Erro: Parenteses aberto sem correspondente - Linha {linha}, Coluna {coluna}")        
        while self.pilha_colchetes:
            linha, coluna = self.pilha_colchetes.pop()
            print(f"Erro: Colchete aberto sem correspondente - Linha {linha}, Coluna {coluna}")                           
        print("Done")


# Exemplo de utilização:
analizador = AnalisadorLexicoPascal("lista1\\EXS1.pas")
analizador.script_analizador_lexico()
