import pygame
import BJ_gameconfig as bjgc
import random
import os
from pygame import display, event, image
import time
import sys
import subprocess

pygame.init()

while True:

    pygame.init()

    bl = 'BlackJack.exe'

    background = (0, 32, 47)

    restart1 = False

    event = pygame.event.get()

    # random cards
    cards_randomchoice = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice)
    cards_randomchoice2 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice2)
    cards_randomchoice_ai1 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice_ai1)
    cards_randomchoice_ai2 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice_ai2)
    cards_randomchoice_ai3 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice_ai3)
    cards_randomchoice3 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice3)
    cards_randomchoice4 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice4)
    cards_randomchoice5 = random.choice(bjgc.BJCARDS_FILES)
    bjgc.BJCARDS_FILES.remove(cards_randomchoice5)

    # images files
    path = os.getcwd()
    randomcard_user1 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice
    randomcard_user2 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice2
    randomcard_user3 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice3
    randomcard_user4 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice4
    randomcard_user5 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice5
    ai_randomcard1 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice_ai1
    ai_randomcard2 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice_ai2
    ai_randomcard3 = path + "\\" + "blackjackcards" + "\\" + cards_randomchoice_ai3
    ai_upturnedcard = 'vcard' + '\\' + 'z verso.png'
    hit_botton = path + '\\' + 'hit_stand_botton' + '\\' + 'hit_botton.JPG'
    stand_botton = path + '\\' + 'hit_stand_botton' + '\\' + 'stand_botton.JPG'
    restart = path + '\\' + 'hand_restart_win_images' + '\\' + 'restartbutton.png'
    win = path + '\\' + 'hand_restart_win_images' + '\\' + 'win.png'
    tie =  path + '\\' + 'hand_restart_win_images' + '\\' + 'tie.png'

    # Hand nuser files
    yourhand4 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand4.png'
    yourhand5 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand5.png'
    yourhand6 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand6.png'
    yourhand7 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand7.png'
    yourhand8 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand8.png'
    yourhand9 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand9.png'
    yourhand10 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand10.png'
    yourhand11 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand11.png'
    yourhand12 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand12.png'
    yourhand13 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand13.png'
    yourhand14 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand14.png'
    yourhand15 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand15.png'
    yourhand16 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand16.png'
    yourhand17 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand17.png'
    yourhand18 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand18.png'
    yourhand19 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand19.png'
    yourhand20 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand20.png'
    yourhand21 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand21.png'
    yourhand22 = path + '\\' + 'hand_restart_win_images' + '\\' + 'yourhand21+.png'

    #Hand ai files
    aihand4 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand4.png'
    aihand5 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand5.png'
    aihand6 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand6.png'
    aihand7 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand7.png'
    aihand8 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand8.png'
    aihand9 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand9.png'
    aihand10 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand10.png'
    aihand11 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand11.png'
    aihand12 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand12.png'
    aihand13 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand13.png'
    aihand14 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand14.png'
    aihand15 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand15.png'
    aihand16 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand16.png'
    aihand17 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand17.png'
    aihand18 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand18.png'
    aihand19 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand19.png'
    aihand20 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand20.png'
    aihand21 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand21.png'
    aihand22 = path + '\\' + 'hand_restart_win_images' + '\\' + 'aihand21+.png'



    # images
    image_ru1 = pygame.image.load(randomcard_user1)
    image2_ru2 = pygame.image.load(randomcard_user2)
    image3_air1 = pygame.image.load(ai_randomcard1)
    image4_aiuc = pygame.image.load(ai_upturnedcard)
    image5_hit = pygame.image.load(hit_botton)
    image6_stand = pygame.image.load(stand_botton)
    image7_ru3 = pygame.image.load(randomcard_user3)
    image8_air2 = pygame.image.load(ai_randomcard2)
    image9_ru4 = pygame.image.load(randomcard_user4)
    image10_ru5 = pygame.image.load(randomcard_user5)
    image11_rt = pygame.image.load(restart)
    image12_win = pygame.image.load(win)
    image13_tie = pygame.image.load(tie)
    image14_ai3card = pygame.image.load(ai_randomcard3)

    # Hand user images print
    image1_yh = pygame.image.load(yourhand4)
    image2_yh = pygame.image.load(yourhand5)
    image3_yh = pygame.image.load(yourhand6)
    image4_yh = pygame.image.load(yourhand7)
    image5_yh = pygame.image.load(yourhand8)
    image6_yh = pygame.image.load(yourhand9)
    image7_yh = pygame.image.load(yourhand10)
    image8_yh = pygame.image.load(yourhand11)
    image9_yh = pygame.image.load(yourhand12)
    image10_yh = pygame.image.load(yourhand13)
    image11_yh = pygame.image.load(yourhand14)
    image12_yh = pygame.image.load(yourhand15)
    image13_yh = pygame.image.load(yourhand16)
    image14_yh = pygame.image.load(yourhand17)
    image15_yh = pygame.image.load(yourhand18)
    image16_yh = pygame.image.load(yourhand19)
    image17_yh = pygame.image.load(yourhand20)
    image18_yh = pygame.image.load(yourhand21)
    image19_yh = pygame.image.load(yourhand22)

    #Ai hand number
    image1_aih = pygame.image.load(aihand4)
    image2_aih = pygame.image.load(aihand5)
    image3_aih = pygame.image.load(aihand6)
    image4_aih = pygame.image.load(aihand7)
    image5_aih = pygame.image.load(aihand8)
    image6_aih = pygame.image.load(aihand9)
    image7_aih = pygame.image.load(aihand10)
    image8_aih = pygame.image.load(aihand11)
    image9_aih = pygame.image.load(aihand12)
    image10_aih = pygame.image.load(aihand13)
    image11_aih = pygame.image.load(aihand14)
    image12_aih = pygame.image.load(aihand15)
    image13_aih = pygame.image.load(aihand16)
    image14_aih = pygame.image.load(aihand17)
    image15_aih = pygame.image.load(aihand18)
    image16_aih = pygame.image.load(aihand19)
    image17_aih = pygame.image.load(aihand20)
    image18_aih = pygame.image.load(aihand21)
    image19_aih = pygame.image.load(aihand22)

    # images sizes

    width = 60
    height = 100

    width_hs = 130
    height_hs = 60

    width_hd = 220
    height_hd = 320

    width_aihd = 200
    height_aihd = 250

    width_rt = 170
    height_rt = 260

    width_win = 180
    height_win = 200

    # images sizes
    image_user1 = pygame.transform.scale(image_ru1, (width, height))
    image_user2 = pygame.transform.scale(image2_ru2, (width, height))
    image_ai1 = pygame.transform.scale(image3_air1, (width, height))
    image_ai3 = pygame.transform.scale(image14_ai3card, (width, height))
    image_aiup = pygame.transform.scale(image4_aiuc, (width, height))
    image_hitbutton = pygame.transform.scale(image5_hit, (width_hs, height_hs))   #hit button
    image_standbutton = pygame.transform.scale(image6_stand, (width_hs, height_hs))   #stand button
    image_user3 = pygame.transform.scale(image7_ru3, (width, height))
    image_aiup1 = pygame.transform.scale(image8_air2, (width, height))
    image_user4 = pygame.transform.scale(image9_ru4, (width, height))
    image_user5 = pygame.transform.scale(image10_ru5, (width, height))
    image_restart = pygame.transform.scale(image11_rt, (width_rt, height_rt))
    image_win = pygame.transform.scale(image12_win, ( width_win, height_win))
    image_tie = pygame.transform.scale(image13_tie, (width_win, height_win))

    # hand number size
    image_hand4 = pygame.transform.scale(image1_yh, (width_hd, height_hd))
    image_hand5 = pygame.transform.scale(image2_yh, (width_hd, height_hd))
    image_hand6 = pygame.transform.scale(image3_yh, (width_hd, height_hd))
    image_hand7 = pygame.transform.scale(image4_yh, (width_hd, height_hd))
    image_hand8 = pygame.transform.scale(image5_yh, (width_hd, height_hd))
    image_hand9 = pygame.transform.scale(image6_yh, (width_hd, height_hd))
    image_hand10 = pygame.transform.scale(image7_yh, (width_hd, height_hd))
    image_hand11 = pygame.transform.scale(image8_yh, (width_hd, height_hd))
    image_hand12 = pygame.transform.scale(image9_yh, (width_hd, height_hd))
    image_hand13 = pygame.transform.scale(image10_yh, (width_hd, height_hd))
    image_hand14 = pygame.transform.scale(image11_yh, (width_hd, height_hd))
    image_hand15 = pygame.transform.scale(image12_yh, (width_hd, height_hd))
    image_hand16 = pygame.transform.scale(image13_yh, (width_hd, height_hd))
    image_hand17 = pygame.transform.scale(image14_yh, (width_hd, height_hd))
    image_hand18 = pygame.transform.scale(image15_yh, (width_hd, height_hd))
    image_hand19 = pygame.transform.scale(image16_yh, (width_hd, height_hd))
    image_hand20 = pygame.transform.scale(image17_yh, (width_hd, height_hd))
    image_hand21 = pygame.transform.scale(image18_yh, (width_hd, height_hd))
    image_hand22 = pygame.transform.scale(image19_yh, (width_hd, height_hd))

    # ai hand number size
    image_ai4 = pygame.transform.scale(image1_aih, (width_aihd, height_aihd))
    image_ai5 = pygame.transform.scale(image2_aih, (width_aihd, height_aihd))
    image_ai6 = pygame.transform.scale(image3_aih, (width_aihd, height_aihd))
    image_ai7 = pygame.transform.scale(image4_aih, (width_aihd, height_aihd))
    image_ai8 = pygame.transform.scale(image5_aih, (width_aihd, height_aihd))
    image_ai9 = pygame.transform.scale(image6_aih, (width_aihd, height_aihd))
    image_ai10 = pygame.transform.scale(image7_aih, (width_aihd, height_aihd))
    image_ai11 = pygame.transform.scale(image8_aih, (width_aihd, height_aihd))
    image_ai12 = pygame.transform.scale(image9_aih, (width_aihd, height_aihd))
    image_ai13 = pygame.transform.scale(image10_aih, (width_aihd, height_aihd))
    image_ai14 = pygame.transform.scale(image11_aih, (width_aihd, height_aihd))
    image_ai15 = pygame.transform.scale(image12_aih, (width_aihd, height_aihd))
    image_ai16 = pygame.transform.scale(image13_aih, (width_aihd, height_aihd))
    image_ai17 = pygame.transform.scale(image14_aih, (width_aihd, height_aihd))
    image_ai18 = pygame.transform.scale(image15_aih, (width_aihd, height_aihd))
    image_ai19 = pygame.transform.scale(image16_aih, (width_aihd, height_aihd))
    image_ai20 = pygame.transform.scale(image17_aih, (width_aihd, height_aihd))
    image_ai21 = pygame.transform.scale(image18_aih, (width_aihd, height_aihd))
    image_ai22 = pygame.transform.scale(image19_aih, (width_aihd, height_aihd))

    # others
    display.set_caption('BlackJack')
    screen = display.set_mode((600, bjgc.SCREEN_SIZE))
    hit_and_stand = True
    card3 = False
    card4 = False
    card5 = False
    ai1card = False
    next_card = False
    next_card2 = False
    stophitbutton = False
    card1_v = False
    card2_v = False
    card3_v = False
    card4_v = False
    card5_v = False
    card1ai_v = False
    card2ai_v = False
    card3ai_v = False
    cardv3 = False
    fristhand = False
    secondhand = False
    thirdhand = False
    fourthand = False
    aifirsthand = False
    aisecondhand = False
    hand2_value = False
    hand3_value = False
    secondhand_true = True
    thirdhand_true = True
    fourthand_true = True
    aihand = True
    aisecondhand_true = True
    show_ai = True
    stand_sla = False
    whowins = False
    morethan21 = False
    valuelocation = -20, -100
    valuelocationai = -20, 320
    location_win_user = 300, 70
    location_win_ai = 300, 170
    location_tie = 300, 120
    location_user_final = 100, 10
    location_ai_final = 120, 150
    finalhand = 0
    finalhand2 = 0
    finalhand_ai = 0
    finalhand_ai2 = 0


    # cards values
    if cards_randomchoice in bjgc.BJCARDS_FILES2:
        card1_v = True
        card1_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice)
    if cards_randomchoice2 in bjgc.BJCARDS_FILES2:
        card2_v = True
        card2_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice2)
    if cards_randomchoice3 in bjgc.BJCARDS_FILES2:
        card3_v = True
        card3_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice3)
    if cards_randomchoice4 in bjgc.BJCARDS_FILES2:
        card4_v = True
        card4_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice4)
    if cards_randomchoice5 in bjgc.BJCARDS_FILES2:
        card5_v = True
        card5_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice5)
    if cards_randomchoice_ai1 in bjgc.BJCARDS_FILES2:
        card1ai_v = True
        card1ai_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice_ai1)
    if cards_randomchoice_ai2 in bjgc.BJCARDS_FILES2:
        card2ai_v = True
        card2ai_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice_ai2)
    if cards_randomchoice_ai3 in bjgc.BJCARDS_FILES2:
        card3ai_v = True
        card3ai_va = bjgc.BJCARDS_FILES2.index(cards_randomchoice_ai3)

    bjgc.BJCARDS_FILES2[0] = 10
    bjgc.BJCARDS_FILES2[1] = 10
    bjgc.BJCARDS_FILES2[2] = 10
    bjgc.BJCARDS_FILES2[3] = 10
    bjgc.BJCARDS_FILES2[4] = 2
    bjgc.BJCARDS_FILES2[5] = 2
    bjgc.BJCARDS_FILES2[6] = 2
    bjgc.BJCARDS_FILES2[7] = 2
    bjgc.BJCARDS_FILES2[8] = 3
    bjgc.BJCARDS_FILES2[9] = 3
    bjgc.BJCARDS_FILES2[10] = 3
    bjgc.BJCARDS_FILES2[11] = 3
    bjgc.BJCARDS_FILES2[12] = 4
    bjgc.BJCARDS_FILES2[13] = 4
    bjgc.BJCARDS_FILES2[14] = 4
    bjgc.BJCARDS_FILES2[15] = 4
    bjgc.BJCARDS_FILES2[16] = 5
    bjgc.BJCARDS_FILES2[17] = 5
    bjgc.BJCARDS_FILES2[18] = 5
    bjgc.BJCARDS_FILES2[19] = 5
    bjgc.BJCARDS_FILES2[20] = 6
    bjgc.BJCARDS_FILES2[21] = 6
    bjgc.BJCARDS_FILES2[22] = 6
    bjgc.BJCARDS_FILES2[23] = 6
    bjgc.BJCARDS_FILES2[24] = 7
    bjgc.BJCARDS_FILES2[25] = 7
    bjgc.BJCARDS_FILES2[26] = 7
    bjgc.BJCARDS_FILES2[27] = 7
    bjgc.BJCARDS_FILES2[28] = 8
    bjgc.BJCARDS_FILES2[29] = 8
    bjgc.BJCARDS_FILES2[30] = 8
    bjgc.BJCARDS_FILES2[31] = 8
    bjgc.BJCARDS_FILES2[32] = 9
    bjgc.BJCARDS_FILES2[33] = 9
    bjgc.BJCARDS_FILES2[34] = 9
    bjgc.BJCARDS_FILES2[35] = 9
    bjgc.BJCARDS_FILES2[36] = 11
    bjgc.BJCARDS_FILES2[37] = 11
    bjgc.BJCARDS_FILES2[38] = 11
    bjgc.BJCARDS_FILES2[39] = 11
    bjgc.BJCARDS_FILES2[40] = 10
    bjgc.BJCARDS_FILES2[41] = 10
    bjgc.BJCARDS_FILES2[42] = 10
    bjgc.BJCARDS_FILES2[43] = 10
    bjgc.BJCARDS_FILES2[44] = 10
    bjgc.BJCARDS_FILES2[45] = 10
    bjgc.BJCARDS_FILES2[46] = 10
    bjgc.BJCARDS_FILES2[47] = 10
    bjgc.BJCARDS_FILES2[48] = 10
    bjgc.BJCARDS_FILES2[49] = 10
    bjgc.BJCARDS_FILES2[50] = 10
    bjgc.BJCARDS_FILES2[51] = 10

    if card1_v == True:
        card1_value = (bjgc.BJCARDS_FILES2[card1_va])
    if card2_v == True:
        card2_value = (bjgc.BJCARDS_FILES2[card2_va])
        cardv3 = True
        hand1 = card1_value + card2_value
    if card3_v == True:
        card3_value = (bjgc.BJCARDS_FILES2[card3_va])
        hand2 = hand1 + card3_value
    if card4_v == True:
        card4_value = (bjgc.BJCARDS_FILES2[card4_va])
        hand3 = hand2 + card4_value
    if card5_v == True:
        card5_value = (bjgc.BJCARDS_FILES2[card5_va])
        hand4 = hand3 + card5_value
    if card1ai_v == True:
        card1ai_value = (bjgc.BJCARDS_FILES2[card1ai_va])
    if card2ai_v == True:
        card2ai_value = (bjgc.BJCARDS_FILES2[card2ai_va])
        hand1ai = card1ai_value + card2ai_value
    if card3ai_v == True:
        card3ai_value = (bjgc.BJCARDS_FILES2[card3ai_va])
        hand2ai = card3ai_value + hand1ai

    #finalhand_ai = hand1ai

    # Game
    while True:
        screen.fill(background)
        screen.blit(image_user1, (175, 0))
        screen.blit(image_user2, (240, 0))
        screen.blit(image_ai1, (240, 400))
        screen.blit(image_aiup, (175, 400))
        screen.blit(image_restart, (420, 410))

        if hit_and_stand == True:
            screen.blit(image_hitbutton, (120, 130))
            screen.blit(image_standbutton, (280, 130))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart1 = True
            # Hit button first time
            if ai1card == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if my < 187 and my > 130 and mx > 120 and mx < 245:
                        card3 = True
                        fristhand = True

            # Hit button second time
            if next_card == True:
                if ai1card == False:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if my < 187 and my > 130 and mx > 120 and mx < 250:
                            card4 = True
                            secondhand = False
            # Hit button third time and last time
            if next_card2 == True:
                if ai1card == False:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if my < 187 and my > 130 and mx > 120 and mx < 250:
                            card5 = True
                            whowins = True
                            ai1card = True

            # stand button
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if m_y < 187 and m_y > 130 and m_x > 279 and m_x < 409:
                    ai1card = True
                    stand_sla = True

        # user card 3 appears
        if card3 == True:
            screen.blit(image_user3, (305, 0))
            next_card = True
            secondhand = True
        # user card 4 appears
        if card4 == True:
            screen.blit(image_user4, (370, 0))
            next_card2 = True
            secondhand = False
            thirdhand = True
        # User card 5 and last card
        if card5 == True:
            screen.blit(image_user5, (435, 0))
            stophitbutton = True
            fourthand = True

        # ai upturned card appears
        if ai1card == True or stophitbutton == True:
            hit_and_stand = False
            screen.blit(image_aiup1, (175, 400))
            aifirsthand = True

        # print hand1 value
        if fristhand == False:
            if hand1 == 4:
                screen.blit(image_hand4, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 5:
                screen.blit(image_hand5, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 6:
                screen.blit(image_hand6, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 7:
                screen.blit(image_hand7, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 8:
                screen.blit(image_hand8, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 9:
                screen.blit(image_hand9, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 10:
                screen.blit(image_hand10, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 11:
                screen.blit(image_hand11, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 12:
                screen.blit(image_hand12, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 13:
                screen.blit(image_hand13, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 14:
                screen.blit(image_hand14, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 15:
                screen.blit(image_hand15, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 16:
                screen.blit(image_hand16, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 17:
                screen.blit(image_hand17, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 18:
                screen.blit(image_hand18, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 19:
                screen.blit(image_hand19, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 20:
                screen.blit(image_hand20, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 == 21:
                screen.blit(image_hand21, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1
            elif hand1 >= 22:
                screen.blit(image_hand22, (valuelocation))
                finalhand = hand1
                finalhand2 = hand1

        # Print second hand value
        if secondhand_true == True:
            if secondhand == True:
                if hand2 == 4:
                    screen.blit(image_hand4, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 5:
                    screen.blit(image_hand5, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 6:
                    screen.blit(image_hand6, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 7:
                    screen.blit(image_hand7, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 8:
                    screen.blit(image_hand8, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 9:
                    screen.blit(image_hand9, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 10:
                    screen.blit(image_hand10, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 11:
                    screen.blit(image_hand11, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 12:
                    screen.blit(image_hand12, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 13:
                    screen.blit(image_hand13, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 14:
                    screen.blit(image_hand14, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 15:
                    screen.blit(image_hand15, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 16:
                    screen.blit(image_hand16, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 17:
                    screen.blit(image_hand17, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 18:
                    screen.blit(image_hand18, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 19:
                    screen.blit(image_hand19, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 20:
                    screen.blit(image_hand20, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 == 21:
                    screen.blit(image_hand21, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2
                elif hand2 >= 22:
                    screen.blit(image_hand22, (valuelocation))
                    finalhand = hand2
                    finalhand2 = hand2

        # Print third hand value
        if thirdhand_true == True:
            if thirdhand == True:
                if hand3 == 4:
                    screen.blit(image_hand4, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 5:
                    screen.blit(image_hand5, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 6:
                    screen.blit(image_hand6, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 7:
                    screen.blit(image_hand7, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 8:
                    screen.blit(image_hand8, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 9:
                    screen.blit(image_hand9, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 10:
                    screen.blit(image_hand10, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 11:
                    screen.blit(image_hand11, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 12:
                    screen.blit(image_hand12, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 13:
                    screen.blit(image_hand13, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 14:
                    screen.blit(image_hand14, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 15:
                    screen.blit(image_hand15, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 16:
                    screen.blit(image_hand16, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 17:
                    screen.blit(image_hand17, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 18:
                    screen.blit(image_hand18, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 19:
                    screen.blit(image_hand19, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 20:
                    screen.blit(image_hand20, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 == 21:
                    screen.blit(image_hand21, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3
                elif hand3 >= 22:
                    screen.blit(image_hand22, (valuelocation))
                    finalhand = hand3
                    finalhand2 = hand3

        #print fourth hand
        if fourthand_true == True:
            if fourthand == True:
                if hand4 == 4:
                    screen.blit(image_hand4, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 5:
                    screen.blit(image_hand5, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 6:
                    screen.blit(image_hand6, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 7:
                    screen.blit(image_hand7, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 8:
                    screen.blit(image_hand8, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 9:
                    screen.blit(image_hand9, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 10:
                    screen.blit(image_hand10, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 11:
                    screen.blit(image_hand11, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 12:
                    screen.blit(image_hand12, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 13:
                    screen.blit(image_hand13, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 14:
                    screen.blit(image_hand14, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 15:
                    screen.blit(image_hand15, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 16:
                    screen.blit(image_hand16, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 17:
                    screen.blit(image_hand17, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 18:
                    screen.blit(image_hand18, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 19:
                    screen.blit(image_hand19, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 20:
                    screen.blit(image_hand20, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 == 21:
                    screen.blit(image_hand21, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4
                elif hand4 >= 22:
                    screen.blit(image_hand22, (valuelocation))
                    finalhand = hand4
                    finalhand2 = hand4

        #Ai 1 hand value
        if aihand == True:
            if aifirsthand == True or finalhand >= 22 or finalhand == 21:
                if hand1ai == 4:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 5:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 6:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 7:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 8:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 9:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 10:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 11:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 12:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 13:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 14:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 15:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 16:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 17:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 18:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 19:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 20:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                elif hand1ai == 21:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                    handai1_value = True
                elif hand1ai >= 22:
                    finalhand_ai = hand1ai
                    finalhand_ai2 = hand1ai
                aisecondhand = True


        if aisecondhand == True:
            aihand = False
            if finalhand_ai2 <= 15 and finalhand_ai2 < finalhand and finalhand <= 21:
                screen.blit(image_ai3, (305, 400))
                if hand2ai == 4:
                    finalhand_ai = hand2ai
                elif hand2ai == 5:
                    finalhand_ai = hand2ai
                elif hand2ai == 6:
                    finalhand_ai = hand2ai
                elif hand2ai == 7:
                    finalhand_ai = hand2ai
                elif hand2ai == 8:
                    finalhand_ai = hand2ai
                elif hand2ai == 9:
                    finalhand_ai = hand2ai
                elif hand2ai == 10:
                    finalhand_ai = hand2ai
                elif hand2ai == 11:
                    finalhand_ai = hand2ai
                elif hand2ai == 12:
                    finalhand_ai = hand2ai
                elif hand2ai == 13:
                    finalhand_ai = hand2ai
                elif hand2ai == 14:
                    finalhand_ai = hand2ai
                elif hand2ai == 15:
                    finalhand_ai = hand2ai
                elif hand2ai == 16:
                    finalhand_ai = hand2ai
                elif hand2ai == 17:
                    finalhand_ai = hand2ai
                elif hand2ai == 18:
                    finalhand_ai = hand2ai
                elif hand2ai == 19:
                    finalhand_ai = hand2ai
                elif hand2ai == 20:
                    finalhand_ai = hand2ai
                elif hand2ai == 21:
                    finalhand_ai = hand2ai
                elif hand2ai >= 22:
                    finalhand_ai = hand2ai
        if stand_sla ==  True:
            whowins = True
        if finalhand == 21 or finalhand >= 22:
            ai1card = True
            whowins = True
        # Display who win the game
        if  whowins == True:
            # when user win
            if finalhand > finalhand_ai and finalhand < 22 or finalhand == 21 and finalhand != finalhand_ai or finalhand_ai >= 22:
                screen.blit(image_win, (location_win_user))
                fristhand = True
                secondhand_true = False
                thirdhand_true = False
                ai1card = True
                show_ai = False
                hit_and_stand = False
                aihand = False
                #userhandlocation
                if finalhand == 4:
                    screen.blit(image_hand4, (location_user_final))
                elif finalhand == 5:
                    screen.blit(image_hand5, (location_user_final))
                elif finalhand == 6:
                    screen.blit(image_hand6, (location_user_final))
                elif finalhand == 7:
                    screen.blit(image_hand7, (location_user_final))
                elif finalhand == 8:
                    screen.blit(image_hand8, (location_user_final))
                elif finalhand == 9:
                    screen.blit(image_hand9, (location_user_final))
                elif finalhand == 10:
                    screen.blit(image_hand10, (location_user_final))
                elif finalhand == 11:
                    screen.blit(image_hand11, (location_user_final))
                elif finalhand == 12:
                    screen.blit(image_hand12, (location_user_final))
                elif finalhand == 13:
                    screen.blit(image_hand13, (location_user_final))
                elif finalhand == 14:
                    screen.blit(image_hand14, (location_user_final))
                elif finalhand == 15:
                    screen.blit(image_hand15, (location_user_final))
                elif finalhand == 16:
                    screen.blit(image_hand16, (location_user_final))
                elif finalhand == 17:
                    screen.blit(image_hand17, (location_user_final))
                elif finalhand == 18:
                    screen.blit(image_hand18, (location_user_final))
                elif finalhand == 19:
                    screen.blit(image_hand19, (location_user_final))
                elif finalhand == 20:
                    screen.blit(image_hand20, (location_user_final))
                elif finalhand == 21:
                    screen.blit(image_hand21, (location_user_final))
                elif finalhand >= 22:
                    screen.blit(image_hand22, (location_user_final))
                #aihandlocation
                if finalhand_ai == 4:
                    screen.blit(image_ai4, (location_ai_final))
                elif finalhand_ai == 5:
                    screen.blit(image_ai5, (location_ai_final))
                elif finalhand_ai == 6:
                    screen.blit(image_ai6, (location_ai_final))
                elif finalhand_ai == 7:
                    screen.blit(image_ai7, (location_ai_final))
                elif finalhand_ai == 8:
                    screen.blit(image_ai8, (location_ai_final))
                elif finalhand_ai == 9:
                    screen.blit(image_ai9, (location_ai_final))
                elif finalhand_ai == 10:
                    screen.blit(image_ai10, (location_ai_final))
                elif finalhand_ai == 11:
                    screen.blit(image_ai11, (location_ai_final))
                elif finalhand_ai == 12:
                    screen.blit(image_ai12, (location_ai_final))
                elif finalhand_ai == 13:
                    screen.blit(image_ai13, (location_ai_final))
                elif finalhand_ai == 14:
                    screen.blit(image_ai14, (location_ai_final))
                elif finalhand_ai == 15:
                    screen.blit(image_ai15, (location_ai_final))
                elif finalhand_ai == 16:
                    screen.blit(image_ai16, (location_ai_final))
                elif finalhand_ai == 17:
                    screen.blit(image_ai17, (location_ai_final))
                elif finalhand_ai == 18:
                    screen.blit(image_ai18, (location_ai_final))
                elif finalhand_ai == 19:
                    screen.blit(image_ai19, (location_ai_final))
                elif finalhand_ai == 20:
                    screen.blit(image_ai20, (location_ai_final))
                elif finalhand_ai == 21:
                    screen.blit(image_ai21, (location_ai_final))
                elif finalhand_ai >= 22:
                    screen.blit(image_ai22, (location_ai_final))
            #when ai win
            if finalhand_ai > finalhand and finalhand_ai < 22 or finalhand >= 22:
                screen.blit(image_win, (location_win_ai))
                fristhand = True
                secondhand_true = False
                thirdhand_true = False
                fourthand_true = False
                ai1card = True
                show_ai = False
                hit_and_stand = False
                sla = False
                aihand = False
                # userhandlocation
                if finalhand == 4:
                    screen.blit(image_hand4, (location_user_final))
                elif finalhand == 5:
                    screen.blit(image_hand5, (location_user_final))
                elif finalhand == 6:
                    screen.blit(image_hand6, (location_user_final))
                elif finalhand == 7:
                    screen.blit(image_hand7, (location_user_final))
                elif finalhand == 8:
                    screen.blit(image_hand8, (location_user_final))
                elif finalhand == 9:
                    screen.blit(image_hand9, (location_user_final))
                elif finalhand == 10:
                    screen.blit(image_hand10, (location_user_final))
                elif finalhand == 11:
                    screen.blit(image_hand11, (location_user_final))
                elif finalhand == 12:
                    screen.blit(image_hand12, (location_user_final))
                elif finalhand == 13:
                    screen.blit(image_hand13, (location_user_final))
                elif finalhand == 14:
                    screen.blit(image_hand14, (location_user_final))
                elif finalhand == 15:
                    screen.blit(image_hand15, (location_user_final))
                elif finalhand == 16:
                    screen.blit(image_hand16, (location_user_final))
                elif finalhand == 17:
                    screen.blit(image_hand17, (location_user_final))
                elif finalhand == 18:
                    screen.blit(image_hand18, (location_user_final))
                elif finalhand == 19:
                    screen.blit(image_hand19, (location_user_final))
                elif finalhand == 20:
                    screen.blit(image_hand20, (location_user_final))
                elif finalhand == 21:
                    screen.blit(image_hand21, (location_user_final))
                elif finalhand >= 22:
                    screen.blit(image_hand22, (location_user_final))
                #ai hand location
                if finalhand_ai == 4:
                    screen.blit(image_ai4, (location_ai_final))
                elif finalhand_ai == 5:
                    screen.blit(image_ai5, (location_ai_final))
                elif finalhand_ai == 6:
                    screen.blit(image_ai6, (location_ai_final))
                elif finalhand_ai == 7:
                    screen.blit(image_ai7, (location_ai_final))
                elif finalhand_ai == 8:
                    screen.blit(image_ai8, (location_ai_final))
                elif finalhand_ai == 9:
                    screen.blit(image_ai9, (location_ai_final))
                elif finalhand_ai == 10:
                    screen.blit(image_ai10, (location_ai_final))
                elif finalhand_ai == 11:
                    screen.blit(image_ai11, (location_ai_final))
                elif finalhand_ai == 12:
                    screen.blit(image_ai12, (location_ai_final))
                elif finalhand_ai == 13:
                    screen.blit(image_ai13, (location_ai_final))
                elif finalhand_ai == 14:
                    screen.blit(image_ai14, (location_ai_final))
                elif finalhand_ai == 15:
                    screen.blit(image_ai15, (location_ai_final))
                elif finalhand_ai == 16:
                    screen.blit(image_ai16, (location_ai_final))
                elif finalhand_ai == 17:
                    screen.blit(image_ai17, (location_ai_final))
                elif finalhand_ai == 18:
                    screen.blit(image_ai18, (location_ai_final))
                elif finalhand_ai == 19:
                    screen.blit(image_ai19, (location_ai_final))
                elif finalhand_ai == 20:
                    screen.blit(image_ai20, (location_ai_final))
                elif finalhand_ai == 21:
                    screen.blit(image_ai21, (location_ai_final))
                elif finalhand_ai >= 22:
                    screen.blit(image_ai22, (location_ai_final))
        #Wen the game is tie
        if finalhand == finalhand_ai:
            screen.blit(image_tie, (location_tie))
            fristhand = True
            secondhand_true = False
            thirdhand_true = False
            fourthand_true = False

            show_ai = False
            hit_and_stand = False
            ai1card = True
            aihand = False
            # userhandlocation
            if finalhand == 4:
                screen.blit(image_hand4, (location_user_final))
            elif finalhand == 5:
                screen.blit(image_hand5, (location_user_final))
            elif finalhand == 6:
                screen.blit(image_hand6, (location_user_final))
            elif finalhand == 7:
                screen.blit(image_hand7, (location_user_final))
            elif finalhand == 8:
                screen.blit(image_hand8, (location_user_final))
            elif finalhand == 9:
                screen.blit(image_hand9, (location_user_final))
            elif finalhand == 10:
                screen.blit(image_hand10, (location_user_final))
            elif finalhand == 11:
                screen.blit(image_hand11, (location_user_final))
            elif finalhand == 12:
                screen.blit(image_hand12, (location_user_final))
            elif finalhand == 13:
                screen.blit(image_hand13, (location_user_final))
            elif finalhand == 14:
                screen.blit(image_hand14, (location_user_final))
            elif finalhand == 15:
                screen.blit(image_hand15, (location_user_final))
            elif finalhand == 16:
                screen.blit(image_hand16, (location_user_final))
            elif finalhand == 17:
                screen.blit(image_hand17, (location_user_final))
            elif finalhand == 18:
                screen.blit(image_hand18, (location_user_final))
            elif finalhand == 19:
                screen.blit(image_hand19, (location_user_final))
            elif finalhand == 20:
                screen.blit(image_hand20, (location_user_final))
            elif finalhand == 21:
                screen.blit(image_hand21, (location_user_final))
            elif finalhand >= 22:
                screen.blit(image_hand22, (location_user_final))
            # ai hand location
            if finalhand_ai == 4:
                screen.blit(image_ai4, (location_ai_final))
            elif finalhand_ai == 5:
                screen.blit(image_ai5, (location_ai_final))
            elif finalhand_ai == 6:
                screen.blit(image_ai6, (location_ai_final))
            elif finalhand_ai == 7:
                screen.blit(image_ai7, (location_ai_final))
            elif finalhand_ai == 8:
                screen.blit(image_ai8, (location_ai_final))
            elif finalhand_ai == 9:
                screen.blit(image_ai9, (location_ai_final))
            elif finalhand_ai == 10:
                screen.blit(image_ai10, (location_ai_final))
            elif finalhand_ai == 11:
                screen.blit(image_ai11, (location_ai_final))
            elif finalhand_ai == 12:
                screen.blit(image_ai12, (location_ai_final))
            elif finalhand_ai == 13:
                screen.blit(image_ai13, (location_ai_final))
            elif finalhand_ai == 14:
                screen.blit(image_ai14, (location_ai_final))
            elif finalhand_ai == 15:
                screen.blit(image_ai15, (location_ai_final))
            elif finalhand_ai == 16:
                screen.blit(image_ai16, (location_ai_final))
            elif finalhand_ai == 17:
                screen.blit(image_ai17, (location_ai_final))
            elif finalhand_ai == 18:
                screen.blit(image_ai18, (location_ai_final))
            elif finalhand_ai == 19:
                screen.blit(image_ai19, (location_ai_final))
            elif finalhand_ai == 20:
                screen.blit(image_ai20, (location_ai_final))
            elif finalhand_ai == 21:
                screen.blit(image_ai21, (location_ai_final))
            elif finalhand_ai >= 22:
                screen.blit(image_ai22, (location_ai_final))

        if restart1 == True:
            pygame.quit()
            os.system(bl)
            exit()

        pygame.display.update()
