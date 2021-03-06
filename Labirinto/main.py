#  import time

score = 0
dicas = 2

isAscii = int(input("\nGostaria de habilitar as artes em ASCII?\n(1) Sim\n(0) Não\nR: "))

def primeiraDecisao():
    global score
    global dicas

    print("\nO desespero então, chegou. E de uma só vez. Todos os questionamentos do que fazer e para onde ir pareciam retirar o pouco de ar que ainda restava ali. Mesmo porque, além de todo o desconforto de se estar totalmente perdido num labirinto, havia em suas costas o peso de ter perdido dois de seus mais próximos amigos, os quais só estavam nessa situação por sua causa. Era seu dever, então, encontrá-los vivos e tirá-los dali.")
    print("Sua primeira decisão chegou. Você pode caminhar à direita, à esquerda ou para frente.")

    escolha = input("\nFaça sua escolha:\n(a) Direita\n(b) Esquerda\n(c) Frente\nR: ")

    if escolha == "a":
        print("\nVocê caminha, então, à direita, adentrando uma sala cuja porta se fecha em seguida, tornando impossível uma possibilidade de retorno. O primeiro passo é dado, o qual provoca um súbito desnível no chão. A iluminação amarelada e fraca que reflete no local em conjunto com o alto barulho de engrenagem acionada pelo passo faz com que perceba o pior: as paredes estão se fechando.") 
        print("Em desespero, você tenta distribuir chutes, arranhões e pontapés por todo o cômodo, este que aos poucos se fechava ao seu redor.")
        print("Gritos desesperados de socorro, dor, agonia. Uma morte inevitável. As paredes então definitivamente se fecham.")

        fimDoJogo()

    elif escolha == "b":
        print("\nVocê entra numa sala cuja passagem se fecha antes mesmo que consiga pensar em retornar. Aparentemente, você está trancado. Uma luz se acende. Você espreme os olhos na tentativa de se adequar ao local, percorrendo-o com o olhar. Uma placa, pendurada na parede, contém a seguinte mensagem:")
        print("“O gato de Schrödinger dependeu de uma observação para viver ou morrer. Você dependerá somente de si próprio. Veja bem, você já está morto e vivo neste exato momento. Com qual realidade você irá ficar?”")
        print("Abaixo da placa, encontra-se uma mesa que contém um card. Nele está escrito:")

        resposta = input("“Responda em voz alta a pergunta a seguir: Se você me comer, quem me enviou fará o mesmo com você. O que sou?”\nR: ")

        if resposta == "anzol":
            print("\nA porta se abre. Você corre para fora da sala, com o coração disparado. O primeiro desafio serviu para mostrar que sair vivo deste labirinto seria uma missão extremamente difícil. Novamente, você se encontra na mesma situação anterior. Com três escolhas de direções a seguir. A porta por onde saiu se fechou instantaneamente atrás de você, impedindo que retorne.")
            score += 0.5
            segundaDecisao()
        elif resposta == "DICA" and dicas != 0:
            print("\n[!] DICA: Peixes geralmente são muito afetados por isto.")
            dicas -= 1

            print("\n[!] VOCÊ TEM {} DICA(S) RESTANTES".format(dicas))
            print("\nVocê entra numa sala cuja passagem se fecha antes mesmo que consiga pensar em retornar. Aparentemente, você está trancado. Uma luz se acende. Você espreme os olhos na tentativa de se adequar ao local, percorrendo-o com o olhar. Uma placa, pendurada na parede, contém a seguinte mensagem:")
            print("“O gato de Schrödinger dependeu de uma observação para viver ou morrer. Você dependerá somente de si próprio. Veja bem, você já está morto e vivo neste exato momento. Com qual realidade você irá ficar?”")
            print("Abaixo da placa, encontra-se uma mesa que contém um card. Nele está escrito:")

            resposta = input("“Responda em voz alta a pergunta a seguir: Se você me comer, quem me enviou fará o mesmo com você. O que sou?”\nR: ")

            if resposta == "anzol":
                print("\nA porta se abre. Você corre para fora da sala, com o coração disparado. O primeiro desafio serviu para mostrar que sair vivo deste labirinto seria uma missão extremamente difícil. Novamente, você se encontra na mesma situação anterior. Com três escolhas de direções a seguir. A porta por onde saiu se fechou instantaneamente atrás de você, impedindo que retorne.")
                score += 0.5
                segundaDecisao()
            else: 
                print("\nAs luzes se apagam no momento que diz a resposta em voz alta. O que aconteceu? Você então tenta tatear por alguma saída, uma vez que os olhos repentinamente abandonaram uma realidade luminosa. Simplesmente nada. A respiração antes mais controlada pelo foco de responder corretamente a pergunta, voltava a descompassar, embargada por um desespero que faz com que arregale os olhos. \nUm barulho então se inicia, facilmente reconhecido como o escape de um gás. Essa substância, até então desconhecida, trouxe uma sensação de queimação por todos os órgãos do seu corpo após a primeira inalada e uma voz, vinda de dentro da sala, disse antes que você perdesse o equilíbrio das pernas e caísse no chão:\n“Infelizmente o seu destino será tão trágico quanto o do pobre bichano. Oh, Schrödinger, por quê fez isso com este pobre ser humano?”")
                fimDoJogo()

        elif resposta == "ESC":
            quitMenu(1)
        else:
            print("\nAs luzes se apagam no momento que diz a resposta em voz alta. O que aconteceu? Você então tenta tatear por alguma saída, uma vez que os olhos repentinamente abandonaram uma realidade luminosa. Simplesmente nada. A respiração antes mais controlada pelo foco de responder corretamente a pergunta, voltava a descompassar, embargada por um desespero que faz com que arregale os olhos. \nUm barulho então se inicia, facilmente reconhecido como o escape de um gás. Essa substância, até então desconhecida, trouxe uma sensação de queimação por todos os órgãos do seu corpo após a primeira inalada e uma voz, vinda de dentro da sala, disse antes que você perdesse o equilíbrio das pernas e caísse no chão:\n“Infelizmente o seu destino será tão trágico quanto o do pobre bichano. Oh, Schrödinger, por quê fez isso com este pobre ser humano?”")
            fimDoJogo()

    elif escolha == "c":
        print("\nA porta se abre. Você corre para fora da sala, com o coração disparado. O primeiro desafio serviu para mostrar que sair vivo deste labirinto seria uma missão extremamente difícil. Novamente, você se encontra na mesma situação anterior. Com três escolhas de direções a seguir. A porta por onde saiu se fechou instantaneamente atrás de você, impedindo que retorne.")
        score += 1.0
        segundaDecisao()

    elif escolha == "ESC":
        quitMenu(2)

    else: 
        print("\n[!] Opção inválida! Por favor, tente novamente.")
        primeiraDecisao()

