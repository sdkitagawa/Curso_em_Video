'''
Colors in the Terminal


Text                Background

30      Black       Preto       40
31      Red         Vermelho    41
32      Green       Verde       42
33      Yellow      Amarelo     43
34      Blue        Azul        44
35      Magenta     Magenta     45
36      Cyan        Ciano       46
37      Grey        Cinza       47
97      White       Branco      107

\033[text_format;text_color;background_color;m

'''

print("\033[0;30;41m\nWhite Text, Red Background\n")
print("\033[0;33;44m\nUnderscored, White Text, Blue Background\n")
print("\033[0;35;43m\nYellow Text, Yellow Background\n")
print("\033[0;97;42m\nWhite Text, Green Background\n")
print("\033[0;97;46m\nWhite Text, Cyan Background\n")
print("\033[0;97;45m\nWhite Text, Magenta Background\n")
print("\033[0;97;47m\nWhite Text, Grey Background\n")
print("\033[0;32;107mCorrect\033[m,\033[1;31;107mIncorrect")
