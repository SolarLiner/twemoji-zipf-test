#%%
def inverse_function(x, s, p):
    return s * x**-p


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
from collections import Counter
import operator

random_text = open('./assets/frequency_analysis_jp.txt', mode='rt')
text_data = random_text.read().replace(' ', '')  # Remove spaces from text

occurences = dict(Counter(text_data))
occurences = dict(sorted(occurences.items(), key=operator.itemgetter(1))[::-1])

data = np.array([occurences[key] for key in occurences])
index = np.arange(data.size)

popt, pcov = curve_fit(inverse_function, index + 1, data)
freq_fit = inverse_function(index + 1, *popt)

plt.bar(index, data,
        label="Number of occurences"
        )
plt.plot(index, freq_fit, '--',
         c='r',
         label="Zipf's law ($f(x) = \\frac{{ {} }}{{ x^{{ {} }} }}$)\nCorr: {}%".format(
             round(popt[0], 2),
             round(popt[1], 2),
             round(np.corrcoef(data, freq_fit)[0][1] * 100.0, 1)
         )
         )
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off'  # labels along the bottom edge are off
)
plt.xlabel('Japanese caracters count')
plt.legend(loc='upper right')
plt.show()
