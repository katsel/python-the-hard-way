class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
Central Corridor. Get the bomb, put it in the bridge, blow the ship up after
getting into an escape pod.

A Gothon is blocking your way.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You tell the Gothon a joke and it is laughing and can't move.
You enter Weapon Armory.

The bomb is locked with a keypad. If you get the code wrong 10 times you
can't get the bomb. The code is 3 digits.
""")

the_bridge = Room("The Bridge",
"""
You take the bomb and run to the bridge.

There's 5 Gothons here.
""")

escape_pod = Room("Escape_Pod",
"""
You place the bomb on the floor, get out of the bridge and lock the Gothons in.

You run to the chamber with the escape pods. Some of them could be damaged.
Which one do you take?
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and fly away. The ship explodes. You win!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and eject, then it implodes.
""")


escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor
