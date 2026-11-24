# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def choptrees(height):
    for i in range(height):
        agent.destroy(FORWARD) 
        agent.move(UP, 1)
    agent.move (DOWN, height)
    agent.collect_all()
    agent.move(RIGHT, 1)
player.on_chat("Chop", choptrees)






def mining(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.move(FORWARD, 1)
        agent.collect_all()

player.on_chat("mine", mining)
