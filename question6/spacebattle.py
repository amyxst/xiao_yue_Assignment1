import random

class Ship(object):
    def __init__(
            self,
            name,
            laser_power=20,
            shield_strength=400,
            hull_strength=300):
        self.name = name
        self.laser_power = laser_power
        self.shield_strength = shield_strength
        self.hull_strength = hull_strength
        self.destroyed = False
   
    def __str__(self):
        if self.destroyed is True:
            return "Ship {0} is destroyed. :(\n".format(self.name)
        else:
            return "Ship {} statistics:\nShield strength: {}\nHull strength: {}\n".format(
                       self.name,
                       self.shield_strength,
                       self.hull_strength)

    def shoot(self, target):
        print "Ship {} launched a shot of power {} at Ship {}!".format(self.name, self.laser_power, target.name)
        target._is_shot(self)

    def _is_shot(self, src_ship, src_power=None):
        """
        scenarios:
        a) remaining shield strength
        b) no shield strength but hull strength
        c) ship destroyed
        """
        if src_ship is self:
            print "A ship cannot attack itself...!\n"
            return

        attack_power = src_power if src_power is not None else src_ship.laser_power

        if self.destroyed is True:
            pass
        elif self.shield_strength != 0:
            original_shield = self.shield_strength

            if (self.shield_strength - attack_power) <= 0:
                remaining_laser = attack_power - self.shield_strength
                self.shield_strength = 0
                
                self.hull_strength -= remaining_laser
                self.destroyed = True if self.hull_strength <= 0 else False
            else:
                self.shield_strength -= attack_power

        elif self.shield_strength == 0 and self.hull_strength != 0:
            remaining_laser = attack_power / 2
            if (self.hull_strength - remaining_laser) <= 0:
                self.hull_strength = 0
                self.destroyed = True
            else:
                self.hull_strength -= remaining_laser

        print self

class Warship(Ship):
    def __init__(self, name):
        Ship.__init__(self, name)
        self.hp_laser_power = 50

    def shoot(self, target):
        if random.random() <= 0.3:
            print "Ship {} has charged its laser! Ship {} launched an extra big blast of power {} towards ship {}!\n".format(self.name, self.name, self.hp_laser_power, target.name)

            target._is_shot(self, self.hp_laser_power)
        else: 
            super(Warship, self).shoot(target)

class Speeder(Ship):
    def __init__(self, name):
        Ship.__init__(self, name)

    def _is_shot(self, src_ship, src_power=None):
        if random.random() <= 0.5: # evades laser 50% of the time
            print "Ship {} evaded laser from {}!\n".format(self.name, src_ship.name)
        else:
            super(Speeder, self)._is_shot(src_ship)        

def init_game(ships):
    if len(ships) < 2:
        print "Insufficient number of ships to start a game."

    def pick_ship(ships):
        return int(round(random.uniform(len(ships)-1,0)))
        
    #Initiates and monitors game status.
    print "===\nStarting Diagnostics\n==="
    for ship in ships:
        print ship
    print "==="

    gameover = False

    while not gameover:
        target = ships[pick_ship(ships)]
        attacker = ships[pick_ship(ships)]

        if target is not attacker:
            attacker.shoot(target)
            if target.destroyed:
                ships.remove(target)
        
            if len(ships) == 1:
                gameover = True

    print "Ship {} has won the battle!\n\nGameover".format(ships[0].name)

if __name__ == "__main__":
    ships = [Ship("Ol' A"), Ship("Ol' B"), Ship("Ol' C"), Warship("Warzo"), Speeder("Evader")]
    init_game(ships)
    """
    aship = Ship("bob")
    bship = Speeder("mary")
    cship = Warship("diego")

    ships = [aship, bship, cship]

    print "===\nStarting Diagnostics\n==="
    for ship in ships:
        print ship
    print "==="

    for i in xrange(2):
       for attacker in ships:
          for target in ships:
              if attacker is not target:
                  attacker.shoot(target)
    """
