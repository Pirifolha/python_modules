# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 18:10:02 by misousa         #+#    #+#               #
#  Updated: 2026/03/04 16:52:56 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    x = int(input("Day 1 Harvest: "))
    y = int(input("Day 2 Harvest: "))
    z = int(input("Day 3 Harvest: "))
    print("Total harvest:", x + y + z)
