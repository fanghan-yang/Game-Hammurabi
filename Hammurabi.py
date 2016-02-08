# Hammurabi.py
import random

def print_intro():
        '''Print introduction'''
        print """Congrats, you are the newest ruler of ancient Samaria, elected for a ten year
term of office. Your duties are to distribute food, direct farming, and buy and
sell land as needed to support your people. Watch out for rat infestations and
the resultant plague! Grain is the general currency, measured in bushels. The
following will help you in your decisions:

        (a) Each person needs at least 20 bushels of grain per year to survive.
        (b) Each person can farm at most 10 acres of land.
        (c) It takes 2 bushels of grain to farm an acre of land.
        (d) The market price for land fluctuates yearly.
        
Rule wisely and you will be showered with appreciation at the end of your term.
Rule poorly and you will be kicked out of office!"""

def ask_to_buy_land(bushels, cost):
        '''Ask user how many bushels to spend buying land.'''
        acres = input("How many acres will you buy? ")
        while acres * cost > bushels:
                print "O great Hammurabi, we have but", bushels, "bushels of grain!"
                acres = input("How many acres will you buy? ")
        return acres

def ask_to_sell_land(acres):
        '''Ask user how much land they want to sell.'''
        acres_to_sell = input("How many acres will you sell? ")
        while acres_to_sell > acres:
                print "O great Hammurabi, we have but", acres, "acres of land!"
                acres_to_sell = input("How many acres will you sell? ")
        return acres_to_sell
        
def ask_to_feed(bushels):
        '''Ask user how many bushels they want to use for feeding.'''
        bushels_to_feed = input("How many bushels will you feed the people? ")
        while bushels_to_feed > bushels:
                print "O great Hammurabi, we have but", bushels, "bushels of grain!"
                bushels_to_feed = input("How many bushels will you feed the people? ")
        return bushels_to_feed

def ask_to_cultivate(acres, population, bushels):
        '''Ask user how much land they want to plant seed in.'''
        acres_to_plant = input("How many acres will you plant with seed? ")
        while acres_to_plant > min(acres, 10 * population, bushels/2):
                if acres_to_plant > acres:
                        print "O great Hammurabi, we have but", acres, "acres of land!"
                        acres_to_plant = input("How many acres will you plant with seed? ")
                elif acres_to_plant > 10 * population:
                        print "O great Hammurabi, we have but", population, "people!"   # each person can till at most 10 acres of land
                        acres_to_plant = input("How many acres will you plant with seed? ")
                else:
                        print "O great Hammurabi, we have but", bushels, "bushels of grain!"    # each acre requires two bushels to plant seeds
                        acres_to_plant = input("How many acres will you plant with seed? ")
        return acres_to_plant

def is_plague():
        '''Check if there is a horrible plague'''
        r = random.randint(1, 100)
        if r <= 15:
                print "  - Terrible! There is a severe plague, half people die..."
                return True     # half people die
        else:
                print "  - Luckily, no plague this year!"
                return False

def num_starving(population, bushels):
        '''Calculate number of people starving'''
        num_feed = bushels/20   # each person needs 20 bushels to survive
        if num_feed > population:
                return 0
        else:
                return population - num_feed

def num_immigrants(land, grain_in_storage, population, num_starving):
        '''Calculate number of immigrants'''
        if num_starving == 0:
                immigrants = (20 * land + grain_in_storage)/(100 * population + 1)
                print "  -", immigrants, "immigrants come to the city this year!"
                return immigrants
        else:
                print "  - No immigrants this year..."
                return 0

def get_harvest():
        '''Calculate harvest'''
        r = random.randint(1, 8)
        print "  - Grain gets rippen and harvested!"
        return r

def do_rats_infest():
        '''Check if there is a rat infestation'''
        r = random.randint(1, 100)
        if r <= 40:
                print "  - Terrible! There is a rat infestation, some bushels of grain are eaten..."
                return True
        else:
                print "  - Luckily, no rat infestation this year!"
                return False

def percent_destroyed():
        '''Determine the percentage of bushels destoryed'''
        r = random.randint(10,30)
        return float(r)/100

def price_of_land():
        '''Determine land price for next year'''
        r = random.randint(16, 22)
        return r

