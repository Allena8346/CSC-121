"""
Text-Based RPG Game with S.P.E.C.I.A.L. System
Created by: Alexander Allen
Date: December 2024

This game demonstrates object-oriented programming concepts including:
- Classes and inheritance
- Encapsulation (private attributes)
- Methods and attributes
- File I/O
- Exception handling
- Collections/Data structures
"""

"""
1. Need a return to main menu upon selecting exit and exit game option

2.



"""




import random
import json
import os


class SPECIALAttributes:
    """
    S.P.E.C.I.A.L. attribute system for character creation.
    
    Attributes:
    - Strength: Affects attack power
    - Perception: Affects critical hit chance
    - Endurance: Affects max health
    - Charisma: Affects item drop rates
    - Intelligence: Affects XP gained
    - Agility: Affects dodge chance
    - Luck: Affects overall random outcomes
    """
    
    # Phrases for each attribute level (1-10)
    ATTRIBUTE_PHRASES = {
        1: "Terrible", 2: "Very Poor", 3: "Poor", 4: "Below Average",
        5: "Average", 6: "Above Average", 7: "Good", 8: "Very Good",
        9: "Excellent", 10: "Legendary"
    }
    
    def __init__(self):
        """Initialize S.P.E.C.I.A.L. attributes with minimum values."""
        self.__attributes = {
            "Strength": 1,
            "Perception": 1,
            "Endurance": 1,
            "Charisma": 1,
            "Intelligence": 1,
            "Agility": 1,
            "Luck": 1
        }
        self.__total_points = 28
        self.__used_points = 7  # Minimum 1 in each attribute
        self.__available_points = self.__total_points - self.__used_points
    
    def randomize_attributes(self):
        """Randomly distribute 21 points among attributes."""
        # Reset to minimum values
        for attr in self.__attributes:
            self.__attributes[attr] = 1
        
        # Distribute 21 points randomly
        points_to_distribute = 21
        attributes_list = list(self.__attributes.keys())
        
        while points_to_distribute > 0:
            attr = random.choice(attributes_list)
            # Max 10 per attribute
            if self.__attributes[attr] < 10:
                self.__attributes[attr] += 1
                points_to_distribute -= 1
        
        self.__used_points = 28
        self.__available_points = 0
        
        print("\n21 points randomly distributed!")
        print("You have 7 bonus points to distribute manually.")
        self.__available_points = 7
        self.__used_points = 21
    
    def get_attribute(self, attr_name):
        """Get the value of a specific attribute."""
        return self.__attributes.get(attr_name, 0)
    
    def set_attribute(self, attr_name, value):
        """Set the value of a specific attribute."""
        if attr_name in self.__attributes:
            old_value = self.__attributes[attr_name]
            self.__attributes[attr_name] = value
            self.__used_points += (value - old_value)
            self.__available_points = self.__total_points - self.__used_points
    
    def get_all_attributes(self):
        """Return all attributes as a dictionary."""
        return self.__attributes.copy()
    
    def get_available_points(self):
        """Return number of available points to distribute."""
        return self.__available_points
    
    def display_attributes(self):
        """Display all attributes with their phrases."""
        print("\n" + "="*60)
        print("S.P.E.C.I.A.L. ATTRIBUTES")
        print("="*60)
        for attr, value in self.__attributes.items():
            phrase = self.ATTRIBUTE_PHRASES[value]
            print(f"{attr:15} [{value:2}] - {phrase}")
        print(f"\nTotal Points Used: {self.__used_points}/{self.__total_points}")
        print(f"Available Points: {self.__available_points}")
        print("="*60)
    
    def modify_attribute(self, attr_name, change):
        """
        Modify an attribute by a certain amount.
        
        Args:
            attr_name (str): Name of attribute to modify
            change (int): Amount to change (positive or negative)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if attr_name not in self.__attributes:
            print("Invalid attribute name!")
            return False
        
        new_value = self.__attributes[attr_name] + change
        
        # Check constraints
        if new_value < 1:
            print("Attributes cannot be less than 1!")
            return False
        
        if new_value > 10:
            print("Attributes cannot exceed 10!")
            return False
        
        # Check if we have points available (when increasing)
        if change > 0 and self.__available_points < change:
            print(f"Not enough points! You only have {self.__available_points} available.")
            return False
        
        # Apply change
        self.__attributes[attr_name] = new_value
        self.__used_points += change
        self.__available_points -= change
        
        return True
    
    def save_to_file(self, filename="character_sheet.txt"):
        """Save character sheet to a text file."""
        try:
            with open(filename, 'w') as f:
                f.write("="*60 + "\n")
                f.write("S.P.E.C.I.A.L. CHARACTER SHEET\n")
                f.write("="*60 + "\n\n")
                
                for attr, value in self.__attributes.items():
                    phrase = self.ATTRIBUTE_PHRASES[value]
                    f.write(f"{attr:15} [{value:2}] - {phrase}\n")
                
                f.write(f"\nTotal Points Used: {self.__used_points}/{self.__total_points}\n")
                f.write("="*60 + "\n")
            
            print(f"\nCharacter sheet saved to {filename}!")
            return True
        except Exception as e:
            print(f"Error saving character sheet: {e}")
            return False
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            "attributes": self.__attributes.copy(),
            "total_points": self.__total_points,
            "used_points": self.__used_points,
            "available_points": self.__available_points
        }
    
    @staticmethod
    def from_dict(data):
        """Create SPECIALAttributes from dictionary."""
        special = SPECIALAttributes()
        special._SPECIALAttributes__attributes = data["attributes"].copy()
        special._SPECIALAttributes__used_points = data["used_points"]
        special._SPECIALAttributes__available_points = data["available_points"]
        return special


class Character:
    """
    Base class for all characters in the game.
    Demonstrates inheritance - both Player and Enemy inherit from this.
    """
    
    def __init__(self, name, health, attack_power):
        """
        Initialize a character with basic attributes.
        
        Args:
            name (str): Character's name
            health (int): Character's health points
            attack_power (int): Character's attack damage
        """
        self.__name = name  # Private attribute
        self.__health = health  # Private attribute
        self.__max_health = health  # Private attribute
        self.__attack_power = attack_power  # Private attribute
    
    # Getter methods (encapsulation)
    def get_name(self):
        """Return the character's name."""
        return self.__name
    
    def get_health(self):
        """Return the character's current health."""
        return self.__health
    
    def get_max_health(self):
        """Return the character's maximum health."""
        return self.__max_health
    
    def get_attack_power(self):
        """Return the character's attack power."""
        return self.__attack_power
    
    # Setter methods
    def set_health(self, health):
        """Set the character's health (cannot exceed max health)."""
        self.__health = min(health, self.__max_health)
    
    def set_max_health(self, max_health):
        """Set the character's maximum health."""
        self.__max_health = max_health
        if self.__health > max_health:
            self.__health = max_health
    
    def set_attack_power(self, attack_power):
        """Set the character's attack power."""
        self.__attack_power = attack_power
    
    def attack(self, target):
        """
        Attack another character.
        
        Args:
            target (Character): The character being attacked
            
        Returns:
            int: Damage dealt
        """
        damage = random.randint(self.__attack_power - 2, self.__attack_power + 2)
        target.take_damage(damage)
        return damage
    
    def take_damage(self, damage):
        """
        Reduce health by damage amount.
        
        Args:
            damage (int): Amount of damage to take
        """
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
    
    def is_alive(self):
        """Check if character is still alive."""
        return self.__health > 0
    
    def heal(self, amount):
        """
        Heal the character.
        
        Args:
            amount (int): Amount to heal
        """
        self.__health = min(self.__health + amount, self.__max_health)


