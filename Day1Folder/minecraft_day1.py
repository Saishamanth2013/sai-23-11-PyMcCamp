# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
# def on_on_chat():
#     pass
# player.on_chat("run", on_on_chat)

def Teleport():
    agent.teleport_to_player()

player.on_chat("come", Teleport)

# move commands
def turn_right():
    agent.turn(RIGHT)
player.on_chat("R", turn_right)

def turn_left():
    agent.turn(LEFT )
player.on_chat("L", turn_left)

def move_up(steps):
    agent.move(UP, steps)
player.on_chat("U",move_up)

def move_down(steps):
    agent.move(DOWN, steps)
player.on_chat("D", move_down)

def move_forward(steps): 
    agent.move(FORWARD, steps)
player.on_chat("F", move_forward)

def move_back(steps): 
    agent.move(BACK, steps)
player.on_chat("B", move_back)


def move_steps():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD,4)
player.on_chat("obst1", move_steps)


def move_steps2():
    agent.move(UP, 1)
    agent.move(FORWARD,1)
    agent.move(UP, 1) 
    agent.move(FORWARD,1)
    agent.move(UP, 1)
    agent.move(FORWARD,3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
player.on_chat("obst3", move_steps2)




    



