class Item:
    def __init__(self, item_name, item_description=None, item_use=None, item_value="0gp"):
        self.name = item_name
        self.description = item_description
        self.use = item_use
        self.value = item_value

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def get_use(self):
        return self.use

    def set_use(self, item_use):
        self.use = item_use

    def describe(self):
        print(self.description)

    def get_details(self):
        print(self.name)
        print("-" * len(self.description))
        print(self.description)
        print(self.use)
        print(f"This item is worth: {self.value}")