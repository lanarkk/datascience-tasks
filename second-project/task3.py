def encoder(_decoded_word, _key_dict):
    _meaning_dict = {}
    encorded_word = _decoded_word
    for letter in _decoded_word:
        if _meaning_dict.get(letter):
            _meaning_dict[letter] = _meaning_dict[letter] + 1
        else:
            _meaning_dict[letter] = 1
    for sign, sign_count in _meaning_dict.items():
        for letter, letter_count in _key_dict.items():
            if sign_count == letter_count:
                encorded_word = encorded_word.replace(sign, letter)
                del _key_dict[letter]
                break
    return encorded_word


def main():
    decoded_word = input('введите шифр: ')
    count = int(input('сколько букв в словаре? '))
    key_dict = {}
    for i in range(count):
        letter = input('введите букву: ')
        key_dict[letter] = int(input(
            'введите количество повторений: '
        ))
    print(encoder(decoded_word, key_dict))


if __name__ == '__main__':
    main()
