from random import randint

def rolar_dados(size):
    """retornar um valor aleatorio entre 1 e o size"""
    return randint(1,size)

def values_for_enemy(difficult):
    """retornar random strenght, ability and constitution"""
    #difficult = forca + habilidade + constituicao
    forca = randint(1,difficult-2)
    habilidade = randint(1,(difficult - forca)-1)
    constituicao = difficult - (forca + habilidade)
    return forca, habilidade, constituicao
