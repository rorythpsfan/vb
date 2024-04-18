import pygame
import constants as C
import math
import time
import player as P
import imageController as IC
import gameOver as GO
import collisions
import random
import cameraModule
import levels
import socialMech as SM
import screenFade
import explosions
import titlescreen
import kickstarter as ks
import webbrowser



def main():
	pygame.init()
	previousTime = time.time()
	oneSecondTimer = 0

	player = P.Player()
	ts = titlescreen.TitleScreen()
	camera = cameraModule.Camera(player)
	C.LEVEL = levels.Level0(player)
	socialmech = SM.SocialMech(player)
	kickstarter = ks.KickstarterLink()
	screenfade = screenFade.Fade(player)
	



	while not C.QUIT:

			for event in pygame.event.get():

				#Check For Exit
				if event.type == pygame.QUIT:
					C.QUIT = True

				#Q key to quit#
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						C.QUIT = True

					if event.key == pygame.K_o:
						player.overloaded = True

					if event.key == pygame.K_y:
						C.LEVEL.advance = True
					if event.key == pygame.K_t:
						C.LEVEL.reverse = True

					if event.key == pygame.K_SPACE and player.inFlyingLevel:
						player.shoot()

					if event.key == pygame.K_UP and socialmech.isVisible == True:
						socialmech.selected_option = (socialmech.selected_option - 1) % len(socialmech.npc_game_states[socialmech.current_state]["options"])
					if event.key == pygame.K_DOWN and socialmech.isVisible == True:
						socialmech.selected_option = (socialmech.selected_option + 1) % len(socialmech.npc_game_states[socialmech.current_state]["options"])
					if event.key == pygame.K_RETURN and socialmech.isVisible == True and socialmech.done == False:
						next_state = list(socialmech.npc_game_states[socialmech.current_state]["options"].values())[socialmech.selected_option]
						socialmech.current_state = next_state
						socialmech.selected_option = 0

				#elif event.type == pygame.MOUSEBUTTONDOWN:
				#	ts = titlescreen.TitleScreen()

				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and kickstarter.isVisible == True:
					if kickstarter.button_rect.collidepoint(event.pos):
						webbrowser.open(kickstarter.link)

			C.CLOCK.tick(C.FPS)
			# Compute delta time
			now = time.time()
			C.DT = now - previousTime
			previousTime = now

			C.SCREEN.fill('black')

			if C.GAMEOVER == True:
				GO.show_game_over_screen()

			if player.isInvincible == False:
				collisions.checkCollisions(player, socialmech, C.LEVEL, kickstarter)

			if player.inOverheadLevel == False:
				C.LEVEL.update()
				C.all_sprites_list.update()
				C.all_sprites_list.draw(C.SCREEN)

			if player.inOverheadLevel == True:
				C.all_sprites_list.update()
				C.firefly_list.update()

				pos = (0 - camera.position.x,0 - camera.position.y)
				C.LEVEL.Render_Map(pos[0], pos[1], player)



				camera.move()

				for sprite in C.all_sprites_list:
					sprite.draw(C.SCREEN, camera)

				screenfade.update()


				for sprite in C.firefly_list:
					sprite.draw(C.SCREEN, camera)

				C.LEVEL.drawLights(pos[0], pos[1])


	
				if socialmech.isVisible == True:
					socialmech.update()

				if kickstarter.isVisible == True:
					kickstarter.update()

				C.LEVEL.update()

			oneSecondTimer += C.DT
			#print (oneSecondTimer)
			if oneSecondTimer >= 1:
				print ("It has been one second")
				oneSecondTimer = 0

			#print (C.CLOCK.get_fps())		
			#print (C.DT)
			pygame.display.flip() 

	pygame.quit()

if __name__ == "__main__":
	#import cProfile as profile
	#profile.run('main()')	
	main()
