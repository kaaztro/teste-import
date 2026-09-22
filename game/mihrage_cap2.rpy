################################################################
# MIHRAGE — CAPÍTULO 2
# Daniel, ainda 2014 — fases 7 a 13
# ==========================================
#   Fase 7   tutorial_music      escrita
#   Fase 8   tutorial_menus      escolha
#   Fase 9   tutorial_input      escrita
#   Fase 10  tutorial_video      escolha
#   Fase 11  tutorial_nvlmode    debug
#   Fase 12  director            escolha
#   Fase 13  distribute          escrita
################################################################

label cap2_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "cap2_checkpoint"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 2{/size}\nDaniel — ainda 2014"

    scene black
    with dissolve

    "Três semanas depois, a cadeira dela continuava vazia, e ninguém no CEFET sabia dizer desde quando."

    d "Cadê aquela menina, a Mirela? Alguém sabe alguma coisa?"

    "E como ninguém sabia, cada um inventou a sua: que fugiu de casa, que largou o curso, que arranjou alguém em outra cidade e sumiu sem avisar."

    "Piada é o que as pessoas fazem quando não têm a história de verdade."


# ---- FASE 7 — tutorial_music (escrita) -------------------------
label cap2_fase7:

    scene bg washington
    with dissolve

    "O violão continuava encostado no canto do quarto, com a mesma corda desafinada de sempre."

    d "Ela pediu uma música. Eu enrolei, falei que era difícil, que eu tinha acabado de começar."

    d "Naquele dia eu tava tocando Hey Jude. De todas as músicas do mundo, Hey Jude."

    $ reset_example()
    call tutorial_music

    call fase_escrita(
        "Põe pra tocar o arquivo sunflower-slow-drag.ogg no canal music.",
        [
            "play music 'sunflower-slow-drag.ogg'",
            "play music 'sunflower-slow-drag'",
        ],
        "Ainda não. São três partes: play, o canal music, e o nome do arquivo entre aspas.",
        "Antes: pra tocar algo em loop que continua entre as cenas, usa o canal music. A ordem é play, o canal, e o nome do arquivo entre aspas. Por exemplo: play music 'tower_clock.ogg'",
        "Toque a música:")

    if not _return:
        jump game_over

    play music "sunflower-slow-drag.ogg"

    d "Se ela não vai me ouvir tocar, pelo menos vai existir uma música que é dela."


# ---- FASE 8 — tutorial_menus (escolha) -------------------------
label cap2_fase8:

    "A lista de contatos tinha três nomes que talvez soubessem de alguma coisa. O crédito do telefone dava pra uma ligação."

    $ reset_example()
    call tutorial_menus

    call fase_escolha(
        "Ele vai escolher pra quem ligar, e o jogo precisa lembrar dessa escolha lá na frente. O que guarda a decisão?",
        [
            ("Guardar a resposta numa variável e testar ela depois com um if", True,
             "Isso. A escolha vira um valor guardado, e o if consulta esse valor quando for preciso."),
            ("Só escrever as opções no menu e seguir em frente", False,
             "Não. Sem guardar nada, o jogo esquece o que foi escolhido assim que o menu fecha."),
            ("Repetir o menu toda vez que precisar da resposta", False,
             "Não. Isso obriga o jogador a decidir de novo a mesma coisa - a resposta antiga continua perdida."),
        ])

    if not _return:
        jump game_over

    menu:
        "Pra quem ele liga primeiro?"

        "Pra secretaria do CEFET.":
            $ primeira_ligacao = "escola"
            d "Alô, boa tarde. Eu queria saber de uma aluna do técnico de automação."

        "Pra casa dela.":
            $ primeira_ligacao = "casa"
            d "Alô? ...Alô?"
            "A ligação caiu antes da segunda palavra. Nas outras vezes, deu ocupado."

        "Pra Lucy.":
            $ primeira_ligacao = "lucy"
            l "Ai, Daniel, deixa isso pra lá. Ela sumiu porque quis sumir."


# ---- FASE 9 — tutorial_input (escrita) -------------------------
label cap2_fase9:

    "Sobrou a internet do laboratório, quinze minutos por aluno, e uma caixa de busca piscando."

    $ reset_example()
    call tutorial_input

    call fase_escrita(
        "Faz o jogo perguntar e guardar na variável busca. A pergunta, entre aspas, é exatamente: Nome:",
        [
            "busca = renpy.input('Nome:')",
            "$ busca = renpy.input('Nome:')",
        ],
        "Ainda não. É o nome da variável, o sinal de igual, e renpy.input com a pergunta entre aspas.",
        "Antes: pra perguntar alguma coisa ao jogador e guardar o que ele digitar, usa renpy.input com a pergunta entre aspas, e põe o resultado numa variável. Guardando numa variável chamada cidade, ficaria: cidade = renpy.input('Cidade:')",
        "Escreva a busca:")

    if not _return:
        jump game_over

    $ busca = renpy.input("Quem você está procurando?", default="Mirela").strip()
    $ busca = busca or "Mirela"

    d "[busca]. Só isso. Nem sobrenome completo eu sabia direito."

    "Nenhum resultado. Duas páginas de nomes parecidos, nenhum deles ela."


