class TrackOrders:
    # aqui deve expor a quantidade de estoque
    total_pedidos = 0

    def __init__(self):
        self.total_pedidos

    def __len__(cls):
        return cls.total_pedidos

    def add_new_order(self):
        self.total_pedidos += 1

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


teste = TrackOrders()
print(len(teste))
