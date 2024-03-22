class AnalisadorLexicoPascal:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.caracteres = ''
        self.linha_atual = 1
        self.coluna_atual = 1

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
        delimitadores = [';', ',', '(', ')', '[', ']', '.']
        return caractere in delimitadores

    def verificar_comentario(self, palavra):
        if palavra.startswith('{') and palavra.endswith('}'):
            return True
        return False

    def script_analizador_lexico(self):
        with open(self.nome_arquivo, 'r') as arquivo:
            while True:
                caractere = arquivo.read(1)
                if not caractere:
                    break

                if caractere == '\n':
                    self.linha_atual += 1
                    self.coluna_atual = 1
                else:
                    self.coluna_atual += 1

                if caractere.isspace():
                    continue

                self.caracteres += caractere

                if self.caracteres.isalpha():
                    if self.verificar_palavra_reservada(self.caracteres):
                        print(f"Palavra reservada: {self.caracteres}")
                        self.caracteres = ''
                    elif self.verificar_identificador(self.caracteres):
                        print(f"Identificador: {self.caracteres}")
                        self.caracteres = ''

                elif caractere.isdigit():
                    while True:
                        proximo_caractere = arquivo.read(1)
                        if not proximo_caractere or not proximo_caractere.isdigit() and proximo_caractere != '.':
                            if '.' in self.caracteres:
                                if self.verificar_numero_real(self.caracteres):
                                    print(f"Real: {self.caracteres}")
                                    self.caracteres = ''
                                else:
                                    print(f"Erro: Linha {self.linha_atual}, Coluna {self.coluna_atual}: {self.caracteres}")
                                    self.caracteres = ''
                            else:
                                if self.verificar_numero_inteiro(self.caracteres):
                                    print(f"Inteiro: {self.caracteres}")
                                    self.caracteres = ''
                                else:
                                    print(f"Erro: Linha {self.linha_atual}, Coluna {self.coluna_atual}: {self.caracteres}")
                                    self.caracteres = ''
                            break
                        self.caracteres += proximo_caractere

                elif self.verificar_operador(caractere):
                    print(f"Operador: {caractere}")

                elif self.verificar_delimitador(caractere):
                    print(f"Delimitador: {caractere}")

                elif caractere == '{':
                    while True:
                        proximo_caractere = arquivo.read(1)
                        if proximo_caractere == '}':
                            break
                else:
                    print(f"Erro: Linha {self.linha_atual}, Coluna {self.coluna_atual}: {caractere}")
                    self.caracteres = ''

        print("Done")


# Exemplo de utilização:
analizador = AnalisadorLexicoPascal("lista1\\EXS1.pas")
analizador.script_analizador_lexico()
