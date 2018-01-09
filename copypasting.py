class tool(object):
    """tools defines the tool"""
    def __init__(name2, ability2, amount2):
        """name is the name of the tool, ablitity is the amount of blocks it
        mines per use, and amount is the amount of the tool you have"""
        self.name2 = name2
        self.ability2 = ability2
        self.amount2 = amount2
wood_pickaxe = tool("Wood Pickaxe", 1, 0)
stone_pickaxe = tool("Stone Pickaxe", 5, 0)
iron_pickaxe = tool("Iron Pickaxe", 20, 0)
diamond_pickaxe = tool("Diamond Pickaxe", 50, 0)
""" These are tools you can use"""