class Player(Character):
    """
    Player class - inherits from Character.
    Adds experience, leveling, inventory management, and S.P.E.C.I.A.L. attributes.
    """
    
    def __init__(self, name, special_attributes):
        """
        Initialize a player character.
        
        Args:
            name (str): Player's name
            special_attributes (SPECIALAttributes): S.P.E.C.I.A.L. attributes
        """
        self.__special = special_attributes  # Private attribute
        
        # Calculate base stats from S.P.E.C.I.A.L. attributes
        base_health = 80 + (self.__special.get_attribute("Endurance") * 10)
        base_attack = 8 + (self.__special.get_attribute("Strength") * 2)
        
        super().__init__(name, health=base_health, attack_power=base_attack)
        
        self.__level = 1  # Private attribute
        self.__experience = 0  # Private attribute
        self.__inventory = []  # Private attribute
        self.__exp_to_next_level = 100  # Private attribute
        self.__critical_chance = self.__special.get_attribute("Perception") * 5  # Private attribute
        self.__dodge_chance = self.__special.get_attribute("Agility") * 3  # Private attribute
    
    def get_level(self):
        """Return player's current level."""
        return self.__level
    
    def get_experience(self):
        """Return player's current experience."""
        return self.__experience
    
    def get_inventory(self):
        """Return player's inventory."""
        return self.__inventory
    
    def get_special_attributes(self):
        """Return S.P.E.C.I.A.L. attributes."""
        return self.__special
    
    def get_critical_chance(self):
        """Return critical hit chance percentage."""
        return self.__critical_chance
    
    def get_dodge_chance(self):
        """Return dodge chance percentage."""
        return self.__dodge_chance
    
    def attack(self, target):
        """
        Attack with chance for critical hit based on Perception.
        
        Args:
            target (Character): The character being attacked
            
        Returns:
            tuple: (damage, is_critical)
        """
        base_damage = random.randint(self.get_attack_power() - 2, self.get_attack_power() + 2)
        
        # Check for critical hit (Perception affects this)
        is_critical = random.randint(1, 100) <= self.__critical_chance
        
        if is_critical:
            damage = int(base_damage * 1.5)
            print("💥 CRITICAL HIT! 💥")
        else:
            damage = base_damage
        
        # Luck can add bonus damage
        luck_bonus = random.randint(0, self.__special.get_attribute("Luck"))
        damage += luck_bonus
        
        target.take_damage(damage)
        return damage, is_critical
    
    def try_dodge(self):
        """
        Attempt to dodge an attack based on Agility.
        
        Returns:
            bool: True if dodge successful
        """
        return random.randint(1, 100) <= self.__dodge_chance
    
    def add_experience(self, exp):
        """
        Add experience points and check for level up.
        Intelligence affects XP gain.
        
        Args:
            exp (int): Experience points to add
        """
        # Intelligence bonus to XP
        intelligence_multiplier = 1 + (self.__special.get_attribute("Intelligence") * 0.05)
        exp = int(exp * intelligence_multiplier)
        
        self.__experience += exp
        print(f"\n+{exp} XP gained!")
        
        # Check for level up
        while self.__experience >= self.__exp_to_next_level:
            self.level_up()
    
    def level_up(self):
        """Level up the player, increasing stats based on S.P.E.C.I.A.L."""
        self.__level += 1
        self.__experience -= self.__exp_to_next_level
        self.__exp_to_next_level = int(self.__exp_to_next_level * 1.5)
        
        # Check max level
        if self.__level > 20:
            self.__level = 20
            print("\nYou have reached the maximum level!")
            return
        
        # Increase stats based on S.P.E.C.I.A.L. attributes
        endurance = self.__special.get_attribute("Endurance")
        strength = self.__special.get_attribute("Strength")
        
        health_increase = 8 + (endurance * 2)
        attack_increase = 1 + (strength // 2)
        
        current_max = self.get_max_health()
        self.set_max_health(current_max + health_increase)
        
        # Restore to full HP on level up
        self.set_health(self.get_max_health())
        
        self.set_attack_power(self.get_attack_power() + attack_increase)
        
        # Increase critical and dodge chances slightly
        self.__critical_chance = min(self.__critical_chance + 1, 75)
        self.__dodge_chance = min(self.__dodge_chance + 1, 50)
        
        print(f"\n{'='*50}")
        print(f"LEVEL UP! You are now level {self.__level}!")
        print(f"Max health increased by {health_increase}!")
        print(f"HP fully restored to {self.get_max_health()}!")
        print(f"Attack power increased by {attack_increase}!")
        print(f"Critical chance: {self.__critical_chance}%")
        print(f"Dodge chance: {self.__dodge_chance}%")
        print(f"{'='*50}\n")
        
        # Every 2 levels, allow player to increase a S.P.E.C.I.A.L. attribute
        if self.__level % 2 == 0:
            self.increase_special_attribute()
    
    def add_item(self, item):
        """
        Add an item to inventory.
        
        Args:
            item (Item): Item to add
        """
        self.__inventory.append(item)
        print(f"\n{item.get_name()} added to inventory!")
    
    def increase_special_attribute(self):
        """Allow player to increase one S.P.E.C.I.A.L. attribute by 1 point."""
        print("\n" + "="*60)
        print("ATTRIBUTE INCREASE!")
        print("="*60)
        print("You can increase one S.P.E.C.I.A.L. attribute by 1 point!")
        print("\nCurrent Attributes:")
        
        attrs = self.__special.get_all_attributes()
        for attr, value in attrs.items():
            print(f"  {attr}: {value}/10")
        
        while True:
            print("\nWhich attribute would you like to increase?")
            print("1) Strength")
            print("2) Perception")
            print("3) Endurance")
            print("4) Charisma")
            print("5) Intelligence")
            print("6) Agility")
            print("7) Luck")
            
            choice = input("\nEnter choice: ").strip()
            
            attr_map = {
                "1": "Strength",
                "2": "Perception",
                "3": "Endurance",
                "4": "Charisma",
                "5": "Intelligence",
                "6": "Agility",
                "7": "Luck"
            }
            
            if choice in attr_map:
                attr_name = attr_map[choice]
                current_value = self.__special.get_attribute(attr_name)
                
                if current_value >= 10:
                    print(f"\n{attr_name} is already at maximum (10)! Choose another.")
                    continue
                
                self.__special.set_attribute(attr_name, current_value + 1)
                print(f"\n{attr_name} increased to {current_value + 1}!")
                
                # Update player stats based on new attributes
                if attr_name == "Strength":
                    self.set_attack_power(self.get_attack_power() + 2)
                    print("Attack power increased!")
                elif attr_name == "Endurance":
                    old_max = self.get_max_health()
                    self.set_max_health(old_max + 10)
                    self.set_health(self.get_health() + 10)
                    print("Max health increased!")
                elif attr_name == "Perception":
                    self.__critical_chance = min(self.__critical_chance + 5, 75)
                    print("Critical chance increased!")
                elif attr_name == "Agility":
                    self.__dodge_chance = min(self.__dodge_chance + 3, 50)
                    print("Dodge chance increased!")
                
                print("="*60)
                break
            else:
                print("Invalid choice!")
    
    def use_item(self, item_index):
        """
        Use an item from inventory.
        
        Args:
            item_index (int): Index of item in inventory
            
        Returns:
            bool: True if item was used successfully
        """
        try:
            if 0 <= item_index < len(self.__inventory):
                item = self.__inventory[item_index]
                item.use(self)
                self.__inventory.pop(item_index)
                return True
            else:
                print("Invalid item selection!")
                return False
        except Exception as e:
            print(f"Error using item: {e}")
            return False
    
    def display_stats(self):
        """Display player statistics including S.P.E.C.I.A.L."""
        print(f"\n{'='*50}")
        print(f"Player: {self.get_name()}")
        print(f"Level: {self.__level}")
        print(f"Health: {self.get_health()}/{self.get_max_health()}")
        print(f"Attack Power: {self.get_attack_power()}")
        print(f"Critical Chance: {self.__critical_chance}%")
        print(f"Dodge Chance: {self.__dodge_chance}%")
        print(f"Experience: {self.__experience}/{self.__exp_to_next_level}")
        print(f"Inventory: {len(self.__inventory)} items")
        print(f"{'='*50}")
        
        # Show S.P.E.C.I.A.L. attributes
        print("\nS.P.E.C.I.A.L. Attributes:")
        for attr, value in self.__special.get_all_attributes().items():
            print(f"  {attr}: {value}")
        print(f"{'='*50}\n")
    
    def save_to_file(self, filename="savegame.json"):
        """
        Save player data to a file.
        
        Args:
            filename (str): Name of save file
        """
        try:
            save_data = {
                "name": self.get_name(),
                "health": self.get_health(),
                "max_health": self.get_max_health(),
                "attack_power": self.get_attack_power(),
                "level": self.__level,
                "experience": self.__experience,
                "exp_to_next_level": self.__exp_to_next_level,
                "critical_chance": self.__critical_chance,
                "dodge_chance": self.__dodge_chance,
                "special": self.__special.to_dict(),
                "inventory": [item.to_dict() for item in self.__inventory]
            }
            
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=4)
            print(f"\nGame saved to {filename}!")
            
            # Also save character sheet
            self.__special.save_to_file("character_sheet.txt")
        except Exception as e:
            print(f"Error saving game: {e}")
    
    @staticmethod
    def load_from_file(filename="savegame.json"):
        """
        Load player data from a file.
        
        Args:
            filename (str): Name of save file
            
        Returns:
            Player: Loaded player object or None
        """
        try:
            if not os.path.exists(filename):
                print(f"Save file {filename} not found!")
                return None
            
            with open(filename, 'r') as f:
                save_data = json.load(f)
            
            # Restore S.P.E.C.I.A.L. attributes
            special = SPECIALAttributes.from_dict(save_data["special"])
            
            player = Player(save_data["name"], special)
            player.set_health(save_data["health"])
            player.set_max_health(save_data["max_health"])
            player._Player__level = save_data["level"]
            player._Player__experience = save_data["experience"]
            player._Player__exp_to_next_level = save_data["exp_to_next_level"]
            player._Player__critical_chance = save_data["critical_chance"]
            player._Player__dodge_chance = save_data["dodge_chance"]
            player.set_attack_power(save_data["attack_power"])
            
            # Load inventory
            for item_data in save_data["inventory"]:
                item = Item.from_dict(item_data)
                player._Player__inventory.append(item)
            
            print(f"\nGame loaded from {filename}!")
            return player
        except Exception as e:
            print(f"Error loading game: {e}")
            return None


