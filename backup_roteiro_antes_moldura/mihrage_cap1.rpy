################################################################
# MIHRAGE — CAPÍTULO 1
# Mirela, CEFET 2014 — fases 1 a 6
# ==========================================
# Conceito: a Mirela está RECONSTRUINDO a própria memória. A tela
# começa vazia porque nada foi montado ainda, e cada ponto do
# tutorial é a técnica que ela precisa lembrar pra trazer de volta
# mais um pedaço.
#
#   Fase 1  tutorial_playing            escolha
#   Fase 2  tutorial_create             debug
#   Fase 3  tutorial_dialogue           escrita
#   Fase 4  tutorial_images             escolha
#   Fase 5  tutorial_simple_positions   escrita
#   Fase 6  tutorial_transitions        debug
################################################################

label cap1_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "cap1_checkpoint"
    $ e.name = _("Mirela")

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 1{/size}\nMirela — CEFET, 2014"

    scene black
    with dissolve

    "Escuro. Não o escuro de quem fechou os olhos: o escuro de um lugar que ainda não existe."

    show screen reconstruindo

    mi "CEFET, 2014. É só isso que veio até agora: o ano e o nome do lugar."

    mi "O resto sumiu. Mas sumir não é a mesma coisa que nunca ter existido."

    mi "Se eu quiser isso de volta, vou ter que montar tudo de novo, do zero. E eu lembro como se monta."

    hide screen reconstruindo


# ---- FASE 1 — tutorial_playing (múltipla escolha) ---------------
label cap1_fase1:

    show screen reconstruindo
    mi "Primeiro as regras. O que é que eu posso fazer aqui dentro?"
    hide screen reconstruindo

    $ reset_example()
    call tutorial_playing

    call fase_escolha(
        "De tudo isso, ela precisa de uma coisa só: o poder de voltar atrás quando errar a lembrança. Qual recurso faz isso?",
        [
            ("Rollback - volta pra tela anterior e permite escolher diferente", True,
             "Isso. Voltar atrás é a única ferramenta que ela vai usar em todas as fases."),
            ("Skip - pula o texto que já foi lido", False,
             "Não. Pular só acelera o que ela já recuperou; não devolve nada perdido."),
            ("Auto - avança sozinho sem clique", False,
             "Não. Isso só tira a mão dela do volante - ela continua sem poder corrigir nada."),
        ])

    if not _return:
        jump game_over

    show screen reconstruindo
    mi "Dá pra voltar atrás. Isso vai ser útil: eu erro muito quando tento lembrar."
    hide screen reconstruindo


# ---- FASE 2 — tutorial_create (debug) --------------------------
label cap1_fase2:

    show screen reconstruindo
    mi "E antes de qualquer coisa, precisa existir um lugar vazio onde isso tudo vai caber. Um projeto novo."
    hide screen reconstruindo

    $ reset_example()
    call tutorial_create

    show screen reconstruindo
    mi "O espaço existe. Agora ele precisa de um ponto de partida - o lugar onde a história começa a rodar."
    hide screen reconstruindo

    call fase_debug(
        "PONTO DE PARTIDA — algo está errado",
        [
            "label start",
            "    \"CEFET, 2014.\"",
        ],
        "A primeira linha está incompleta. Escreve ela do jeito certo.",
        ["label start:"],
        "Quase. O nome está certo, falta só o dois-pontos no fim da linha.",
        "Antes: um bloco de roteiro sempre abre com a palavra label, o nome dele, e dois-pontos no fim da linha. É o dois-pontos que diz 'tudo que estiver indentado embaixo pertence a mim'. Um bloco chamado memoria ficaria: label memoria:")

    if not _return:
        jump game_over

    show screen reconstruindo
    mi "Pronto. Existe um espaço, e existe um começo. Vazio, mas existe."
    hide screen reconstruindo


# ---- FASE 3 — tutorial_dialogue (escrita) ----------------------
label cap1_fase3:

    show screen reconstruindo

    mi "A primeira coisa que volta nunca é a imagem. É a voz."

    mi "Uma frase sozinha, sem nome na frente, é a própria cena contando. Com um nome na frente, é uma pessoa falando alto, pra quem quiser ouvir."

    hide screen reconstruindo

    "Tá escuro demais aqui dentro."

    show screen reconstruindo

    mi "Essa fui eu. Sem nome na frente, porque eu ainda não me montei."

    mi "Agora ela. E ela merece mais que uma frase solta."

    hide screen reconstruindo

    $ reset_example()
    call tutorial_dialogue

    call fase_escrita(
        "Agora faz isso pra Lucy: apelido l, nome Lucy.",
        [
            "define l = Character('Lucy')",
            "define l = Character('lucy')",
        ],
        "Ainda não. A ordem é: define, o apelido, o sinal de igual, e Character com o nome entre aspas.",
        "Antes: definir uma personagem é escrever define, um apelido curto pra usar depois, o sinal de igual, e Character com o nome entre aspas. Pra uma personagem chamada Ana, com apelido a, ficaria: define a = Character('Ana')",
        "Defina a personagem:")

    if not _return:
        jump game_over

    l "Cadê você? Some daí, Mirela."

    show screen reconstruindo
    mi "A voz dela. Primeiro a voz."
    hide screen reconstruindo