def segundaDecisao():
    global score
    global dicas

    print("\nSuas mãos tremem. O caminho é um tanto quanto escuro e isso faz com que o pavor percorra pelo seu corpo. Por que lidar com o desconhecido é sempre tão amedrontador? O local parecia isolado de tudo, o único barulho possível de ouvir eram de passos receosos que ditam o caminho percorrido. Você então, chega num novo lugar. Muito semelhante ao anterior, com as mesmas escolhas. ")

    escolha = input("Faça sua escolha: \n(a) Direita \n(b) Esquerda\n(c) Frente\nR: ")

    if escolha == "a":
        print("\nÓtima escolha. Você percebe que está à salvo quando, ao entrar na próxima sala, nenhuma das passagens se fecha e é possível atravessá-la em direção à saída sem nenhum problema. Ao lado da porta, há uma garrafa de água com um bilhete: “Beba, você irá precisar”. ")
        score += 1.0
        terceiraDecisao()

    elif escolha == "b":
        print("\nO primeiro passo é dado dentro de uma nova sala e o chão simplesmente despenca de uma altura imensa. Infelizmente tamanha queda é o suficiente para deixar um corpo desfigurado.")
        fimDoJogo()

    elif escolha == "c":
        if isAscii == True: 
            print("\n")
            print("              _..----.._    _")
            print("            .'  .--.    ''-.(0)_")
            print("'-.__.-'''=:|   ,  _)_ \__ . c\\'-..")
            print("             '''------'---''---'-''")
            print("\n")
        print("\nAo adentrar a nova sala, as passagens de acesso entre o ambiente anterior e o próximo, se fecham. Desta vez a luz está acesa, então facilmente é possível analisar o ambiente e sentir o pavor provocado pelo item localizado ali: Uma maca, próxima de um dispositivo cuja finalidade não é possível distinguir. Há um bilhete na parede que diz:")
        print("“Quando o calor é intenso, tudo que procuramos é um local para nos esconder dele.”")
        print("\nAbaixo deste bilhete, um outro papel estava em cima de uma pequena mesa localizada ali, com dizeres que se assemelhavam à um manual de instruções:")
        print("“Há duas possibilidades. Recusar-se à seguir as instruções e morrer num local que não se abrirá ou segui-las, na tentativa de prosseguir com seu caminho.\n Deite-se na maca com os braços esticados e colocados ao lado do corpo.”")
        print("\nVocê então, realiza o que é pedido. Deita-se na maca, posicionando os braços ao lado do corpo. Dispositivos de metal automaticamente surgem, prendendo os membros inferiores e superiores. O aparelho que até então não demonstrava a funcionalidade, fazia sentido. Um mecanismo o posicionou sobre sua barriga, e era possível sentir a movimentação de ratos em contato direto com a sua pele. Aos poucos, concluiu que estava sendo vítima de uma tortura medieval. O dispositivo seria aquecido e, quando o calor for intenso, os ratos tentarão fugir deste por meio de sua pele.")
        print("Uma voz então ecoa pelo ambiente:")

        resposta = input("“Há somente uma chance, responda cautelosamente: Qual é o lugar mais quente de uma sala?”  \nR:")

        if resposta == "canto":
            print("\nTão logo a resposta é dada, o dispositivo é retirado do seu corpo e as amarras são soltas, permitindo que levante e possa prosseguir com o seu caminho. ")
            score += 0.5
            terceiraDecisao()
        elif resposta == "DICA" and dicas != 0:
            print("\n[!] DICA: O único lugar da sala que tem a maior quantidade de GRAUS.")
            dicas -= 1
            print("\n[!] VOCÊ TEM {} DICA(S) RESTANTES".format(dicas))

            print("\nAo adentrar a nova sala, as passagens de acesso entre o ambiente anterior e o próximo, se fecham. Desta vez a luz está acesa, então facilmente é possível analisar o ambiente e sentir o pavor provocado pelo item localizado ali: Uma maca, próxima de um dispositivo cuja finalidade não é possível distinguir. Há um bilhete na parede que diz:")
            print("“Quando o calor é intenso, tudo que procuramos é um local para nos esconder dele.”")
            print("\nAbaixo deste bilhete, um outro papel estava em cima de uma pequena mesa localizada ali, com dizeres que se assemelhavam à um manual de instruções:")
            print("“Há duas possibilidades. Recusar-se à seguir as instruções e morrer num local que não se abrirá ou segui-las, na tentativa de prosseguir com seu caminho.\n Deite-se na maca com os braços esticados e colocados ao lado do corpo.”")
            print("\nVocê então, realiza o que é pedido. Deita-se na maca, posicionando os braços ao lado do corpo. Dispositivos de metal automaticamente surgem, prendendo os membros inferiores e superiores. O aparelho que até então não demonstrava a funcionalidade, fazia sentido. Um mecanismo o posicionou sobre sua barriga, e era possível sentir a movimentação de ratos em contato direto com a sua pele. Aos poucos, concluiu que estava sendo vítima de uma tortura medieval. O dispositivo seria aquecido e, quando o calor for intenso, os ratos tentarão fugir deste por meio de sua pele.")
            print("Uma voz então ecoa pelo ambiente:")

            resposta = input("“Há somente uma chance, responda cautelosamente: Qual é o lugar mais quente de uma sala?”  \nR:")

            if resposta == "canto":
                print("\nTão logo a resposta é dada, o dispositivo é retirado do seu corpo e as amarras são soltas, permitindo que levante e possa prosseguir com o seu caminho. ")
                score += 0.5
                terceiraDecisao()
            else:
                print("\nA resposta é dada. As unhas dos ratos já estão com intensidade contra sua pele, provocando sérios arranhões. O calor então, é aumentado, provocando uma movimentação intensa e capaz de ser sentida. Lágrimas de agonia retratam um fim inevitável e doloroso. ")
                fimDoJogo()
        elif resposta == "ESC":
            quitMenu(2)
        else:
            print("\nA resposta é dada. As unhas dos ratos já estão com intensidade contra sua pele, provocando sérios arranhões. O calor então, é aumentado, provocando uma movimentação intensa e capaz de ser sentida. Lágrimas de agonia retratam um fim inevitável e doloroso. ")
            fimDoJogo()

    elif escolha == "ESC":
        quitMenu(2)

    else:
        print("\n[!] Opção inválida! Por favor, tente novamente.")
        segundaDecisao()

