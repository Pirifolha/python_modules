# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 17:15:53 by misousa         #+#    #+#               #
#  Updated: 2026/03/10 18:10:40 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..ex1.ft_garden_data import Plant


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)


def grow() -> None:
    rose.height += 2


def age() -> None:
    rose.age += 1


def get_info() -> None:
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")


def main() -> None:
    day = 1
    while day <= 7:
        print(f"=== Day {day} ===")
        get_info()
        grow()
        age()
        day += 1
    print(f"Growth this week: +{2*6}cm")


if __name__ == "__main__":
    main()
