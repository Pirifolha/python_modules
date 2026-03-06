# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 16:54:42 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 17:14:40 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    x = int(input("Enter plant age in days: "))
    if x > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
