from dataclasses import dataclass, field, asdict


@dataclass
class SessionToppingOrder:
    topping_id: int
    quantity: int

    def __str__(self):
        return f'{self.topping_id} x {self.quantity}'

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class SessionOrder:
    table_no: int
    item_id: int = None
    toppings: list[SessionToppingOrder] = field(default_factory=list)

    def __str__(self):
        return f'{self.item_id} {self.toppings}'

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        toppings = [SessionToppingOrder.from_dict(d) for d in data['toppings']]
        return cls(**data, toppings=toppings)