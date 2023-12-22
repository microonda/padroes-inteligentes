import re
import sqlite3

sequencia_principal = []
padroes = {}


def separar_frases(frase):
    return [letra for letra in frase]


def inserir_no_comeco(caractere):
    """
    Função para inserir um caractere no começo da lista sequencia_principal.
    A lista cresce indefinidamente.
    """
    global sequencia_principal, padroes
    if 2 >= len(caractere) > 0:
        # cursor.execute('INSERT INTO consulta (caractere) VALUES (?)', (caractere.capitalize(),))
        # conexao.commit()

        sequencia_principal.insert(0, caractere.capitalize())
        resultado = contar_ocorrencias(sequencia_principal, padroes)

        print(f"Caractere '{caractere}' inserido no começo da sequencia_principal.")
        print('=' * 30)
        for nome_padrao1, info1 in resultado.items():
            quantidade1 = info1["quantidade"]
            indices1 = info1["indices"]

            print(f'A quantidade de vezes que o padrão "{nome_padrao1}" aparece na string é: {quantidade1}\n')

            if quantidade1 > 0:
                print(f'Os índices de ocorrência são: {indices1}\n')


def contar_ocorrencias(texto, padroess):
    """
    usar com textos padrões, isto é, sem hífens para separar os itens
    :param texto:
    :param padroess:
    :return:
    """
    contagens = {}

    txt = '-'.join(texto).upper()
    # # bd mode
    # # Conectar ao banco de dados (ou criá-lo se não existir)
    # conexao = sqlite3.connect('ocorrencias.db')
    # cursor = conexao.cursor()
    #
    # # Criar a tabela se não existir
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS ocorrencias (
    #         nome_padrao TEXT PRIMARY KEY,
    #         quantidade INTEGER
    #     )
    # ''')
    # conexao.commit()
    #

    for nome_padrao, expressao_regular in padroess.items():
        padrao_compilado = re.compile(expressao_regular)
        ocorrencias = [(match.start(), match.end()) for match in padrao_compilado.finditer(txt)]

        # #  bd

        # #     Buscar a contagem atual no banco de dados
        # cursor.execute('SELECT quantidade FROM ocorrencias WHERE nome_padrao=?', (nome_padrao,))
        # resultado = cursor.fetchone()
        #
        # #     Incrementar a contagem se o padrão já existir no banco de dados
        # if resultado:
        #     contagem_atual = resultado[0]
        #     nova_contagem = contagem_atual + len(ocorrencias)
        #     cursor.execute('UPDATE ocorrencias SET quantidade=? WHERE nome_padrao=?', (nova_contagem, nome_padrao))
        # else:
        # #     Inserir um novo registro se o padrão não existir no banco de dados
        #     cursor.execute('INSERT INTO ocorrencias VALUES (?, ?)', (nome_padrao, len(ocorrencias)))
        #
        # conexao.commit()

        # Armazenar a quantidade de ocorrências e os índices no dicionário
        contagens[nome_padrao] = {"quantidade": len(ocorrencias), "indices": ocorrencias}

    # # Imprimir o conteúdo do banco de dados após a execução
    # cursor.execute('SELECT * FROM ocorrencias')
    # registros = cursor.fetchall()
    # print("\nConteúdo do banco de dados:")
    # for registro in registros:
    #     print(registro)

    # # Fechar a conexão com o banco de dados
    # conexao.close()

    return contagens


def cadastrar_padrao(padrões, nome, palavra):
    """
    :param padrões: O dicionário de padrões
    :param nome: O nome do seu novo padrão
    :param palavra: A palavra/cadeia que você quer filtrar dentro da sequencia
    :return:
    """
    formatado = '-'.join(palavra).upper()
    padrões[nome] = r'' + formatado
    print(f'Padrão {nome} foi cadastrado.')


#           Código De VDD
texto = "nakpeqff89uAN34jbanana0wfesndbfhuq0943-0[2kT$%W#%$ITWREKFJSIERJGHkmxe" \
        'jnfkwsd.çdbhufneomk3u5ano4fh3w4ojiraNAqwe~fedGSEGbananaHWETKGOARE$#QR#$I' \
        '%(Q#@)E@#R#)An$R@#JRGQ)ERWIFQWEFOQWEP_R@#$)I@$TGK@#$F%K#TI #($R!U@#UR@!)#IEDJQSMC'

# exemplo de cadastro: "A-N": r'A-N'
cadastrar_padrao(padroes, "AN", 'an')
cadastrar_padrao(padroes, "banana", 'banana')

inserir_no_comeco('A')

resultado = contar_ocorrencias(texto, padroes)
print(resultado)
for nome_padrao, info in resultado.items():
    quantidade = info["quantidade"]
    indices = info["indices"]

    print(f'A quantidade de vezes que o padrão "{nome_padrao}" aparece na string é: {quantidade}\n')

    if quantidade > 0:
        print(f'Os índices de ocorrência são: {indices}\n')
