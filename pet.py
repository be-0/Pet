import pygame
from typing import List
from item import Item
from abilities import Abilities
from character import Character
from enemy import Enemy
class Pet(Item): #inheritance
    def __init__(self, name: str, level: int, ability: List[int], icon: pygame.surface) -> None:
        super().__init__(name, level, None, icon)
        #aggregation
        self._abilities = Abilities(level, ability[0], ability[1])
    

    def heal_player(self, player: Character) -> None:
        self._abilities._heal(player)

    def attack_enemy(self, enemy: Enemy) -> None:
        self._abilities._attack(enemy)
    
    #aggregate methods & wrappers   
    def get_attack_power(self) -> int:
        return self._abilities._attack_power
    def get_heal_power(self) -> int:
        return self._abilities._heal_power
        
    def get_cost(self):
        cost = super().get_cost()
        return cost
    def get_level(self) -> int:
        return self._level
        
    #aggregate methods & encapsulation
    def set_level_and_abilities(self, level: int, attack_power: int, heal_power: int) -> None:
        #checks if level < 1
        if level < 1:
            raise ValueError("The level cannot go under 1")
        #checks if attack_power < 0
        if attack_power < 0:
            raise ValueError("The attack power cannot go under 0")
        #checks if heal_power < 0
        if heal_power < 0:
            raise ValueError("The heal power cannot go under 0")
        #checks if sum of abilities is equal to the level
        if attack_power + heal_power != level:
            raise ValueError("The sum of attack_power and heal_powering must be equal to the level of pet")
        self._level = level
        self._abilities.set_attack_power_and_heal_power(attack_power, heal_power)
