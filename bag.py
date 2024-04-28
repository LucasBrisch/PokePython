import utils
import batalhasv2 as b
import CompiladorJogo as cj

player_bag = []
def receber_item ():
    global player_bag, obj
    if obj in player_bag:
        utils.delay_print (f'Você já tem um {obj} na sua mochila... \n Você deixou {obj} para trás e voltou para casa...')
        cj.menu()
    else:
     player_bag.append(obj)
     utils.delay_print (f'O/A {obj} foi adicionado a sua mochila!\nVocê volta para casa com seu novo item')
     cj.menu()
    
def mochila ():
    utils.delay_print('Esses são os itens na sua mochila:')
    for i in range(len(utils.mochila)):
        utils.delay_print(f"{i+1} - {utils.mochila[i]}")
    utils.delay_print('Gostaria de usar algum deles? S/N')
    escolha = input().capitalize()
    while escolha not in ["Sim", "Nao", "N", "S"]:
        utils.delay_print("Desculpe, não entendi, gostaria de usal aguns dos seus itens? S/N")
        escolha = input().capitalize()
    if escolha in ["Sim,", "S"]:
        for i in range(len(player_bag)):
            utils.delay_print(f"{i+1} - {player_bag[i]}")
        escolha = int(input())
        if escolha == 1:
            item_escolhido = player_bag #nao sei como fazer termino o sistema de escolha depois
