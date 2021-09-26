import operator # might need

import calc
import data
import main

commands_Dict = {
    '-search': {
        'Desc': 'Search for coin(s).',
        'minArgs': 1,
        'maxArgs': 5,
        'SUBS': {
            '-c': {
                'Desc': 'Specific coin category lookup',
                'minArgs': 0,
                'maxArgs': 33,
                'syntax': None,
                'help': '[fields]'
            }
        },
        'Help': '[coinID]'
    },
    '-currency':{
        'Desc': 'Manage primary currency.',
        'minArgs': 1,
        'maxArgs': 2,
        'SUBS': {},
        'Help': '[subCommand] [args]'
    },
    '-watch':{
        'Desc': 'Watch crypto in realtime.',
        'minArgs': 1,
        'maxArgs': 1,
        'SUBS': {},
        'Help': '[coinID]'
    },
    '-pair':{
        'Desc': 'View buy and sell cost of pair across multiple exchanges',
        'minArgs': 1,
        'maxArgs': 5,
        'SUBS': {},
        'Help': '[pairID]'
    },
    '-bid':{
        'Desc': 'Switch pair side param to bids',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-bid'
    },
    '-ask':{
        'Desc': 'Switch pair side param to asks',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-ask'
    },
    '-q': {
        'Desc': 'Change pair quantity param',
        'minArgs': 1,
        'maxArgs': 1,
        'SUBS': {},
        'Help': '[int]'
    },
    '-info':{
        'Desc': 'Get coin specific info.',
        'minArgs': 1,
        'maxArgs': 1,
        'SUBS': {},
        'Help': '[coinID]'
    },
    '-help': {
        'Desc': 'View commands',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-help'
    }
}

def quantity(splits):
    splits.remove(splits[0])
    main.pairQuantity = splits[0]
    print('Pair quantity param changed to', main.pairQuantity)

def bidsSide():
    calc.side = 'bids'
    print('Pair side param changed to bids')

def asksSide():
    calc.side = 'asks'
    print('Pair side param changed to asks')

def checkPair(splits):
    splits.remove(splits[0])
    data.checkPair(splits)

def watch(splits):
    for split in splits:
        if split != splits[0]:
            data.watch(split)

def coinInfo(splits):
    for split in splits:
        if split != splits[0]:
            data.coinInfo(split)

def searchCoin(splits):
    for split in splits:
        if split != splits[0] and not split.__contains__('-'):
            main.activeCoins.append(split)
    data.searchCoin(main.activeCoins, main.currency)

def manageCurrency(splits):
    cmd = splits[0]
    splits.remove(splits[0])
    for split in splits:
        if split.__contains__('-v'):
            print('has v')
            splits.remove(split)
            if len(splits) == 0:
                print('Current Currency: ' + main.currency)
            else:
                print('Invalid syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])
        if split.__contains__('-c'):
            splits.remove(split)
            if len(splits) == 1:
                for split in splits:
                    main.currency = split
                    print('Changed primary currency to', main.currency)
            else:
                print('Invalid syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])


def validateCommand():
    global command
    #Split command input into pieces where split[0] is main command
    splits = command.split(' ')
    cmd = splits[0]
    args = len(splits)-1
    if (args < commands_Dict[cmd]['minArgs'] or args > commands_Dict[cmd]['maxArgs']):
        print('Improper syntax, proper usage:', cmd, commands_Dict[cmd]['Help'])
    else:
        return True


def commands():
    global command
    splits = command.split(' ')
    cmd = splits[0]
    if commands_Dict.__contains__(cmd):
        if (cmd == '-help'):
            if(validateCommand()):
                print("\nCommands")
                for command in commands_Dict:
                    print('\t', command, ':', commands_Dict[command]['Desc'], 'Usage:', commands_Dict[command]['Help'])
                #for comm in commands_dict:
                #    print('\t', comm, ':', commands_dict[comm])
        if (cmd == '-search'):
            if(validateCommand()):
                searchCoin(splits)
        if (cmd == '-currency'):
            if(validateCommand()):
                manageCurrency(splits)
        if (cmd == '-info'):
            if(validateCommand()):
                coinInfo(splits)
        if (cmd == '-watch'):
            if(validateCommand()):
                watch(splits)
        if (cmd == '-pair'):
            if(validateCommand()):
                checkPair(splits)
        if cmd == '-bid':
            if validateCommand():
                bidsSide()
        if cmd == '-ask':
            if validateCommand():
                asksSide()
        if cmd == '-q':
            if validateCommand():
                quantity(splits)

    else:
        print('Command', command, 'does not exist\n')
    waitCommand()


def waitCommand():
    global command
    command = input('')
    commands()

main.init()
waitCommand()