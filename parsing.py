import operator

import data
import main

commands_Dict = {
    '-search':{
        'Desc': 'Search for coin(s).',
        'minArgs': 1,
        'maxArgs': 5,
        'SUBS': {},
        'Help': '[coinID]'
    },
    '-currency':{
        'Desc': 'Manage primary currency.',
        'minArgs': 1,
        'maxArgs': 2,
        'SUBS': {
            '-v':{
                'Desc': 'View current currency',
                'minArgs': 0,
                'maxArgs': 0,
                'syntax': None,
                'help': '-v'
            },
            '-c':{
                'Desc': 'Change current currency',
                'minArgs': 1,
                'maxArgs': 1,
                'syntax': [str],
                'help': '-v'
            }
        },
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


def validateCommand():
    global command
    #Split command input into pieces where split[0] is main command
    splits = command.split(' ')
    args = len(splits)-1
    if (args < commands_Dict[splits[0]]['minArgs'] or args > commands_Dict[splits[0]]['maxArgs']):
        print('Improper syntax, proper usage:', splits[0], commands_Dict[splits[0]]['Help'])


def commands():
    global command
    splits = command.split(' ')
    cmd = splits[0]
    if commands_Dict.__contains__(cmd):
        if (cmd == '-help'):
            print("\nCommands")
            for command in commands_Dict:
                print('\t', command, ':', commands_Dict[command]['Desc'], 'Usage:', commands_Dict[command]['Help'])
            #for comm in commands_dict:
            #    print('\t', comm, ':', commands_dict[comm])
            validateCommand()
        if (cmd == '-search'):
            validateCommand()
    else:
        print('Command', command, 'does not exist\n')
    waitCommand()


def waitCommand():
    global command
    command = input('')
    commands()


print("Welcome to CoinRoute Tracker\n")

waitCommand()