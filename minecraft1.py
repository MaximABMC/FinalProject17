import time
class block(object):
    """Block defines the type of block"""
    def __init__(self, name, amount):
        """name is the name of the block and amount is the number of that block you have"""
        self.name = name
        self.amount= amount

wood = block("Wood", 0)
stone = block("Stone", 0)
coal = block("Coal", 0)
iron_ore = block("Iron Ore", 0)
iron = block("Iron Ingot", 0)
gold_ore = block("Gold Ore", 0)
gold = block("Golden Ingot", 0)
diamond = block("Diamond", 0)
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

class crafting(object):
    """crafting defines the object used for crafting"""
    def __init__(self, name, amount):
        """name is the name of the crafting tool and amount is the amount you own"""
        self.name = name
        self.amount = amount
crafting_table = crafting("Crafting Table", 0)
furnace = crafting("Furnace", 0)

def mine(self):
    self.amount += 1
    time.sleep(2)
    print(f'you `have {self.amount} blocks of {self.name}')