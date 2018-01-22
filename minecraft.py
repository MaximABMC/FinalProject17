print("""Welcome to Minecraft! In this program you can mine different blocks and craft tools.

You start with no blocks at all.
However, you can mine wood with your hand.
With that wood you can craft a wooden pickaxe.
The wooden pickaxe can mine more blocks at a time compared to your hand.
You can collect more resources and craft better pickaxes.

There are three commands in the game.

Type mine(*name of block*, *pickaxe you are using*) to mine a block.


Type craft(*name of pickaxe*) to craft a pickaxe.
You must have the necessary resources to craft a pickaxe or it will not work.

Type inventory() to access your inventory.
This will tell you what resources you have.""")

"""This is the intro to the game"""

class Block(object):
    """Block class defines the type of block"""
    def __init__(self, name, amount):
        """name is the name of the block and amount is the number of that block you have"""
        self.name = name
        self.amount = amount

wood = Block("Wood", 0)
stone = Block("Stone", 0)
iron = Block("Iron Ingot", 0)
diamond = Block("Diamond", 0)
"""These resources you can aquire"""

class pickaxe(object):
    """pickaxe class defines the type of pickaxe"""
    def __init__(self, name, ability, amount, wood1, stone1, iron1, diamond1):
        """name is the name of the pickaxe, ability is the amount of blocks the
        pickaxe mines per use, amount is the number of a pickaxe you have,
        wood1 is the necessary amount of wood needed to craft the pickaxe,
        stone1 is the necessary stone needed, iron1 is the necessary iron
        needed and diamond1 is the necassary diamond"""
        self.name = name
        self.ability = ability
        self.amount = amount
        self.wood_needed = wood1
        self.stone_needed = stone1
        self.iron_needed = iron1
        self.diamond_needed = diamond1
hand = pickaxe("Hand", 1, 1, 0, 0, 0, 0)
wooden_pickaxe = pickaxe("Wood Pickaxe", 3, 0, 20, 0, 0, 0)
stone_pickaxe = pickaxe("Stone Pickaxe", 8, 0, 100, 200, 0, 0)
iron_pickaxe = pickaxe("Iron Pickaxe", 20, 0, 400, 0, 400, 0)
diamond_pickaxe = pickaxe("Diamond Pickaxe", 50, 0, 1000, 0, 0, 2000)
""" These are pickaxe you can use"""

def mine(block, pickaxe):
    if pickaxe.amount >= 1:
        block.amount += pickaxe.ability
    else:
        block.amount += 1
        print("You don't have that pickaxe.  You mine with your hand instead.")
    print(f'you have {block.amount} blocks of {block.name}')

"""The mine function allows the player to mine blocks by typing mine(block, pickaxe).
The player must have the pickaxe they are using or else they mine with their hand and recieve an error message.
If they do have the pickaxe they are using then the block.amount will increase by that pickaxe's pickaxe.ability
which is higher for better pickaxes.
At the end of every use of the mine function it will alert the player how many blocks of the newly mined block the player has."""

def craft(pickaxe):
    if wood.amount >= pickaxe.wood_needed and stone.amount >= pickaxe.stone_needed and iron.amount >= pickaxe.iron_needed and diamond.amount >= pickaxe.diamond_needed:
        pickaxe.amount += 1
        wood.amount -= pickaxe.wood_needed
        stone.amount -= pickaxe.stone_needed
        iron.amount -= pickaxe.iron_needed
        diamond.amount -= pickaxe.diamond_needed
        print(f'You crafted a {pickaxe.name}')
    else:
        print(f'You don\'t have enough of the correct resources to craft a {pickaxe.name}')

"""The craft function allows the user to craft pickaxes by typing craft(pickaxe).
The function first checks to see that the player's block.amount is greater or equal to the pickaxe.block_needed for each type of block.
This makes sure that the player has the necessary blocks to craft the pickaxe.
If the player does have the correct resources then their pickaxe.amount increases
by 1 and they get a message alerting them they crafted the pickaxe.
If the player does not have the necessary blocks then the player is  alerted they failed to craft the pickaxe."""

def inventory():
    print(f'You have: \n{wood.amount} block/s of wood \n{stone.amount} block/s of stone \n{iron.amount} block/s of iron \n{diamond.amount} block/s of diamond \n{wooden_pickaxe.amount} wooden pickaxe/s \n{stone_pickaxe.amount} stone pickaxe/s \n{iron_pickaxe.amount} iron pickaxe/s \n{diamond_pickaxe.amount} diamond pickaxe/s')

"""The inventory function allows the user to see the amount of each blocks and pickaxes they have by typing inventory().
It does this by printing the block.amount or pickaxe.amount for each type of block and pickaxe."""

