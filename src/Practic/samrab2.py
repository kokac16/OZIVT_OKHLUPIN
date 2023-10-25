import random

def play_dice():
    
    dice = random.randint(1, 6)
    
    print(f"Вы бросили кубик и выпало: {dice}")

    if dice in [5, 6]:
        print("Вы победили!")
    elif dice in [3, 4]:
        print("Бросаем кубик ещё раз...")
        play_dice()  
    else:
        print("Вы проиграли!")

if __name__ == '__main__':
    play_dice() 
