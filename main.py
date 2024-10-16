import pygame
import sys
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from bullet import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	

	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for objects in updatable:
			objects.update(dt)
		for objects in asteroids:
			for bullets in shots:
				if objects.collision(bullets):
					objects.split()
					bullets.kill()
			if objects.collision(player):
				sys.exit("Game over!")
		screen.fill("black")
		for objects in drawable:
			objects.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

	
		


if __name__ == "__main__":
	main()
