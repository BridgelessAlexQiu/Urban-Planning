from collections import defaultdict
import numpy as np

# ------------------------open file--------------------------------#
nyc = open("nyc.txt", encoding='ISO-8859-1')
#------------------------------------------------------------------#

'''
the dictonary 'user_checkin_history' (defined below) contains inputs to POPTICS
Data format:
{
    user_1 : [(venue_category_1, lantitude_1, longtitude_1), (venue_category_2, lantitude_2, longtitude_2) ...],
    user_2 : [(venue_category_i, lantitude_i, longtitude_i), (venue_category_i+1, lantutide_i+1, longtitude_i+1) ...],
    user_3 : [...],
    ...    :  ... ,
    user_n : [...]
}
'''
user_checkin_history = defaultdict(list)



#---------------------extract data from file-----------------------------#
for line in nyc:
    # index 3 : venue category, 4 : Latitude, 5 : Longitude
    lst = line.split('\t')
    
    # lantitude and longtitude
    lantitude = float(lst[4])
    longtitude = float(lst[5])
    
    # venue category, combine categories into a single category
    category = lst[3]
    if 'Restaurant' in category:
        venue_category = 'Restaurant'
    elif 'Joint' in category:
        venue_category = 'Food Joint'
    elif 'Museum' in category:
        venue_category = 'Museum'
    else:
        venue_category = category
    
    # construct the checkin
    single_checkin = (venue_category, lantitude, longtitude)
    
    # add this checking location, lst[0] is the user's id
    user_checkin_history[lst[0]].append(single_checkin)
#----------------------------------------------------------------------#



#-------------------remove insignificant venues categories and users-----------#
# format : {venue_category_1 : count 1, venue_category_2 : count 2, ...}
venue_count = defaultdict(lambda : 0)
for user, checkins in user_checkin_history.items():
    for checkin in checkins:
        venue_count[checkin[0]] += 1

# delete all checkins whose venue categories have not been visited over 1200 times
for user, checkins in user_checkin_history.items():
    new_checkins = []
    for checkin in checkins:
        if venue_count[checkin[0]] >= 1200:
            new_checkins.append(checkin)
    user_checkin_history[user] = new_checkins

# remove users who visited less than 100 places
remove = []
for user, checkins in user_checkin_history.items():
    if len(checkins) < 100:
        remove.append(user)
for r in remove:
    del user_checkin_history[r]
#----------------------------------------------------------------------------------#


#---------------------------Remaining users---------------------------#
users = []
for user in user_checkin_history.keys():
    users.append(user)
#---------------------------------------------------------------------#


#-------------------------Example code-------------------------------#
def poptics(checkin_location, yita):
    # something...
    pass

# Example : run POPIICS on user 10, note that the user id '10' is a string
poptics(user_checkin_history['10'], 0.5)

# Example : run POPTICS on every user:
for user in users:
    poptics(user_checkin_history[user], 0.5)