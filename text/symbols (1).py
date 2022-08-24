""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
'''
_pad        = '_'
_punctuation = ',.!?-'
_letters = 'AEINOQUabdefghijkmnoprstuvwyz'
_letters_ipa = 'ʃʧ↓↑ '
'''

# japanese_cleaners2
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧʦ↓↑ '


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")

'''
symbols = list(' !"&*,-.?ABCINU[]abcdefghijklmnoprstuwyz{}~')
SPACE_ID = symbols.index(" ")
'''
