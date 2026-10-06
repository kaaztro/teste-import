################################################################
# MIHRAGE — CAPÍTULO 3 "Mihlena"
# 2024 — fases 14 a 26
# ==========================================
# O Daniel conta os dez anos e o dia de hoje até alcançar o prólogo
# (fases 14 a 20). A partir da fase 21 a conversa segue no presente:
# o que ela mudou, as lembranças voltando, o print da fita, o porquê
# do sumiço e o nome novo.
#
#   Fase 14  text                  escrita   (hoje cedo, aeroporto)
#   Fase 15  demo_character        escolha   (os dez anos)
#   Fase 16  simple_displayables   debug     (aeroporto)
#   Fase 17  demo_transitions      escolha   (até o congresso)
#   Fase 18  tutorial_positions    escrita   (checkpoint · coquetel)
#   Fase 19  tutorial_atl          escolha   (a conversa antes do nome)
#   Fase 20  transform_properties  escrita   (o reconhecimento = prólogo)
#   Fase 21  new_gui               escolha   (agora · checkpoint)
#   Fase 22  styles                debug
#   Fase 23  tutorial_screens      escolha
#   Fase 24  screen_displayables   escrita
#   Fase 25  demo_minigame         escolha
#   Fase 26  translations          escrita   (o nome novo)
################################################################

label cap3_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ ambiente(None)
    $ checkpoint_atual = "cap3_checkpoint"
    $ nome_dela = "Mirela"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 3 — Mihlena{/size}\n2024"

    $ quando = "2014-2024 · lembrança dele"

    scene black
    with dissolve

    "Dez anos é tempo suficiente pra uma pessoa virar uma história que a gente conta pros outros sem esperar resposta."

    dh "Eu contava você pros outros. Virou uma história minha: \"uma amiga que sumiu\"."

    mh "E eles?"

    dh "Faziam cara de pena e mudavam de assunto."


# ---- FASE 14 — text (escrita) ----------------------------------
label cap3_fase14:

    $ quando = "2024 · hoje cedo"

    scene bg aeroporto
    show daniel idle at left
    with dissolve

    $ ambiente("aeroporto")

    "Desembarque em Salvador, três da tarde, o saguão cheio."

    "Uma mulher de costas na fila do café, com o mesmo jeito de apoiar o peso numa perna só."

    dh "Hoje cedo, no aeroporto. Eu já achei que era você."

    call modulo("text", 14, "Texto e marcações")

    call fase_escrita(
        "O que ele pensou não foi dito em voz alta. Escreve a marcação que abre o itálico.",
        [
            "{i}",
        ],
        "Ainda não. É a letra i entre chaves, sem espaço e sem barra - a barra é só pra fechar.",
        "Antes: as marcações de texto vão entre chaves. A que abre o negrito é a letra b entre chaves, e fecha com barra antes da letra. O itálico funciona igual, com a letra i.",
        "Abra o itálico:")

    if not _return:
        jump game_over

    scene bg aeroporto
    show daniel idle at left

    d "{i}É ela. Tem que ser ela.{/i}"

    "Não era."


# ---- FASE 15 — demo_character (escolha) ------------------------
label cap3_fase15:

    $ quando = "2014-2024 · lembrança dele"

    "Aconteceu no metrô de São Paulo, numa fila de banco, num show, num aeroporto. Dez vezes, talvez mais."

    mh "Dez vezes?"

    dh "Mais. Parei de contar."

    call modulo("demo_character", 15, "Personagens")

    call fase_escolha(
        "Cada uma dessas vezes soou diferente na cabeça dele: umas gritadas, outras quase sussurradas. O que controla isso?",
        [
            ("As propriedades do personagem - tamanho, cor e estilo do texto da fala", True,
             "Isso. O mesmo personagem pode ter versões com vozes visualmente diferentes."),
            ("A posição da imagem na tela", False,
             "Não. Onde a pessoa aparece não muda como a fala dela soa."),
            ("A transição entre as cenas", False,
             "Não. A passagem entre cenas não altera o tom de uma fala."),
        ])

    if not _return:
        jump game_over

    d "Da primeira vez eu corri atrás. Da quinta eu só olhei."

    d "Da décima eu já sabia que não era, e fui conferir mesmo assim."

    mh "Eu também fazia isso. Com você, com a Lucy. Qualquer menino de violão nas costas."


