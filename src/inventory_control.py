from collections import defaultdict


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    ingredientes_solicitados = defaultdict(int)
    novo_pedido = {}

    def __init__(self):
        self.ingredientes_solicitados.clear()
        self.ingredientes_solicitados = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        for i in self.INGREDIENTS[order]:
            self.ingredientes_solicitados[i] += 1

        for i, v in self.ingredientes_solicitados.items():
            if v > self.MINIMUM_INVENTORY[i]:
                return False
            self.novo_pedido[i] = v

    def get_quantities_to_buy(self):
        return self.novo_pedido

    def get_available_dishes(self):
        for i, v in self.ingredientes_solicitados.items():
            if v < self.MINIMUM_INVENTORY[i]:
                return self.INGREDIENTS.keys()
