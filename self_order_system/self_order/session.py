from typing import Optional
from dataclasses import dataclass, field, asdict


@dataclass
class SessionToppingOrder:
    '''セッションに保持するトッピング注文データ'''
    topping_id: int
    quantity: int

    def __str__(self):
        return f'{self.topping_id} x {self.quantity}'

    @classmethod
    def from_dict(cls, data: dict):
        '''インスタンスを辞書から作成'''
        return cls(**data)


@dataclass
class SessionOrder:
    '''セッションに保持する注文データ'''
    table_no: int
    item_id: Optional[int] = None
    toppings: list[SessionToppingOrder] = field(default_factory=list)
    is_ordered: bool = False

    def __str__(self):
        return f'{self.item_id} {self.toppings}'

    def as_dict(self):
        '''インスタンスを辞書に変換'''
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        '''インスタンスを辞書から作成'''
        toppings_data = data.pop('toppings', [])
        instance = cls(**data)
        toppings = []
        for topping_data in toppings_data:
            toppings.append(SessionToppingOrder.from_dict(topping_data))
        instance.toppings = toppings
        return instance