# ---- FASE 16 — simple_displayables (debug) ---------------------
label cap3_fase16:

    $ quando = "2024 · hoje cedo"

    scene bg aeroporto
    show daniel idle at left

    dh "Hoje, no aeroporto, eu me virei rápido demais."

    "Ele se virou rápido demais, e o saguão inteiro girou junto."

    call modulo("simple_displayables", 16, "Displayables simples")

    call fase_debug(
        "A VIRADA — a imagem não gira",
        [
            "transform girando:",
            "    rotate",
        ],
        "A segunda linha está incompleta. Escreve ela com quarenta e cinco graus.",
        [
            "rotate 45",
        ],
        "Ainda não. É a propriedade rotate seguida do número, sem mais nada.",
        "Antes: dentro de um transform, cada propriedade é o nome dela seguido do valor. A que gira a imagem se chama rotate, e o valor é o número de graus. Noventa graus seria: rotate 90")

    if not _return:
        jump game_over

    scene bg aeroporto
    show daniel idle at left
    with vpunch

    "Não era ela. Uma desconhecida, incomodada com o homem que a encarava no meio do saguão."

    show daniel sad at left

    d "Desculpa. Achei que fosse outra pessoa."

    dh "E aí eu jurei que era a última vez."


# ---- FASE 17 — demo_transitions (escolha) ----------------------
label cap3_fase17:

    dh "Do aeroporto até aqui foram quarenta minutos de táxi. Não aconteceu nada."

    call modulo("demo_transitions", 17, "Transições em detalhe", com_menu=True)

    call fase_escolha(
        "Do aeroporto até o congresso são quarenta minutos que a história não precisa mostrar. O que resolve isso?",
        [
            ("Uma transição entre as duas cenas", True,
             "Isso. A passagem diz que o tempo andou sem precisar mostrar cada minuto."),
            ("Trocar a cena sem nenhuma passagem", False,
             "Não. O corte seco funciona, mas não dá a sensação de tempo que passou."),
            ("Mostrar o trajeto inteiro em imagens", False,
             "Não. Isso arrasta a história por quarenta minutos que não contam nada."),
        ])

    if not _return:
        jump game_over

    scene bg aeroporto
    show daniel idle at left
    scene bg saguao tarde
    with slowdissolve

    $ ambiente("coquetel")

    "Congresso de automação e controle, auditório lateral, crachás azuis."


# ---- FASE 18 — tutorial_positions (escrita) --------------------
label cap3_fase18:

    $ checkpoint_atual = "cap3_fase18"
    $ quando = "2024 · hoje, no coquetel"
    $ nome_dela = "Mirela"

    scene bg saguao tarde

    "O coquetel do fim do primeiro dia. Vinte e poucas pessoas, taças de plástico, conversa de crachá."

    dh "E aí, umas duas horas atrás..."

    call modulo("tutorial_positions", 18, "Posições")

    call fase_escrita(
        "Ele varre o salão e para numa pessoa à direita. A imagem é mirela happy, a posição é right.",
        [
            "show mirela happy at right",
            "re:show mirela happy at right with \\w+",
        ],
        "Ainda não. É show, o nome da imagem, a palavra at, e o nome da posição.",
        "Antes: é a mesma forma de sempre - show, o nome da imagem, at, e a posição. Só muda qual posição você escolhe.",
        "Fixe o olhar:")

    if not _return:
        jump game_over

    scene bg saguao tarde
    show mirela happy at right
    show daniel idle at left
    with dissolve

    "Uma mulher perto da mesa de café, explicando alguma coisa com as duas mãos."

    dh "Você tava ali, explicando um sensor com as duas mãos."

    mh "Era um encoder. E eu tava certa."