class Enemy(Character):
    """
    Enemy class - inherits from Character.
    Represents enemies the player will fight.
    """
    
    def __init__(self, name, health, attack_power, exp_reward):
        """
        Initialize an enemy.
        
        Args:
            name (str): Enemy's name
            health (int): Enemy's health
            attack_power (int): Enemy's attack damage
            exp_reward (int): Experience points awarded when defeated
        """
        super().__init__(name, health, attack_power)
        self.__exp_reward = exp_reward  # Private attribute
    
    def get_exp_reward(self):
        """Return experience reward for defeating this enemy."""
        return self.__exp_reward
    
    @staticmethod
    def create_random_enemy(player_level):
        """
        Create a random enemy scaled to player level.
        
        Args:
            player_level (int): Player's current level
            
        Returns:
            Enemy: Randomly generated enemy
        """
        enemy_types = [
            ("Goblin", 30, 5),
            ("Orc", 50, 8),
            ("Troll", 70, 12),
            ("Dark Knight", 90, 15),
            ("Dragon", 120, 20)
        ]
        
        # Select random enemy type
        name, base_health, base_attack = random.choice(enemy_types)
        
        # Scale to player level
        health = base_health + (player_level * 10)
        attack_power = base_attack + (player_level * 2)
        exp_reward = 50 + (player_level * 25)
        
        return Enemy(name, health, attack_power, exp_reward)


