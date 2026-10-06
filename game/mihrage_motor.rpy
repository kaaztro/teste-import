################################################################
# MIHRAGE — MOTOR
# ==========================================
# Personagens, imagens, estado de jogo (vidas/checkpoints), HUD,
# caderno, a moldura dos módulos e as três dinâmicas de fase.
# Nada de narrativa aqui: a história fica em mihrage_cap1.rpy,
# mihrage_cap2.rpy e mihrage_cap3.rpy.
#
# MOLDURA DA HISTÓRIA
# O jogo inteiro é a conversa de Daniel e Mirela no reencontro, em
# 2024, no coquetel de um congresso. O prólogo mostra o momento em que
# ele a reconhece; os capítulos 1 e 2 são os dois montando o passado
# juntos; o capítulo 3 alcança o prólogo e segue até o fim da conversa.
#
#   fala normal   -> a cena sendo montada (2014, ou hoje cedo)
#   fala itálica  -> os dois conversando AGORA, no canto do saguão
################################################################


# ==========================================
# 1. PERSONAGENS
# ==========================================

# A guia dos módulos (o tutorial original do Ren'Py fala por `e`).
# Ela NÃO é a Mirela: a protagonista usa `m`.
define e = Character(_("Eileen"), color="#c8ffc8")

# `l` (Lucy) já vem definida em tutorial_quickstart.rpy.

# O nome dela muda ao longo do jogo ("???" -> "Mirela" -> "Mihlena").
# Fica numa variável `default` pra entrar no save e no rollback.
default nome_dela = "Mirela"
define NOME_NOVO = "Mihlena"

define m = Character("[nome_dela]", color="#c8ffc8")
define d = Character("Daniel", color="#a3c9ff")

# As vozes de AGORA: os dois contando um pro outro, em itálico.
define mh = Character("[nome_dela]", who_color="#ffe08a",
                      what_color="#ffe08a", what_italic=True)
define dh = Character("Daniel", who_color="#a3c9ff",
                      what_color="#cfe2ff", what_italic=True)

# A voz do jogo (módulos, falhas, vidas).
define sistema = Character("SISTEMA", who_color="#ff6b6b", what_color="#ffb3b3")


# ==========================================
# 2. IMAGENS (placeholders do tutorial)
# ==========================================
# Quando a arte final chegar, basta trocar o arquivo à direita.

image bg patio = "bg whitehouse.jpg"
image bg morro = "bg washington.jpg"
image bg quarto = "bg washington.jpg"
image bg aeroporto = "bg washington.jpg"
image bg congresso = "bg whitehouse.jpg"

image mirela happy = "eileen happy.png"
image mirela vhappy = "eileen vhappy.png"
image mirela concerned = "eileen concerned.png"

# O Daniel de 2014 ela não consegue montar: só o contorno.
image daniel sombra = "lucy happy.png"

image exclamation = "exclamation.png"
image reconstrucao_icone = "logo solid.png"

transform silhueta_pessoa:
    matrixcolor TintMatrix("#000000")

transform icone_canto:
    xalign 1.0
    yalign 0.0
    alpha 0.9


# ==========================================
# 3. ESTADO DE JOGO
# ==========================================

define VIDAS_INICIAIS = 3
define config.default_language = "portuguese"

default vidas = 3
default checkpoint_atual = "prologo"

# Rótulo de tempo no HUD: quando é a cena que está na tela.
default quando = ""

# Módulo em andamento (vai pro caderno junto com a lição).
default modulo_atual = ""
default quando_antes = ""

# Caderno: lista de (módulo, lição) já vistas.
default caderno = []

# Estado narrativo do Capítulo 2 (usado de novo no Capítulo 3).
default primeira_ligacao = ""
default busca = "Mirela"