# ---- FASE 10 — tutorial_video (escolha) ------------------------
label cap2_fase10:

    "No fundo da gaveta, uma fita que alguém tinha gravado na festa de junho."

    $ reset_example()
    call tutorial_video

    call fase_escolha(
        "Ele quer que a gravação tome a tela inteira e só devolva o controle quando acabar. O que serve?",
        [
            ("Uma cutscene de vídeo, que roda o arquivo e depois continua a história", True,
             "Isso. O vídeo ocupa tudo, roda até o fim, e a cena segue de onde parou."),
            ("Uma imagem parada do primeiro quadro", False,
             "Não. Uma foto não devolve a voz dela nem o movimento - e é justamente isso que ele foi procurar ali."),
            ("Um som tocando no canal de música", False,
             "Não. O som sozinho deixaria a tela vazia; ele quer ver a festa de novo."),
        ])

    if not _return:
        jump game_over

    "Doze segundos de câmera tremida: a Lucy rindo perto da caixa de som, ele de costas, e num canto do quadro, por menos de um segundo, ela."

    d "É só isso que sobrou. Doze segundos, e ela aparece em um."


# ---- FASE 11 — tutorial_nvlmode (debug) ------------------------
label cap2_fase11:

    "A carta da direção chegou num envelope pardo, com o timbre do colégio no canto."

    $ reset_example()
    call tutorial_nvlmode

    call fase_debug(
        "O COMUNICADO — a tela não limpa entre um bloco e outro",
        [
            "nvl",
            "\"A direção informa que entrou em contato com os responsáveis.\"",
        ],
        "A primeira linha está incompleta. Escreve ela inteira.",
        [
            "nvl clear",
        ],
        "Ainda não. É a palavra nvl seguida do comando que esvazia a tela.",
        "Antes: no modo de tela cheia, o texto vai se acumulando um embaixo do outro até alguém mandar limpar. Quem limpa é a palavra nvl seguida de clear.")

    if not _return:
        jump game_over

    scene black
    with dissolve

    "A direção informa que entrou em contato com os responsáveis pela aluna."

    "A família solicitou que não sejam feitas novas tentativas de contato."

    "A aluna foi desligada do colégio a pedido dos responsáveis."

    "Não há mais informações a prestar."

    d "\"Não há mais informações a prestar.\""

    d "E acabou aí. Eu não tinha mais pra onde ligar, não tinha mais quem perguntar."


# ---- FASE 12 — director (escolha) ------------------------------
label cap2_fase12:

    "A vida se reorganizou sozinha, do jeito que as coisas se reorganizam quando ninguém está segurando elas."

    $ reset_example()
    call director

    call fase_escolha(
        "A cena da vida dele mudou de elenco sem ele decidir nada. No Ren'Py, o que decide quem está em cena?",
        [
            ("Mostrar e esconder imagens, trocando quem ocupa a tela", True,
             "Isso. Quem entra, quem sai e quem fica é decidido uma linha por vez - inclusive quando ninguém repara."),
            ("Mudar a cor do nome dos personagens", False,
             "Não. Isso muda a aparência da fala, não quem está presente na cena."),
            ("Aumentar o volume da música", False,
             "Não. O som acompanha a cena, mas não decide quem está nela."),
        ])

    if not _return:
        jump game_over

    show lucy happy at center
    with dissolve

    l "Você ainda pensa nisso, né?"

    d "Todo dia um pouco menos."

    l "Então tá funcionando."

    "Eles começaram a namorar em outubro. A Lucy achava graça do assunto, e com o tempo ele parou de puxar."


# ---- FASE 13 — distribute (escrita) ----------------------------
label cap2_fase13:

    hide lucy
    with dissolve

    "A música ficou pronta num sábado de madrugada, com a mesma corda desafinada de sempre."

    $ reset_example()
    call distribute

    call fase_escrita(
        "Antes de gravar a dele, para a música que está tocando com dois segundos de fade.",
        [
            "stop music fadeout 2",
            "stop music fadeout 2.0",
        ],
        "Ainda não. É stop, o canal music, a palavra fadeout, e o número de segundos.",
        "Antes: pra parar o som devagar em vez de cortar seco, usa stop, o canal, e fadeout com o número de segundos. Com um segundo ficaria: stop music fadeout 1",
        "Pare a música:")

    if not _return:
        jump game_over

    stop music fadeout 2

    d "Pronto. Existe."

    d "Não sei onde ela tá, não sei se um dia ela escuta. Mas agora existe uma música que é dela."

    scene black
    with dissolve

    centered "{size=+8}Fim do Capítulo 2{/size}"

    jump cap3_checkpoint
