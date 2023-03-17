from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit

class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.user.is_skill_used.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if not self.user.is_skill_used.used:
            if self.user.is_skill_used._is_stamina_enough(self):
                self.user.is_skill_used.used = True
                return self.user.is_skill_used.skill_effect(self)
            return f"{self.user.name} попытался использовать {self.user.is_skill_used.name} но у него не хватило выносливости."
        else:

            return f"{self.user.name} не может использовать {self.user.is_skill_used.name} т.к. уже его использовал"


class FuryPunch(Skill):
    name = 'Яростный удар'
    stamina = 10
    damage = 20
    used = False

    def skill_effect(self):
        # TODO логика использования скилла -> return str
        # TODO в классе нам доступны экземпляры user и target - можно использовать любые их методы
        # TODO именно здесь происходит уменшение стамины у игрока применяющего умение и
        # TODO уменьшение здоровья цели.
        # TODO результат применения возвращаем строкой

        self.user.stamina = round(self.user.stamina - self.stamina, 1)
        self.target.hp = round(self.target.hp - self.user.is_skill_used.damage, 1)
        return f"{self.user.name} ненес {self.user.is_skill_used.name} мощностью {self.user.is_skill_used.damage} врагу {self.target.name}"


class HardShot(Skill):
    name = 'Жестокий выстрел'
    stamina = 16
    damage = 20
    used = False

    def skill_effect(self):
        self.user.stamina = round(self.user.stamina - self.stamina, 1)
        self.target.hp = round(self.target.hp - self.user.is_skill_used.damage, 1)
        return f"{self.user.name} нанес {self.user.is_skill_used.name} мощностью {self.user.is_skill_used.damage} врагу {self.target.name}"

