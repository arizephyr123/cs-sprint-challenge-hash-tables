# Your code here
def finder(files, queries):
    path_dict = {}
    result = []
    for file in files:
        temp_paths = file.split('/')
        for path in temp_paths:
            if path is '':
                pass
            else:
                try:
                    if path_dict[path]:
                        path_dict[path].append(file)
                except:
                    path_dict[path] = [file]

    for query in queries:
        try:
            if path_dict[query]:
                result = result + path_dict[query]
            else:
                pass
        except:
            pass

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    # print(finder(files, queries))
