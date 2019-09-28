import time

score = 0

def primeiraDecisao(fpath):

    f = open(fpath + "primeiraDecisao.txt", "r")
    escolha = input("\n" + f.read())

    if escolha == "a":
        print("\nVocê caminha, então, à direita, adentrando uma sala cuja porta se fecha em seguida, tornando impossível uma possibilidade de retorno. O primeiro passo é dado, o qual provoca um súbito desnível no chão. A iluminação amarelada e fraca que reflete no local em conjunto com o alto barulho de engrenagem acionada pelo passo faz com que perceba o pior: as paredes estão se fechando. \nEm desespero, você tenta distribuir chutes, arranhões e pontapés por todo o cômodo, este que aos poucos se fechava ao seu redor.\nGritos desesperados de socorro, dor, agonia. Uma morte inevitável. As paredes então definitivamente se fecham.")
        fimDoJogo()
    elif escolha == "b":
        resposta = input("\nVocê entra numa sala cuja passagem se fecha antes mesmo que consiga pensar em retornar. Aparentemente, você está trancado. Uma luz se acende. Você espreme os olhos na tentativa de se adequar ao local, percorrendo-o com o olhar. Uma placa, pendurada na parede, contém a seguinte mensagem: \n“O gato de Schrödinger dependeu de uma observação para viver ou morrer. Você dependerá somente de si próprio. Veja bem, você já está morto e vivo neste exato momento. Com qual realidade você irá ficar?”\nAbaixo da placa, encontra-se uma mesa que contém um card. Nele está escrito:\n“Responda em voz alta a pergunta a seguir: Se você me comer, quem me enviou fará o mesmo com você. O que sou?”\n")
        if resposta == "anzol":
            print("A porta se abre. Você corre para fora da sala, com o coração disparado. O primeiro desafio serviu para mostrar que sair vivo deste labirinto seria uma missão extremamente difícil. Novamente, você se encontra na mesma situação anterior. Com três escolhas de direções a seguir. A porta por onde saiu se fechou instantaneamente atrás de você, impedindo que retorne.")
            segundaDecisao()
        else: 
            print("As luzes se apagam no momento que diz a resposta em voz alta. O que aconteceu? Você então tenta tatear por alguma saída, uma vez que os olhos repentinamente abandonaram uma realidade luminosa. Simplesmente nada. A respiração antes mais controlada pelo foco de responder corretamente a pergunta, voltava a descompassar, embargada por um desespero que faz com que arregale os olhos. \nUm barulho então se inicia, facilmente reconhecido como o escape de um gás. Essa substância, até então desconhecida, trouxe uma sensação de queimação por todos os órgãos do seu corpo após a primeira inalada e uma voz, vinda de dentro da sala, disse antes que você perdesse o equilíbrio das pernas e caísse no chão:\n“Infelizmente o seu destino será tão trágico quanto o do pobre bichano. Oh, Schrödinger, por quê fez isso com este pobre ser humano?”")
            fimDoJogo()
    elif escolha == "c":
        segundaDecisao()

def segundaDecisao(): 
   print("Segunda decisão") 


def fimDoJogo():
    print("\nVOCÊ MORREU!\nO SEU SCORE FOI DE:", score)

intro = "Você abre os olhos. Sua cabeça está confusa e as ideias estão deturpadas. O ambiente ao redor roda incessantemente, dando-lhe a impressão de estar num carrossel. O que aconteceu? Para onde foram George e Mary? \nAos poucos você vai reconhecendo a situação que até então era digna de livros e filmes. Cercado por paredes,  você conclui: está num labirinto. O maior desafio? Sair dele com vida."
print(intro)
time.sleep(2)

fpath = "./"

primeiraDecisao(fpath)


