diagonal, heightratio, widthratio = map(int, input().split())

diagonalratio = diagonal / ((heightratio ** 2 + widthratio ** 2) ** 0.5)

print(int(heightratio * diagonalratio), int(widthratio * diagonalratio))