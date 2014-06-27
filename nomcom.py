import csv, os, sys

from bs4 import BeautifulSoup
import requests

def generate():
    names = []
    for path in os.listdir('names'): 
        with open('names/%s' % path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0].strip().split()
                name = [name[0], name[-1]]
                if name[0] == name[1] or name in names:
                    continue
                names.append(name)

    total = len(names)
    combos = []
    for n, name in enumerate(names):
        print('%s / %s - %s' % (n + 1, total, name))
        for name2 in names:
            if name == name2:
                continue
            if name[-1] == name2[0]:
                combos.append(name + name2[1:])

    total = len(combos)
    for n, combo in enumerate(combos):
        print('%s / %s - %s' % (n + 1, total, combo))
        for name in names:
            if name in (combo[:2], combo[1:]):
                continue
            if combo[-1] == name[0]:
                combos[n] = combo + name[1:]

    with open('combos.txt', 'w') as file:
        for combo in sorted(c for c in combos if len(c) == 4):
            file.write(' '.join(combo) + '\n')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        generate()
    else:
        url = sys.argv[1]
        res = requests.get(url)
        soup = BeautifulSoup(res.text)
        with open('names/%s.csv' % url.split('/')[-1], 'w') as file:
            writer = csv.writer(file)
            for li in soup.find_all('li'):
                if li.a and li.a.get('title'):
                    if 'table' in [p.name for p in li.parents]:
                        continue
                    name = li.a['title'].split(',')[0].split('(')[0]
                    if 'List' in name or 'Template' in name or 'Wikipedia' in name:
                        continue
                    writer.writerow([name])


