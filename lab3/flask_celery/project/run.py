from flask import Flask, request
from flask_restful import Resource, Api

from .tasks import analyze
import time
import os

app = Flask(__name__)
api = Api(app)

class Statistics(Resource):
    def __init__(self):
        self.stats = {'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0, 'hen':0}

    def get_all(self):
        # check if stats has been done
        records = 0
        for key in self.stats:
            records += self.stats[key]

        # do full statistics if stats is empty
        if records == 0:
            baseDir = "project/data/"
            files = os.listdir(baseDir)
            files = map(lambda a: baseDir+a, files)

            results = []
            for i in files:
                results.append(analyze.delay(i))

            finished = 0
            while (finished != len(results)):
                print("Waiting...")
                time.sleep(3)
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

    # def get_element(self, pronoun):
    #     sum = 0
    #     for key in self.stats:
    #         sum += self.stats[key]
    #     if sum == 0:
    #         _ = self.get_all()
    #     return {pronoun:self.stats[pronoun]}

    def get(self):
        return self.get_all()

api.add_resource(Statistics, '/')

if __name__ == '__main__':
    app.run(debug=True)