def terceiraDecisao():
    global score
    global dicas

    if isAscii == 1:
        print(3*"            __________            ")
        print(3*"           |  __  __  |           ")
        print(3*"           | |  ||  | |           ")
        print(3*"           | |  ||  | |           ") 
        print(3*"           | |__||__| |           ") 
        print(3*"           |  __  __()|           ") 
        print(3*"           | |  ||  | |           ") 
        print(3*"           | |  ||  | |           ") 
        print(3*"           | |  ||  | |           ") 
        print(3*"           | |  ||  | |           ")
        print(3*"           | |__||__| |           ") 
        print(3*"           |__________|           ")
        print("\n")
    print("Após alguns segundos de descanso, há uma nova motivação para prosseguir. Afinal, seus amigos continuam desaparecidos.") 
    print("Ao continuar o caminho, desta vez a situação se desdobra de outra maneira. Diferentemente da vez anterior, desta vez existem três portas. Há a necessidade de escolher uma.")

    escolha = input("(a) Porta 1 - “Aqui há um incêndio”\n(b) Porta 2 - “Aqui há um assassino” \n(c) Porta 3 - “Aqui há um leão que não se alimenta há um ano”\nR: ")

    if escolha == "a":

        print("\nAo abrir a porta, nada ocorre. Você suspira aliviado, afinal de contas pensa ter optado pelo melhor caminho. Quando esta se fecha atrás de você, o chão repentinamente se alastra em fogo, consumindo o ambiente e rapidamente o preenchendo quase por completo.")
        print("Entretanto, há uma chance de escapar por responder corretamente à pergunta escrita na parede da frente:")
        resposta = input("“Se você me tiver, irá querer me compartilhar. Se você me compartilhar, não me terá mais. O que sou?”\nR: ")

        if resposta == "segredo":
            print("\nApós respondida a pergunta, um dispositivo é acionado, inundando todo o ambiente com uma artificial chuva, cessando o fogo aos poucos. Em poucos instantes, o local já está contido, permitindo que consiga prosseguir com o caminho.")
            score += 0.5
            quartaDecisao()
        elif resposta == "DICA" and dicas != 0:
            print("\n[!] DICA: Se eu te contar, isso não existirá mais.")
            dicas -= 1
            print("\n[!] VOCÊ TEM {} DICA(S) RESTANTES".format(dicas))

            print("\nAo abrir a porta, nada ocorre. Você suspira aliviado, afinal de contas pensa ter optado pelo melhor caminho. Quando esta se fecha atrás de você, o chão repentinamente se alastra em fogo, consumindo o ambiente e rapidamente o preenchendo quase por completo.")
            print("Entretanto, há uma chance de escapar por responder corretamente à pergunta escrita na parede da frente:")
            resposta = input("“Se você me tiver, irá querer me compartilhar. Se você me compartilhar, não me terá mais. O que sou?”\nR: ")

            if resposta == "segredo":
                print("\nApós respondida a pergunta, um dispositivo é acionado, inundando todo o ambiente com uma artificial chuva, cessando o fogo aos poucos. Em poucos instantes, o local já está contido, permitindo que consiga prosseguir com o caminho.")
                score += 0.5
                quartaDecisao()
            else: 
                print("\nA força do fogo é intensificada consumindo o ambiente por inteiro e inevitavelmente alastrando-se pelo seu corpo. Os gritos de dor aos poucos se enfraquecem e silenciam, substituídos pelo estalar da brasa contínua.")
                fimDoJogo()            
        elif resposta == "ESC":
            quitMenu(3)
        else: 
            print("\nA força do fogo é intensificada consumindo o ambiente por inteiro e inevitavelmente alastrando-se pelo seu corpo. Os gritos de dor aos poucos se enfraquecem e silenciam, substituídos pelo estalar da brasa contínua.")
            fimDoJogo()

    elif escolha == "b":
        print("\nO rangido da porta ao abrir ecoa pelo local, que aparenta estar vazio. Você se encaminha para o centro, buscando o acesso ao outro lado que lhe permitirá prosseguir com seu caminho até ser surpreendido por alguém que passa o braço pela sua garganta, pressionando-o contra sua traquéia. A força feita pelo indivíduo aumenta, tornando o ar impossível de passar. Sua visão fica turva aos poucos, lentamente seu corpo deixa de se debater entregando-se ao sono profundo da morte.")
        fimDoJogo()

    elif escolha == "c":
        print("\nVocê abre a porta cuidadosamente, torcendo com todas as forças para ter feito uma boa escolha. E fez. Ao entrar no pequeno recinto, há um bilhete na parede: “Parabéns pela sábia escolha. Nenhum animal seria capaz de viver sem se alimentar por um ano. Boa sorte em sua jornada.")
        score += 1.0
        quartaDecisao()

    elif escolha == "ESC":
        quitMenu(3)

    else:
        print("\n[!] Opção inválida! Por favor, tente novamente.")
        terceiraDecisao()


