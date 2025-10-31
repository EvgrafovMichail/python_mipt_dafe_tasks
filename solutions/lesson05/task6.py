def simplify_path(path: str) -> str:
    commands = []
    command = ''
    for i in range(1,len(path)):
        if path[i] == '/':
            if command != '':
                commands.append(command)
                command = ''
        else:
            command += path[i]
    if path[-1] != '/':
        commands.append(command)
    pos = 0
    for i in range(len(commands)):
        if commands[i] == '..':
            pos -= 1
            if pos < 0:
                return ''
        elif commands[i] == '.':
            continue
        else:
            commands[pos] = commands[i]
            pos += 1
    if pos == 0:
        return '/'
    else:
        return '/' + '/'.join(commands[:pos])