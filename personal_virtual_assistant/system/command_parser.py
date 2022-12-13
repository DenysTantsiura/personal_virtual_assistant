# from typing import List

from .handlers import ALL_COMMAND


def parser(user_input: str) -> list:
    """Command parser. Get a user string - separate the command and parameters - 
    return it to the list, where the first element is the command, 
    the others are parameters.

        Parameters:
            user_input (str): String line of user input.

        Returns:
            list command of user input (list): list of commands (list of strings).
    """
    # Example: aDD BirthDay 2000-11-12   ->   add~birthday~2000-11-12
    command_line = user_input.strip().replace('   ', '~').replace('  ', ' ').replace(' ', '~').lower()
    # Example: ['remove~birthday', 'change~birthday' ... ]
    all_commands = sorted([el.replace('_', '~') for el in ALL_COMMAND], key=len)[::-1]

    for command in all_commands:
        command = str(command)  # Example: 'remove~birthday' ... 'add~birthday'
        if (command_line.startswith(command) and len(command_line) == len(command)) or \
                command_line.startswith(f'{command}~'):   # if command_line.startswith(command):  # Example: 'add~phone'
            # # Example: ['add_birthday'] + ['2000-11-12']
            return [command.replace('~', '_')] + [word for word in user_input[len(command):].split(' ') if word]
    # Example: ['unknown', 'command', 'abracadabra']
    return user_input.strip().split(' ')  # OTHER_MESSAGE.get('Unknown', [AMBUSH])[0]
