from aoc import AOC
from collections import defaultdict

aoc = AOC(year=2022, day=7)
data = aoc.load()

class Computer:
    def __init__(self):
        self.cwd = ''
        self.dirs = {'': []}

    def handle(self, str):
        if str.startswith('$'):
            self._handle_command(str)
        else:
            self._add_listing(str)

    def _handle_command(self, cmd):
        cmd = cmd.split(' ')
        match cmd[1]:
            case 'cd':
                self._cd(cmd[2])
            case 'ls':
                pass

    def _add_listing(self, listing):
        listing = listing.split(' ')
        if listing[0] == 'dir':
            self._cd(listing[1])
            self._cd('..')
        else:
            self.dirs[self.cwd].append((listing[1], int(listing[0])))

    def _cd(self, str):
        if str == '..':
            self.cwd = self.cwd[:self.cwd.rindex('/')]
        elif str == '/':
            self.cwd = ''
        else:
            self.cwd += f'/{str}'

        for dir in self._walk(self.cwd):
            if dir not in self.dirs:
                self.dirs[dir] = []

    def _walk(self, basedir):
        dirnames = ['']
        curdir = ''
        for dir in basedir.split('/'):
            if not dir:
                continue

            curdir += f'/{dir}'
            dirnames.append(curdir)
        return dirnames

    def sizes(self):
        sizes = defaultdict(int)
        for basedir in self.dirs:
            size = sum(f[1] for f in self.dirs[basedir])
            for dir in self._walk(basedir):
                sizes[dir] += size
        return sizes

comp = Computer()
for t in data.lines():
    comp.handle(t)

sizes = comp.sizes()
total_size = sum(sizes[d] for d in sizes if sizes[d] < 100_000)
aoc.p1(total_size)

total_disk_space = 70_000_000
needed_space = 30_000_000
min_dir_size = needed_space - (total_disk_space - sizes[''])
aoc.p2(next(filter(lambda s: s > min_dir_size, sorted(sizes.values()))))
