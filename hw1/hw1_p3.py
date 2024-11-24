"""
Programming assignment # 1
- Problem 3: Find numbers with the same number of 1s
"""
import copy

def main():
    n = int(input('n: '))
    x = copy.deepcopy(n)
    """ implement here """
    howmany1 = 0
    count = 0
    howmany1_ans = 0
    answer = n
    for i in range(0, n*100):
        if x % 2 == 1:
            howmany1 += 1
        x = x//2

    while count < 2:
        answer += 1
        vari = answer
        for j in range(0, n*100):
            if vari % 2 ==1:
                howmany1_ans += 1
            vari = vari//2
        if howmany1_ans == howmany1:
            count += 1
        howmany1_ans = 0
    print(answer)



    """ do not touch below code """


if __name__ == "__main__":
    main()

