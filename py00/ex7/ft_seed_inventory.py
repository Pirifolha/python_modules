# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 17:44:27 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 17:14:52 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "area" and unit != "grams":
        print("Unknown unit type")
    else:
        print(seed_type.capitalize(), "seeds:", quantity, unit, "available")