def quartaDecisao():
    global score
    global dicas

    print("Algo lhe diz, como uma intuição, que o fim dessa agonia está próxima. Você está vivo e não foi fácil para que chegasse até aqui. Ao se encaminhar para próxima etapa, consegue ouvir uma voz familiar distante e abafada. Mary?")
    print("\t- Por favor! Por favor, venha logo! Estou com o George, precisamos sair daqui o mais rápido possível!")
    print("\nVocê então corre em direção ao som, mas se depara com três opções de caminho possíveis:")
    
    escolha = input("(a) Esquerda\n(b) Direita\n(c) Em frente\nR: ")

    if escolha == "a":
        print("\n")
        print(" ||  ||\n \\\()// \n//(__)\\\ \n||    ||")

        print("\nAo optar pela direção esquerda, a entrada para esta sala é diferente das demais. Diferentemente das anteriores cujas entradas eram seladas após estar-se lá dentro, especificamente essa possuía maçaneta. Ao colocar a mão para abri-la, sentiu uma agulhada na ponta do dedo.")
        print("Após entrar no local, uma trava automática é chamada, trancando a entrada atrás de você. O efeito da picada sentida passa a fazer efeito e em poucos segundos você já não possui domínio sobre suas pernas. Todo o seu corpo da cabeça para baixo não obedece seus comandos.")
        print("Você tenta se rastejar até a porta de saída que se mantém aberta, entretanto se dá conta que uma aranha vermelha caminha lentamente em sua direção.")

        resposta = input("O que nasce aos socos e morre à facadas?\n R: ")

        if resposta == "pão":
            print("\nVocê consegue rastejar com extrema dificuldade até o outro lado do cômodo, desviando da aranha. Cerca de 40 minutos após o corpo estar totalmente paralisado, os movimentos começam a retornar lentamente.")
            score += 0.5
            quintaDecisao()
        elif resposta == "DICA" and dicas != 0:
            print("\n[!] DICA: É uma comida")
            dicas -= 1
            print("\n[!] VOCÊ TEM {} DICA(S) RESTANTES".format(dicas))

            print("\nAo optar pela direção esquerda, a entrada para esta sala é diferente das demais. Diferentemente das anteriores cujas entradas eram seladas após estar-se lá dentro, especificamente essa possuía maçaneta. Ao colocar a mão para abri-la, sentiu uma agulhada na ponta do dedo.")
            print("Após entrar no local, uma trava automática é chamada, trancando a entrada atrás de você. O efeito da picada sentida passa a fazer efeito e em poucos segundos você já não possui domínio sobre suas pernas. Todo o seu corpo da cabeça para baixo não obedece seus comandos.")
            print("Você tenta se rastejar até a porta de saída que se mantém aberta, entretanto se dá conta que uma aranha vermelha caminha lentamente em sua direção.")

            resposta = input("O que nasce aos socos e morre à facadas?\n R: ")

            if resposta == "pão":
                print("\nVocê consegue rastejar com extrema dificuldade até o outro lado do cômodo, desviando da aranha. Cerca de 40 minutos após o corpo estar totalmente paralisado, os movimentos começam a retornar lentamente.")
                score += 0.5
                quintaDecisao()
            else:
                print("\nA substância parece contrair todos os seus tendões musculares, tornando cada vez mais impossível realizar qualquer movimento. Apesar da consciência lúcida e mente funcionando em perfeito estado, nada mais restava além de aguardar a aranha se aproximar. ")
                print("Ela então, sobe em um dos seus dedos, caminhando em direção à sua mão. Num dos poucos e limitados reflexos que lhe sobrou, um espasmo faz com que sua mão se mova, sendo imediatamente apanhada pela aranha.")
                print("O veneno é letal.")
                fimDoJogo()

        elif resposta == "ESC":
            quitMenu(4)
        else: 
            print("\nA substância parece contrair todos os seus tendões musculares, tornando cada vez mais impossível realizar qualquer movimento. Apesar da consciência lúcida e mente funcionando em perfeito estado, nada mais restava além de aguardar a aranha se aproximar. ")
            print("Ela então, sobe em um dos seus dedos, caminhando em direção à sua mão. Num dos poucos e limitados reflexos que lhe sobrou, um espasmo faz com que sua mão se mova, sendo imediatamente apanhada pela aranha.")
            print("O veneno é letal.")
            fimDoJogo()

    elif escolha == "b":
        print("\nAo optar pela direção direita, a entrada para esta sala é diferente das demais. Diferentemente das anteriores cujas entradas eram seladas após estar-se lá dentro, especificamente essa possuía maçaneta. Pendura nela, um óculos estava. Ao colocá-lo e adentrar a sala, era possível notar que era feito justamente para que fosse possível enxergar no escuro.")
        print("Para sua surpresa, no cômodo recém entrado havia uma mesa e em cima desta, um aparelho celular. Você sorri aliviado. Acabou. Você sobreviveu e conseguirá finalmente pedir por ajuda. ")
        print("Corre então, em direção ao dispositivo, apertando o botão para ligá-lo.")
        print("A fagulha criada pelo aparelho era o que bastava para que o ambiente preenchido por gás altamente inflamável explodisse com você dentro.")
        fimDoJogo()

    elif escolha == "c":

        print("\nO cômodo para qual se dirige apresenta uma escada, que o coloca num nível abaixo do que se encontra e é compatível com a origem dos sons que ouviu recentemente. Talvez sua intuição realmente esteja certa e de fato isso esteja acabando.")
        print("Você desce as escadas, na esperança de encontrar Mary e George.")
        score += 1.0
        quintaDecisao()

    elif escolha == "ESC":
        quitMenu(4)

    else:
        print("\n[!] Opção inválida! Por favor, tente novamente.")
        quartaDecisao()



