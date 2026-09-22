################################################################
# MIHRAGE — CAPÍTULO 3
# "Nas Profundezas", dez anos depois — fases 14 a 26
# ==========================================
#   Fase 14  text                  escrita
#   Fase 15  demo_character        escolha
#   Fase 16  simple_displayables   debug
#   Fase 17  demo_transitions      escolha
#   Fase 18  tutorial_positions    escrita
#   Fase 19  tutorial_atl          escolha
#   Fase 20  transform_properties  escrita
#   Fase 21  new_gui               escolha
#   Fase 22  styles                debug
#   Fase 23  tutorial_screens      escolha
#   Fase 24  screen_displayables   escrita
#   Fase 25  demo_minigame         escolha
#   Fase 26  translations          escrita
################################################################

label cap3_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "cap3_checkpoint"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 3{/size}\nNas Profundezas — dez anos depois"

    scene black
    with dissolve

    "Dez anos é tempo suficiente pra uma pessoa virar uma história que a gente conta pros outros sem esperar resposta."


# ---- FASE 14 — text (escrita) ----------------------------------
label cap3_fase14:

    scene bg washington
    with dissolve

    "Desembarque em Salvador, três da tarde, o saguão cheio."

    "Uma mulher de costas na fila do café, com o mesmo jeito de apoiar o peso numa perna só."

    $ reset_example()
    call text

    call fase_escrita(
        "Escreve a marcação que abre o itálico.",
        [
            "{i}",
        ],
        "Ainda não. É a letra i entre chaves, sem barra nenhuma - a barra é só pra fechar.",
        "Antes: as marcações de texto vão entre chaves. A que abre o negrito é a letra b entre chaves, e fecha com barra antes da letra. O itálico funciona igual, com a letra i.",
        "Abra o itálico:")

    if not _return:
        jump game_over

    d "{i}É ela. Tem que ser ela.{/i}"

    "Não era."


# ---- FASE 15 — demo_character (escolha) ------------------------
label cap3_fase15:

    "Aconteceu no metrô de São Paulo, numa fila de banco, num show, num aeroporto. Dez vezes, talvez mais."

    $ reset_example()
    call demo_character

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


# ---- FASE 16 — simple_displayables (debug) ---------------------
label cap3_fase16:

    "Ele se virou rápido demais, e o saguão inteiro girou junto."

    $ reset_example()
    call simple_displayables

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

    with vpunch

    "Não era ela. Uma desconhecida, incomodada com o homem que a encarava no meio do saguão."

    d "Desculpa. Achei que fosse outra pessoa."


# ---- FASE 17 — demo_transitions (escolha) ----------------------
label cap3_fase17:

    $ reset_example()
    call demo_transitions

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

    scene bg whitehouse
    with slowdissolve

    "Congresso de automação e controle, auditório lateral, crachás azuis."


# ---- FASE 18 — tutorial_positions (escrita) --------------------
label cap3_fase18:

    "O coquetel do fim do primeiro dia. Vinte e poucas pessoas, taças de plástico, conversa de crachá."

    $ reset_example()
    call tutorial_positions

    call fase_escrita(
        "Ele varre o salão e para numa pessoa à direita. A imagem é eileen happy, a posição é right.",
        [
            "show eileen happy at right",
        ],
        "Ainda não. É show, o nome da imagem, a palavra at, e o nome da posição.",
        "Antes: é a mesma forma de sempre - show, o nome da imagem, at, e a posição. Só muda qual posição você escolhe.",
        "Fixe o olhar:")

    if not _return:
        jump game_over

    show eileen happy at right
    with dissolve

    "Uma mulher perto da mesa de café, explicando alguma coisa com as duas mãos."


# ---- FASE 19 — tutorial_atl (escolha) --------------------------
label cap3_fase19:

    $ reset_example()
    call tutorial_atl

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

    e "Você é do Rio, né? Dá pra ouvir de longe."

    d "Tão óbvio assim?"

    e "Um pouco. Milena, com H no meio. Moro aqui há uns oito anos."


# ---- FASE 20 — transform_properties (escrita) ------------------
label cap3_fase20:

    $ e.name = _("Milena")

    "Ela falava rápido, cortava a própria frase pra rir no meio, e apoiava o peso numa perna só."

    $ reset_example()
    call transform_properties

    call fase_escrita(
        "Aproxima a imagem no dobro do tamanho.",
        [
            "zoom 2.0",
            "zoom 2",
        ],
        "Ainda não. É a propriedade zoom seguida do número, sem mais nada.",
        "Antes: a propriedade que aproxima ou afasta uma imagem se chama zoom. O valor 1.0 é o tamanho normal; menos que isso diminui, mais que isso aumenta. Metade do tamanho seria: zoom 0.5",
        "Aproxime:")

    if not _return:
        jump game_over

    show eileen happy at truecenter
    with Dissolve(1.0)

    d "{i}O jeito de rir antes do fim da frase. A perna. A mão no cabelo.{/i}"


