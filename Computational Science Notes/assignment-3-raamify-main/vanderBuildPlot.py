from VanderBuild import VanderBuild
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lu

x = np.arange(3,21)

y =np.array([])

for i in range (len(x)):
    mat =VanderBuild(x[i])
    temp = lu.norm(mat) * lu.norm(lu.inv(mat))
    y = np.append(y,temp)   

print(x)
print(y)
plt.plot(x, y)
plt.yscale('log')
plt.ylabel('Condition Number')
plt.xlabel('N value')
plt.show()