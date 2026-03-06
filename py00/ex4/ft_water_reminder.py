# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: misousa <misousa@student.42lisboa.com>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 17:01:02 by misousa         #+#    #+#               #
#  Updated: 2026/03/06 17:14:43 by misousa         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    x = int(input("Days since last watering: "))
    if x > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
