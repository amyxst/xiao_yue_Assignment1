class Ship:
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
            return "Ship {0} is destroyed. :(".format(self.name)
        else:
            return "Ship {} statistics:\nLaser power: {}\nShield strength: {}\nHull strength: {}\n".format(
                       self.name,
                       self.laser_power,
                       self.shield_strength,
                       self.hull_strength)

    def shoot(self, target):
        print "Ship {} launched a shot at ship {}!".format(self.name, target.name)
        #scenarios: remaining shield strength, no shield strength, hull strength, ship destroyed
    
        if target.shield_strength != 0 \
            and (target.shield_strength - self.laser_power) <= 0:
            remaining_laser = self.laser_power - target.shield_strength
            target.shield_strength = 0

            target.hull_strength -= remaining_laser
            target.destroyed = True if target.hull_strength <= 0 else False

class Warship(Ship):
    def __init__(self, name):
        Ship.__init__(self, name)
        self.hp_laser_power = 50


if __name__ == "__main__":
    aship = Ship("bob")
    bship = Ship("mary")
    print aship
    print bship

    aship.shoot(bship)
    print bship
