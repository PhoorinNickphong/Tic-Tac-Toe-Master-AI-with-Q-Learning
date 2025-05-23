import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(statistic, save=False):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Learning how to play Tic Tac Toe')
    plt.xlabel('Number of Rounds')
    plt.ylabel('Games')

    plt.plot(statistic["round"], statistic["player1_win"], label="Player 1 win")
    plt.plot(statistic["round"], statistic["player2_win"], label="Player 2 win")
    plt.plot(statistic["round"], statistic["draw"], label="Draw")


    plt.ylim(ymin=0)

    plt.legend()

    plt.show(block=False)

    if save:
        plt.savefig(r'C:\Users\123ph\Downloads\Work\240-318\Project\beyond-tic-tac-toe-ai\image\tresult_.png')
