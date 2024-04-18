import pygame
import random
import constants as C
import imageController as IC


class BattleMechanic(object):
    def __init__(self, player):
        self.player = player

        self.image = IC.battleAnimation[0]
        self.index = 0
        self.animationCounter = 0

        self.friendship = 50
        self.overload = 50
        self.min_friendship = 0
        self.max_friendship = 100
        self.max_overload = 100
        self.min_overload = 0

        self.current_question_index = 0
        self.selected_answer_index = 0

        self.answerList = []
        self.answerCounter = 0
        self.currentlySelected = 0
        
        self.selectStartX = 1190
        self.selectStartY = 840

        self.selectCurrentX = 1190
        self.selectCurrentY = 840

        self.pressedUp = False
        self.pressedDown = False
        self.pressedReturn = False

        self.answer_x = 1200  # Horizontal position for answers
        self.answer_y = 850  # Vertical position for answers
        self.question_x = 200  # Horizontal position for questions
        self.question_y = 850  # Vertical position for questions
        
        self.friendship_bar_x = 255  # X-coordinate of the left edge of the bar
        self.friendship_bar_y = 60  # Y-coordinate of the top edge of the bar
        self.health_bar_x = 255
        self.health_bar_y = 10
        self.bar_width = 200  # Width of the empty bar
        self.bar_height = 30  # Height of the bar
        self.fill_color =  (255, 192, 203)  # Color of the filled portion (pink)
        self.empty_color = (0, 0, 0)   # Color of the unfilled portion (black)
        # Define a list of questions and answers

        self.questions = [
            {
                "question": "Hey, are you new here?",
                "answers": [
                    {"text": "Hello, I am indeed!", "friendship_change": 10, "overload_change": -5},
                    {"text": "FU M8", "friendship_change": -10, "overload_change": 10},
                    {"text": "I might be", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "Whats your name?",
                "answers": [
                    {"text": "UR MAM", "friendship_change": -10, "overload_change": 10},
                    {"text": "Its Alex", "friendship_change": 10, "overload_change": -10},
                    {"text": "Lord Farquad", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "Whats with the slippers?",
                "answers": [
                    {"text": "Fashionscape", "friendship_change": 10, "overload_change": -5},
                    {"text": "Whats with your face?", "friendship_change": -10, "overload_change": -10},
                    {"text": "I forgot to change them", "friendship_change": 5, "overload_change": -5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "What brings you to our village?",
                "answers": [
                    {"text": "I'm trying to make friends", "friendship_change": 10, "overload_change": -10},
                    {"text": "UR MAM", "friendship_change": -10, "overload_change": 10},
                    {"text": "Adventure", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "Wanna hang?",
                "answers": [
                    {"text": "I'd love to!", "friendship_change": 10, "overload_change": -10},
                    {"text": "FU M8", "friendship_change": -10, "overload_change": 10},
                    {"text": "I might...", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
            ],
            },
            {
                "question": "Oh, I LOVE Old Band Tee! whats your favorite song?",
                "answers": [
                    {"text": "Emo Boys Shouting!", "friendship_change": 10, "overload_change": -5},
                    {"text": "The one where you STFU", "friendship_change": -10, "overload_change": 10},
                    {"text": "...WELL, I couldnt possibly choose one song from such an expansive catalog...", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "Whats Cynk City like?",
                "answers": [
                    {"text": "It's very busy but its an amazing city.", "friendship_change": 10, "overload_change": -5},
                    {"text": "LOUD AF", "friendship_change": -10, "overload_change": 10},
                    {"text": "I don't want to talk about it", "friendship_change": -5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "How are you doing?",
                "answers": [
                    {"text": "I'm doing good thanks, yourself?", "friendship_change": 10, "overload_change": -5},
                    {"text": "How TF do you think I'm doing?!", "friendship_change": -10, "overload_change": 10},
                    {"text": "How am I doing what?", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "Lovely weather isn't it?",
                "answers": [
                    {"text": "the temperature is perfect", "friendship_change": 10, "overload_change": -5},
                    {"text": "the sun makes my skin itch", "friendship_change": -10, "overload_change": 10},
                    {"text": "It is! Bit bright though", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "What do you think of Soco Village?",
                "answers": [
                    {"text": "Beautiful, very quaint", "friendship_change": 10, "overload_change": -5},
                    {"text": "shit m8 the dev sux", "friendship_change": -10, "overload_change": 10},
                    {"text": "I love it but it's busier than i thought.", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
            {
                "question": "What do you do for fun?",
                "answers": [
                    {"text": "I have a few interests!", "friendship_change": 10, "overload_change": -5},
                    {"text": "not this.", "friendship_change": -10, "overload_change": 10},
                    {"text": "sit in a dark room alone", "friendship_change": 5, "overload_change": 5},
                    {"text": "*silence*", "friendship_change": -10, "overload_change": 5}
                ],
            },
        ]

        self.current_question = None
        self.selected_answer = 0
        
    def display_background(self):
        C.SCREEN.blit(IC.battleAnimation[self.index], (0, 0))
        self.animationCounter += C.DT
        if self.animationCounter >= 0.1:
            if self.index == (len(IC.battleAnimation) - 1):
                self.index = 0
                self.animationCounter = 0
            else:
                self.index += 1
                self.animationCounter = 0
                
    def display_question(self):
        self.question_dict = self.current_question
        self.question_text = self.question_dict["question"]
        self.printQuestion = C.BATTLEFONT.render((self.question_text), 1, (C.BLACK))
        C.SCREEN.blit(self.printQuestion,(self.question_x, self.question_y))

    def display_answer(self):
        if self.answerCounter < 4:
            self.answers = self.question_dict["answers"]
            for index, answer in enumerate(self.answers):
                self.answer_text = answer["text"]
                printAnswer = C.BATTLEFONT.render((self.answer_text), 1, (C.BLACK))
                self.answerList.append(printAnswer)
                self.answerCounter += 1

        C.SCREEN.blit(self.answerList[0],(self.answer_x, self.answer_y))
        C.SCREEN.blit(self.answerList[1],(self.answer_x, self.answer_y + 40))
        C.SCREEN.blit(self.answerList[2],(self.answer_x, self.answer_y + 80))
        C.SCREEN.blit(self.answerList[3],(self.answer_x, self.answer_y + 120))

    def receiveControls(self):
        if self.pressedUp == True:
            self.pressedUp = False
            self.selected_answer_index = max(0, self.selected_answer_index - 1)
            self.currentlySelected = self.selected_answer_index
            self.selectCurrentY -= 40
            if self.selectCurrentY <= self.selectStartY:
                self.selectCurrentY = self.selectStartY

        elif self.pressedDown == True:
            self.pressedDown = False
            self.selected_answer_index = min(len(self.current_question["answers"]) - 1, self.selected_answer_index + 1)
            self.currentlySelected = self.selected_answer_index
            self.selectCurrentY += 40
            if self.selectCurrentY > self.selectStartY + 120:
                self.selectCurrentY = self.selectStartY + 120

        elif self.pressedReturn == True:
            self.pressedReturn = False
            self.selectCurrentY = self.selectStartY
            self.answer = self.current_question["answers"][self.selected_answer_index]
            #self.friendship = max(self.min_friendship, min(self.max_friendship, self.friendship + self.answer["friendship_change"]))
            #self.overload = max(self.min_overload, min(self.max_overload, self.overload + self.answer["overload_change"]))
            self.selected_answer_index = 0
            self.current_question = None
            self.answerList = []
            self.answerCounter = 0
            if self.current_question_index == 10:
                C.LEVEL = 5

            else:
                self.current_question_index += 1


                    
    def update(self):
        self.receiveControls()
        self.display_background()
        
        if self.current_question is None:
            self.current_question = self.questions[self.current_question_index]

        pygame.draw.rect(C.SCREEN, C.RED, pygame.Rect(self.selectCurrentX, self.selectCurrentY, 400, 40))

        self.display_question()
        self.display_answer()

        


