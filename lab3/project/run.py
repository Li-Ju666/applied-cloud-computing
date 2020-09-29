from .tasks import analyze
import time
import os

if __name__=='__main__':
    baseDir = "project/data/"
    files = os.listdir(baseDir)
    files = map(lambda a: baseDir+a, files)

    results = []
    for i in files:
        results.append(analyze.delay(i))

    finished = 0
    while (finished != len(results)):
        print("Sleeping for 5 sec...")
        time.sleep(5)
        finished = sum(map(lambda a: a.ready(), results))
        print('Now finished: ', finished, '/', len(results))

    print("Finished! ")
    stats = {'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0, 'hen':0}
    for i in results:
        tmp = i.get(timeout=1)
        stats['han'] += tmp['han']
        stats['hon'] += tmp['hon']
        stats['den'] += tmp['den']
        stats['det'] += tmp['det']
        stats['denna'] += tmp['denna']
        stats['denne'] += tmp['denne']
        stats['hen'] += tmp['hen']
    print(stats)
