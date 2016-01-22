from collections import namedtuple, defaultdict





def ReadShop(filename):
    with open(filename) as fd:
        data = fd.read().splitlines()
    shopitem = namedtuple("ShopItem",["name","cost","damage","armor"])
    shopdata = defaultdict(list)
    catagory = 'None'

    shopdata['Armor'].append(shopitem("None",0,0,0))
    
    for d in data:
        if d:
            if 'Weapons:' in d:
                catagory = "Weapons"
            elif 'Armor:' in d:
                catagory = "Armor"
            elif "Rings:" in d:
                catagory = "Rings"
            else:
                itemdata = d.split()
                itemdata[1:] = map(int,itemdata[1:])
                shopdata[catagory].append(shopitem(*itemdata))
    return shopdata
                
char_data = namedtuple("CharInfo",["Health","Damage","Armor"])


def ReadFight(filename):
    with open(filename) as fd:
        data = fd.read().splitlines()
    fightinfo = namedtuple("CharInfo",["Health","Damage","Armor"])
    d = [int(l.split()[-1]) for l in data]
    return char_data(*d)



def powerset(iterable):
    from itertools import chain, combinations
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in reversed(range(len(s)+1)))

def doFight(player,boss):
    b_health = boss.Health
    p_health = player.Health

    p_dmg = max(player.Damage - boss.Armor,1)
    b_dmg = max(boss.Damage - player.Armor,1)

    while 1:
        b_health -= p_dmg
        if (b_health <= 0):
            return True
        p_health -= b_dmg
        if p_health <= 0:
            return False

shop = ReadShop("shop.dat")
boss = ReadFight("fight.dat")


win_costs = []
lose_costs = []

from itertools import chain

for weapon in shop['Weapons']:
    for armor in shop['Armor']:
        for rings in powerset(shop["Rings"]):
            items = list(chain([weapon,armor],rings))

            
            tot_cost = sum(x.cost for x in items)
            tot_dmg = sum(x.damage for x in items)

            cost,dmg,armr = [sum(x) for x in zip(*items) if type(x[0]) is int] 
            
            player = char_data(100,dmg,armr)
            if doFight(player,boss):
                win_costs.append((cost,items))
            else:
                lose_costs.append((cost,items))


            

    
print min(win_costs)
print max(lose_costs)
