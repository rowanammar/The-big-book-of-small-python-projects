Bitmap = '''             
                                                                                    ++
                                                                                   ++++
                                                                                  ++ +++
                                                                              +++++    ++++
                                    +++++++++++               +++++++++++     ++++     +++++
                                +++++++    +++++++         ++++++     +++++++    +++ +++
                              ++                ++++    +++++              ++++    ++++
                            ++++                   +++ +++                   +++   +++
                           +++                      +++++                     ++++
                          +++                        +++                        +++
                         +++                          +                          +++
                         +++                                                     +++
                         +++                                                     +++
                         +++                                                     +++
                         +++                                                     +++
                          ++                                                    +++
                          +++                                                   +++
                           +++                                                 +++
                            +++                                              ++++
                             ++++                                          ++++
                               ++++                                       ++++
                                 ++++                                   ++++
                                   ++++                               ++++
                                     ++++                           ++++
                               ++      +++                        ++++      +++
                              +++       ++++                    ++++       ++++
                              ++++        ++++                 +++        +++ ++
                            +++  +++        ++++             ++++       ++++   +++
                         +++       ++++       ++++         ++++      ++++         ++++
                            +++  +++            ++++     ++++           +++    ++++
                              ++++                ++++ ++++               +++ ++
                              +++                   +++++                  ++++
                               ++                     +                     +++
                                                                                                    '''
x = input("Enter the message to display with the bitmap ")
while x == '':
    x = input("Enter the message to display with the bitmap ")
index = 0
for i in Bitmap:
    if i != ' ':
        print(x[index % len(x)], end='')  # default of print ends with \n , so we overwrite this prompt
        index += 1
    if i == ' ':
        print(' ', end='')
    if i == '\n':
        print()
