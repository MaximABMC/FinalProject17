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
    def __init__(self, name, ability, amount, wood1):
        """name is the name of the tool, ablitity is the amount of blocks it
        mines per use for pickaxes and the amount of mobs it kills for swords,
        amount is the amount of the tool you have, and durability is the amount of blocks you can mine before it breaks"""
        self.name = name
        self.ability = ability
        self.amount = amount
        self.wood_needed = wood1
wooden_sword = tool("Wooden Sword", 1, 0, 15)
stone_sword = tool("Stone Sword", 5, 0, 200)
iron_sword = tool("Iron Sword", 20, 0, 400)
diamond_sword = tool("Diamond Sword", 50, 0, 500)
wooden_pickaxe = tool("Wood Pickaxe", 1, 0, 15)
stone_pickaxe = tool("Stone Pickaxe", 5, 0, 200)
iron_pickaxe = tool("Iron Pickaxe", 20, 0, 400)
diamond_pickaxe = tool("Diamond Pickaxe", 50, 0, 500)
""" These are tools you can use"""

def mine(block):
    block.amount += 1
    print(f'you have {block.amount} blocks of {block.name}')

def craft(tool):
    if wood.amount >= tool.wood_needed:
        tool.amount += 1
        wood.amount -= tool.wood_needed
        print(f'You crafted a {tool.name}')
    else:
        print(f'You don\'t have enough of the correct resources to craft a {tool.name}')

def inventory():
    print(f'You have: \n{wood.amount} block/s of wood \n{stone.amount} block/s of stone \n{iron.amount} block/s of iron \n{diamond.amount} block/s of diamond \n{wooden_sword.amount} wooden sword/s \n{stone_sword.amount} stone sword/s \n{iron_sword.amount} iron sword/s \n{diamond_sword.amount} diamond sword/s \n{wooden_pickaxe.amount} wooden pickaxe/s \n{stone_pickaxe.amount} stone pickaxe/s \n{iron_pickaxe.amount} iron pickaxe/s \n{diamond_pickaxe.amount} diamond pickaxe/s')
