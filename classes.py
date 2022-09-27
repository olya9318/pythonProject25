from dataclasses import dataclass
from skills import *

@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=100,
    max_stamina=20,
    attack=1,
    stamina=0.9,
    armor=2,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=60,
    max_stamina=15,
    attack=2,
    stamina=0.9,
    armor=0.7,
    skill=HardShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}