def decode_rune(runes, translations):
    rune_map = {}
    for rune, letter in translations:
        rune_map[rune] = letter
    
    decoded_text = []
    for line in runes:
        decoded_line = ''
        i = 0
        while i < len(line):
            if line[i] in rune_map:
                decoded_line += rune_map[line[i]]
            elif i + 1 < len(line) and line[i:i+2] in rune_map:
                decoded_line += rune_map[line[i:i+2]]
                i += 1
            elif i + 3 < len(line) and line[i:i+4] in rune_map:
                decoded_line += rune_map[line[i:i+4]]
                i += 3
            elif line[i] == '0':
                decoded_line += ' '
            i += 1
        decoded_text.append(decoded_line)
    return decoded_text

# Sample Input 1
runes = [
    '* h',
    '* \' . . .# 0 \'',
    '%- #. /% . & >',
    'hello world.'
]
translations = [('*', 'h'), ('\'', 'e')]
print(decode_rune(runes, translations))

# Sample Input 2
runes = [
    '/! n',
    '." \' !.) \'.& 0 ) "/ +% /! # 0 ) + +- \' 0 ! ,% "\'',
    '0 #.& *( >$, \'-+ \' &\'. 0 ) &+ &* !/ # 0 . \' $+\' 0 ! !)',
    '+, 0 & "/ \'',
    '#/ !/ >',
    '/! \' .* \' .& 0 ) +& %+ &* # 0 $." .) (( 0 # ,( %, #\'',
    '+ *& & <# /! & 0 & \' #+\' \', %/ *, 0 ! .# \'',
    '$ >$, \' \%/$ \', !.% 0 ) +& )\' *& # 0 / # - \' 0 ! ,% -* 0 % \'',
    '- ! <# *& & 0 * &!+% )+ ++ 0 ! .# \'',
    '$, >never gonna give you up.',
    'never gonna let you down.',
    'never gonna run around,',
    'and desert you.',
    'never gonna make you cry,',
    'never gonna say goodbye.',
    'never gonna tell a lie,',
    'and hurt you.'
]
translations = [('/!', 'n'), ('."', 'v'), ('\'', 'e')]
print(decode_rune(runes, translations))