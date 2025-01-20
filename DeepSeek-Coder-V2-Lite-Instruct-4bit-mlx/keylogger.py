def decode_keystrokes(sounds):
    keyboard = {
        'clank': 'a',
        'bong': 'A',
        'click': '',
        'poing': 'b',
        'clonk': 'B',
        'clang': 'c',
        'pang': 'C',
        'clong': 'D',
        'tac': 'e',
        'boing': 'f',
        'boink': 'F',
        'cloink': 'g',
        'rattle': 'h',
        'clock': 'H',
        'toc': 'i',
        'clink': 'I',
        'tuc': 'k',
        'bing': 'K',
        'pong': 'l',
        'clangbang': 'M',
        'whack': 'W'
    }
    
    result = []
    caps_lock = False
    shift = False
    buffer = ""
    
    for sound in sounds:
        if sound == 'tap':
            buffer = keyboard.get(buffer, '')
            result.append(buffer)
        elif sound == 'poing' or sound == 'clonk':
            buffer = keyboard.get(sound, '')
        elif sound == 'bong' or sound == 'pang':
            buffer = keyboard.get(sound, '')
        elif sound in ['ping', 'pong']:
            buffer = keyboard.get(sound, '')
        elif sound in ['clank', 'clang', 'clonk']:
            buffer = keyboard.get(sound, '')
        elif sound == 'rattle':
            caps_lock = not caps_lock
        elif sound in ['clock', 'toc']:
            shift = not shift
        else:
            buffer = sound
        
        if caps_lock and buffer.isalpha():
            buffer = buffer.upper() if buffer.islower() else buffer.lower()
        elif shift and buffer.isalpha():
            buffer = buffer.upper() if buffer.islower() else buffer.lower()
    
    return ''.join(result) + (' ' if caps_lock else '')

# Read input
N = int(input())
sounds = [input().strip() for _ in range(N)]

# Decode and print the result
print(decode_keystrokes(sounds))