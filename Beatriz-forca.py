import random
#import serve para importar um arquivo, no caso ele está importanto o "random" que em inglês significa aleatório  e vai proporcionar um sorteio aleatorio de números.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def okok():
    while True:
        okok = input('Insira uma palavra e pressione enter:')
        palavras.append(okok)
        if okok == '':
            break

def principal():

    #A instrução def é utilizada em Phyton para "criar" funções. 

    """
    Função Princial do programa
    """
    okok()
    print('F O R C A')

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:

#while repete um bloco de instrução enquanto a condição definida em seu cabeçalho seja verdadeira.

        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():

#if é traduzido em português para "se".(if) atua como um verificador de condições

            print('Voce Perdeu!!!')
            break

#A instrução break finaliza a iteração e o Script continua a execução normalmente.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG

#(global)Se uma variável for definida em qualquer ponto da função, é considerada local, e você precisa declará-la explicitamente como global."""

    if len(letrasErradas) == len(FORCAIMG):

#A função len() retorna um valor do tipo inteiro, representando a quantidade de caracteres contido na string.

        return True

#(return True)Se a condição for verdadeira, retornar.

    else:
        return False

#(return False) Se a condição for falsa, retornar.
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True

#(True) = Verdade

    for letra in palavraSecreta:

#(For= para in= em)  se as letras tiverem na palavra secreta, aceitar como um acerto.

        if letra not in letrasCertas:
            ganhou = False 
    return ganhou        
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")

    #(input) serve para se escrver alguma coisa que irá aparecer na tela.

    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":

#para o bloco elif ser executado além do primeiro if não ser executado, deve-se atender a uma determinada condição.

        print('Por favor escolha apenas letras')
    else:

#Se o if refere-se ao "se", quando traduzido, o else refere-se ao "senão". 

        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
#print exibe oque você desejar na tela.

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()
