from character import Character
from enemy import Enemy

class Abilities:
    def __init__(self, level: int, attack_power: int, heal_power: int) -> None:
        if attack_power + heal_power != level:
            raise ValueError("The sum of attack_power and heal_powering must be equal to the level of pet")
        self._attack_power = attack_power
        self._heal_power = heal_power
        
    
    def heal_player(self, player: Character) -> None:
        player.heal(self._heal_power)     
    def attack_enemy(self, enemy: Enemy) -> None:
        enemy.take_damage(self._attack_power)
    

    def get_attack_power(self) -> int:
        return self._attack_power
    def get_heal_power(self) -> int:
        return self._heal_power


    def set_attack_power_and_heal_power(self, attack_power: int, heal_power: int) -> None:
        self._attack_power = attack_power
        self._heal_power = heal_power
        
        
       

