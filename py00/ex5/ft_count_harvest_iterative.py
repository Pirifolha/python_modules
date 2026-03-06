# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 17:06:30 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 17:14:45 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))
    y = range(1, x + 1)
    for n in y:
        print("Day", n)
    print("Harvest time!")
