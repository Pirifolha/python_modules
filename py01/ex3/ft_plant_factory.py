# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 18:17:52 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 18:28:43 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    count = 0
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1

rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
tulip = Plant("Tulip", 8, 28)
lavender = Plant("Lavender", 13, 37)
orchid = Plant("Orchid", 12, 73)

def main():
    print(f"Created: {rose.name} ({rose.height} cm, {rose.age} days)")
    print(f"Created: {sunflower.name} ({sunflower.height} cm, {sunflower.age} days)")
    print(f"Created: {cactus.name} ({cactus.height} cm, {cactus.age} days)")
    print(f"Created: {tulip.name} ({tulip.height} cm, {tulip.age} days)")
    print(f"Created: {lavender.name} ({lavender.height} cm, {lavender.age} days)")
    print(f"Created: {orchid.name} ({orchid.height} cm, {orchid.age} days)\n")
    print(f"Total plants created {Plant.count}")

if __name__ == "__main__":
    main()