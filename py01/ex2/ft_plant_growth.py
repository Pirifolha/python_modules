# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 17:15:53 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 18:01:57 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..ex1.ft_garden_data import *

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
