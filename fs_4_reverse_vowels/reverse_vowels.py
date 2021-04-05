def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    strVowels = [n for n in list(s) if n in vowels]
    strVowels.reverse()
    i = 0
    n = 0
    for n in range(len(s)):
        if s[n] in vowels:
            s = s[0:n]+strVowels[i]+s[n+1:]
            i += 1
            n += 1
        else:
            n += 1
    return s
