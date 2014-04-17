from random import randint

def calls(n): # n is the number of days we want
              # to inspect the function for
    positive_outcome = 0
    days_of_week = [0, 0, 0, 0, 0, 0, 0]
    for number in range(0, n):
        for i in range(0, 12):
            days_of_week[randint(0, 6)] +=1
        if 0 not in days_of_week:
            positive_outcome += 1
        days_of_week = [0, 0, 0, 0, 0, 0, 0]
    return float(positive_outcome / n)

def main():
    print(calls(10))
    print(calls(100))
    print(calls(1000))
    print(calls(10000))
    print(calls(100000))
    print(calls(1000000))

if __name__ == '__main__':
    main()