# ---- FASE 21 — new_gui (escolha) -------------------------------
label cap3_fase21:

    $ reset_example()
    call new_gui

    call fase_escolha(
        "Ele emudece no meio da conversa. Nada se move, nada muda de cor, nada entra em cena. O que a história faz nesse instante?",
        [
            ("Nada - só a fala segue, e o silêncio é o próprio acontecimento", True,
             "Isso. Nem toda cena precisa de efeito: às vezes a ausência de qualquer mudança é o efeito."),
            ("Uma transição forte pra marcar o susto", False,
             "Não. Um efeito grande aqui quebraria justamente o silêncio que é o ponto da cena."),
            ("Trocar a interface inteira do jogo", False,
             "Não. A interface não tem nada a ver com o que travou nele."),
        ])

    if not _return:
        jump game_over

    e "...Que foi? Falei alguma bobagem?"

    e "Que foi? Tá branco."

    d "Mirela?"


# ---- FASE 22 — styles (debug) ----------------------------------
label cap3_fase22:

    "O nome ficou pendurado no ar entre os dois por um tempo bem mais longo que uma palavra."

    $ reset_example()
    call styles

    call fase_debug(
        "AS LEMBRANÇAS VOLTANDO — o estilo não aplica",
        [
            "style lembranca:",
            "    color",
        ],
        "A segunda linha está incompleta. Escreve ela com o branco em hexadecimal.",
        [
            "color '#ffffff'",
            "color '#fff'",
        ],
        "Ainda não. É a propriedade color e o valor entre aspas, começando com cerquilha.",
        "Antes: dentro de um style, cada propriedade é o nome dela e o valor. A cor do texto se chama color, e o valor vai entre aspas, começando com cerquilha. Vermelho puro seria: color '#ff0000'")

    if not _return:
        jump game_over

    scene black
    with dissolve

    "A caixa de som alta demais pro tamanho do pátio."

    "O risco de tinta no muro, atrás da Lucy."

    "A trilha do morro, o vento, e uma frase que ficou sem ser dita."


# ---- FASE 23 — tutorial_screens (escolha) ----------------------
label cap3_fase23:

    $ reset_example()
    call tutorial_screens

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

    e "Eu tinha dezoito anos."

    e "Eu ia te contar uma coisa naquele dia, lá em cima."


# ---- FASE 24 — screen_displayables (escrita) -------------------
label cap3_fase24:

    scene bg whitehouse
    show eileen happy at center
    with dissolve

    d "Espera. Deixa eu te mostrar uma coisa."

    "Ele destravou o celular e foi descendo até uma pasta que não abria havia anos."

    $ reset_example()
    call screen_displayables

    call fase_escrita(
        "Põe uma imagem chamada foto_festa dentro da tela do celular.",
        [
            "add 'foto_festa'",
        ],
        "Ainda não. É a palavra add seguida do nome da imagem entre aspas.",
        "Antes: dentro de uma tela, a palavra add põe uma imagem ali. O nome dela vai entre aspas logo depois. Com uma imagem chamada logo, seria: add 'logo'",
        "Mostre a foto:")

    if not _return:
        jump game_over

    "Doze segundos de câmera tremida. A Lucy rindo perto da caixa de som. Ele de costas. E num canto do quadro, por menos de um segundo, ela."

    e "Eu não tenho nenhuma foto dessa época. Nenhuma."

    e "Eles levaram tudo."


# ---- FASE 25 — demo_minigame (escolha) -------------------------
label cap3_fase25:

    "Antes do resto, ela quis lembrar de uma coisa boa - e lembrou rindo."

    $ reset_example()
    call demo_minigame

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

    e "Você perdia todas. Todas."

    d "Eu deixava você ganhar."

    e "Mentira. Você perdia todas."

    "Riram junto pela primeira vez em dez anos, e por um segundo a diferença entre as duas décadas não existiu."


# ---- FASE 26 — translations (escrita) --------------------------
label cap3_fase26:

    scene black
    with dissolve

    e "Eles acharam as drogas no meu quarto. Coisa de adolescente, nada muito além disso - a gente usava lá no morro, todo mundo usava."

    e "Naquele mesmo dia. Bem no dia em que eu ia te contar."

    e "A solução deles foi me formatar. Tiraram do CEFET, tiraram o telefone, tiraram os amigos, mudaram a gente de cidade."

    e "Um hard reset. Foi isso que fizeram comigo."

    $ reset_example()
    call translations

    call fase_escrita(
        "Escreve o nome novo - o que ela escolheu pra si mesma.",
        [
            "milena",
            "mi",
        ],
        "Ainda não. É o nome que ela usa hoje, o que ela mesma escolheu.",
        "Antes: traduzir é trocar uma palavra pela outra e passar a mostrar só a nova, mantendo a antiga guardada embaixo. Foi exatamente isso que ela fez com o próprio nome.",
        "O novo nome:")

    if not _return:
        jump game_over

    e "No começo era só Mi. Servia pra qualquer coisa, não puxava nada atrás."

    e "Aí começaram a perguntar \"Mi de quê?\", e eu tive que inventar o resto. Milena."

    e "E eu não voltei atrás. Não porque eu não pudesse - porque aquela ali já não era mais eu."

    scene bg washington
    show eileen vhappy at center
    with slowdissolve

    d "Eu fiz uma música pra você. Em 2014."

    d "Nunca mostrei pra ninguém."

    e "Toca."

    play music "sunflower-slow-drag.ogg" fadein 2

    "Não teve final feliz, porque dez anos não voltam. Mas ela estava viva, estava inteira, e tinha um nome que ninguém tinha escolhido por ela."

    hide screen hud_vidas

    scene black
    with slowdissolve

    centered "{size=+10}MIHRAGE{/size}\n\nFim"

    return
