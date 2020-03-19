

import numpy as np 	# For arrays
import math 		# For useful mathematical operations
import random 		# For generators
import time			# For measuring the pass of time
import os 			# For path and console operations

# Clear console
clear = lambda: os.system('clear')

# User input prompt symbol
input_txt = ".[*]/"



"""
	VERSION

	0.0.1 - 19/03/2020
		- First self-consistent version.
		- Simple main menu, intro sequence, tutorial, and basic terminal.

	0.0.2 - 19/03/2020
		- Added: Modify status of modules through command line arguments
		- Skip intro suing 'boot' in main menu
		- Improved tutorial to keep up with development

	TASKS
	- Finish tutorial
	- Solve bug to turn module on/off
	- Improve help command (suage of [module] [on/off/float])
	- Solve command-names/module-index confusion
"""


# Game class. Contains everything.
class Game():
	def __init__(self):
		# Game commands
		self.cmd = None
		# Link to ship systems class
		self.ship = None

		# Measures pass of real time
		self.time_passed = 0
		# Game loop variable
		self.run = True
		# Player name
		self.name = None
		# Ship location. Will evolve into more complex class
		self.location = None
		# Number of commands
		self.cmd_num = None

	def setup(self):
		self.location = "(unknown)"
		self.ship = Ship()
		self.cmd = []
		# Module commands
		self.cmd.append(Commands("reactor",	"Modify status of Reactor"))
		self.cmd.append(Commands("support",	"Modify status of Life Support Systems"))
		self.cmd.append(Commands("engine",	"Modify status of Engine"))
		self.cmd.append(Commands("hyperdr",	"Modify status of Hyperdrive"))
		# Basic commands
		self.cmd.append(Commands("help",	"displays available commands"))
		self.cmd.append(Commands("status",	"updates ship's status"))
		self.cmd.append(Commands("exit",	"quits game"))
		# Number of commands
		self.ncmd = len(self.cmd)
		
		
	def fancy_boot_up(self):
		delay = 2
		print(" Booting up...")
		time.sleep(delay)
		print("///////////////////////")
		print("  NOVAMIND MEGASYSTEMS")
		print("///////////////////////")
		print(" NovaMind OS [v40.5.125]\n")
		time.sleep(delay)
		print(" ERROR: no previous logs detected.")
		print(" WARNING: Battery levels very low! (2%)")
		time.sleep(delay*1.5)
		print(" Error Management procedures activated.")
		print(" Secure Mode activated. Human input required.")
		print(" Running wake-up procedures...")
		input(" (press any key to continue)")

		print("\n\n[..] Welcome back. You have been brought back from hybernation.")
		print("[..] Internal chamber clock shows last hybernation period was [146930] days long.")
		print("[..] You might be disoriented or have slight memory loss. Please, stay calm.")
		input("[..] Press any key to continue...\n")
		
		print("[..] Warning: unknown booting-up errors detected.")
		print("[..] All previous ship logs have been overwritten.")
		self.name = input("[..] Please, input your name: ")

		print("\n[..] Hello, %s." % self.name)
		print("[..] System was booted through Safe Mode. Diagnostics show no further errors.")
		print("[..] Ship command has been transfered to you.")
		print("[..] Do you wish to run a tutorial on operating the ship? (yes/no)")
		dotut = input(input_txt)
		if(dotut=='yes' or dotut=='y'):
			self.tutorial()

	def tutorial(self):
		print("[..] You can communicate with the ship using commands. ")
		print("[..] Begin by typing the command 'help'.")
		while(input(input_txt) != "help"):
			continue
		self.print_help()
		print("[..] In doubt, use this command. It shows what other commands you can use.")
		print("[..] Now, the second most important command, type 'status'.")
		while(input(input_txt) != "status"):
			continue
		self.print_status()
		print("[..] This command tells you important info about the ship.")
		print("[..] Status shows whether the module is on (1) or off (0).")
		print("[..] Power shows the capacity at which the module is functioning.")
		input("[..] Press any key to continue...\n")
		self.print_status()
		print("[..] At the bottom you can see the main resources of the ship.")
		print("[..] You can see the energy is very low (as the ship is running on the battery)")
		print("[..] Try turning on the reactor with the command 'reactor on'.")
		while(input(input_txt) != "reactor on"):
			continue
		self.interpreter("reactor on")
		self.print_status()
		print("[..] The reactor is now on. However, it is not generating energy!")
		print("[..] Try increasing the reactor output to 20% with 'reactor 20'.")
		while(input(input_txt) != "reactor 20"):
			continue
		self.interpreter("reactor 20")
		self.print_status()
		print("[..] Great! Now the reactor is generating enough energy to supply the ship's systems.")
		print("[..] If you turn-on more systems or increase their power, ")
		print("[..] you will need to increase the reactor's output to keep up with the ship's needs.")
		print("[..] You can modify the status of other modules in a similar way.")
		input("[..] Press any key to continue...\n")
		print("[..] This is the end of the tutorial, good luck out there!")


	def print_help(self):
		for c in self.cmd:
			print(" -%s     	:%s" % (c.name, c.desc))

	def print_status(self):
		stats = self.ship.stats

		print(" ____________________________________________")
		print(" Module  	Status  Power   Energy")
		for m in self.ship.modules:
			print(" %s 	%d 	%.1f%%" %(m.name, m.state, m.power))
		print(" --------------------------------------------")
		print(" Net energy production here!")
		print(" ____________________________________________")
		print(" Hull(%d/%d)  Energy(%d/%d) "
				% (stats.hull, stats.max_hull, stats.energy, stats.max_energy))
		print(" Fuel(%d/%d)  Oxygen(%d/%d) " 
				% (stats.fuel, stats.max_fuel, stats.oxygen, stats.max_oxygen))
		print(" ____________________________________________")
		print(" Location: %s" % self.location)
		print(" ____________________________________________")

	# Compares input command with a list of valid commands.
	# Returns the command list index if input command is valid.
	# and None otherwise.
	def interpreter(self,inputc):
		#Splits input command into list of arguments
		s = inputc.split()
		#No arguments (user just pressed enter)
		if(len(s) == 0):
			return None
		#Collect command names
		cmd_names = [c.name for c in self.cmd]
		if s[0] not in cmd_names:
			print("[..] Error: command '%s' not recognised" % s[0])
			return None
		cind = cmd_names.index(s[0])
		# Basic commands
		if(s[0] == "help"):
			self.print_help()
		elif(s[0] == "status"):
			self.print_status()
		elif(s[0] == "exit"):
			return (-1)
		#Module commands
		else:
			if(len(s)!=2):
				print("[..] Error: wrong number of arguments")
			elif(isfloat(s[1])):
				self.ship.modules[cind].set_power(float(s[1]))
			elif(s[1]=='on'):
				self.ship.modules[cind].state == 1
			elif(s[1]=='off'):
				self.ship.modules[cind].state == 0
			else:
				print("[..] Error: invalid argument '%s'" % s[1])
		return None


	def main_loop(self):
		while(self.run):
			# -----Input here
			c = input(input_txt)
			retval = self.interpreter(c)
			if(retval == -1):
				break



