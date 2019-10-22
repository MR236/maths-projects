from random import randint


def new():
    matrix = [[], [], []]
    n = 0
    while n < len(matrix):
        matrix[n] = [randint(-5,5), randint(-5,5), randint(-5,5)]
        n += 1
    return matrix


def inverse(matrix):
    identity = [[1,0,0],
                [0,1,0],
                [0,0,1]]
    inverted = [[1,0,0],
                [0,1,0],
                [0,0,1]]
    detA = (matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])
    detB = (matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])
    detC = (matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])
    detM = matrix[0][0] * detA - matrix[0][1] * detB + matrix[0][2] * detC
    n = 0
    while n < len(identity):
        i = 0
        while i < len(identity[n]):
            identity[n][i] = float(identity[n][i])
            inverted[n][i] = float(inverted[n][i])
            matrix[n][i] = float(matrix[n][i])
            i += 1
        n += 1
    if detM != 0:
        #print "The determinant is " + str(detM) + ", therefore the matrix is INVERTIBLE."
        lst = []
        i = 0
        while matrix != identity and i < 500:
            #print
            #print matrix
            #print inverted
            R1 = randint(0, 2)
            while R1 in lst:
                R1 = randint(0, 2)
            R2 = randint(0, 2)
            while R2 == R1:
                R2 = randint(0,2)
            zero = randint(0,2)
            while R1 == zero:
                zero = randint(0,2)
            if matrix[R2][zero] != 0:
                C = matrix[R1][zero] / matrix[R2][zero]
                matrix[R1][0] -= matrix[R2][0] * C
                matrix[R1][1] -= matrix[R2][1] * C
                matrix[R1][2] -= matrix[R2][2] * C
                inverted[R1][0] -= inverted[R2][0] * C
                inverted[R1][1] -= inverted[R2][1] * C
                inverted[R1][2] -= inverted[R2][2] * C
            if matrix[0][0] != 0 and matrix[0][1] == 0 and matrix[0][2] == 0:
                C = 1 / matrix[0][0]
                matrix[0][0] *= C
                matrix[0][1] *= C
                matrix[0][2] *= C
                inverted[0][0] *= C
                inverted[0][1] *= C
                inverted[0][2] *= C
                lst.append(0)
            if matrix[1][1] != 0 and matrix[1][0] == 0 and matrix[1][2] == 0:
                C = 1 / matrix[1][1]
                matrix[1][0] *= C
                matrix[1][1] *= C
                matrix[1][2] *= C
                inverted[1][0] *= C
                inverted[1][1] *= C
                inverted[1][2] *= C
                lst.append(1)
            if matrix[2][2] != 0 and matrix[2][1] == 0 and matrix[2][0] == 0:
                C = 1 / matrix[2][2]
                matrix[2][0] *= C
                matrix[2][1] *= C
                matrix[2][2] *= C
                inverted[2][0] *= C
                inverted[2][1] *= C
                inverted[2][2] *= C
                lst.append(2)
            i += 1
        if matrix == identity:
            return inverted
            #print "INVERSION (" + str(i) + " Operations)"
            #print inverted
        else:
            print("FAILED")
    else:
        #print "The determinant is " + str(detM) + ", therefore the matrix is NON-INVERTIBLE."
        return False


def multiply(matrix, matrix2):
    matrix3 = []
    n = 0
    while n < len(matrix):
        matrix3.append([])
        i = 0
        while i < len(matrix2[n]):
            x = 0
            u = 0
            while u < len(matrix2):
                x += matrix[n][u] * matrix2[u][i]
                u += 1
            matrix3[n].append(x)
            i += 1
        n += 1
    return matrix3


def equation_solver():
    print("WELCOME TO EQUATION SOLVER")
    print()
    print("INPUT FIRST EQUATION")
    print("Ax + By + Cz = D")
    A = int(input("A? "))
    B = int(input("B? "))
    C = int(input("C? "))
    D = int(input("D? "))
    print()
    print("INPUT SECOND EQUATION")
    print("Ex + Fy + Gz = H")
    E = int(input("E? "))
    F = int(input("F? "))
    G = int(input("G? "))
    H = int(input("H? "))
    print()
    print("INPUT THIRD EQUATION")
    print("Ix + Jy + Kz = L")
    I = int(input("I? "))
    J = int(input("J? "))
    K = int(input("K? "))
    L = int(input("L? "))
    matrix = [[A,B,C],[E,F,G],[I,J,K]]
    matrix2 = [[D],[H],[L]]
    inverted = inverse(matrix)
    print()
    if inverted == False:
        print("NO INDIVIDUAL SOLUTION")
    else:
        ans = multiply(inverted, matrix2)
        print("X = " + str(round(ans[0][0],2)))
        print("Y = " + str(round(ans[1][0],2)))
        print("Z = " + str(round(ans[2][0],2)))



equation_solver()