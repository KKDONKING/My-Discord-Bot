import random

def coin_flip():
    coin_sides = ["Heads", "Tails"]
    coin_sides_images = ["https://media.discordapp.net/attachments/1141333358731858101/1143462453032783953/coin_head.png","https://cdn.discordapp.com/attachments/1141333358731858101/1143462453305430046/coin_tails.png"]

    outcome = random.choice(coin_sides)
    if outcome == "Heads":
        return outcome, coin_sides_images[0]
    else:
        return outcome, coin_sides_images[1]
