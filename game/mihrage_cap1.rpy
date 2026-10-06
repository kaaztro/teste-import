################################################################
# MIHRAGE — PRÓLOGO + CAPÍTULO 1
# ==========================================
# Prólogo (2024): o coquetel do congresso, o instante em que o Daniel
# reconhece a Mirela. Eles se sentam num canto do saguão - e o resto
# do jogo é essa conversa.
#
# Capítulo 1 "Mihrela" (fases 1 a 6): ela conta 2014. A memória foi
# apagada à força, então ela RECONSTRÓI a lembrança enquanto fala, e
# cada módulo é a técnica que ela precisa pra trazer mais um pedaço.
# O Daniel, que estava lá, interrompe e completa.
#
#   Fase 1  tutorial_playing            escolha
#   Fase 2  tutorial_create             debug
#   Fase 3  tutorial_dialogue           escrita
#   Fase 4  tutorial_images             escolha   (checkpoint)
#   Fase 5  tutorial_simple_positions   escrita
#   Fase 6  tutorial_transitions        debug
################################################################


# ==========================================
# PRÓLOGO — o reencontro
# ==========================================
label prologo:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "prologo"
    $ nome_dela = "???"
    $ quando = "2024 · agora"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}MIHRAGE{/size}"

    scene bg saguao tarde
    with dissolve

    $ ambiente("coquetel")

    "Congresso de automação e controle, fim do primeiro dia. Coquetel no saguão do hotel: taças de plástico, conversa de crachá."

    show mirela happy at right
    show daniel idle at left
    with dissolve

    m "...e aí o problema nem era o controlador, sabe? Era o encoder. Ninguém tinha olhado o encoder."

    m "Que foi?"

    m "Que foi? Tá branco."

    d "Mirela?"

    "O nome ficou pendurado no ar entre os dois por um tempo bem mais longo que uma palavra."

    show mirela concerned at right

    $ nome_dela = "Mirela"

    m "Faz dez anos que ninguém me chama assim."

    show daniel sad at left

    d "Você sumiu."

    m "Eu sei."

    d "Do nada. Sem tchau, sem nada. A gente ficou..."

    m "Eu sei, Daniel."

    "Ela olhou pro saguão cheio, pro relógio, pra porta. Depois puxou duas cadeiras pro canto, longe da mesa do café."

    show mirela idle at right
    show daniel idle at left

    m "Senta. Se eu for contar, vai ter que ser do começo. Do fim não sai."

    d "Do começo onde?"

    m "Do pátio. Da festa. Eu nem sei se ainda lembro direito."

    sistema "O que você vai jogar a partir daqui é essa conversa."

    sistema "As falas em itálico são os dois conversando agora, nesse canto do saguão. O resto é a lembrança que eles estão montando."

    sistema "Pra montar cada lembrança, você usa o que aprender nos módulos do Ren'Py. Se errar, a lembrança falha e custa uma vida: são três por capítulo."

    sistema "Tudo que você aprender vai pro CADERNO, no canto da tela. Dá pra abrir a qualquer hora, inclusive na hora de responder."

    jump cap1_checkpoint


# ==========================================
# CAPÍTULO 1 — Mihrela
# ==========================================
label cap1_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ ambiente(None)
    $ checkpoint_atual = "cap1_checkpoint"
    $ nome_dela = "Mirela"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 1 — Mihrela{/size}\nCEFET, 2014 · o que ela lembra"

    $ quando = "2014 · lembrança dela"

    scene black
    with dissolve

    "Escuro. Não o escuro de quem fechou os olhos: o escuro de um lugar que ainda não existe."

    show screen reconstruindo

    mh "CEFET, 2014. É só isso que vem: o ano e o nome do lugar."

    mh "O resto eu apaguei. Ou apagaram. Mas apagar não é a mesma coisa que nunca ter existido."

    mh "Se eu quiser te contar, vou ter que montar tudo de novo, do zero. E eu ainda lembro como se monta."

    dh "Eu ajudo. Eu tava lá."

    hide screen reconstruindo


