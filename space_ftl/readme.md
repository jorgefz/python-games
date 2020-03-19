# GALACTICA
## Space Exploration Game

Python-based game that revolves around surviving in a spaceship
whilst exploring the universe.

The game is text-based, imitating the user interface of a command terminal.
The user inputs commands and the ship responds.

## The Ship

The Ship has several key stats that are vital to its normal
functioning: hull integrity, oxygen, energy, and fuel.
	- Low hull integrity causes loss of oxygen.
	- Lack of oxygen kills you.
	- Lack of energy makes modules stop working, including the atmoshperic recycler.
	- Lack of fuel leaves you stranded in space.

The Ship also has several modules that perform various tasks in the ship:
	- Computer: lets you control and manage the ship as well as performing analysis on
			gathered data.
	- Reactor: fusion reactor that produces energy at a certain rate. Allows to power
			all other modules in the ship. The user must manage energy
			consumption wisely to avoid overload.
	- Life Supprot: Reclycles air to make a breathable atmoshpere, regulates temperature, etc.
	- Engines: For moving the ship within a system and down to planets. Requires fuel.
	- Hyperdrive: For distorting spacetime to travel to other stars.
	- Extras: scanner, driller, shields, weaponry, comms, etc.

## Vitals & Resources
### Hull
 Mesure of the structural integrity of a ship. It is reduced when the ship is damaged
 becuse of attacks, explosions, or external phenomena.
 When the hull reaches new lows, more systems in the ship will cease to work:
	- Below 50%, the oxygen starts to run out.
	- Below 25%, fuel leaks.
	- Below 15%, the engines stop working.
	- Below 5%, the reactor stops working.
	- At 0%, the ship is destroyed!
 It can be repaired using materials collected from space.
### Energy
 The resource that powers the ship. Necessary for all modules to function.
 It is produced by the Reactor and can be stored in the battery.
### Oxygen
 Necessary for the player to breathe. It is only used by the player, which dies if it runs out.
 The atmosphere is recycled by the Life Support Module (which doesn't have a 100% efficiency),
 and can be stored in an Oxygen tank.
### Fuel
 Necessary for the ship's engines to move the ship. Stored in a fuel tank.
 If it runs out, the ship is stranded in space. It can be gathered from space.
### Hydrogen
 Fuel that the Reactor uses to generate energy. Widely available in space.

## Modules
### Computer
 The interface through which the player controls the ship.
 Communicate with computer using command line arguments to control the ship.
 The main Control Centre summarises the ship's status, like current vital resources,
 and 
### Reactor
 Produces energy at a certain rate fusing Hydrogen into Helium.
 Requires small amounts of hydrogen to work.
 Modules consume energy at a certain rate too, so ensure that the reactor produces enough
 energy to supply the demand, or turn off unused modules.
 The surplus energy goes into a battery.
 If the reactor is off or damaged, the ship will drain energy from the battery.
 If the battery runs out, you'll be stranded in space!
### Life Support
 
