from dataclasses import dataclass


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
    pass

@dataclass
class ThiefClass(UnitClass): # = ... # TODO действуем так же как и с войном
    pass

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}