init python:

    import re

    def normaliza(s):
        """
        Sanitiza o que o jogador digitou SEM mexer em maiúsculas -
        no Ren'Py `L` e `l` são nomes diferentes, e o jogo ensina isso.

        - tira espaços das pontas e colapsa espaços repetidos;
        - aspas duplas e simples contam igual;
        - descarta os prefixos `$ ` e `define `;
        - ignora espaço em volta de = , ( );
        - 2.0 vale o mesmo que 2.
        """
        s = s.strip().replace('"', "'")
        s = " ".join(s.split())

        if s.startswith("$"):
            s = s[1:].strip()

        if s.startswith("define "):
            s = s[len("define "):].strip()

        s = re.sub(r"\s*([=,()])\s*", r"\1", s)
        s = re.sub(r"\b(\d+)\.0+\b", r"\1", s)

        return s

    def confere(resposta, aceitas):
        """
        True se a resposta bate com alguma das formas aceitas.

        Cada forma pode ser:
          "texto"        -> comparado depois de normalizar os dois lados
          "re:padrão"    -> expressão regular sobre a resposta normalizada
          "rei:padrão"   -> idem, sem diferenciar maiúsculas (cores hex)
        """
        r = normaliza(resposta)

        for a in aceitas:
            if a.startswith("re:"):
                if re.fullmatch(a[3:], r):
                    return True
            elif a.startswith("rei:"):
                if re.fullmatch(a[4:], r, re.IGNORECASE):
                    return True
            elif r == normaliza(a):
                return True

        return False

    def anota(licao):
        """Guarda a lição no caderno (uma vez só por módulo+lição)."""
        item = (modulo_atual, licao)
        if licao and item not in caderno:
            caderno.append(item)


# ==========================================
# 4. HUD, CADERNO E TELAS DE APOIO
# ==========================================

screen hud_vidas():
    zorder 50

    hbox:
        xalign 0.01
        yalign 0.02
        spacing 8

        frame:
            background "#000000bb"
            padding (14, 8)
            text "VIDAS: [vidas]/[VIDAS_INICIAIS]" size 18 color "#ff8f8f"

        if quando:
            frame:
                background "#000000bb"
                padding (14, 8)
                text "[quando]" size 18 color "#e6e6e6"

        if caderno:
            textbutton "CADERNO":
                background "#000000bb"
                padding (14, 8)
                text_size 18
                text_color "#ffe08a"
                text_hover_color "#ffffff"
                action Show("caderno_tela")


