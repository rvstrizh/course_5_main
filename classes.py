from dataclasses import dataclass
from skills import FuryPunch, HardShot, Skill

@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


@dataclass
class WarriorClass(UnitClass): # =  ... # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов
    name: str = 'Воин'
    max_health: float = 60
    max_stamina: float = 30
    attack: float = 1.1
    stamina: float = 0.9
    armor: float = 1
    skill: Skill = FuryPunch

@dataclass
class ThiefClass(UnitClass): # = ... # TODO действуем так же как и с войном
    name: str = 'Вор'
    max_health: float = 60
    max_stamina: float = 30
    attack: float = 1.1
    stamina: float = 0.9
    armor: float = 1
    skill: Skill = HardShot


unit_classes = {
    ThiefClass.name: ThiefClass(),
    WarriorClass.name: WarriorClass()
}
