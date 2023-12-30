from die import Die
from action import Action
from enum import Enum

die1 = Die('1')
die2 = Die('2')
die3 = Die('3')
die4 = Die('4')
die5 = Die('5')

dice = [die1, die2, die3, die4, die5]

newGameAction = Action('new', 'n')
freezeAction = Action('freeze', 'f')
unfreezeAction = Action('unfreeze', 'u')
reTossAction = Action('re-toss', 'r')
statusAction = Action('status', 's')

actions = [newGameAction, freezeAction, unfreezeAction, reTossAction, statusAction]
actionNames = [action.name for action in actions]
actionCodes = [action.abbreviation for action in actions]

diceNames = [die.name for die in dice]

toss_counter = 1
MAX_ROUNDS = 3

def play():
    global toss_counter 
    print(f'Die Würfel sind gefallen - Round {toss_counter}')
    for die in dice:
        die.toss()
    toss_counter += 1
    status()


def freeze(freez: bool):
    die_ids_input = input(f'choose die to freeze. Multiple options may be separated by comas. Options: {diceNames}\n')
    die_ids = [str.strip(id) for id in die_ids_input.split(',')]
    for die_id in die_ids:
        if die_id in diceNames:
            for die in dice:
                if die.name == die_id:
                    die.freeze = freez


def re_toss():
    if toss_counter <= MAX_ROUNDS:
        play()
    else:
        print('you can only toss three times in a row')


def status():
    print(f'tossed {toss_counter - 1} times')
    for die in dice:
        frozen = '(frozen)' if die.freeze else ''
        print(f'Die {die.name}: {die.pips} {frozen}')


def main():
    
    global toss_counter 
    action = 'invalid'
    play()
    print()

    while True:
        valid_options = [f'{a.name} ({a.abbreviation})' for a in actions]

        action = input(f'choose your next action. Options: {valid_options}\n')
        print()

        action_cleaned = str.strip(action.lower())
        if action_cleaned in actionNames or action_cleaned in actionCodes:
            match action:
                case newGameAction.name | newGameAction.abbreviation:
                    toss_counter = 1
                    for die in dice:
                        die.freeze = False
                    play()
                case freezeAction.name | freezeAction.abbreviation:
                    freeze(True)
                case unfreezeAction.name | unfreezeAction.abbreviation:
                    freeze(False)
                case reTossAction.name | reTossAction.abbreviation:
                    re_toss()
                case statusAction.name | statusAction.abbreviation:
                    status()
            print()


if __name__ == '__main__':
    main()