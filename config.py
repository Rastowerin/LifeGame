SIZE = 50

SETTINGS = (range(4, 9))
SETTINGS = (0, 1, *SETTINGS)

m, cm = [], []
for i in range(SIZE):
    m.append([])
    cm.append([])
    for j in range(SIZE):
        m[i].append(0)
        cm[i].append(0)