def quintaDecisao():
    global score
    global dicas

    print("A escada levou até uma grande região central, iluminada e cinza, diferente dos ambientes obscuros visitados anteriormente. Um grande painel repleto de botões fazia parte do local que lembrava uma sala de controle. Próximo do teto, havia um painel com um relógio em contagem regressiva. Um total de 3 minutos era tudo que restava.")
    print("Havia uma tela em sua frente que repentinamente apresentou uma pessoa mascarada, que dizia com a voz transformada por meio de efeitos:")
    print("“Devo dizer que subestimei sua capacidade em chegar até aqui. Porque simplesmente achei que não fosse ser capaz de passar da primeira sala. Gosto quando meus participantes se superam. Pois bem. Alcançamos o auge da pontuação de audiência do dia, espero que fique feliz com essa informação.” ")
    print("A tela ao lado então, ligou, mostrando Mary e George dentro de cômodos, com olhares de desespero e preocupação.")
    print("A voz então continuou:\n\t“Bem vindo ao Hunner. Espero que consiga sair vivo para acompanhar as próximas temporadas desse programa. Vamos à etapa final. Tudo que tem que fazer é escolher um botão dentre os três abaixo e apertar. Ah, devo dizer que seus dois amigos possuem um dispositivo no corpo que pode explodi-los dependendo do botão que escolher.”")

    escolha = input("(a) Botão verde\n(b) Botão roxo\n(c) Botão amarelo\nR: ")

    if escolha == "a":
        print("Enquanto apertava o botão, sabia que o poder daquela decisão poderia salvar ou custar alguma vida, Você fechou os olhos esperando pelo pior mas uma porta se abriu em sua frente, de onde Mary e George saíram de lá, aliviados por estarem vivos. A voz então, ressurgiu com a seguinte mensagem:\n“Meus parabéns! São poucas as vezes que temos finais felizes por aqui. Nossa equipe estará entrando em contato para oferecer suporte à vocês. Após isso, serão encaminhados para serem entrevistados”.\nA indignação por serem submetidos à condições mortais por entretenimento estava misturada com o alívio de poder estar junto das pessoas pelas quais se preocupou durante todo o percurso. ")
        score += 1.0
        win()

    elif escolha == "b":
        print("Enquanto apertava o botão, sabia que o poder daquela decisão poderia salvar ou custar alguma vida. Após pressionado, a câmera que focava Mary e George, televisionou em tempo real e ao vivo a morte de George e Mary, cujos corpos instantaneamente explodiram pelo dispositivo acionado por meio do botão roxo. O espanto, horror e desespero tomaram conta do seu corpo. \nA voz então, ressurgiu com a seguinte mensagem:\n“Poxa vida, sinto muito pela sua perda. Nossa equipe estará entrando em contato para oferecer suporte à você. Após isso, será encaminhado para ser entrevistado.”\nSeu corpo foi ao chão. As lágrimas escorriam pelo seu rosto sem que  tivesse total controle da situação. Não havia mais nada que poderia ser feito. Seus melhores amigos haviam morrido em prol do entretenimento popular. Esse pensamento consumia todos os pedaços de si.")
        win()

    elif escolha == "c":
        print("Enquanto apertava o botão, sabia que o poder daquela decisão poderia salvar ou custar alguma vida. Após pressionado, a câmera que focava Mary e George, televisionou em tempo real e ao vivo a morte de George, cujo corpo instantaneamente explodiu pelo dispositivo acionado por meio do botão amarelo. O espanto, horror e desespero tomaram conta do seu corpo. \nA porta do local onde se encontrava Mary abriu, libertando-a de vez.\nA voz então, ressurgiu com a seguinte mensagem:\n“Poxa vida, sinto muito pela sua perda. Nossa equipe estará entrando em contato para oferecer suporte à vocês. Após isso, serão encaminhados para serem entrevistados.”")
        score += 0.5
        win()

    elif escolha == "ESC":
        quitMenu(5)

    else:
        print("\n[!] Opção inválida! Por favor, tente novamente.")
        quintaDecisao()


