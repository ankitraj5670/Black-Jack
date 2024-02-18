#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Constants for card images
CARD_WIDTH = 73
CARD_HEIGHT = 98

# Define constants for the card suits, ranks, and values
SUITS = ("Diamonds", "Clubs", "Spades", "Hearts")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "King", "Queen", "Ace")
VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "King": 10, "Queen": 10, "Ace": 11}

# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((suit, rank))
    random.shuffle(deck)
    return deck

# Function to load card images
def load_card_images():
    images = {}
    for suit in SUITS:
        for rank in RANKS:
            card_image = Image.open(f"cards/{rank.lower()}_of_{suit.lower()}.png")
            card_image = card_image.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
            images[(suit, rank)] = ImageTk.PhotoImage(card_image)
    return images

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total_value = 0
    ace_count = 0
    for card in hand:
        rank = card[1]
        total_value += VALUES[rank]
        if rank == "Ace":
            ace_count += 1
    while total_value > 21 and ace_count > 0:
        total_value -= 10
        ace_count -= 1
    return total_value

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop(0)

# Function to start the game
def start_game():
    # Initialize deck and player's and dealer's hands
    global deck, player_hand, dealer_hand
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Display initial hands
    update_display()
    
    # Check for blackjack
    player_hand_value = calculate_hand_value(player_hand)
    if player_hand_value == 21:
        messagebox.showinfo("Blackjack", "You got a Blackjack!")
        end_game()
    else:
        hit_button.config(state="normal")
        stand_button.config(state="normal")

# Function to update the display with current hands
def update_display():
    player_canvas.delete("all")
    dealer_canvas.delete("all")
    
    for i, card in enumerate(player_hand):
        player_canvas.create_image(20 + i * 20, 10, anchor="nw", image=card_images[card])
    
    dealer_canvas.create_image(20, 10, anchor="nw", image=card_images[dealer_hand[0]])
    dealer_canvas.create_image(20 + CARD_WIDTH + 20, 10, anchor="nw", image=back_image)

# Function to handle player's hit action
def hit():
    player_hand.append(deal_card(deck))
    update_display()
    
    # Check if player busts
    if calculate_hand_value(player_hand) > 21:
        messagebox.showinfo("Bust", "You busted! Dealer wins.")
        end_game()

# Function to handle player's stand action
def stand():
    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    update_display()
    
    # Determine the winner
    player_hand_value = calculate_hand_value(player_hand)
    dealer_hand_value = calculate_hand_value(dealer_hand)
    if player_hand_value > dealer_hand_value or dealer_hand_value > 21:
        messagebox.showinfo("Winner", "You win!")
    elif player_hand_value < dealer_hand_value:
        messagebox.showinfo("Winner", "Dealer wins!")
    else:
        messagebox.showinfo("Winner", "It's a tie!")
    end_game()

# Function to end the game and disable action buttons
def end_game():
    hit_button.config(state="disabled")
    stand_button.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Blackjack")
root.configure(background="green")

# Load card images
card_images = load_card_images()
back_image = ImageTk.PhotoImage(Image.open("cards/back.png").resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS))

# Create canvas for player's and dealer's hands
player_canvas = tk.Canvas(root, width=300, height=CARD_HEIGHT + 20, background="green", highlightthickness=0)
player_canvas.pack(pady=20)

dealer_canvas = tk.Canvas(root, width=300, height=CARD_HEIGHT + 20, background="green", highlightthickness=0)
dealer_canvas.pack(pady=20)

# Create and pack GUI elements
button_frame = tk.Frame(root, background="green")
button_frame.pack()

start_button = tk.Button(button_frame, text="Start Game", command=start_game, font=("Arial", 14), bg="white", fg="black", padx=10, pady=5, bd=0)
start_button.grid(row=0, column=0, padx=10)

hit_button = tk.Button(button_frame, text="Hit", command=hit, state="disabled", font=("Arial", 14), bg="white", fg="black", padx=10, pady=5, bd=0)
hit_button.grid(row=0, column=1, padx=10)

stand_button = tk.Button(button_frame, text="Stand", command=stand, state="disabled", font=("Arial", 14), bg="white", fg="black", padx=10, pady=5, bd=0)
stand_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()


# In[1]:


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Constants for card images
CARD_WIDTH = 73
CARD_HEIGHT = 98

