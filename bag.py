import utils
import Batalhas as b
import CompiladorJogo as cj

player_bag = []
def receber_item ():
    global player_bag
    if b.item in player_bag:
        utils.delay_print (f'Você já tem um {b.item} na sua mochila... \n Você deixou {b.item} para trás e voltou para casa...')
        cj.menu()
    else:
     player_bag.append(b.item)
     utils.delay_print (f'O/A {b.item} foi adicionado a sua mochila!\n Você volta para casa com seu novo item')
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
