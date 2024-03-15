#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden = dir(hidden_4)
    for func in hidden:
        if func[0] != "_":
            print(func)