class Item:
    """
    Item class for inventory management.
    """
    
    def __init__(self, name, item_type, value):
        """
        Initialize an item.
        
        Args:
            name (str): Item name
            item_type (str): Type of item (health_potion, attack_boost)
            value (int): Value/effect of the item
        """
        self.__name = name  # Private attribute
        self.__item_type = item_type  # Private attribute
        self.__value = value  # Private attribute
    
    def get_name(self):
        """Return item name."""
        return self.__name
    
    def get_type(self):
        """Return item type."""
        return self.__item_type
    
    def get_value(self):
        """Return item value."""
        return self.__value
    
    def use(self, player):
        """
        Use the item on a player.
        
        Args:
            player (Player): Player using the item
        """
        if self.__item_type == "health_potion":
            player.heal(self.__value)
            print(f"\nUsed {self.__name}! Restored {self.__value} HP!")
        elif self.__item_type == "attack_boost":
            player.set_attack_power(player.get_attack_power() + self.__value)
            print(f"\nUsed {self.__name}! Attack power increased by {self.__value}!")
    
    def to_dict(self):
        """Convert item to dictionary for saving."""
        return {
            "name": self.__name,
            "type": self.__item_type,
            "value": self.__value
        }
    
    @staticmethod
    def from_dict(data):
        """Create item from dictionary."""
        return Item(data["name"], data["type"], data["value"])
    
    @staticmethod
    def create_random_item():
        """
        Create a random item.
        
        Returns:
            Item: Randomly generated item
        """
        item_options = [
            ("Health Potion", "health_potion", 30),
            ("Greater Health Potion", "health_potion", 50),
            ("Attack Boost Elixir", "attack_boost", 5),
            ("Power Crystal", "attack_boost", 10)
        ]
        
        name, item_type, value = random.choice(item_options)
        return Item(name, item_type, value)


