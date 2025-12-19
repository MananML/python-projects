import random

MAX_BET = 300
MIN_BET = 20
MAX_NUMBER_OF_LINES = 3
COL = 3
ROW = 3

symbols = {
    "🍀": 3,
    "🌺": 7,
    "🍓": 4,
    "🥝": 6,
    "🍇": 5,
}

symbols_value = {
    "🍀": 7,
    "🌺": 4,
    "🍓": 6,
    "🥝": 3,
    "🍇": 5,   
}

def get_machine_spin(symbols, cols, rows):
    all_symbols = []
    for symbol, _ in symbols.items():
        for _ in range(_):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_machine_spin(columns, rows):
    for row in range(rows):
        for _, column in enumerate(columns):
            if _ != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


#collect user input
def get_user_deposit():
    while True:
        money = input("How much would you like to deposit? $")
        if money.isdigit():
            money = int(money)
            if money > 50:
                return money  
            else: 
                print("\nYour money must be greater than 50\n")
        else:
            print("Please input a digit.")


#collect number of lines
def get_number_of_lines():
    while True:    
        lines = input(f"How many lines do you want to bet on (1 - {MAX_NUMBER_OF_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if (0 < lines <= MAX_NUMBER_OF_LINES):
                return lines  
            else:
                print("Enter a valid number of lines.") 
        else:
            print("Please enter a digit.")



def get_bet():
    while True:
        bet = input(f"How much do you want to bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Enter an amount in this range ({MIN_BET} - {MAX_BET})")
        else:
            print("Please enter a digit.")


def check_winning(slots, lines, value, bet):
    winning = 0
    lines_won_on = []
    for line in range(lines):
        symbol = slots[0][line]
        for _ in slots:
            symbol_to_check = _[line]
            if symbol != symbol_to_check:
                break
        else:
            winning = value[symbol] * bet
            lines_won_on.append(line + 1)

    return winning, lines_won_on


def spin_machine(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines, your total_bet is ${total_bet}.")

    slots = get_machine_spin(symbols, COL, ROW)
    print_machine_spin(slots, ROW)

    winning, lines_won_on = check_winning(slots, lines, symbols_value, bet)
    print(f"You won ${winning}")
    if winning > 0:
        print(f"You won on line:", *lines_won_on)

    return winning - total_bet


def main():
    print("THIS__IS__SLOT__MACHINE")
    balance = get_user_deposit()
    while True:
        print(f"Current balance is ${balance}")
        _ = input("PRESS ANY BUTTON TO START (Q TO QUIT) ")
        if _ == "q".lower():
            break
        balance += spin_machine(balance)

    print(f"You left with ${balance}")
    print("____THANKS FOR PLAYING____")


main()