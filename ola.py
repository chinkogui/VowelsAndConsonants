class LetterFilter:

    def __init__(self, s):
        self.s = s

    # Enter your code here. Read input from STDIN. Print output to STDOUT
    global vowels
    vowels = ('a', 'e', 'i', 'o', 'u')

    def filter_vowels(self):
        str = self.s
        for x in str:
            if x in vowels:
                str = str.replace(x, "")
        return str

    def filter_consonants(self):
        # Enter your code here
        str = self.s
        for x in str:
            if x not in vowels:
                str = str.replace(x, "")
        return str


s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())