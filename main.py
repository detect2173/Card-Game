from tkinter import *
import random
from PIL import Image, ImageTk

###------------------START GAME LOGIC-------------------###
def shuffle():
    #Define the deck
    suits = ['diamonds', 'hearts', 'clubs','spades']
    values = range(2,15)

    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f"{value}_of_{suit}")


    #Create players
    global dealer, player, dscore , pscore
    dealer = []
    player = []
    dscore = []
    pscore = []


    # Grab a random Card for Dealer
    dealer_card = random.choice(deck)
    # Remove card from deck
    deck.remove(dealer_card)
    # Append card to dealer list
    dealer.append(dealer_card)
    # Output card to screen
    global dealer_card_img
    dealer_card_img = resize_image(f"images/cards/{dealer_card}.png")
    dealer_label.config(image=dealer_card_img)

    # Grab a random Card for player
    player_card = random.choice(deck)
    # Remove card from deck
    deck.remove(player_card)
    # Append card to dealer list
    player.append(player_card)
    # Output card to screen
    global player_card_img
    player_card_img = resize_image(f"images/cards/{player_card}.png")
    player_label.config(image=player_card_img)

    root.title(f'JFB Card Game - {len(deck)} cards left in deck')

    # Get score
    score(dealer_card, player_card)


def deal_cards():
    try:
        # Get the dealer Card
        dealer_card = random.choice(deck)
        # Remove card from deck
        deck.remove(dealer_card)
        # Append card to dealer list
        dealer.append(dealer_card)
        # Output card to screen
        global dealer_card_img
        dealer_card_img = resize_image(f"images/cards/{dealer_card}.png")
        dealer_label.config(image=dealer_card_img)

        # Get the player Card
        player_card = random.choice(deck)
        # Remove card from deck
        deck.remove(player_card)
        # Append card to dealer list
        player.append(player_card)
        # Output card to screen
        global player_card_img
        player_card_img = resize_image(f"images/cards/{player_card}.png")
        player_label.config(image=player_card_img)
        # Get score
        score(dealer_card, player_card)

        #root.title(f'JFB Card Game - {len(deck)} cards left in deck | Dealer: {dscore.count("x")} Player: {pscore.count("x")}')
    except:
        if dscore.count('x') == pscore.count('x'):
            root.title(f'JFB Card Game - Game Over - TIE! {dscore.count("x")} to {pscore.count("x")}')
            score_label.config(text="Game Over, Tie Game!")
        elif dscore.count('x') > pscore.count('x'):
            root.title(f'JFB Card Game - Game Over - Dealer Wins! --> {dscore.count("x")} to {pscore.count("x")}')
            score_label.config(text=f"Game Over, Dealer Wins! {dscore.count('x')} to {pscore.count('x')}")
        elif dscore.count('x') < pscore.count('x'):
            root.title(f'JFB Card Game - Game Over - Player Wins! --> {pscore.count("x")} to {dscore.count("x")}')
            score_label.config(text=f"Game Over, Player Wins! {pscore.count('x')} to {dscore.count('x')}")



# Function to resize images
def resize_image(card):
    # Open the image
    our_card_img = Image.open(card)

    # Resize Image
    our_card_resize_img = our_card_img.resize((175,254))

    # Output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_img)

    return our_card_image

def score(dealer_card, player_card):
    # Split out Card Values
    dealer_card = int(dealer_card.split('_', 1)[0])
    player_card = int(player_card.split('_', 1)[0])
    # Compare numbers
    if dealer_card == player_card:
        score_label.config(text="Tie! Play again")
    elif dealer_card > player_card:
        score_label.config(text="Dealer Wins!")
        dscore.append('x')
    else:
        score_label.config(text="Player Wins!")
        pscore.append('x')

    root.title(f'JFB Card Game - {len(deck)} cards left in deck |   Dealer: {dscore.count("x")}   Player: {pscore.count("x")}')

root = Tk()
root.title('JFB Card Game')
root.iconbitmap('spade.ico')
root.geometry('900x650')
root.configure(background='green')
my_frame = Frame(root, background='green')
my_frame.pack(pady=20)


# Create frames for cards
dealer_frame = LabelFrame(my_frame, text='Dealer:', bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)
player_frame = LabelFrame(my_frame, text='Player:', bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)
player_label = Label(player_frame, text='')
player_label.pack(pady=20)
score_label = Label(root, text='', font=("Helvetica", 20), background='green', foreground='yellow')
score_label.pack(pady=20)
# Create two buttons
shuffle_button = Button(root, text='Shuffle Deck', font=('Helvetica', 14), command=shuffle)
shuffle_button.pack(pady=20)


card_button = Button(root, text='Get Cards', font=('Helvetica', 14), command=deal_cards)
card_button.pack(pady=20)





shuffle()



root.mainloop()