# ---- FASE 19 — tutorial_atl (escolha) --------------------------
label cap3_fase19:

    call modulo("tutorial_atl", 19, "Animação e transformações (ATL)")

    call fase_escolha(
        "A conversa começa e a cena precisa respirar junto: movimento leve ao longo do tempo. Como isso se descreve?",
        [
            ("Num bloco de transform, com as propriedades mudando em sequência", True,
             "Isso. É o bloco que diz o que muda, em que ordem, e em quanto tempo."),
            ("Numa única linha de show, sem mais nada", False,
             "Não. Uma linha só coloca a imagem parada - não descreve movimento nenhum."),
            ("No arquivo de opções do jogo", False,
             "Não. Ali ficam as configurações gerais, não a animação de uma cena."),
        ])

    if not _return:
        jump game_over

    # Revivendo o começo da conversa de hoje: ele ainda não sabia
    # quem ela era.
    $ nome_dela = "Moça do café"

    scene bg saguao tarde
    show mirela happy at right
    show daniel idle at left
    with dissolve

    m "Você é do Rio, né? Dá pra ouvir de longe."

    d "Tão óbvio assim?"

    m "Um pouco. [NOME_NOVO], com H no meio. Moro aqui há uns oito anos."

    $ nome_dela = "Mirela"

    dh "\"Com H no meio.\" Eu fiquei preso nesse H."

    mh "Depois eu te explico o H."


# ---- FASE 20 — transform_properties (escrita) ------------------
label cap3_fase20:

    scene bg saguao tarde
    show mirela happy at right
    show daniel idle at left

    "Ela falava rápido, cortava a própria frase pra rir no meio, e apoiava o peso numa perna só."

    dh "E aí eu comecei a reparar. Uma coisa de cada vez, bem de perto."

    call modulo("transform_properties", 20, "Propriedades de transform")

    call fase_escrita(
        "Aproxima a imagem no dobro do tamanho.",
        [
            "zoom 2",
        ],
        "Ainda não. É a propriedade zoom seguida do número, sem mais nada.",
        "Antes: a propriedade que aproxima ou afasta uma imagem se chama zoom. O valor 1.0 é o tamanho normal; menos que isso diminui, mais que isso aumenta. Metade do tamanho seria: zoom 0.5",
        "Aproxime:")

    if not _return:
        jump game_over

    scene bg saguao tarde
    show mirela happy at truecenter
    with Dissolve(1.0)

    d "{i}O jeito de rir antes do fim da frase. A perna. A mão no cabelo.{/i}"

    $ nome_dela = "Moça do café"

    m "Que foi? Tá branco."

    d "Mirela?"

    $ nome_dela = "Mirela"

    dh "E o resto você sabe."

    mh "Sei. Eu tava lá."


# ---- FASE 21 — new_gui (escolha) -------------------------------
label cap3_fase21:

    $ checkpoint_atual = "cap3_fase21"
    $ quando = "2024 · agora"
    $ nome_dela = "Mirela"

    scene bg saguao noite
    show mirela happy at right
    show daniel idle at left
    with dissolve

    $ ambiente("saguao_vazio")

    "Já era noite. O saguão tinha esvaziado quase todo; alguém empilhava cadeiras perto da mesa do café."

    d "Você mudou tudo. O sotaque, o cabelo, o jeito de vestir. Até a profissão: você queria ser professora."

    m "Mudei tudo que aparece."

    call modulo("new_gui", 21, "A interface (GUI)")

    call fase_escolha(
        "Ela trocou tudo que aparece por fora. No Ren'Py, onde se mexe pra mudar a cara inteira do jogo - caixa de texto, menus, cores - sem reescrever a história?",
        [
            ("Nas imagens da pasta gui e nas variáveis do gui.rpy", True,
             "Isso. A interface muda inteira, e o roteiro embaixo continua o mesmo."),
            ("Reescrevendo os labels do roteiro", False,
             "Não. Isso muda a história, não a cara do jogo."),
            ("Trocando o define dos personagens", False,
             "Não. Isso muda quem fala, não a interface em volta."),
        ])

    if not _return:
        jump game_over

    scene bg saguao noite
    show mirela happy at right
    show daniel idle at left

    m "Por fora. O motor é o mesmo."

    m "Eu é que demorei pra saber disso."


# ---- FASE 22 — styles (debug) ----------------------------------
label cap3_fase22:

    scene bg saguao noite
    show mirela concerned at right
    show daniel idle at left

    m "Sabe o que é estranho? Desde que você falou meu nome, as coisas tão voltando. Com cor."

    m "Durante anos eu lembrava daquela época em cinza. Sem querer, de propósito, não sei."

    call modulo("styles", 22, "Estilos", com_menu=True)

    call fase_debug(
        "AS LEMBRANÇAS VOLTANDO — o estilo não aplica",
        [
            "style lembranca:",
            "    color",
        ],
        "A segunda linha está incompleta. Escreve ela com o branco em hexadecimal.",
        [
            "rei:color '#(fff|ffffff)'",
        ],
        "Ainda não. É a propriedade color e o valor entre aspas, começando com cerquilha.",
        "Antes: dentro de um style, cada propriedade é o nome dela e o valor. A cor do texto se chama color, e o valor vai entre aspas, começando com cerquilha. Vermelho puro seria: color '#ff0000'")

    if not _return:
        jump game_over

    scene black
    with dissolve

    "A caixa de som alta demais pro tamanho do pátio."

    "O risco de tinta no muro, atrás da Lucy."

    "O Parafuso dormindo no meio da trilha."

    "A trilha do morro, o vento, e uma frase que ficou sem ser dita."


