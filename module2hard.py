stone_22 = []
options_spicok = []
a = 1
while a <= 101:
    options_spicok.append(a)
    a = a + 1

name = int(input("Введите число написанное на камне: "))
if name <= 20 and name >= 3:
        for i in range(len(options_spicok)):
            for j in range(len(options_spicok)):
                if i == j:
                    continue
                if options_spicok[i] + options_spicok[j] == name:
                    stone_22 += [[options_spicok[i], options_spicok[j]]]
        for k in stone_22[:len(stone_22) // 2]:
#            print('Число на камне: ', name)
            print(*k, end='')
else:
        print("На камне не может быть этого чила, перепроверь и напиши правильный ")
