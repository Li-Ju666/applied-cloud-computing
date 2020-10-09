from flask import Flask, request
from flask_restful import Resource, Api

from .tasks import analyze
import time
import os, random

app = Flask(__name__)
api = Api(app)

class Statistics(Resource):
    def __init__(self):
        self.stats = {'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0, 'hen':0}

    def get_all(self, num):
        # check if stats has been done
        records = 0
        for key in self.stats:
            records += self.stats[key]

        # do full statistics if stats is empty
        if records == 0:
            baseDir = "project/data/"
            all_files = os.listdir(baseDir)
            files = []
            for i in range(0, num):
                files.append(all_files[random.randint(1,100)])

            files = map(lambda a: baseDir+a, files)
            results = []
            for i in files:
                results.append(analyze.delay(i))
            finished = 0
            while (finished != len(results)):
                print("Waiting...")
                time.sleep(0.1)
                finished = sum(map(lambda a: a.ready(), results))
                print('Now finished: ', finished, '/', len(results))

            # print("Finished! ")
            for i in results:
                tmp = i.get(timeout=1)
                self.stats['han'] += tmp['han']
                self.stats['hon'] += tmp['hon']
                self.stats['den'] += tmp['den']
                self.stats['det'] += tmp['det']
                self.stats['denna'] += tmp['denna']
                self.stats['denne'] += tmp['denne']
                self.stats['hen'] += tmp['hen']
        return self.stats
    def get(self, num):
        return self.get_all(num)

api.add_resource(Statistics, '/<int:num>')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')