def win(): 
    if isAscii == 1:
        print("\n")
        print("             /\ o") 
        print("   o     /_ /~~/   ")
        print("    \      /\/     ")
        print("     \    /        ") 
        print("      \  /         ") 
        print(",-----------------,")
        print("| ,-----------,   |")
        print("| |           | O |")
        print("| |           | O |")
        print("| |           |...|")
        print("| |___________|I#I|")
        print("|_________________|")

    percent_score = (score/5) * 100
    if percent_score == 100:
        print("\nVOCÊ GANHOU!\nO SEU SCORE FOI DE {}%. PARABÉNS, VOCÊ OBTEVE UM SCORE PERFEITO!".format(percent_score))
    elif percent_score >= 75 and percent_score < 100:
        print("\nVOCÊ GANHOU!\nO SEU SCORE FOI DE {}%. VOCÊ TEVE UM ÓTIMO SCORE, MAS AINDA HÁ MUITO O QUE APRENDER".format(percent_score))
    elif percent_score >= 50 and percent_score < 75:
        print("\nVOCÊ GANHOU!\nO SEU SCORE FOI DE {}%. TEM MUITO O QUE APRENDER AINDA...".format(percent_score))
    else:
        print("\nVOCÊ GANHOU!\nO SEU SCORE FOI DE {}%. FRACASSO!".format(percent_score))

