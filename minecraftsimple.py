import time
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

class tool(object):
    """tools defines the tool"""
    def __init__(self, name, ability, amount):
        """name is the name of the tool, ablitity is the amount of blocks it
        mines per use for pickaxes and the amount of mobs it kills for swords,
        amount is the amount of the tool you have, and durability is the amount of blocks you can mine before it breaks"""
        self.name = name
        self.ability = ability
        self.amount = amount
wood_sword = tool("Wooden Sword", 1, 0)
stone_sword = tool("Stone Sword", 5, 0)
iron_sword = tool("Iron Sword", 20, 0)
diamond_sword = tool("Diamond Sword", 50, 0)
wood_pickaxe = tool("Wood Pickaxe", 1, 0)
stone_pickaxe = tool("Stone Pickaxe", 5, 0)
iron_pickaxe = tool("Iron Pickaxe", 20, 0)
diamond_pickaxe = tool("Diamond Pickaxe", 50, 0)
""" These are tools you can use"""

def mine(block):
    block.amount += 1
    time.sleep(2)
    print(f'you have {self.amount} blocks of {self.name}')

def craft(wood_sword):
    if wood.amount >= 15:
        wood_sword.amount += 1
        time.sleep(1)
        print('You crafted a wooden sword')

