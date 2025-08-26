import re

#test x^2+17x+27

def main():
    qd_inpt = input("Ex.(x^2-17x+10), Input your quadratic: ")

    sqd = re.split(r'[-+=]', qd_inpt)
    aqd = sqd[1].split
    for i in aqd:
        if i != type(int):
            aqd.remove[i]
    bqd = 1
    cqd = 2
    print(aqd)
    print(bqd)
    print(cqd)

    def factor(qd_input):
        next
        

    while True:
        option = 0
        try:
            option == int(input("What would you like to do with this quadratic?\n(1) Factor it\n(2) Solve for variable\nType the number corrosponding to your selection: "))
            if option != 1 or option != 2:
                option = ("Error")
        except(ValueError):
            print("Please only type '1', or '2'")
            continue
        if option == 1:
            factor(qd_inpt)

main()