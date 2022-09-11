def checkIfCorrectTriangle(a, b, c):
    if(a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False

print(checkIfCorrectTriangle(20, 30, 20))
print(checkIfCorrectTriangle(5, 30, 20))
print(checkIfCorrectTriangle(5, 10, 8))
print(checkIfCorrectTriangle(2, 3, 1))