################################################################
# MIHRAGE — ponto de entrada
# ==========================================
# O jogo é a conversa de Daniel e Mirela no reencontro, em 2024.
#
#   mihrage_motor.rpy  -> personagens, vidas, checkpoints, caderno,
#                         moldura dos módulos e as três dinâmicas de
#                         fase (escolha, escrita, debug)
#   mihrage_cap1.rpy   -> Prólogo (o reencontro) + Capítulo 1
#                         "Mihrela": o que ela lembra de 2014 (fases 1-6)
#   mihrage_cap2.rpy   -> Capítulo 2 "Mihrage": o que ele viveu
#                         depois que ela sumiu (fases 7-13)
#   mihrage_cap3.rpy   -> Capítulo 3 "Mihlena": os dez anos, o dia de
#                         hoje e o fim da conversa (fases 14-26)
#
# Os arquivos tutorial_*.rpy e indepth_*.rpy são do tutorial original
# do Ren'Py e não foram alterados - cada fase chama o label deles
# pelo `call modulo(...)`.
################################################################

label start:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "prologo"

    jump prologo
