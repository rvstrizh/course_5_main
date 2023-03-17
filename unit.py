from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Equipment, Weapon, Armor
from classes import UnitClass, ThiefClass
from random import uniform
from typing import Optional


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """
    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self._is_skill_used = unit_class.skill

    @property
    def health_points(self):
        # TODO возвращаем аттрибут hp в красивом виде
        return self.hp

    @property
    def stamina_points(self):
        return self.stamina

    def equip_weapon(self, weapon: Weapon):
        # TODO присваиваем нашему герою новое оружие
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        # TODO одеваем новую броню
        self.armor = armor
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        # TODO Эта функция должна содержать:
        #  логику расчета урона игрока
        #  логику расчета брони цели
        #  здесь же происходит уменьшение выносливости атакующего при ударе
        #  и уменьшение выносливости защищающегося при использовании брони
        #  если у защищающегося нехватает выносливости - его броня игнорируется
        #  после всех расчетов цель получает урон - target.get_damage(damage)
        #  и возвращаем предполагаемый урон для последующего вывода пользователю в текстовом виде
        if self.weapon.stamina_per_hit < self.stamina:
            self.stamina = round((self.stamina - self.weapon.stamina_per_hit) * self.unit_class.stamina, 1)
            if target.stamina > target.armor.stamina_per_turn:
                target.stamina = round((target.stamina - target.armor.stamina_per_turn) * target.unit_class.stamina, 1)
                armor = target.armor.defence
            else:
                armor = 0
            damage = round(uniform(self.weapon.min_damage, self.weapon.max_damage) * self.unit_class.attack, 1)
        else:
            return 'not_stamina'

        return target.get_damage(damage, armor)

    def get_damage(self, damage: int, armor: int) -> Optional[int]:
        # TODO получение урона целью
        #      присваиваем новое значение для аттрибута self.hp

        self.hp = round(self.hp - damage + armor, 1)
        return round(damage - armor, 1)

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """
        этот метод будет переопределен ниже
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        return self.unit_class.skill.use(self, user=self, target=target)

    @property
    def is_skill_used(self):
        return self._is_skill_used


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        damage = self._count_damage(target)
        try:
            if damage > 0:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {round(damage, 1)} урона."
            elif damage == 0:
                return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        except TypeError:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."

class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар соперника
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target
        """
        damage = self._count_damage(target)
        try:
            if damage > 0:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
            elif damage == 0:
                return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        except TypeError:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        # TODO результат функции должен возвращать результат функции skill.use или же следующие строки:




