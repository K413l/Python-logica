import random

def cria():
    monte = []
    for v in range(1,14):
        monte.append((v,'p')) 
        monte.append((v,'c'))
        monte.append((v,'o'))
        monte.append((v,'e'))
    
    return monte

def compra(monte: list):
    return monte.pop()

def distribui(monte: list, qtd: int):
    mao = []
    while qtd > 0:
        c =  compra(monte)
        mao.append(c)
        qtd = qtd - 1
    return mao

def embaralha(monte: list):
    random.shuffle(monte)




deck = cria()
#print(deck)
#card = compra(deck)
#print(card)
embaralha(deck)
print(deck)