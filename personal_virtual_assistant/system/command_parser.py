from typing import List

from .handlers import ALL_COMMAND

def parser(user_input: str) -> List[str]:
    """Command parser. Get a user string - separate the command and parameters - 
    return it to the list, where the first element is the command, 
    the others are parameters.

        Parameters:
            user_input (str): String line of user input.

        Returns:
            list command of user input (list): list of comands (list of strings).
    """
    command_line = user_input.strip().replace(' ','~').lower()
    all_commands = sorted([el.replace('_','~') for el in ALL_COMMAND], key=len)[::-1]   
    for command in all_commands:
        if command_line.startswith(command):
            command.replace('~','_')
            return [command.replace('~','_')] + [word for word in user_input[len(command):].split(' ') if word]

    return user_input.strip().split(' ')  #  OTHER_MESSAGE.get('Unknown', [AMBUSH])[0]

