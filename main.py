from func import *

create(11, 3)
create(12, 3)
create(13, 3)
create(13, 2)
create(12, 1)

# cord = SIZE // 2 - 1
# create(cord, cord)
# create(cord + 1, cord - 1)
# create(cord - 1, cord - 1)
# create(cord + 1, cord + 1)
# create(cord - 1, cord + 1)

a = 0
while True:
    a += 1
    for i in range(SIZE):
        for j in range(SIZE):
            cm[i][j] = check(m, i, j)

    for i in range(SIZE):
        for j in range(SIZE):
            if cm[i][j] == 3 and m[i][j] == 0:
                create(i, j)
            elif m[i][j] == 1 and (cm[i][j] in SETTINGS):
                destroy(i, j)
            else:
                pass

    if a == 50:
        w.update_idletasks()
        w.update()
        a = 0
