# GALACTICA
## Space Exploration Game

This document details how gameplay in the game will work.

## Introduction

This game is centered around space exploration and survival.
You have a small one-person ship that allows you to travel through the universe,
discovering unique systems and phenomena, and adding them to your logs.

You also have to take care of your ship. Using it will drain its resources,
which you should replenish from raw materials found in space.

Finally, there will be a storyline which you can follow, guiding the pilot to its origins.
But this story can me completely ignored too.

## Starting the game
The player wakes-up from hibernation in a small spaceship. The ship's computer has had an unknown 
error and all previous log files have been erased. You are asked for your name.
You are given a small tutorial to run the ship (which you can choose to skip) and off you go.

## Gameplay Overview
This is mainly a text-based game. All the necessary information will be displayed in the form of
text in the GUI.
You can power different modules in the ship to use an array of tools. These tools allow you to
interact with the universe, from which you can gather resources, explore planets and asteroids, etc.
A vast procedurally generated universe is out there for you to explore.

## The Ship
The ship has four vital resources: Hull, Energy, Oxygen, and Fuel.
Running out of any of these 'Vitals' will result in death and game-over.

The Ship also has a number of main 'Modules', which control the main functionalities
of the ship: Reactor, Life Support, Engines, and Hyperdrive.
All these consume some resources and produce others at a certain rate.
You can turn these modules on are off, and edit they percentage at which they function.
For example, "Reactor - On - 35%"

Based on these modules, the ship also has a number of 'Tools', that allow it to interact
with the universe. These tools both require a certain amount of energy to run and for a
certain module to be functioning above a given percentage threshold.
For example, the Scanner would require the Antenna Module to be running at 50% at least,
and more energy the further you want the scanner to reach, or the more precise it is.

### Ship Vitals
 - Hull
Ship's structural integrity. Repaired using (yet unspecified) metals from space.
Reduced via external damage (solar flares, atmospheric entry, crashes, etc).
Low levels creates oxygen leaks and other problems.
 - Energy
Produced by the reactor, used by everything else. Stored in the battery.
 - Oxygen
Gathered from space ice or atmospheres. Used by life support and player.
Stored in oxygen tank.
 - Fuel
Used by engines to move ship within a star system. Synthesised from space materials.
Stored in fuel tank.

### Ship Systems
 - Reactor
Fusion reactor uses hydrogen to generate energy.
 - Life Support
Supplies oxygen to ship's atmosphere and recycles it.
 - Antenna
Powers scanners and comms.
 - Engines
Move the ship within a star system. Consumes fuel.
 - Hyperdrive
Allow interstellar travel. The more power, the larger the jump range.
VERY power hungry.

### Ship Tools
 - Scanner
Powered by the Antenna. Scans obejcts and systems for physical information.
It can scan far-away stars for physical info, look for planets in a system,
look for asteroids in an area of space, maps a planet, etc.
Different scan types will have different energy and Antenna power requirements.
Scanner results can be displayed in the screen.
 - Drill
Allows to harvest mineral resources from asteroids and planets.
 - Recycler
Reuses atmospheric air, extracting Oxygen from Carbon Dioxide exhaled by player.
Uses up energy but consumes little Oxygen.
The alternative is using the Oxygen Tank directly, but consumes a lot of Oxygen
and little energy.
 - Defences
Defence systems against agressors. Not sure if include or not.
 - Comms
Allows to communicate with others. Not sure if include or not.
 - Self-repair
Allows to self-repair the Hull with collected materials. Consumes energy.

### Ship Resources
 - Oxygen
Stored in Oxygen tank directly. Used by Life Support automatically.
 - Hydrogen
Stored in Hydrogen tank automatically, which is a small tank.
Used by Reactor automaitcally.
 - Engine Fuel
Synthesised from other materials and stored in fuel tank.
Used automatically by engines.
 - Hull materials
Synthesised from other materials. Used by Self-repair to regenerate hull.

### Ship Logs 
Keeps track of every system/planet scanned.


## Travelling
The ship can travel to different star systems and planets.
This is done by going to the 'Logs' tabs, looking for the 
