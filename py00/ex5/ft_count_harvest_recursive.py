# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 17:18:22 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 17:14:47 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def helper(x, y):
        if x >= y:
            print("Day", y)
            helper(x, y + 1)
        else:
            print("Harvest time!")
    helper(x, 1)
