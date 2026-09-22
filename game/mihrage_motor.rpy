################################################################
# MIHRAGE — MOTOR
# ==========================================
# Personagens, imagens, estado de jogo (vidas/checkpoints), HUD e as
# três dinâmicas de fase. Nada de narrativa aqui: os capítulos ficam
# em mihrage_cap1.rpy, mihrage_cap2.rpy e mihrage_cap3.rpy.
################################################################


# ==========================================
# 1. PERSONAGENS
# ==========================================

# `e` é a protagonista. Em 2014 ela é Mirela; no Capítulo 3, dez anos
# depois, ela se apresenta como Milena (e.name é trocado lá).
# `l` (Lucy) já vem definido em tutorial_quickstart.rpy.
define e = Character(_('Mirela'), color="#c8ffc8")
define d = Character("Daniel", color="#a3c9ff")

# A voz dela reconstruindo a memória: sem caixa de nome, itálico.
define mi = Character(None, what_color="#ffe08a", what_italic=True)

# A voz do sistema (lições, falhas, vidas, reinicialização).
define sistema = Character("SISTEMA", who_color="#ff6b6b", what_color="#ffb3b3")


# ==========================================
# 2. IMAGENS E TRANSFORMS
# ==========================================

# Arquivos soltos na raiz de game/ precisam de registro explícito.
image exclamation = "exclamation.png"
image reconstrucao_icone = "logo solid.png"

# O rosto que ela não consegue montar: só o contorno.
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

default vidas = 3
default checkpoint_atual = "cap1_checkpoint"

# Estado narrativo do Capítulo 2.
default primeira_ligacao = ""
default busca = "Mirela"

init python:

    def normaliza(s):
        """
        Sanitiza o que o jogador digitou: tira espaços das pontas, põe
        em minúsculo, trata aspas simples e duplas como equivalentes e
        colapsa espaços repetidos.

        Também descarta os prefixos `define ` e `$ `, que são formas
        equivalentes de escrever a mesma atribuição - sem isso,
        `l = Character('Lucy')` era recusado só por não ter o define
        na frente.
        """
        s = s.strip().lower().replace('"', "'")
        s = " ".join(s.split())

        if s.startswith("$"):
            s = s[1:].strip()

        if s.startswith("define "):
            s = s[len("define "):].strip()

        return s

    def confere(resposta, aceitas):
        """
        True se a resposta bate com alguma das formas aceitas. Compara
        duas vezes: normalizada, e também sem espaço nenhum - assim
        `m=Character('x')` e `m = Character("x")` contam como iguais.
        """
        r = normaliza(resposta)
        r_sem_espaco = r.replace(" ", "")

        for a in aceitas:
            a = normaliza(a)
            if r == a or r_sem_espaco == a.replace(" ", ""):
                return True

        return False


# ==========================================
# 4. HUD E TELAS DE APOIO
# ==========================================

screen hud_vidas():
    zorder 50

    frame:
        xalign 0.01
        yalign 0.02
        background "#000000bb"
        padding (14, 8)

        text "VIDAS: [vidas]/3" size 18 color "#ff8f8f"


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
# 5. VIDAS, FALHA E CHECKPOINT
# ==========================================

# Label universal de falha. Tira uma vida e devolve True se ainda
# sobrou alguma, False se zerou (quem chamou decide o que fazer).
# Ele só RETORNA, nunca salta - assim a pilha de call fica limpa.
label perder_vida:

    $ vidas -= 1

    if vidas > 0:
        with vpunch
        sistema "Falha registrada. Vidas restantes: [vidas]."
        return True

    with vpunch
    sistema "Falha crítica. Nenhuma vida restante."
    return False


label game_over:

    hide screen reconstruindo
    hide screen trecho_codigo

    scene black
    with dissolve

    sistema "MEMÓRIA CORROMPIDA."

    sistema "Fragmentos demais perdidos de uma vez. Não dá pra continuar montando a partir daqui."

    centered "{size=+8}REINICIALIZANDO SISTEMA{/size}"

    $ vidas = VIDAS_INICIAIS

    sistema "Estado restaurado. Vidas: [vidas]/3. Voltando pro último ponto estável."

    jump expression checkpoint_atual


# ==========================================
# 6. AS TRÊS DINÂMICAS DE FASE
# ==========================================
# Regra geral: nenhuma fase cobra algo que não tenha sido ensinado
# antes. Quem chama passa `licao` com a regra e o formato, e só
# depois vem a pergunta.

# --- Dinâmica 1: múltipla escolha -------------------------------
# opcoes: lista de (texto_da_opcao, é_a_correta, feedback)
label fase_escolha(pergunta, opcoes, licao=""):

    if licao:
        sistema "[licao]"

    while True:

        sistema "[pergunta]"

        python:
            _itens = [(texto, i) for i, (texto, ok, fb) in enumerate(opcoes)]
            _escolhido = renpy.display_menu(_itens)
            _texto, _acertou, _feedback = opcoes[_escolhido]

        if _acertou:
            sistema "[_feedback]"
            return True

        sistema "[_feedback]"

        call perder_vida

        if not _return:
            return False


# --- Dinâmica 2: escrita de código ------------------------------
# aceitas: lista de formas válidas (comparadas com sanitização)
label fase_escrita(instrucao, aceitas, dica, licao="", prompt="Digite o comando:"):

    if licao:
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
# O trecho quebrado aparece na tela ANTES da lição, e fica visível
# enquanto o jogador corrige.
label fase_debug(titulo, linhas, instrucao, aceitas, dica, licao=""):

    show screen trecho_codigo(titulo, linhas)

    sistema "Tem um trecho quebrado aí em cima. Olha ele com calma."

    if licao:
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