def final_summary(total_starved, acres_owned, population, bushels_in_storage, plague_times, rat_times):
        '''Print Summery'''
        print "****************************** Congrats ******************************"
        print "You have been a successful ruler in the past ten years!"
        print
        print "During your reigh:"
        if total_starved == 0:
                print "    No one starved. What a miracle!"
        else:
                print "    Only", total_starved, "people starved."
        if plague_times > 0 and rat_times > 0:
                print "    You led people to survive in", plague_times, "plagues and", rat_times,"rat infestations."
        elif plague_times > 0:
                print "    You led people to survive in", plague_times, "plagues."
        elif rat_times > 0:
                print "    You led people to survive in", rat_times, "rat infestations."
        print "    You ended up with", acres_owned, "acres land,", population, "population,"
        print "         and", bushels_in_storage, "bushels of grain in your city."
        if float(acres_owned)/population > 10:
                print "    You started with 10 acres per person and ended with", float(acres_owned)/population
                print "         acres per person."
        elif bushels_in_storage > 2800:
                print "    You had so many bushels in storage to buy more land in a more seasonable price."
        print
        print "My dear lord, you are now the top Hammurabi ruler!"
        print "A new prosperous era begins!"
        print
        print "    The end..."
        print
        print "Saving..."
        print "Done"
        print

def Hammurabi():
	# declare variables
	starved = 0
	immigrants = 5
	population = 100
	harvest = 3000		# total bushels harvested
	bushels_per_acre = 3 	# amount harvested for each acre planted
	rats_ate = 200 		# bushels destoryed by rats
	bushels_in_storage = 2800
	acres_owned = 1000
	cost_per_acre = 19	# each acre costs this many bushels
	plague_deaths = 0
	total_starved = 0
	plague_times = 0
	rat_times = 0
	# call print intro
	print_intro()
	print
        # year rounds begin
	for year in range(1,11):
                
		# report at the begin of each year
		print "*************************** New Year Round ***************************"
		print "      O great Hammurabi!"
		print "      You are in year " + str(year) + " of your ten year rule."
		print "      In the previous year " + str(starved) + " people starved to death."
		print "      In the previous year " + str(immigrants) + " people entered the kingdom."
		print "      The population is now " + str(population) + "."
		print "      We harvested " + str(harvest) + " bushels at " + str(bushels_per_acre) + " bushels per acre."
		print "      Rats destroyed " + str(rats_ate) + " bushels, leaving " + str(bushels_in_storage) + " bushels in storage."
		print "      The city owns " + str(acres_owned) + " acres of land."
		print "      Land is currently worth " + str(cost_per_acre) + " bushels per acre."
		print "      There were " + str(plague_deaths) + " deaths from the plague."
		print
		
		# ask for the Great Hammurabi (the user) to make some decisions
		acres_to_buy = ask_to_buy_land(bushels_in_storage, cost_per_acre)
		print
		
		if acres_to_buy == 0:
			acres_to_cell = ask_to_sell_land(acres_owned)
			print
		else:
			acres_to_cell = 0
		acres_owned = acres_owned + acres_to_buy - acres_to_cell        # update acres_owned, buy land
		bushels_in_storage = bushels_in_storage - cost_per_acre * (acres_to_buy - acres_to_cell)       # update bushels_in_storage, cell land
		
		bushels_to_feed = ask_to_feed(bushels_in_storage)
		bushels_in_storage = bushels_in_storage - bushels_to_feed       # update bushels_in_storage, feed people
		print
		
		acres_to_plant = ask_to_cultivate(acres_owned, population, bushels_in_storage)
		bushels_in_storage = bushels_in_storage - 2 * acres_to_plant    # update bushels_in_storage, each acre requires two bushels to plant seeds
		print

		if is_plague():
			plague_times += 1
			plague_deaths = population/2
			population = population - plague_deaths                 # update population, plague
		else:
			plague_deaths = 0
		print

		starved = num_starving(population, bushels_to_feed)
		if float(starved)/population > 0.45:
			print "****************************** Fail ******************************"
			print "    More than 45% people starved. People uprise."
			print "    Your suppression failed after 41 days..."
			print
			print "    Game over..."
			print
			return          # game over
		if starved == 0:
			print "  - No people die for starving. Good job!"
		else:
			print "  - A few people die for starving, but not a big deal..."
			population = population - starved                       # update population, starving
		print

		immigrants = num_immigrants(acres_owned, bushels_in_storage, population, starved)
		population = population + immigrants                            # update population, immigrants
		print

		bushels_per_acre = get_harvest()
		harvest = bushels_per_acre * acres_to_plant
		bushels_in_storage = bushels_in_storage + harvest               # update bushels_in_storage, harvest
		print

		if do_rats_infest():
			rat_times += 1
			p = percent_destroyed()
			rats_ate = int(p * bushels_in_storage)
			bushels_in_storage = bushels_in_storage - rats_ate      # update bushels_in_storage, rat infestation
		else:
			rats_ate = 0
		print

		cost_per_acre = price_of_land()
		total_starved = total_starved + starved

	final_summary(total_starved, acres_owned, population, bushels_in_storage, plague_times, rat_times)


if __name__ == "__main__":
	Hammurabi()
