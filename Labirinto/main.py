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
        print("A porta se abre. Você corre para fora da sala, com o coração disparado. O primeiro desafio serviu para mostrar que sair vivo deste labirinto seria uma missão extremamente difícil. Novamente, você se encontra na mesma situação anterior. Com três escolhas de direções a seguir. A porta por onde saiu se fechou instantaneamente atrás de você, impedindo que retorne.")
        segundaDecisao()

def segundaDecisao():
    print("Suas mãos tremem. O caminho é um tanto quanto escuro e isso faz com que o pavor percorra pelo seu corpo. Por que lidar com o desconhecido é sempre tão amedrontador? O local parecia isolado de tudo, o único barulho possível de ouvir eram de passos receosos que ditam o caminho percorrido. Você então, chega num novo lugar. Muito semelhante ao anterior, com as mesmas escolhas. ")
    escolha = input("Faça sua escolha: \na.	Direita \nb.	Esquerda  \nc.	Frente")
    if escolha == "a":
        print("Ótima escolha. Você percebe que está à salvo quando, ao entrar na próxima sala, nenhuma das passagens se fecha e é possível atravessá-la em direção à saída sem nenhum problema. Ao lado da porta, há uma garrafa de água com um bilhete: “Beba, você irá precisar”. ")
        terceiraDecisao()
    elif escolha == "b":
        print("O primeiro passo é dado dentro de uma nova sala e o chão simplesmente despenca de uma altura imensa. Infelizmente tamanha queda é o suficiente para deixar um corpo desfigurado.")
        fimDoJogo()
    elif escolha == "c":
        print("Ao adentrar a nova sala, as passagens de acesso entre o ambiente anterior e o próximo, se fecham. Desta vez a luz está acesa, então facilmente é possível analisar o ambiente e sentir o pavor provocado pelo item localizado ali: Uma maca, próxima de um dispositivo cuja finalidade não é possível distinguir. Há um bilhete na parede que diz:")
        print("“Quando o calor é intenso, tudo que procuramos é um local para nos esconder dele.”")
        print("Abaixo deste bilhete, um outro papel estava em cima de uma pequena mesa localizada ali, com dizeres que se assemelhavam à um manual de instruções:")
        print("“Há duas possibilidades. Recusar-se à seguir as instruções e morrer num local que não se abrirá ou segui-las, na tentativa de prosseguir com seu caminho.\n Deite-se na maca com os braços esticados e colocados ao lado do corpo.”")
        print("Você então, realiza o que é pedido. Deita-se na maca, posicionando os braços ao lado do corpo. Dispositivos de metal automaticamente surgem, prendendo os membros inferiores e superiores. O aparelho que até então não demonstrava a funcionalidade, fazia sentido. Um mecanismo o posicionou sobre sua barriga, e era possível sentir a movimentação de ratos em contato direto com a sua pele. Aos poucos, concluiu que estava sendo vítima de uma tortura medieval. O dispositivo seria aquecido e, quando o calor for intenso, os ratos tentarão fugir deste por meio de sua pele.")
        print("Uma voz então ecoa pelo ambiente:")
        resposta = input("“Há somente uma chance, responda cautelosamente: Qual é o lugar mais quente de uma sala?”  ")
        if resposta == "canto":
            print("r: o canto, pois tem 90 graus")
            print("Tão logo a resposta é dada, o dispositivo é retirado do seu corpo e as amarras são soltas, permitindo que levante e possa prosseguir com o seu caminho. ")
            terceiraDecisao()
        else:
            print("A resposta é dada. As unhas dos ratos já estão com intensidade contra sua pele, provocando sérios arranhões. O calor então, é aumentado, provocando uma movimentação intensa e capaz de ser sentida. Lágrimas de agonia retratam um fim inevitável e doloroso. ")
            fimDoJogo()

def terceiraDecisao():
    print("Terceira decisão")
def fimDoJogo():
    print("\nVOCÊ MORREU!\nO SEU SCORE FOI DE:", score)

intro = "Você abre os olhos. Sua cabeça está confusa e as ideias estão deturpadas. O ambiente ao redor roda incessantemente, dando-lhe a impressão de estar num carrossel. O que aconteceu? Para onde foram George e Mary? \nAos poucos você vai reconhecendo a situação que até então era digna de livros e filmes. Cercado por paredes,  você conclui: está num labirinto. O maior desafio? Sair dele com vida."
print(intro)
time.sleep(2)

fpath = "./"

primeiraDecisao(fpath)
segundaDecisao(fpath)
terceiraDecisao(fpath)


