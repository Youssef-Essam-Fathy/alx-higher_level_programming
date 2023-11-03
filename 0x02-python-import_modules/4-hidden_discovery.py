#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for indx in dir(hidden_4):
        if indx[:2] != "__":
            print(indx)