def fimDoJogo():
    if isAscii == 1:
        print("\n")
        print("     .... NO! ...                  ... MNO! ...")
        print("   ..... MNO!! ...................... MNNOO! ...")
        print(" ..... MMNO! ......................... MNNOO!! .")
        print(".... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .")
        print(" ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....")
        print("    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...")
        print("   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....")
        print("   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ... ") 
        print("    ....... MMMMM..    OPPMMP    .,OMI! ....")
        print("     ...... MMMM::   o.,OPMP,.o   ::I!! ...")
        print("         .... NNM:::.,,OOPM!P,.::::!! ....")
        print("          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....")
        print("         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....")
        print("           .. MMMMMNNOOMMNNIIIPPPOO!! ......")
        print("          ...... MMMONNMMNNNIIIOO!..........")
        print("       ....... MN MOMMMNNNIIIIIO! OO ..........")
        print("    ......... MNO! IiiiiiiiiiiiI OOOO ...........")
        print("  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........")
        print("   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........")
        print("   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........")
        print("      ...... OO! ................. ON! .......")
        print("         ................................")
        print("\n")

    percent_score = (score/5) * 100
    if percent_score == 100:
        print("\nVOCÊ MORREU!\nO SEU SCORE FOI DE {}%. PARABÉNS, VOCÊ OBTEVE UM SCORE PERFEITO!".format(percent_score))
    elif percent_score >= 75 and percent_score < 100:
        print("\nVOCÊ MORREU!\nO SEU SCORE FOI DE {}%. VOCÊ TEVE UM ÓTIMO SCORE, MAS AINDA HÁ MUITO O QUE APRENDER".format(percent_score))
    elif percent_score >= 50 and percent_score < 75:
        print("\nVOCÊ MORREU!\nO SEU SCORE FOI DE {}%. TEM MUITO O QUE APRENDER AINDA...".format(percent_score))
    else:
        print("\nVOCÊ MORREU!\nO SEU SCORE FOI DE {}%. FRACASSO!".format(percent_score))

def quitMenu(state):
    choice = input("\nVocê gostaria de salvar o seu progresso?\n(1) Sim\n(0) Não\nR: ") 
    if choice == "1":
        save(state)
        print("\nSalvo com sucesso! Encerrando o programa...")
    else: 
       quit() 

