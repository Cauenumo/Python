import re 
patterns = ['term1', 'term2']

text = 'This is a string with term1. This another with term3.'

print(re.search(patterns[0],text))

for pattern in patterns:
    print(f'Searching for {pattern} in: {text}')

    if re.search(pattern,text):
        print('\n')
        print('Match was found. \n')
    
    else:
        print('\n')
        print('No Match was found.\n')