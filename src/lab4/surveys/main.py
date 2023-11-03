import sys

arguments = list(map(int, sys.argv[1:]))
groups = { group:[] for group in arguments }
respondents = []

while True:
    data = input()

    if data == 'END': break

    fullname, age = data.split(',')

    for group in groups.keys():
        print(group)
    

    respondents.append([fullname, int(age)])

print(groups)