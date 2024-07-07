trips = [
    {"start": "B", "end": "C"},
    {"start": "A", "end": "B"},
    {"start": "A", "end": "B"},
    {"start": "A", "end": "C"},
    {"start": "B", "end": "A"},
    {"start": "A", "end": "B"},
    {"start": "B", "end": "C"},
    {"start": "A", "end": "C"}
]


def counter(trips):
    routes_dict = {}
    for routes in trips:
        if routes_dict.get(f'{routes["start"]}->{routes["end"]}'):
            routes_dict[f'{routes["start"]}->{routes["end"]}'] += 1
        else:
            routes_dict[f'{routes["start"]}->{routes["end"]}'] = 1
    sorted_dict = dict(sorted(
        routes_dict.items(), key=lambda item: item[1], reverse=True
    ))
    output = []
    for route, count in sorted_dict.items():
        output.append({"route": route, "count": count})
    output = output[0:3]
    return output


if __name__ == '__main__':
    print(counter(trips))