# ---- FASE 1 — tutorial_playing (múltipla escolha) ---------------
label cap1_fase1:

    mh "Primeiro as regras. Numa conversa dessas, o que é que dá pra fazer?"

    call modulo("tutorial_playing", 1, "Jogando")

    call fase_escolha(
        "De tudo isso, uma coisa ela vai querer o tempo inteiro: voltar e ouvir de novo o que acabou de passar. Qual recurso faz isso?",
        [
            ("Rollback - volta pras falas anteriores", True,
             "Isso. O rollback deixa reler o que já passou. Só não desfaz uma falha: o que deu errado fica registrado."),
            ("Skip - pula o texto que já foi lido", False,
             "Não. Pular só acelera o que já foi dito; não traz nada de volta."),
            ("Auto - avança sozinho sem clique", False,
             "Não. Isso só tira a mão dela do volante - não volta pra lugar nenhum."),
        ])

    if not _return:
        jump game_over

    show screen reconstruindo
    mh "Dá pra voltar e ouvir de novo. Desdizer é que não dá."
    dh "Isso vale pra muita coisa."
    hide screen reconstruindo


# ---- FASE 2 — tutorial_create (debug) --------------------------
label cap1_fase2:

    show screen reconstruindo
    mh "Antes de qualquer coisa, precisa existir um lugar vazio onde isso tudo vai caber. Um projeto novo."
    hide screen reconstruindo

    call modulo("tutorial_create", 2, "Criando um projeto")

    show screen reconstruindo
    mh "O espaço existe. Agora precisa de um ponto de partida - o lugar onde a história começa a rodar."
    dh "E onde começa?"
    mh "Onde tudo começa. No start."
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
    mh "Pronto. Existe um espaço, e existe um começo. Vazio, mas existe."
    hide screen reconstruindo


# ---- FASE 3 — tutorial_dialogue (escrita) ----------------------
label cap1_fase3:

    show screen reconstruindo

    mh "A primeira coisa que volta nunca é a imagem. É a voz."

    mh "Uma frase sozinha, sem nome na frente, é a própria cena contando. Com um nome na frente, é uma pessoa falando."

    hide screen reconstruindo

    "Tá escuro demais aqui dentro."

    show screen reconstruindo

    mh "Essa fui eu, naquela noite. Sem nome na frente, porque eu ainda não me montei."

    mh "Agora ela. A Lucy."

    mh "Minha dupla desde o primeiro ano. Sentava do meu lado em todas as aulas, copiava meu caderno e me devolvia com desenho na margem."

    mh "Foi ela que inventou o Mih."

    mh "E foi a única pessoa que soube o que eu ia te falar lá em cima."

    dh "...A Lucy sabia?"

    mh "Depois. Deixa eu montar ela primeiro."

    mh "Ela merece mais que uma frase solta. Ela merece um nome."

    hide screen reconstruindo

    call modulo("tutorial_dialogue", 3, "Escrevendo diálogo")

    call fase_escrita(
        "Agora faz isso pra Lucy: apelido l, nome Lucy.",
        [
            "l = Character('Lucy')",
            "l = Character(_('Lucy'))",
            "re:l=Character\\((_\\()?'Lucy'(\\))?,.+\\)",
        ],
        "Ainda não. A ordem é: define, o apelido (l minúsculo), o sinal de igual, e Character com o nome entre aspas.",
        "Antes: definir uma personagem é escrever define, um apelido curto pra usar depois, o sinal de igual, e Character com o nome entre aspas. Maiúscula e minúscula contam: A e a são apelidos diferentes. Pra uma personagem chamada Ana, com apelido a, ficaria: define a = Character('Ana')",
        "Defina a personagem:")

    if not _return:
        jump game_over

    l "Cadê você, Mih? Some daí, não."

    show screen reconstruindo
    mh "A voz dela. Primeiro a voz."
    dh "\"Mih.\" Fazia anos que eu não ouvia ninguém te chamar assim."
    mh "Só ela chamava assim. Pra todo o resto do CEFET eu era Mirela."
    hide screen reconstruindo


