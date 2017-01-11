import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.,5.,0.2)
line1, line2 , line3 = plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')

plt.setp(line1,color='g',linewidth=30.0)

plt.show()

