from dataclasses import dataclass


@dataclass
class MenuItem :

    item_id : int
    name : str
    description : str
    price : float
    is_available : bool = True