def save(state):
    with open("save.dat", "w+") as f:
        f.write(str(state))



if isAscii == 1:
    print("\n __          ___      .______    __  .______      __  .__   __. .___________. ______      .___  ___.   ______   .______     .___________.    ___       __")  
    print("|  |        /   \     |   _  \  |  | |   _  \    |  | |  \ |  | |           |/  __  \     |   \/   |  /  __  \  |   _  \    |           |   /   \     |  |")
    print("|  |       /  ^  \    |  |_)  | |  | |  |_)  |   |  | |   \|  | `---|  |----|  |  |  |    |  \  /  | |  |  |  | |  |_)  |   `---|  |----`  /  ^  \    |  |") 
    print("|  |      /  /_\  \   |   _  <  |  | |      /    |  | |  . `  |     |  |    |  |  |  |    |  |\/|  | |  |  |  | |      /        |  |      /  /_\  \   |  |") 
    print("|  `----./  _____  \  |  |_)  | |  | |  |\  \----|  | |  |\   |     |  |    |  `--'  |    |  |  |  | |  `--'  | |  |\  \----.   |  |     /  _____  \  |  `----.")
    print("|_______/__/     \__\ |______/  |__| | _| `._____|__| |__| \__|     |__|     \______/     |__|  |__|  \______/  | _| `._____|   |__|    /__/     \__\ |_______|")
    print("\n")
else: 
    print("\nLabirinto Mortal")

print("\nAutores: \n\tFrancielly Ortiz - TIA 41991788\n\tJoão Victor - TIA 41990870\n\tMarcello Cestaro - TIA 41919297")

print("\nInstruções para jogar:")
print("\t- Neste jogo, tem dois tipos de escolhas: de multipla escolha e dissertativa")
print("\t- Responda todas as perguntas somente com PALAVRAS ou LETRAS sem letras maiúsculas")
print("\t\t Exemplo: ")
print("\t\t\t (a) Escolha 1")
print("\t\t\t (b) Escolha 2")
print("\t\t\t (c) Escolha 3")
print("\t\t\t R: a")
print("\t\t Exemplo 2: ")
print("\t\t\t Qual vai ser a nota deste trabalho?")
print("\t\t\t R: 10")
print("\t- As suas escolhas serão avaliadas e colocadas em um SCORE final para avaliar o seu desempenho. O score máximo é 100%.")
print("\t- Para que as artes em ASCII funcionem da melhor forma, é recomendado que o programa esteja rodando em tela cheia.")
print("\t- Em qualquer momento você pode escrever ESC (em letras maiúsculas) para ir no menu de salvar e sair")
print("\t- Nas charadas escritas, você tem direito a DUAS dicas! Para usa-las na parte da charada, digite 'DICA' em caixa alta")

print("\nBoa sorte com as suas escolhas!")


try:
    save_file = open("save.dat", "r")
    pronto = input("\nDetectamos um arquivo salvo no seu computador. Você gostaria de continuar a sua aventura de onde parou?\n(1) Sim\n(0) Não\nR: ")
    isSaved = True
except: 
    pronto = "0"

if pronto == "1" and isSaved == True:

    stage = save_file.readline()
    if stage == "1":
        primeiraDecisao()
    elif stage == "2":
        segundaDecisao()
    elif stage == "3":
        terceiraDecisao()
    elif stage == "4":
        quartaDecisao()
    elif stage == "5":
        quintaDecisao()
    else: 
        print("Arquivo de save corrompido! Iniciando novo jogo...")
        primeiraDecisao()

else:

    pronto = input("\nVocê está pronto(a) para encarar os desafios?\n(1) Sim! (Novo jogo) \n(2) Não, preciso ainda de um tempo para pensar.\n(3) Sair do programa\nR: ")

    while pronto != "1":  
        if(pronto == "3"):
            quit()
        pronto = input("\nVocê está pronto(a) para encarar os desafios?\n(1) Sim! (Novo jogo) \n(2) Não, preciso ainda de um tempo para pensar.\n(3) Sair do programa\nR: ")

    print("\n")
    print(70*"~*~*")
    print("Você abre os olhos. Sua cabeça está confusa e as ideias estão deturpadas. O ambiente ao redor roda incessantemente, dando-lhe a impressão de estar num carrossel. O que aconteceu? Para onde foram George e Mary? \nAos poucos você vai reconhecendo a situação que até então era digna de livros e filmes. Cercado por paredes,  você conclui: está num labirinto. O maior desafio? Sair dele com vida.")

    primeiraDecisao()