# ---- FASE 23 — tutorial_screens (escolha) ----------------------
label cap3_fase23:

    scene bg saguao noite
    show mirela concerned at right
    show daniel idle at left
    with dissolve

    m "Vem tudo de uma vez. Uma por cima da outra."

    call modulo("tutorial_screens", 23, "Telas (screens)", com_menu=True)

    call fase_escolha(
        "As lembranças vêm uma por cima da outra, rápidas, e depois somem. O que aparece por cima da cena e pode ser escondido de novo?",
        [
            ("Uma tela mostrada por cima, que dá pra esconder quando não for mais necessária", True,
             "Isso. Ela entra por cima do que já está lá e sai sem apagar a cena de baixo."),
            ("Um novo fundo de cena", False,
             "Não. Trocar o fundo apagaria tudo que estava embaixo."),
            ("Uma variável guardada na memória", False,
             "Não. A variável guarda o valor, mas não desenha nada na tela."),
        ])

    if not _return:
        jump game_over

    scene bg saguao noite
    show mirela concerned at right
    show daniel idle at left

    m "Eu tinha dezoito anos."

    m "Eu ia te contar uma coisa naquele dia, lá em cima."

    d "Eu sei. Eu tava lá também."

    m "A Lucy sabia. Eu contei pra ela uma semana antes. Ela me fez ensaiar a frase umas vinte vezes."

    d "A Lucy sabia."

    d "Em 2014 ela me disse que você contava tudo pra ela. \"Quase tudo.\" Eu nunca entendi aquele quase."

    m "Ela prometeu que não ia contar. Pelo jeito, cumpriu. Dez anos."

    d "Dez anos."


# ---- FASE 24 — screen_displayables (escrita) -------------------
label cap3_fase24:

    scene bg saguao noite
    show mirela happy at right
    show daniel idle at left

    d "Espera. Deixa eu te mostrar uma coisa."

    "Ele destravou o celular e foi descendo até uma pasta que não abria havia anos."

    call modulo("screen_displayables", 24, "Elementos de tela", com_menu=True)

    call fase_escrita(
        "Põe o print da fita, a imagem foto_festa, dentro da tela do celular.",
        [
            "re:add '(images/)?foto_festa(\\.png|\\.jpg|\\.webp)?'",
        ],
        "Ainda não. É a palavra add seguida do nome da imagem entre aspas.",
        "Antes: dentro de uma tela, a palavra add põe uma imagem ali. O nome dela vai entre aspas logo depois. Com uma imagem chamada logo, seria: add 'logo'",
        "Mostre a foto:")

    if not _return:
        jump game_over

    scene bg saguao noite
    show mirela concerned at right
    show daniel idle at left

    scene cg print
    with dissolve

    "Um quadro só, borrado, tirado da fita da festa. A Lucy rindo perto da caixa de som. Ele de costas. E no canto, meio cortada, ela."

    scene bg saguao noite
    show mirela concerned at right
    show daniel idle at left
    with dissolve

    m "Eu não tenho nenhuma foto dessa época. Nenhuma."

    m "Eles levaram tudo."

    show daniel happy at left

    d "Agora você tem uma."


