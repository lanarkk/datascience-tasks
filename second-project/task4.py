def query(dictionary):
    query_to_list = []
    for key, item in dictionary.items():
        query_to_list.append(f'{key}={item}')
    query_to_list.sort()
    query_to_list = '&'.join(query_to_list)
    return query_to_list


def test():
    try:
        assert (
            (
                query(
                    {
                        'course': 'python',
                        'lesson': 2,
                        'challenge': 17
                    }
                )
            ) == 'challenge=17&course=python&lesson=2'
        )
    except AssertionError:
        print('Ошибка в query, возращает не то значение.')
    else:
        print('тест пройден.')


def main():
    test()


if __name__ == '__main__':
    main()
