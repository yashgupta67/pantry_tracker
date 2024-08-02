class Item:
    def __init__(self, name: str, type: str) -> None:
        """Creates an item with a name and type to be stored in Pantry object.

        Args:
            name (str): Name of the Item.
            type (str): 'Category' of the Item.
        """
        self.name = name.capitalize()
        self.type = type.capitalize()

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.name == other.name and self.type == other.type

    def __hash__(self):
        return hash(self.name + self.type)

    def __str__(self) -> str:
        return f"{self.name}-{self.type}"

    def __repr__(self) -> str:
        return f"{self.name}-{self.type}"

class Pantry:
    def __init__(self, items: list = None) -> None:
        """Creates an object to keep track of pantry items. Uses a dict to do so.

        Args:
            items (list, optional): List of Item objects to add to pantry. Defaults to None.
        """
        self.table = {}

        if items:
            for item in items:
                if not isinstance(item, Item):
                    raise TypeError("All items must be of type Item")
                self.add(item)

    def add(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item must be of type Item")

        if item in self.table:
            self.table[item] += 1
        else:
            self.table[item] = 1

    def remove(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item must be of type Item")

        if item in self.table:
            if self.table[item] > 1:
                self.table[item] -= 1
            else:
                self.table.pop(item)
        else:
            raise ValueError("Item not found in pantry")