# ---- FASE 25 — demo_minigame (escolha) -------------------------
label cap3_fase25:

    scene bg saguao noite
    show mirela vhappy at right
    show daniel idle at left

    "Antes do resto, ela quis lembrar de uma coisa boa - e lembrou rindo."

    m "Antes. Antes da parte ruim, deixa eu lembrar de uma coisa boa."

    call modulo("demo_minigame", 25, "Minigames")

    call fase_escolha(
        "Aquele joguinho de bater bola que eles jogavam lá no morro. O que faz uma partida dessas funcionar dentro de uma visual novel?",
        [
            ("Uma tela própria, com as regras do jogo rodando dentro dela", True,
             "Isso. A partida acontece numa tela separada e devolve o resultado pra história quando acaba."),
            ("Uma sequência de imagens paradas", False,
             "Não. Imagens paradas mostram a partida, mas ninguém joga nada."),
            ("Um menu de escolhas comum", False,
             "Não. Um menu escolhe entre caminhos; não é uma partida."),
        ])

    if not _return:
        jump game_over

    scene bg saguao noite
    show mirela vhappy at right
    show daniel idle at left

    m "Você perdia todas. Todas."

    show daniel happy at left

    d "Eu deixava você ganhar."

    m "Mentira. Você perdia todas."

    "Riram junto pela primeira vez em dez anos, e por um segundo a diferença entre as duas décadas não existiu."


# ---- FASE 26 — translations (escrita) --------------------------
label cap3_fase26:

    scene black
    with dissolve

    m "Eles acharam as drogas no meu quarto. Coisa de adolescente, nada muito além disso - a gente usava lá no morro, todo mundo usava."

    m "Naquele mesmo dia. Bem no dia em que eu ia te contar."

    m "A solução deles foi me formatar. Tiraram do CEFET, tiraram o telefone, tiraram os amigos, mudaram a gente de cidade."

    if primeira_ligacao == "casa":
        m "Quando você ligou lá em casa, eu tava na cozinha. Minha mãe atendeu, olhou pra mim e desligou."
    elif primeira_ligacao == "escola":
        m "A secretaria sabia onde eu tava. Meus pais pediram pra ninguém falar nada. Pra ninguém."
    elif primeira_ligacao == "lucy":
        m "A Lucy achava que eu tinha sumido porque quis. Era isso que eles queriam que todo mundo achasse."

    m "Um hard reset. Foi isso que fizeram comigo."

    d "E o H?"

    m "O H."

    call modulo("translations", 26, "Traduções")

    call fase_escrita(
        "Pra ela, Mirela é a língua original. O nome novo é a tradução que ela mesma escreveu. Marca o nome Mihlena como traduzível, do jeito que o módulo fez com o nome da Lucy.",
        [
            "re:_\\('Mihlena'\\)",
            "re:(m=)?Character\\(_\\('Mihlena'\\)(,.+)?\\)",
        ],
        "Ainda não. É o nome entre aspas, cercado por parênteses, com um sublinhado logo antes do primeiro parêntese.",
        "Antes: pra marcar um texto como traduzível, cerca ele com parênteses e põe um sublinhado antes. O nome da Lucy ficou assim: _('Lucy')",
        "O nome novo:")

    if not _return:
        jump game_over

    $ nome_dela = NOME_NOVO

    scene bg saguao noite
    show mirela happy at right
    show daniel idle at left
    with dissolve

    m "No começo era só Mih. A Lucy que inventou, lembra? Servia pra qualquer coisa, não puxava nada atrás."

    m "Aí começaram a perguntar \"Mih de quê?\", e eu tive que inventar o resto. [NOME_NOVO]."

    m "Com o H no meio. É o que sobrou da Mih."

    m "Mirela é a minha língua original. Ainda tá lá embaixo, guardada. Só não é mais a que eu falo."

    m "E eu não voltei atrás. Não porque eu não pudesse - porque aquela ali já não era mais eu."

    show mirela vhappy at right

    show daniel happy at left

    d "Eu fiz uma música pra você. Em 2014."

    d "Aquela das quarenta e três visualizações."

    m "Toca."

    play music "sunflower-slow-drag.ogg" fadein 2

    scene cg final
    with dissolve

    $ ambiente(None)

    "Ele pôs o celular na mesa, entre as duas taças vazias, e deixou tocar."

    "Antes da música acabar, ele pegou o celular de volta, digitou duas palavras e mandou."

    d "{i}Achei ela.{/i}"

    "O celular vibrou na mesa quase na mesma hora."

    l "ONDE"

    l "me liga AGORA"

    m "Ela não mudou nada."

    d "Nem um pouco."

    "Não teve final feliz, porque dez anos não voltam. Mas ela estava viva, estava inteira, e tinha um nome que ninguém tinha escolhido por ela."

    hide screen hud_vidas

    scene black
    with slowdissolve

    centered "{size=+10}MIHRAGE{/size}\n\nFim"

    return
