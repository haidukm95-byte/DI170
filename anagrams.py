import anagram_checker

print("WELCOME TO THE ANAGRAM CHECKER V 1.0!")
end=("""
Thank you for playing AnagramChecker v.1.0.
Made by Marko Haiduk
Email: haidukm95@gmail.com
""")


def main():
    while True:
        menu='''
MENU COMMANDS:
"S" for start or continue
"Q" for quit 
'''
        print(menu)
        choice=input('What`s your choice: ')
        if choice.strip().upper()=='Q':
            print('See you soon:)')
            print(end)
            break
        elif choice.strip().upper()=='S':
            gameplay()   
        else:
            print('Invalid choice. Please enter S or Q.')

def gameplay():
    while True:
        word_input=input(f'Please type here any word: ')
        if not word_input:
            print('Please enter a valid word.')
            continue

        checker=anagram_checker.AnagramChecker(word_input)
        if checker.isvalid_word():
            print(f'''Your word: "{word_input}"
This is a valid English word.
''')
            print(f'Anagrams for your word: {checker.get_anagrams()}')
            break
        elif bool(checker)==False:
            print('No anagrams were found.')
            break
        else:
            print(f'''Your word: "{word_input}"
This is not a valid English word.
''')
            break
            
main()