# Define constants for the card suits, ranks, and values
SUITS = ("Diamonds", "Clubs", "Spades", "Hearts")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "King", "Queen", "Ace")
VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "King": 10, "Queen": 10, "Ace": 11}

# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((suit, rank))
    random.shuffle(deck)
    return deck

# Function to load card images
# Function to load card images
def load_card_images():
    images = {}
    for suit in SUITS:
        for rank in RANKS:
            card_image = Image.open(f"cards/{rank.lower()}_of_{suit.lower()}.png")
            card_image = card_image.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
            images[(suit, rank)] = ImageTk.PhotoImage(card_image)
    # Load back image
    back_card_image = Image.open("cards/back.png")
    back_card_image = back_card_image.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
    images["back"] = ImageTk.PhotoImage(back_card_image)
    return images


# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total_value = 0
    ace_count = 0
    for card in hand:
        rank = card[1]
        total_value += VALUES[rank]
        if rank == "Ace":
            ace_count += 1
    while total_value > 21 and ace_count > 0:
        total_value -= 10
        ace_count -= 1
    return total_value

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop(0)

# Function to start the game
def start_game():
    # Initialize deck and player's and dealer's hands
    global deck, player_hand, dealer_hand
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Display initial hands
    update_display()
    
    # Check for blackjack
    player_hand_value = calculate_hand_value(player_hand)
    if player_hand_value == 21:
        messagebox.showinfo("Blackjack", "You got a Blackjack!")
        end_game()
    else:
        hit_button.config(state="normal")
        stand_button.config(state="normal")

# Function to update the display with current hands
def update_display():
    player_canvas.delete("all")
    dealer_canvas.delete("all")
    
    for i, card in enumerate(player_hand):
        player_canvas.create_image(20 + i * 20, 10, anchor="nw", image=card_images[card])
    
    # Show only the first card of the dealer's hand
    dealer_canvas.create_image(20, 10, anchor="nw", image=card_images[dealer_hand[0]])
    
    # Place face down cards for the rest of the dealer's hand
    for i in range(1, len(dealer_hand)):
        dealer_canvas.create_image(20 + i * 20, 10, anchor="nw", image=card_images["back"])  # Use back_image


# Function to handle player's hit action
def hit():
    player_hand.append(deal_card(deck))
    update_display()
    
    # Check if player busts
    if calculate_hand_value(player_hand) > 21:
        messagebox.showinfo("Bust", "You busted! Dealer wins.")
        end_game()

# Function to handle player's stand action
def stand():
    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    update_display()
    
    # Determine the winner
    player_hand_value = calculate_hand_value(player_hand)
    dealer_hand_value = calculate_hand_value(dealer_hand)
    if player_hand_value > dealer_hand_value or dealer_hand_value > 21:
        messagebox.showinfo("Winner", "You win!")
    elif player_hand_value < dealer_hand_value:
        messagebox.showinfo("Winner", "Dealer wins!")
    else:
        messagebox.showinfo("Winner", "It's a tie!")
    end_game()

# Function to end the game and disable action buttons
def end_game():
    hit_button.config(state="disabled")
    stand_button.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Blackjack")
root.configure(background="black")

# Load card images
card_images = load_card_images()

# Create canvas for player's and dealer's hands
player_canvas = tk.Canvas(root, width=500, height=CARD_HEIGHT + 20, background="black", highlightthickness=0)
player_canvas.pack(pady=20)

dealer_canvas = tk.Canvas(root, width=500, height=CARD_HEIGHT + 20, background="black", highlightthickness=0)
dealer_canvas.pack(pady=20)

# Create and pack GUI elements
button_frame = tk.Frame(root, background="black")
button_frame.pack()

start_button = tk.Button(button_frame, text="Start Game", command=start_game, font=("Arial", 14), bg="white", fg="black", padx=10, pady=5, bd=0)
start_button.grid(row=0, column=0, padx=10)

hit_button = tk.Button(button_frame, text="Hit", command=hit, state="disabled", font=("Arial", 14), bg="white", fg="black", padx=10, pady=5, bd=0)
hit_button.grid(row=0, column=1, padx=10)

stand_button = tk.Button(button_frame, text="Stand", command=stand, state="disabled", font=("Arial", 14), bg="white", fg="black", padx=10, pady=5, bd=0)
stand_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()


# In[ ]:




