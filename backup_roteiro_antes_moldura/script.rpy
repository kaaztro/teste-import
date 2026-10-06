################################################################
# MIHRAGE — ponto de entrada
# ==========================================
# Este arquivo só dá a partida. O jogo está dividido assim:
#
#   mihrage_motor.rpy  -> personagens, vidas, checkpoints, game over
#                         e as três dinâmicas de fase (escolha,
#                         escrita, debug)
#   mihrage_cap1.rpy   -> Capítulo 1 (Mirela, CEFET 2014) - fases 1 a 6
#   mihrage_cap2.rpy   -> Capítulo 2 (Daniel, ainda 2014) - fases 7 a 13
#   mihrage_cap3.rpy   -> Capítulo 3 (dez anos depois)    - fases 14 a 26
#
# Os arquivos tutorial_*.rpy e indepth_*.rpy são do tutorial original
# do Ren'Py e não foram alterados - cada fase chama o label deles.
################################################################

label start:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "cap1_checkpoint"

    jump cap1_checkpoint