# ---- FASE 4 — tutorial_images (escolha) ------------------------
label cap1_fase4:

    show screen reconstruindo
    mi "Voz eu já tenho. Falta o lugar, e falta o rosto."
    hide screen reconstruindo

    $ reset_example()
    call tutorial_images

    call fase_escolha(
        "Ela quer trocar tudo que está na tela pelo pátio da festa, e só depois trazer a Lucy por cima. Qual é a ordem certa?",
        [
            ("scene bg whitehouse, e depois show lucy happy", True,
             "Isso. scene limpa e põe o fundo; show acrescenta por cima sem apagar nada."),
            ("show bg whitehouse, e depois show lucy happy", False,
             "Não. show não limpa o que estava antes - o escuro continuaria embaixo de tudo."),
            ("scene bg whitehouse, e depois scene lucy happy", False,
             "Não. O segundo scene limparia o pátio inteiro pra pôr só a Lucy no vazio."),
        ])

    if not _return:
        jump game_over

    scene bg whitehouse
    with dissolve

    "A festa. Aquela festa boba no meio do semestre, com a caixa de som alta demais pro tamanho do pátio."

    show lucy happy
    with dissolve

    l "Demorou, hein. Achei que tinha me largado sozinha aqui."

    "O rosto da Lucy. Inteiro, do jeito que era."

    show exclamation at truecenter behind lucy
    with vpunch

    "Atrás dela, no muro, um risco antigo de tinta que já estava ali muito antes da turma delas."

    hide exclamation
    with dissolve

    show lucy happy as daniel at right, silhueta_pessoa
    with dissolve

    d "Vocês duas cochichando de novo. Um dia eu ainda descubro o que é engraçado."

    l "Nesse dia a gente para de rir, Daniel."

    show screen reconstruindo

    mi "O Daniel eu não consigo montar."

    mi "Sei o tamanho dele, sei de que lado ele ficava, sei o jeito de falar. O rosto não vem. Faz dez anos que não vem."

    mi "Fica o contorno, então. É mais do que nada."

    hide screen reconstruindo


# ---- FASE 5 — tutorial_simple_positions (escrita) --------------
label cap1_fase5:

    show screen reconstruindo
    mi "E não era assim que a gente ficava. A Lucy no meio da tela, eu em lugar nenhum. Tá errado."
    hide screen reconstruindo

    $ reset_example()
    call tutorial_simple_positions

    call fase_escrita(
        "Põe ela em cena à esquerda: a imagem é eileen happy, a posição é left.",
        [
            "show eileen happy at left",
        ],
        "Ainda não. A ordem é: show, o nome da imagem com as duas partes, a palavra at, e o nome da posição.",
        "Antes: pra colocar uma imagem numa posição, escreve show, o nome da imagem, a palavra at, e a posição. As prontas são left, center e right. Por exemplo: show lucy mad at center",
        "Posicione a Mirela:")

    if not _return:
        jump game_over

    show eileen happy at left
    show lucy happy at center
    with move

    "Os três nos lugares de sempre, quase por costume: ela de um lado, a Lucy no meio, o Daniel do outro."

    show screen reconstruindo

    mi "Aqui. Era exatamente aqui que eu ficava."

    mi "E as posições grudam: se eu trocar a imagem de alguém sem dizer a posição de novo, a pessoa fica onde estava."

    hide screen reconstruindo

    show eileen vhappy at left

    "A noite foi esfriando. A caixa de som baixou sozinha, e o pátio começou a esvaziar."

    e "Vem comigo. Eu quero te mostrar uma coisa lá em cima."

    d "Lá em cima? Agora? Tá bom, mas se eu cair rolando a culpa é sua, viu."

    l "Vão lá. Eu fico aqui vendo as bolsas de vocês, como sempre."

    hide lucy
    with dissolve


# ---- FASE 6 — tutorial_transitions (debug) ---------------------
label cap1_fase6:

    show screen reconstruindo

    mi "Agora o morro. E é aqui que eu sempre erro."

    mi "Do jeito que eu monto, um lugar vira o outro de estalo, sem nada no meio. Não foi assim: teve caminho, teve subida, teve o tempo que a gente levou."

    hide screen reconstruindo

    $ reset_example()
    call tutorial_transitions

    call fase_debug(
        "A SUBIDA — o corte está seco demais",
        [
            "scene bg washington",
            "show eileen happy",
            "with",
        ],
        "A última linha está pela metade. Escreve ela inteira, usando a dissolve.",
        [
            "with dissolve",
        ],
        "Ainda não. É a palavra with seguida do nome da transição, nada mais.",
        "Antes: depois de trocar a cena, uma linha com a palavra with e o nome de uma transição faz a passagem ser suave em vez de um corte seco. Com a fade, por exemplo, ficaria: with fade")

    if not _return:
        jump game_over

    scene bg washington
    show eileen happy
    show lucy happy as daniel at right, silhueta_pessoa
    with slowdissolve

    "O barulho da festa foi ficando pra trás aos poucos, abafado pelo mato, até sobrar só o vento e as luzes da cidade lá embaixo."

    e "Daniel."

    d "Oi."

    "Ela tinha uma frase guardada fazia semanas. Tinha ensaiado no ônibus, no banho, na fila do bandejão."

    show screen reconstruindo

    mi "É aqui."

    mi "Eu montei o lugar. Montei a noite, o vento, ele do meu lado. Montei tudo."

    mi "E essa parte não tem comando nenhum. O que eu não falei naquele dia não tem como fazer aparecer."

    hide screen reconstruindo

    e "...Deixa pra lá. Vamos descer."

    d "Tem certeza? A gente subiu até aqui só pra isso?"

    e "Tenho certeza. Foi bobagem minha."

    "E desceram. Sem que nada tivesse sido dito."

    scene black
    with slowdissolve

    "Foi a última vez que alguém do CEFET viu Mirela."

    "Ela não voltou pras aulas na semana seguinte. Nem na outra. Nem nunca."

    centered "{size=+8}Fim do Capítulo 1{/size}"

    jump cap2_checkpoint
