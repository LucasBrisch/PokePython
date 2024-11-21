import Pokemons as p
import utils as u
import CompiladorJogo as cp
import bag as b

def PokeShop ():
    u.delay_print("Bem-vindo à loja de itens!\n")
    u.delay_print("O que deseja comprar?\n")
    u.delay_print(f"seu saldo é de:  {u.dinheiro}\n")
    u.delay_print(f"1. Potion - {p.Potion.preco}\n")
    u.delay_print(f"2. Super Potion - {p.Super_Potion.preco}\n")
    u.delay_print(f"3. Hyper Potion - {p.Hyper_Potion.preco}\n")
    u.delay_print(f"4. Revive - {p.Revive.preco}\n")
    u.delay_print("5. Voltar\n")
    choice = int(input())
    
    if choice == 1:
        if u.dinheiro >= p.Potion.preco:
            u.delay_print("Quantas poções deseja comprar?\n")
            qtd = int(input())
            if u.dinheiro >= p.Potion.preco * qtd:
                u.dinheiro -= p.Potion.preco * qtd
                p.Potion.qtd += qtd
                u.delay_print(f"Você comprou {qtd} poções!\n")
                if p.Potion in b.player_bag:
                    p.Potion.qtd += qtd
                else:
                    b.player_bag.append(p.Potion)
                    p.Potion.qtd += qtd
                PokeShop()
            else:
                u.delay_print("Você não tem dinheiro suficiente!\n")
                PokeShop()
        else:
            u.delay_print("Você não tem dinheiro suficiente!\n")
            PokeShop()
    elif choice == 2:
        if u.dinheiro >= p.Super_Potion.preco:
            u.delay_print("Quantas poções deseja comprar?\n")
            qtd = int(input())
            if u.dinheiro >= p.Super_Potion.preco * qtd:
                u.dinheiro -= p.Super_Potion.preco * qtd
                p.Super_Potion.qtd += qtd
                u.delay_print(f"Você comprou {qtd} poções!\n")
                if p.Super_Potion in b.player_bag:
                    p.Super_Potion.qtd += qtd
                else:
                    b.player_bag.append(p.Super_Potion)
                    p.Potion.qtd += qtd
                PokeShop()
            else:
                u.delay_print("Você não tem dinheiro suficiente!\n")
                PokeShop()
        else:
            u.delay_print("Você não tem dinheiro suficiente!\n")
            PokeShop()
    elif choice == 3:
        if u.dinheiro >= p.Hyper_Potion.preco:
            u.delay_print("Quantas poções deseja comprar?\n")
            qtd = int(input())
            if u.dinheiro >= p.Hyper_Potion.preco * qtd:
                u.dinheiro -= p.Hyper_Potion.preco * qtd
                p.Hyper_Potion.qtd += qtd
                u.delay_print(f"Você comprou {qtd} poções!\n")
                if p.Hyper_Potion in b.player_bag:
                    p.Hyper_Potion.qtd += qtd
                else:
                    b.player_bag.append(p.Hyper_Potion)
                    p.Hyper_Potion.qtd += qtd
                PokeShop()
            else:
                u.delay_print("Você não tem dinheiro suficiente!\n")
                PokeShop()
        else:
            u.delay_print("Você não tem dinheiro suficiente!\n")
            PokeShop()
    elif choice == 4:
        if u.dinheiro >= p.Revive.preco:
            u.delay_print("Quantos revives deseja comprar?\n")
            qtd = int(input())
            if u.dinheiro >= p.Revive.preco * qtd:
                u.dinheiro -= p.Revive.preco * qtd
                p.Revive.qtd += qtd
                u.delay_print(f"Você comprou {qtd} revives!\n")
                if p.Revive in b.player_bag:
                    p.Revive.qtd += qtd
                else:
                    b.player_bag.append(p.Revive)
                    p.Revive.qtd += qtd
                PokeShop()
            else:
                u.delay_print("Você não tem dinheiro suficiente!\n")
                PokeShop()
        else:
            u.delay_print("Você não tem dinheiro suficiente!\n")
            PokeShop()
    else:
        u.delay_print("Voltando ao menu...\n")
        cp.menu()
        
    