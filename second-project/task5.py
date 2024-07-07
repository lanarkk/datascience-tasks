import re
from json import dumps


def analisys(filepath):
    dictionary_final = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        line_count = 1
        for line in f:
            words = line.split()
            for word in words:
                cleaned_word = re.match(r'\w+', word).group().lower()

                if cleaned_word in dictionary_final:
                    dictionary_final[cleaned_word]['count'] += 1
                    dictionary_final[cleaned_word]['lines'].append(line_count)
                else:
                    dictionary_final[cleaned_word] = {
                        'count': 1, 'lines': [line_count]
                    }
            line_count += 1

    print(dumps(dictionary_final, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    analisys('file_to_read.txt')
