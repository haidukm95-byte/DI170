class AnagramChecker:
    def __init__(self, word):
        #1. sets the word as an attribute
        self.word=word
        try:
            with open('words.txt') as f:
                word_list = f.readlines()
                self.word_list = word_list
        except FileNotFoundError:
            print("Error: 'words.txt' file not found.")
            self.word_list = []
        except Exception as e:
            print(f"Error reading word list: {e}")
            self.word_list = []
        
    def isvalid_word(self):
        # Strip newlines and convert to uppercase for comparison
        words = [word.strip().upper() for word in self.word_list]
        return self.word.upper() in words

    def get_anagrams(self):
        if not self.isvalid_word():
            return []

        anagrams = []
        sorted_word=sorted(self.word.upper())

        for word in self.word_list:
            word_clean = word.strip().upper()
            if word_clean != self.word.upper() and sorted(word_clean) == sorted_word:
                anagrams.append(word_clean)

        return anagrams
        