# ---- FASE 4 — tutorial_images (escolha) ------------------------
label cap1_fase4:

    $ checkpoint_atual = "cap1_fase4"
    $ quando = "2014 · lembrança dela"

    scene black

    show screen reconstruindo
    mh "Voz eu já tenho. Falta o lugar, e falta o rosto."
    hide screen reconstruindo

    call modulo("tutorial_images", 4, "Imagens")

    call fase_escolha(
        "Ela quer trocar tudo que está na tela pelo pátio da festa (bg patio), e só depois trazer a Lucy por cima (lucy happy). Qual é a ordem certa?",
        [
            ("scene bg patio, e depois show lucy happy", True,
             "Isso. scene limpa e põe o fundo; show acrescenta por cima sem apagar nada."),
            ("show bg patio, e depois show lucy happy", False,
             "Não. show não limpa o que estava antes - o escuro continuaria embaixo de tudo."),
            ("scene bg patio, e depois scene lucy happy", False,
             "Não. O segundo scene limparia o pátio inteiro pra pôr só a Lucy no vazio."),
        ])

    if not _return:
        jump game_over

    scene bg patio
    with dissolve

    $ ambiente("festa")

    "A festa. Aquela festa boba no meio do semestre, com a caixa de som alta demais pro tamanho do pátio."

    show lucy happy
    with dissolve

    l "Demorou, hein. Achei que tinha me largado sozinha aqui."

    mh "Ela vivia dizendo isso. Que um dia eu ia largar ela sozinha."

    dh "..."

    "O rosto da Lucy. Inteiro, do jeito que era."

    show exclamation at truecenter behind lucy
    with vpunch

    "Atrás dela, no muro, um risco antigo de tinta que já estava ali muito antes da turma delas."

    hide exclamation
    with dissolve

    show daniel sombra at right, silhueta_pessoa
    with dissolve

    d "Vocês duas cochichando de novo. Um dia eu ainda descubro o que é engraçado."

    l "Nesse dia a gente para de rir, Daniel."

    show screen reconstruindo

    mh "Você eu não consigo montar."

    mh "Sei o tamanho, sei de que lado você ficava, sei o jeito de falar. O rosto de 2014 não vem."

    mh "Você tá bem aqui na minha frente, e o único rosto que vem é o de agora."

    dh "Melhor assim. Eu tinha um bigodinho horrível."

    mh "Fica o contorno, então. É mais do que nada."

    hide screen reconstruindo


# ---- FASE 5 — tutorial_simple_positions (escrita) --------------
label cap1_fase5:

    show screen reconstruindo
    mh "E não era assim que a gente ficava. A Lucy no meio, eu em lugar nenhum. Tá errado."
    hide screen reconstruindo

    call modulo("tutorial_simple_positions", 5, "Posições simples")

    call fase_escrita(
        "Põe ela em cena à esquerda: a imagem é mirela happy, a posição é left.",
        [
            "show mirela happy at left",
            "re:show mirela happy at left with \\w+",
        ],
        "Ainda não. A ordem é: show, o nome da imagem com as duas partes, a palavra at, e o nome da posição.",
        "Antes: pra colocar uma imagem numa posição, escreve show, o nome da imagem, a palavra at, e a posição. As prontas são left, center e right. Por exemplo: show lucy mad at center",
        "Posicione a Mirela:")

    if not _return:
        jump game_over

    scene bg patio
    show daniel sombra at right, silhueta_pessoa
    show mirela happy at left
    show lucy happy at center
    with move

    "Os três nos lugares de sempre, quase por costume: ela de um lado, a Lucy no meio, o Daniel do outro."

    show screen reconstruindo

    mh "Aqui. Era exatamente aqui que eu ficava."

    mh "E as posições grudam: se eu trocar a imagem de alguém sem dizer a posição de novo, a pessoa fica onde estava."

    hide screen reconstruindo

    show mirela vhappy at left

    "A noite foi esfriando. A caixa de som baixou sozinha, e o pátio começou a esvaziar."

    m "Vem comigo. Eu quero te mostrar uma coisa lá em cima."

    d "Lá em cima? Agora? Tá bom, mas se eu cair rolando a culpa é sua, viu."

    l "Vão lá. Eu fico aqui vendo as bolsas de vocês, como sempre."

    "A Lucy piscou pra ela quando o Daniel virou de costas. Só pra ela."

    dh "Ela piscou pra você?"

    mh "Você não perdia uma, né. Só perdia as importantes."

    hide lucy
    with dissolve

    dh "Eu lembro disso. Eu achei que você ia me mostrar o vira-lata que morava lá em cima."

    mh "O Parafuso."

    dh "O Parafuso! Meu Deus."


