import operator

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
    '-help': {
        'Desc': 'View commands',
        'minArgs': 0,
        'maxArgs': 0,
        'SUBS': {},
        'Help': '-help'
    }
}

def searchCoin(splits):
    for split in splits:
        if split != splits[0] and not split.__contains__('-'):
            print(split)
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

    else:
        print('Command', command, 'does not exist\n')
    waitCommand()


def waitCommand():
    global command
    command = input('')
    commands()

main.init()
waitCommand()