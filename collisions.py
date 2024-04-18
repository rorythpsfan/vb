import pygame
import constants as C
import explosions

def checkCollisions(player, socialmech, level, kickstarter):

	#Check if an enemy collided with a player If so damage or destroy player#
	for x in C.player_sprite_list:
		enemy_hit_list = pygame.sprite.spritecollide(x, C.enemy_sprite_list, False, pygame.sprite.collide_mask)
		for x in enemy_hit_list:
			x.destroy()
			for x in C.player_sprite_list:
				x.health -= 10

	for x in C.bullet_list:
		enemy_hit_list = pygame.sprite.spritecollide(x, C.enemy_sprite_list, False, pygame.sprite.collide_mask)
		#Destroy Bullets that hit enemies#
		for x in C.enemy_sprite_list:
			bullet_hit_list = pygame.sprite.spritecollide(x, C.bullet_list, True, pygame.sprite.collide_mask)
			for x in bullet_hit_list:
				spitsplosion = explosions.SpitSplosion(x.rect.midleft)
				x.destroy()
		#Destroy enemy if hp = 0#
		for x in enemy_hit_list:
			x.hitPoints -= 1
			if x.hitPoints == 0:
				x.destroy()

	if player.inOverheadLevel == True:
		npc_hit_list = pygame.sprite.spritecollide(x, C.npc_list, False, pygame.sprite.collide_mask)
		for x in npc_hit_list:


			if pygame.Rect.colliderect(x.rect, level.oldLady.rect) == True:

				keys = pygame.key.get_pressed()
				if keys[pygame.K_k]:
					player.inSocialMech = True
					socialmech.isVisible = True
					socialmech.current_state = "start"
					socialmech.smt = True

				socialmech.npc_game_states = socialmech.npc1_game_states
				socialmech.currentNPC = "oldLady"
				print ("Locked on old lady")


			elif pygame.Rect.colliderect(x.rect, level.emo.rect) == True:
				#socialmech.npc_game_states = socialmech.npc2_game_states
				#socialmech.currentNPC = "emo"
				print ("Locked on emo")
				kickstarter.isVisible = True

			elif pygame.Rect.colliderect(x.rect, level.gymBro.rect) == True:
				#socialmech.npc_game_states = socialmech.npc4_game_states
				#socialmech.currentNPC = "gymBro"
				print ("Locked on gymBro")
				kickstarter.isVisible = True

			elif pygame.Rect.colliderect(x.rect, level.hippy.rect) == True:
				#socialmech.npc_game_states = socialmech.npc3_game_states
				#socialmech.currentNPC = "hippy"
				print ("Locked on hippy")
				kickstarter.isVisible = True

			elif pygame.Rect.colliderect(x.rect, level.pinkDress.rect) == True:
				#socialmech.npc_game_states = socialmech.npc5_game_states
				#socialmech.currentNPC = "pinkDress"
				print ("Locked on pinkDress")
				kickstarter.isVisible = True
		if not npc_hit_list:
			kickstarter.isVisible = False
