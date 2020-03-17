

"""
	SPACE GAME

 This is a simple game on Python, created using the Arcade Module
for scenario generation testing.
 The game consists on a spaceship moving on space with realistic inertia.


	VERSION

	0.0.1 - 16 Mar 2020
		- Set-up Arcade

	0.0.2 - 17 Mar 2020
		- Initial Version.
		- Spaceship moving.
		- Wall bounce (dampless)
"""

import arcade
import random
from math import fabs

SCREEN_X = 800
SCREEN_Y = 800
title = "Space"


dt = 1

class PlayerData():
	def __init__(self, x, y, velx, vely):
		self.x = x
		self.y = y
		self.vx = velx
		self.vy = vely
		self.ax = 0
		self.ay = 0

		self.max_vel = 1
		self.max_acc = 0.1
		self.dt = 1

	def move(self):
		self.x += self.vx*dt + (0.5)*self.ax*dt**2
		self.vx += self.ax*dt

		self.y += self.vy*dt + (0.5)*self.ay*dt**2
		self.vy += self.ay*dt

		# Max velocity check
		if( fabs(self.vx) > self.max_vel):
			self.vx = (self.vx/fabs(self.vx))*self.max_vel

		if( fabs(self.vy) > self.max_vel):
			self.vy = (self.vy/fabs(self.vy))*self.max_vel

	def bounce(self, wall_x, wall_y):
		if (self.x > wall_x[1]):
			self.x = wall_x[1]
			self.vx = -fabs(self.vx)
			self.ax = 0
		elif (self.x < wall_x[0]):
			self.x = wall_x[0]
			self.vx = fabs(self.vx) 
			self.ax = 0

		if (self.y > wall_y[1]):
			self.y = wall_y[1]
			self.vy = -fabs(self.vy)
			self.ay = 0
		elif (self.y < wall_y[0]):
			self.y = wall_y[0]
			self.vy = fabs(self.vy) 
			self.ay = 0



class Object():
	def __init__(self):
		self.x = SCREEN_X/4
		self.y = SCREEN_Y/4

# Main game class
class Walker(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		self.player = None
		self.player_sprite = None
		self.pd = None

	def setup(self):
		# Initilaise player class & sprite
		self.pd = PlayerData(SCREEN_X/2, SCREEN_Y/2, 0, 0)
		self.player = arcade.SpriteList()
		self.player_sprite = arcade.Sprite("art/player_basic.png", 1)
		self.player_sprite.center_x = SCREEN_X/2
		self.player_sprite.center_y = SCREEN_Y/2
		self.player.append(self.player_sprite)

		# Background
		arcade.set_background_color(arcade.color.BLACK)

	def on_draw(self):
		arcade.start_render()
		self.player.draw()
		
	def on_update(self, dt):
		# Evolve player
		self.pd.move()
		self.player_sprite.center_x = self.pd.x
		self.player_sprite.center_y = self.pd.y
		self.pd.bounce( (0, SCREEN_X), (0, SCREEN_Y) )

	def on_key_press(self, key, modifiers):
		# Accelerate player
		if (key == arcade.key.W):
			self.pd.ay = self.pd.max_acc
			self.player_sprite.change_y = self.pd.vy

		elif (key == arcade.key.S):
			self.pd.ay = -self.pd.max_acc
			self.player_sprite.change_y = -self.pd.vy

		elif (key == arcade.key.A):
			self.pd.ax = -self.pd.max_acc
			self.player_sprite.change_x = -self.pd.vx

		elif (key == arcade.key.D):
			self.pd.ax = self.pd.max_acc
			self.player_sprite.change_x = self.pd.vx

	def on_key_release(self, key, modifiers):
		# Cut acceleration. Player now has constant speed.
		if (key == arcade.key.W or key == arcade.key.S):
			self.pd.ay = 0
		elif (key == arcade.key.A or key == arcade.key.D):
			self.pd.ax = 0
		




def main():
	game = Walker(SCREEN_X, SCREEN_Y, title)
	game.setup()
	arcade.run()

if __name__ == "__main__":
	main()