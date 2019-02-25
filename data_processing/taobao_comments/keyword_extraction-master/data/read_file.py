with open('csv000.csv', 'r', encoding='utf-8')as r:
    results = r.readlines()

for result in results:
    with open('results.csv', 'a')as f:
        f.write(result)
