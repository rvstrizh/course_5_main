from dataclasses import dataclass
from typing import List
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        pass


@dataclass
class EquipmentData:
    # TODO содержит 2 списка - с оружием и с броней
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        # TODO возвращает объект оружия по имени
        for weapon in self.get_weapons_names():
            if weapon.name == weapon_name:
                return weapon

    def get_armor(self, armor_name) -> Armor:
        # TODO возвращает объект брони по имени
        for armor in self.get_armors_names():
            if armor.name == armor_name:
                return armor

    def get_weapons_names(self) -> list:
        # TODO возвращаем список с оружием
        return self._get_equipment_data().weapons

    def get_armors_names(self) -> list:
        # TODO возвращаем список с броней
        return self._get_equipment_data().armors

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        equipment_file = open("./data/equipment.json")
        data = json.load(equipment_file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError

# eq = Equipment()
#
# print(type(eq._get_equipment_data()))
# # @dataclass
# class WarriorClass(Armor, Weapons):
