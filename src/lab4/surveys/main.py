import typing as tp
import sys


class GroupDistributions:

    def __init__(self):          
        self.groups = []
        self.ranges = []
        self.users = []

    def distribute(self, users: tp.List[tp.List], borders: tp.List[tp.List]) -> tp.List:
        borders = sorted([0, *list(map(int, borders)), 123])
        self.ranges = sorted([[borders[i]+1, borders[i+1]] for i in range(len(borders)-1)], reverse=True)
        self.groups  = [ [] for _ in self.ranges ]

        for user in users:
            name, age = user
            for n, border in enumerate(self.ranges):
                start, end = border
                if age in range(start, end+1):
                    self.groups[n] += [user]

        return self.groups


    def input(self):
        input_data = input()
        while input_data != 'END':
            name, age = [ el.strip() for el in input_data.split(',') ]
            self.users.append([name, int(age)]) 
            input_data = input()


    def print(self):
        for n, group in enumerate(self.groups):
            if len(group) > 0:
                start, end = self.ranges[n]
                users_list = [ f"{name} ({age})" for name, age in sorted(group, reverse=True, key=(lambda user: (user[1], user[0]))) ]
                print(f'{start}-{end}: {", ".join(users_list) }')


if __name__ == '__main__':
    borders = sys.argv[1:]

    groupSystem = GroupDistributions()
    groupSystem.input()
    groupSystem.distribute(groupSystem.users, borders)
    groupSystem.print()