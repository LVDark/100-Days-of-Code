#Word list and ascii art for Hangman game
title = '''
   _                                             
  | |                                            
  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
  '''
words = [
    "amount", "argument", "beautiful", "belief", "cause", "certain", 
    "chance", "change", "clear", "common", "comparison", "condition", "connection", 
    "copy", "cecision", "cegree", "desire", "development", "different", "education", 
    "event", "examples", "existence", "experience", "feeling", 
    "fiction", "force", "general", "government", "happy", "history", "important", 
    "interest", "knowledge", "level", "living", "love", "material", "measure", 
    "motion", "nation", "natural", "necessary", "normal", "number", "observation", 
    "opposite", "order", "organization", "place", "pleasure", "possible", "power", 
    "probable", "property", "purpose", "quality", "question", "reason", "relation", 
    "representative", "respect", "responsible", "right", "same", "science", "seem", 
    "sense", "simple", "society", "sort", "special", "substance", "thing", "thought", 
    "true", "wise", "word", "work"
]
the_man = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''

=========''']
Win = ('''
▗▖  ▗▖▗▄▖ ▗▖ ▗▖    ▗▖ ▗▖▗▄▄▄▖▗▖  ▗▖
 ▝▚▞▘▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌  █  ▐▛▚▖▐▌
  ▐▌ ▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌  █  ▐▌ ▝▜▌
  ▐▌ ▝▚▄▞▘▝▚▄▞▘    ▐▙█▟▌▗▄█▄▖▐▌  ▐▌    
                                      
''')
Lose = ('''
▗▖  ▗▖▗▄▖ ▗▖ ▗▖    ▗▖    ▗▄▖  ▗▄▄▖▗▄▄▄▖
 ▝▚▞▘▐▌ ▐▌▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌   ▐▌   
  ▐▌ ▐▌ ▐▌▐▌ ▐▌    ▐▌   ▐▌ ▐▌ ▝▀▚▖▐▛▀▀▘
  ▐▌ ▝▚▄▞▘▝▚▄▞▘    ▐▙▄▄▖▝▚▄▞▘▗▄▄▞▘▐▙▄▄▖
                                           
''')
