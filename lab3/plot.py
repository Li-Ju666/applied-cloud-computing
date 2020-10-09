from matplotlib import pyplot as plt
import numpy as np
# results = {'han': 97933, 'hon': 32512, 'den': 165524, 'det': 69414, 'denna': 2751, 'denne': 693, 'hen': 2792}
# labels = list(results.keys())
# values = list(results.values())
# counts = sum(values)
# values = list(map(lambda a: 100*a/counts, values))
# plt.bar(labels, values, color='b')
# plt.title("Frequencies of pronouns")
# plt.ylabel("%")
# plt.ylim(0,50)
# for i, v in enumerate(values):
#     plt.text(i - 0.25, v + 1.5, str(round(v,2)))
# plt.savefig("frequency.png")

strings = "0m6.721s 0m7.035s 0m6.826s 0m7.083s 0m7.083s\
 0m8.031s 0m8.671s 0m7.965s 0m7.702s 0m7.613s\
 0m8.362s 0m8.263s 0m8.505s 0m8.716s 0m8.620s\
 0m9.174s 0m9.741s 0m8.998s 0m10.234s 0m8.266s\
 0m9.566s 0m10.173s 0m9.401s 0m11.909s 0m9.500s\
 0m9.499s 0m10.054s 0m10.507s 0m11.450s 0m8.956s\
 0m11.056s 0m10.990s 0m9.662s 0m10.141s 0m10.639s\
 0m10.663s 0m11.419s 0m10.899s 0m10.775s 0m10.973s"

timestr = strings.split()
times = list(map(lambda a: float(a[2:][:-1]), timestr))
times = np.array(times).reshape(8,5)
means = list(map(lambda a: a.mean(), times))
stds = list(map(lambda a: a.std(), times))
nums = list(range(1,9))

effs = list(map(lambda a: 100*means[0]/a, means))

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)

ax0.errorbar(nums, means, stds, fmt='-o', ecolor='r')
ax0.set_title("Weak scalability: running time ~ number of workers")
ax0.set_xlabel("Number of workers")
ax0.set_ylabel("Running time/s")
ax0.set_ylim(0, 12)

ax1.plot(nums, effs, marker='o')
ax1.set_title("Weak scalability: efficiency ~ number of workers")
ax1.set_xlabel("Number of workers")
ax1.set_ylabel("Efficiency/%")
ax1.set_ylim(0, 105)

plt.savefig("weak.png")
