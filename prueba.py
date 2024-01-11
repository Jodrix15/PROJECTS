dicc = {"daily": {"temperatura": [2, 0, 4]}}

for x, y in dicc["daily"].items():

    if x == "temperatura":
        for a in y:
            print(a)