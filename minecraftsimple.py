print("""Welcome to Minecraft! In this program you can mine different blocks and craft tools.

You start with no blocks at all.
However, you can mine wood with your hand.
With that wood you can craft a wooden pickaxe.
The wooden pickaxe can mine stone as well as wood and is able to mine more blocks than without it.
With the stone and wood you can craft a stone pickaxe.
With each new pickaxe you can mine blocks faster and the next tier of blocks.

There are four commands in the game.

Type mine(*name of block*, *pickaxe you are using*) to mine a block.


Type craft_pickaxe(*name of pickaxe*) to craft a pickaxe.
You must have the necessary resources to craft a pickaxe or it will not work.

Type craft_sword(*name of sword*) to craft a sword.
You must have the necessary resources to craft a sword or it will not work.

Type inventory() to access your inventory.
This will tell you what resources you have.""")

class Block(object):
    """Block defines the type of block"""
    def __init__(self, name, amount):
        """name is the name of the block and amount is the number of that block you have"""
        self.name = name
        self.amount = amount

wood = Block("Wood", 0)
stone = Block("Stone", 0)
iron = Block("Iron Ingot", 0)
gold = Block("Golden Ingot", 0)
diamond = Block("Diamond", 0)
"""These resources you can aquire"""

class pickaxe(object):
    """pickaxe defines the type of pickaxe"""
    def __init__(self, name, ability, amount, wood1):
        """name is the name of the pickaxe, ability is the amount of blocks the
        pickaxe mines per use, amount is the number of a pickaxe you have, wood1 is the necessary amount of wood needed to craft the pickaxe"""
        self.name = name
        self.ability = ability
        self.amount = amount
        self.wood_needed = wood1
hand = pickaxe("Hand", 1, 1, 0)
wooden_pickaxe = pickaxe("Wood Pickaxe", 3, 0, 15)
stone_pickaxe = pickaxe("Stone Pickaxe", 8, 0, 100)
iron_pickaxe = pickaxe("Iron Pickaxe", 20, 0, 400)
diamond_pickaxe = pickaxe("Diamond Pickaxe", 50, 0, 2000)
""" These are pickaxe you can use"""

class sword(object):
    """sword defines the type of sword"""
    def __init__(self, name, ability, amount, wood1):
        """name is the name of the sword, ability is the damage the sword does,
        amount is the number of a sword you have, wood1 is the required wood to craft the sword"""
        self.name = name
        self.ability = ability
        self.amount = amount
        self.wood_needed = wood1
wooden_sword = sword("Wooden Sword", 1, 0, 100)
stone_sword = sword("Stone Sword", 10, 0, 200)
iron_sword = sword("Iron Sword", 100, 0, 300)
diamond_sword = sword("Diamond Sword", 1000, 0, 500)


def mine(block, pickaxe):
    if pickaxe.amount >= 1:
        block.amount += pickaxe.ability
    elif pickaxe.amount == 0:
        block.amount += 1
        print("You don't have that pickaxe.  You mine with your hand instead.")
    else:
        print('You can\'t mine with a sword.')
    print(f'you have {block.amount} blocks of {block.name}')
"""The mine function allows the player to mine specfic blocks by typing mine(name of block).  When a player mines a block, the block.amount for that block increases."""

def craft_pickaxe(pickaxe):
    if wood.amount >= pickaxe.wood_needed:
        pickaxe.amount += 1
        wood.amount -= pickaxe.wood_needed
        print(f'You crafted a {pickaxe.name}')
    else:
        print(f'You don\'t have enough of the correct resources to craft a {pickaxe.name}')

def craft_sword(sword):
    if wood.amount >= sword.wood_needed:
        sword.wood_needed += 1
        wood.amount -= sword.wood_needed
        print(f'You crafted a {sword.name}')
    else:
        print(f'You don\'t have enough of the correct resources to craft a {sword.name}')

"""the craft function allows the player to craft tools by typing craft(name of tool).  When a player has the necessary resources to craft a tool and they use this function, the tool.amount for that tool increases.  If the player does not have the necessary resources, nothing is crafted and the player is alerted."""

def inventory():
    print(f'You have: \n{wood.amount} block/s of wood \n{stone.amount} block/s of stone \n{iron.amount} block/s of iron \n{diamond.amount} block/s of diamond \n{wooden_sword.amount} wooden sword/s \n{stone_sword.amount} stone sword/s \n{iron_sword.amount} iron sword/s \n{diamond_sword.amount} diamond sword/s \n{wooden_pickaxe.amount} wooden pickaxe/s \n{stone_pickaxe.amount} stone pickaxe/s \n{iron_pickaxe.amount} iron pickaxe/s \n{diamond_pickaxe.amount} diamond pickaxe/s')
"""The inventory function allows the user to see the amount of each block and tool they have by typing inventory()"""

