
# -*- coding:UTF-8 -*-

import numpy as np
def chi2_test(index, *args):

 import numpy as np
 from scipy.stats import chi2
 from scipy.stats import norm
 import statistics
 import scipy
 import sys
 c = [0] * index
 n = [0] * index
 miu = [0] * index
 sigma = [0] * index
 y_sample_bar = [0] * index
 s_sample = [0] * index
 var_y_bar = [0] * index
 wi = [0] * index
 sum_var_y_bar = 0
 y_bar = 0
 Ai = [0] * index
 t = 0
 ai = [0] * index
 sumabc = 0
 for i in range(0, len(n)):
  n[i] = args[i]
  miu[i] = args[len(n) + i]
  sigma[i] = args[len(n) * 2 + i]
  c[i] = np.random.normal(loc=miu[i], scale=sigma[i], size=n[i])

  y_sample_bar[i] = np.mean(c[i])

  s_sample[i] = statistics.variance(c[i])

  var_y_bar[i] = s_sample[i] / n[i]

  sum_var_y_bar += (1 / var_y_bar[i])

 for i in range(0, len(n)):
  wi[i] = (1 / var_y_bar[i]) / sum_var_y_bar
 
  y_bar += (wi[i] * y_sample_bar[i])


 lower_chi = norm.ppf(0.025)

 upper_chi = norm.ppf(0.975)


 lower_ci = y_bar - (upper_chi/np.sqrt(sum_var_y_bar))

 upper_ci = y_bar - (lower_chi/np.sqrt(sum_var_y_bar))




params_list = [
]

output = ""
count_dict = {}
for params in params_list:
 params_tuple = tuple(params)
 count_dict[params_tuple] = 0

count = 1

for _ in range(5000):
    for params in params_list:
        np.random.seed(count)  
        p_value = chi2_test(*params)
        params_tuple = tuple(params)
        if p_value == 1:
            count_dict[params_tuple] += 1
        count += 1

output = ""
for params, count in count_dict.items():
    proportion = count / 5000
    output += f"Parameter: {params}, Proportion: {proportion:.4f}\n"


file = open("ci1.txt", "w")
file.write(output)
file.close()
