# import sys
#
#
# def printsave(*a):
#     file = open('x.txt', 'a')
#
#     print(*a)
#     print(*a, file=file)
#
#     file.close()
#
#
# if __name__ == '__main__':
#     printsave('PyCharm')


a = 98765.4321
print(f"{a}")       # 98765.4321
print(f"{a:>20}")   #           98765.4321
print(f"{a:<20}")   # 98765.4321          /
print(f"{a:^20}")   #     98765.4321      /
print(f"{a:*^20}")  # *****98765.4321*****
print(f"{438765434567654345:,}")  # 438,765,434,567,654,345
print(f"{438765434567654345:,>50,}")
#,,,,,,,,,,,,,,,,,,,,,,,,,,,438,765,434,567,654,345