screen caderno_tela():
    modal True
    zorder 100

    add Solid("#000000cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 600
        background "#f6f1ea"
        padding (36, 28)

        vbox:
            spacing 14
            xfill True

            text "Caderno de anotações" size 30 color "#1f1a24"

            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 440

                vbox:
                    spacing 18
                    xsize 900

                    for titulo, licao in caderno:
                        vbox:
                            spacing 4
                            text titulo size 18 color "#a0522d" bold True
                            text licao size 20 color "#1f1a24"

            textbutton "Fechar":
                xalign 1.0
                text_color "#5f5866"
                text_hover_color "#1f1a24"
                action Hide("caderno_tela")

    key "game_menu" action Hide("caderno_tela")


screen reconstruindo():
    zorder 45

    add "reconstrucao_icone":
        at icone_canto
        xsize 90
        ysize 90


screen trecho_codigo(titulo, linhas):
    zorder 40

    frame:
        xalign 0.5
        ypos 60
        xsize 940
        background "#0d1117ee"
        padding (24, 18)

        vbox:
            spacing 6
            xsize 890

            text titulo size 19 color "#ffcc00"
            text "- - - - - - - - - - - - - - - - - - - -" size 15 color "#586069"

            for linha in linhas:
                text linha size 17 color "#b7f5c0"


# ==========================================
# 5. A MOLDURA DOS MÓDULOS
# ==========================================
# Todo trecho do tutorial oficial entra por aqui: a conversa "pausa",
# o módulo roda, e a tela volta pro preto pra fase remontar a cena.
# `com_menu`: o módulo tem um menu de tópicos - avisa como sair dele.

label modulo(tutorial, numero, titulo, com_menu=False):

    hide screen reconstruindo

    $ quando_antes = quando
    $ quando = "módulo " + str(numero) + "/26"
    $ modulo_atual = "Módulo " + str(numero) + " — " + titulo

    scene black
    with dissolve

    sistema "MÓDULO [numero] — [titulo]"

    if com_menu:
        sistema "Esse módulo tem um menu de tópicos. Vê quantos quiser; a última opção do menu te devolve pra conversa."

    $ reset_example()
    call expression tutorial

    scene black
    with dissolve

    $ quando = quando_antes

    return


# ==========================================
# 6. VIDAS, FALHA E CHECKPOINT
# ==========================================

# Tira uma vida e devolve True se ainda sobrou alguma. Só RETORNA,
# nunca salta - assim a pilha de call fica limpa.
# Bloqueia o rollback: dá pra voltar e reler a conversa, mas não dá
# pra desdizer uma resposta errada.
label perder_vida:

    $ vidas -= 1
    $ renpy.block_rollback()

    if vidas > 0:
        with vpunch
        sistema "A lembrança falhou. Vidas restantes: [vidas]."
        return True

    with vpunch
    sistema "Falha crítica. Nenhuma vida restante."
    return False


label game_over:

    hide screen reconstruindo
    hide screen trecho_codigo
    hide screen caderno_tela

    scene black
    with dissolve

    sistema "A CONVERSA SE PERDEU."

    sistema "Fragmentos demais de uma vez. Os dois precisam voltar um pouco e recomeçar dali."

    $ vidas = VIDAS_INICIAIS

    sistema "Vidas: [vidas]/[VIDAS_INICIAIS]. Voltando pro último ponto estável."

    jump expression checkpoint_atual


# ==========================================
# 7. AS TRÊS DINÂMICAS DE FASE
# ==========================================
# Regra geral: nenhuma fase cobra algo que não tenha sido ensinado
# antes. Quem chama passa `licao` com a regra e o formato, e só
# depois vem a pergunta. Toda lição vai pro caderno.

# --- Dinâmica 1: múltipla escolha -------------------------------
# opcoes: lista de (texto_da_opcao, é_a_correta, feedback)
# A ordem das opções é embaralhada a cada tentativa.
label fase_escolha(pergunta, opcoes, licao=""):

    if licao:
        $ anota(licao)
        sistema "[licao]"

    while True:

        sistema "[pergunta]"

        python:
            _ordem = list(range(len(opcoes)))
            renpy.random.shuffle(_ordem)
            _itens = [(opcoes[i][0], i) for i in _ordem]
            _escolhido = renpy.display_menu(_itens)
            _texto, _acertou, _feedback = opcoes[_escolhido]

        sistema "[_feedback]"

        if _acertou:
            return True

        call perder_vida

        if not _return:
            return False


# --- Dinâmica 2: escrita de código ------------------------------
# aceitas: formas válidas (ver confere: texto, "re:" ou "rei:")
label fase_escrita(instrucao, aceitas, dica, licao="", prompt="Digite o comando:"):

    if licao:
        $ anota(licao)
        sistema "[licao]"

    while True:

        sistema "[instrucao]"

        $ _resposta = renpy.input(prompt, length=160)

        if confere(_resposta, aceitas):
            sistema "Comando aceito."
            return True

        sistema "[dica]"

        call perder_vida

        if not _return:
            return False


# --- Dinâmica 3: correção de código (debug) ---------------------
# O trecho quebrado aparece ANTES da lição e fica visível enquanto o
# jogador corrige.
label fase_debug(titulo, linhas, instrucao, aceitas, dica, licao=""):

    show screen trecho_codigo(titulo, linhas)

    sistema "Tem um trecho quebrado aí em cima. Olha ele com calma."

    if licao:
        $ anota(licao)
        sistema "[licao]"

    while True:

        sistema "[instrucao]"

        $ _resposta = renpy.input("Escreva a linha corrigida:", length=160)

        if confere(_resposta, aceitas):
            sistema "Corrigido."
            hide screen trecho_codigo
            return True

        sistema "[dica]"

        call perder_vida

        if not _return:
            hide screen trecho_codigo
            return False
