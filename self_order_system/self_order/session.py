from typing import Optional
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
    item_id: Optional[int] = None
    toppings: list[SessionToppingOrder] = field(default_factory=list)
    is_ordered: bool = False

    def __str__(self):
        return f'{self.item_id} {self.toppings}'

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        toppings_data = data.pop('toppings', [])
        instance = cls(**data)
        instance.toppings = [SessionToppingOrder.from_dict(d) for d in toppings_data]
        return instance