# Simply stores known commands
class Commands():
	def __init__(self, name, desc):
		self.name = name 	#Command name
		self.desc = desc 	#Command description




"""
	===============================
			SHIP CLASSES
	===============================
"""

# Ship class -- all related to ship
class Ship():
	def __init__(self):
		self.stats = Stats()
		self.modules = []
		self.modules.append(Modules("Reactor", 		1, 15.0))
		self.modules.append(Modules("Life Support", 1, 50.0))
		self.modules.append(Modules("Engines", 		0, 0.0))
		self.modules.append(Modules("Hyperdrive", 	0, 0.0))
		self.modules.append(Modules("Computer", 	1, 10.0))
		# Number of modules
		self.nmodules = len(self.modules)

# Ship vitals and resources
class Stats():
	def __init__(self):
		# Actual stats
		self.hull = 100
		self.oxygen = 100
		self.energy = 100
		self.fuel = 100
		# Max stats (tanks filled)
		self.max_hull = 100
		self.max_oxygen = 100
		self.max_energy = 100
		self.max_fuel = 100
		# Rates show net gain/loss in resource
		self.hull_rate = 0
		self.oxygen_rate = 0
		self.energy_rate = 0
		self.fuel_rate = 0

	def evolve_stats(self):
		self.hull += self.hull_rate
		self.oxygen += self.oxygen_rate
		self.energy += self.oxygen_rate
		self.fuel += self.fuel_rate

# Ship modules and functioms
class Modules():
	def __init__(self, name, state, power):
		self.name = name
		self.state = state
		self.power = power
		# For damaged modules, max percentage goes down
		self.limit = 100.0

	def switch(self):
		sname = None
		if (self.state == 1):
			self.state = 0
			sname = 'off'
		elif (self.state == 0):
			self.state = 1
			sname = 'on'
		print("[..] %s is now %s" %(self.name, sname))

	def set_power(self, npow):
		if( npow<0 or npow>100):
			print("[..] Error: Input power out of range (0,100)")
			return
		if( npow>self.limit):
			print("[..] Error: %s is damaged. Can't use beyond %.1f%" %(self.name,self.limit))
			return
		self.power = npow



"""
	================================
			OTHER FUNCTIONS
	================================
"""
# Checks if input command is in command list
# Returns command list index on success, or None otherwise.
def check_input(inputc, commands):
	# Transforms into string just in case
	inputc = str(inputc)
	found = False
	cindex = 0
	for i,c in enumerate(self.main_commands):
		if (inputc == c):
			found = True
			cindex = i
	if(found == False):
		return None
	else:
		return cindex

# Checks if input string is a float
def isfloat(str):
	try:
		float(str)
		return True
	except ValueError:
		return False



def new_game():
	game = Game()
	game.setup()
	game.fancy_boot_up()
	game.main_loop()

def continue_game():
	game = Game()
	game.setup()
	game.main_loop()

def print_main_menu():
	print("\n\n\n")
	print(" === NovaMind Boot Loader ===\n")
	print(" Version v2177.12.67.1004")
	print(" Copyright: NovaMind Corp (2177)")
	print(" --WARNING: Kernel out-of-date (146917 days old)")
	print(" --Please upgrade with 'upgrade' command.\n")
	print(" Available commands: ")
	print(" 	- build		:start new game")
	print(" 	- boot 		:continue game")
	print(" 	- exit		:exit")
	print(" 	- upgrade	:upgrade kernel")

def main_menu():
	# Option = 	0(exit), 1(new game), 2(continue game)
	option = 0
	commands = np.array(['build', 'boot', 'exit', 'upgrade'])
	print_main_menu()

	while(True):
		c = input(input_txt)
		#retval = check_input(c, commands)
		if (c == "build"):
			option = 1
			break

		elif(c == "boot"):
			option = 2
			break
		
		elif(c == "exit"):
			break

		elif(c == 'upgrade'):
			print(" --WARNING: Could not connect to StarNet. Unable to upgrade.")
			continue
		
		else:
			print(" Error: unrecognised option")
			continue
		break

	return option



"""
	==============================
			MAIN FUNCTION
	==============================
"""

def main():
	option = main_menu()

	# Exit
	if (option == 0):
		return

	# New Game
	if (option == 1):
		new_game()

	# Continue
	if (option == 2):
		continue_game()

	return

if (__name__ == "__main__"):
	main()