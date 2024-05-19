# Create variables
X = True
Y = False
W = X or Y
print("X:", X)
print("Y:", Y)
print("W (X or Y):", W)

#show the W
print("\nW 的真值表:")
print("X | Y | W (X or Y)")
for x in [False, True]:
    for y in [False, True]:
        print(f"{x} | {y} | {x or y}")