# ---- FASE 6 — tutorial_transitions (debug) ---------------------
label cap1_fase6:

    show screen reconstruindo

    mh "Agora o morro. E é aqui que eu sempre erro."

    mh "Do jeito que eu monto, um lugar vira o outro de estalo, sem nada no meio. Não foi assim: teve caminho, teve subida, teve o tempo que a gente levou."

    hide screen reconstruindo

    call modulo("tutorial_transitions", 6, "Transições")

    call fase_debug(
        "A SUBIDA — o corte está seco demais",
        [
            "scene bg trilha",
            "show mirela happy",
            "with",
        ],
        "A última linha está pela metade. Escreve ela inteira, usando a dissolve.",
        [
            "with dissolve",
            "re:with Dissolve\\(\\d+(\\.\\d+)?\\)",
        ],
        "Ainda não. É a palavra with seguida do nome da transição, nada mais.",
        "Antes: depois de trocar a cena, uma linha com a palavra with e o nome de uma transição faz a passagem ser suave em vez de um corte seco. Com a fade, por exemplo, ficaria: with fade")

    if not _return:
        jump game_over

    scene bg trilha
    show mirela happy
    show daniel sombra at right, silhueta_pessoa
    with slowdissolve

    $ ambiente("morro")

    "O barulho da festa foi ficando pra trás aos poucos, abafado pelo mato, até sobrar só o vento e as luzes da cidade lá embaixo."

    scene bg morro
    show mirela happy
    show daniel sombra at right, silhueta_pessoa
    with dissolve

    m "Daniel."

    d "Oi."

    scene cg morro
    with dissolve

    "Ela tinha uma frase guardada fazia semanas. Tinha ensaiado no ônibus, no banho, na fila do bandejão. Tinha ensaiado com a Lucy."

    show screen reconstruindo

    mh "É aqui."

    mh "Eu montei o lugar. Montei a noite, o vento, você do meu lado. Montei tudo."

    mh "E essa parte não tem comando nenhum. O que eu não falei naquele dia não tem como fazer aparecer."

    hide screen reconstruindo

    scene bg morro
    show mirela concerned
    show daniel sombra at right, silhueta_pessoa
    with dissolve

    m "...Deixa pra lá. Vamos descer."

    d "Tem certeza? A gente subiu até aqui só pra isso?"

    m "Tenho certeza. Foi bobagem minha."

    "E desceram. Sem que nada tivesse sido dito."

    dh "Eu passei dez anos tentando adivinhar o que era."

    mh "Eu sei. Calma. Eu chego lá."

    scene black
    with slowdissolve

    "Foi a última vez que alguém do CEFET viu Mirela."

    "Ela não voltou pras aulas na semana seguinte. Nem na outra. Nem nunca."

    $ quando = "2024 · agora"

    scene bg saguao tarde
    show mirela sad at right
    show daniel sad at left
    with dissolve

    $ ambiente("coquetel")

    mh "Daqui pra frente eu não sei nada. Eu não tava lá."

    mh "Me conta você. O que aconteceu depois que eu sumi?"

    centered "{size=+8}Fim do Capítulo 1{/size}"

    jump cap2_checkpoint