class Room:
    """
    Room class for game map.
    """
    
    def __init__(self, description):
        """
        Initialize a room.
        
        Args:
            description (str): Description of the room
        """
        self.__description = description  # Private attribute
        self.__enemy = None  # Private attribute
        self.__item = None  # Private attribute
        self.__visited = False  # Private attribute
    
    def get_description(self):
        """Return room description."""
        return self.__description
    
    def has_enemy(self):
        """Check if room has an enemy."""
        return self.__enemy is not None
    
    def get_enemy(self):
        """Return the enemy in this room."""
        return self.__enemy
    
    def set_enemy(self, enemy):
        """Set an enemy in this room."""
        self.__enemy = enemy
    
    def clear_enemy(self):
        """Remove enemy from room."""
        self.__enemy = None
    
    def has_item(self):
        """Check if room has an item."""
        return self.__item is not None
    
    def get_item(self):
        """Return and remove the item from this room."""
        item = self.__item
        self.__item = None
        return item
    
    def set_item(self, item):
        """Set an item in this room."""
        self.__item = item
    
    def is_visited(self):
        """Check if room has been visited."""
        return self.__visited
    
    def mark_visited(self):
        """Mark room as visited."""
        self.__visited = True


class Game:
    """
    Main game class that controls game flow.
    """
    
    def __init__(self):
        """Initialize the game."""
        self.__player = None  # Private attribute
        self.__current_room = (0, 0)  # Private attribute
        self.__rooms = {}  # Private attribute
        self.__game_running = True  # Private attribute
    
    def create_special_character(self):
        """
        Create a character with S.P.E.C.I.A.L. attributes.
        
        Returns:
            SPECIALAttributes: Configured attributes
        """
        special = SPECIALAttributes()
        
        print("\n" + "="*60)
        print("CHARACTER CREATION - S.P.E.C.I.A.L. SYSTEM")
        print("="*60)
        print("\nYou have 28 total points to distribute:")
        print("- Each attribute starts at 1 (minimum)")
        print("- Each attribute can go up to 10 (maximum)")
        print("- 21 points will be distributed randomly")
        print("- You get 7 bonus points to distribute manually")
        
        input("\nPress Enter to randomize initial distribution...")
        special.randomize_attributes()
        special.display_attributes()
        
        # Manual distribution phase
        while special.get_available_points() > 0:
            print(f"\nYou have {special.get_available_points()} points remaining.")
            print("\nWhich attribute would you like to increase?")
            print("1) Strength    (Increases attack power)")
            print("2) Perception  (Increases critical hit chance)")
            print("3) Endurance   (Increases max health)")
            print("4) Charisma    (Better item drops)")
            print("5) Intelligence (More XP from battles)")
            print("6) Agility     (Increases dodge chance)")
            print("7) Luck        (Better overall outcomes)")
            print("8) View Current Build")
            print("9) Restart Distribution")
            print("0) Finish")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                if special.modify_attribute("Strength", 1):
                    print("Strength increased!")
            elif choice == "2":
                if special.modify_attribute("Perception", 1):
                    print("Perception increased!")
            elif choice == "3":
                if special.modify_attribute("Endurance", 1):
                    print("Endurance increased!")
            elif choice == "4":
                if special.modify_attribute("Charisma", 1):
                    print("Charisma increased!")
            elif choice == "5":
                if special.modify_attribute("Intelligence", 1):
                    print("Intelligence increased!")
            elif choice == "6":
                if special.modify_attribute("Agility", 1):
                    print("Agility increased!")
            elif choice == "7":
                if special.modify_attribute("Luck", 1):
                    print("Luck increased!")
            elif choice == "8":
                special.display_attributes()
            elif choice == "9":
                print("\nRestarting attribute distribution...")
                special.randomize_attributes()
                special.display_attributes()
            elif choice == "0":
                if special.get_available_points() > 0:
                    confirm = input(f"\nYou still have {special.get_available_points()} points. Finish anyway? (y/n): ").strip().lower()
                    if confirm == 'y':
                        break
                else:
                    break
            else:
                print("Invalid choice!")
        
        print("\n" + "="*60)
        print("CHARACTER CREATION COMPLETE!")
        print("="*60)
        special.display_attributes()
        
        return special
    
    def create_rooms(self, player_charisma):
        """
        Create the game map with rooms.
        Charisma affects item drop rates.
        
        Args:
            player_charisma (int): Player's Charisma attribute
        """
        room_descriptions = [
            "a dark dungeon entrance",
            "a dimly lit corridor",
            "a treasure chamber",
            "an ancient library",
            "a throne room",
            "a mysterious cave",
            "a forgotten armory",
            "a mystic sanctuary"
        ]
        
        # Charisma increases item spawn rate
        item_spawn_rate = 0.3 + (player_charisma * 0.05)
        
        # Create a 3x3 grid of rooms
        for x in range(-1, 2):
            for y in range(-1, 2):
                desc = random.choice(room_descriptions)
                room = Room(f"You are in {desc}.")
                
                # Randomly add enemies (60% chance)
                if random.random() < 0.6 and (x, y) != (0, 0):
                    enemy = Enemy.create_random_enemy(self.__player.get_level())
                    room.set_enemy(enemy)
                
                # Randomly add items (affected by Charisma)
                if random.random() < item_spawn_rate and (x, y) != (0, 0):
                    item = Item.create_random_item()
                    room.set_item(item)
                
                self.__rooms[(x, y)] = room
    
    def display_room(self):
        """Display current room information."""
        room = self.__rooms[self.__current_room]
        print(f"\n{room.get_description()}")
        
        if not room.is_visited():
            room.mark_visited()
            
            if room.has_enemy():
                print(f"A {room.get_enemy().get_name()} appears!")
            
            if room.has_item():
                print(f"You spot a {room.get_item().get_name()} on the ground.")
    
    def combat(self, enemy):
        """
        Handle combat between player and enemy.
        
        Args:
            enemy (Enemy): The enemy to fight
            
        Returns:
            bool: True if player wins, False if player loses
        """
        print(f"\n{'='*50}")
        print(f"COMBAT: {self.__player.get_name()} vs {enemy.get_name()}")
        print(f"{'='*50}")
        
        while self.__player.is_alive() and enemy.is_alive():
            # Display health
            print(f"\n{self.__player.get_name()}: {self.__player.get_health()}/{self.__player.get_max_health()} HP")
            print(f"{enemy.get_name()}: {enemy.get_health()}/{enemy.get_max_health()} HP")
            
            print("\nWhat will you do?")
            print("1) Attack")
            print("2) Use Item")
            print("3) Try to Flee")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                # Player attacks
                damage, is_crit = self.__player.attack(enemy)
                print(f"\nYou attack {enemy.get_name()} for {damage} damage!")
                
                if not enemy.is_alive():
                    print(f"\n{enemy.get_name()} has been defeated!")
                    self.__player.add_experience(enemy.get_exp_reward())
                    return True
                
                # Enemy attacks back
                if self.__player.try_dodge():
                    print(f"\n{enemy.get_name()} attacks but you dodge!")
                else:
                    enemy_damage = enemy.attack(self.__player)
                    print(f"\n{enemy.get_name()} attacks you for {enemy_damage} damage!")
                
            elif choice == "2":
                # Use item
                if len(self.__player.get_inventory()) == 0:
                    print("\nYou have no items!")
                    continue
                
                print("\nInventory:")
                for i, item in enumerate(self.__player.get_inventory()):
                    print(f"{i + 1}) {item.get_name()} ({item.get_type()})")
                
                try:
                    item_choice = int(input("\nSelect item (0 to cancel): ").strip())
                    if item_choice == 0:
                        continue
                    if self.__player.use_item(item_choice - 1):
                        # Enemy still gets to attack
                        if self.__player.try_dodge():
                            print(f"\n{enemy.get_name()} attacks but you dodge!")
                        else:
                            enemy_damage = enemy.attack(self.__player)
                            print(f"\n{enemy.get_name()} attacks you for {enemy_damage} damage!")
                except ValueError:
                    print("Invalid input!")
                    continue
                
            elif choice == "3":
                # Try to flee (based on Luck)
                luck = self.__player.get_special_attributes().get_attribute("Luck")
                flee_chance = 30 + (luck * 5)
                
                if random.randint(1, 100) <= flee_chance:
                    print("\nYou successfully fled from combat!")
                    return False
                else:
                    print("\nYou failed to escape!")
                    # Enemy attacks
                    if self.__player.try_dodge():
                        print(f"\n{enemy.get_name()} attacks but you dodge!")
                    else:
                        enemy_damage = enemy.attack(self.__player)
                        print(f"\n{enemy.get_name()} attacks you for {enemy_damage} damage!")
            else:
                print("Invalid choice!")
                continue
            
            # Check if player died
            if not self.__player.is_alive():
                print(f"\n{self.__player.get_name()} has been defeated!")
                print("GAME OVER")
                return False
        
        return True
    
    def move_player(self, direction):
        """
        Move player to adjacent room.
        
        Args:
            direction (str): Direction to move (north, south, east, west)
            
        Returns:
            bool: True if move was successful
        """
        x, y = self.__current_room
        
        if direction == "north":
            new_room = (x, y + 1)
        elif direction == "south":
            new_room = (x, y - 1)
        elif direction == "east":
            new_room = (x + 1, y)
        elif direction == "west":
            new_room = (x - 1, y)
        else:
            print("Invalid direction!")
            return False
        
        if new_room in self.__rooms:
            self.__current_room = new_room
            print(f"\nYou move {direction}.")
            return True
        else:
            print("\nYou can't go that way!")
            return False
    
    def show_inventory(self):
        """Display player inventory."""
        if len(self.__player.get_inventory()) == 0:
            print("\nYour inventory is empty.")
        else:
            print("\n" + "="*50)
            print("INVENTORY")
            print("="*50)
            for i, item in enumerate(self.__player.get_inventory()):
                print(f"{i + 1}) {item.get_name()} - {item.get_type()} (value: {item.get_value()})")
            print("="*50)
    
    def game_loop(self):
        """Main game loop."""
        while self.__game_running:
            self.display_room()
            room = self.__rooms[self.__current_room]
            
            # Handle combat if enemy present
            if room.has_enemy():
                enemy = room.get_enemy()
                if self.combat(enemy):
                    room.clear_enemy()
                    # Check for item drop (affected by Charisma)
                    charisma = self.__player.get_special_attributes().get_attribute("Charisma")
                    drop_chance = 0.3 + (charisma * 0.05)
                    if random.random() < drop_chance:
                        item = Item.create_random_item()
                        print(f"\n{enemy.get_name()} dropped a {item.get_name()}!")
                        self.__player.add_item(item)
                else:
                    if not self.__player.is_alive():
                        self.__game_running = False
                        continue
            
            # Pick up item if present
            if room.has_item():
                item = room.get_item()
                pickup = input(f"\nPick up {item.get_name()}? (y/n): ").strip().lower()
                if pickup == 'y':
                    self.__player.add_item(item)
                else:
                    # Put the item back if not picked up
                    room.set_item(item)
            
            # Show menu
            print("\n" + "="*50)
            print("What would you like to do?")
            print("1) Move North")
            print("2) Move South")
            print("3) Move East")
            print("4) Move West")
            print("5) View Stats")
            print("6) View Inventory")
            print("7) Save Game")
            print("8) Quit")
            print("="*50)
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self.move_player("north")
            elif choice == "2":
                self.move_player("south")
            elif choice == "3":
                self.move_player("east")
            elif choice == "4":
                self.move_player("west")
            elif choice == "5":
                self.__player.display_stats()
            elif choice == "6":
                self.show_inventory()
            elif choice == "7":
                self.__player.save_to_file()
            elif choice == "8":
                print("\nThanks for playing!")
                self.__game_running = False
            else:
                print("Invalid choice!")
    
    def start_new_game(self):
        """Start a new game."""
        print("\n" + "="*60)
        print("WELCOME TO THE DUNGEON CRAWLER RPG")
        print("="*60)
        
        # Get player name
        player_name = input("\nEnter your character's name: ").strip()
        if not player_name:
            player_name = "Hero"
        
        # Create character with S.P.E.C.I.A.L.
        special = self.create_special_character()
        
        # Create player
        self.__player = Player(player_name, special)
        
        # Create game world
        player_charisma = special.get_attribute("Charisma")
        self.create_rooms(player_charisma)
        
        print(f"\nWelcome, {player_name}! Your adventure begins...")
        self.__player.display_stats()
        
        input("\nPress Enter to start your adventure...")
        
        # Start game loop
        self.game_loop()
    
    def load_game(self):
        """Load a saved game."""
        player = Player.load_from_file()
        
        if player is None:
            return False
        
        self.__player = player
        
        # Recreate game world
        player_charisma = player.get_special_attributes().get_attribute("Charisma")
        self.create_rooms(player_charisma)
        
        print(f"\nWelcome back, {player.get_name()}!")
        self.__player.display_stats()
        
        input("\nPress Enter to continue your adventure...")
        
        # Start game loop
        self.game_loop()
        return True
    
    def main_menu(self):
        """Display main menu and handle selection."""
        while True:
            print("\n" + "="*60)
            print("DUNGEON CRAWLER RPG - MAIN MENU")
            print("="*60)
            print("1) New Game")
            print("2) Load Game")
            print("3) Exit")
            print("="*60)
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                self.start_new_game()
                break
            elif choice == "2":
                if not self.load_game():
                    print("\nReturning to main menu...")
                else:
                    break
            elif choice == "3":
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice!")