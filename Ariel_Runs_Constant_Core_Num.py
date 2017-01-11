import matplotlib.pyplot as plt
import numpy as np

OMP_16 = np.array([1.46,10.67,20.67,221.16])
HPX_16 = np.array([1.43, 10.37, 20.31, 168.31])
Linear = np.array([15.71,121.52,236.05,1877.84 ])

OMP_VS_LINEAR_16 = np.array(Linear/OMP_16)
HPX_VS_LINEAR_16 = np.array(Linear/HPX_16)

range = np.array([2000,4000,5000,10000])

plt.figure(1)
line1, line2 = plt.plot(range, OMP_VS_LINEAR_16, 'bs-', range, HPX_VS_LINEAR_16,'g^-')
plt.setp(line1,label='OMP')
plt.setp(line2,label='HPX')
plt.title('OMP & HPX Speed-Up vs Linear\n16 Cores')
plt.xlabel('Size of array')
plt.ylabel('Speed up multiplier')
plt.legend(handles=[line1,line2])
plt.legend(bbox_to_anchor=(.4,.6),bbox_transform=plt.gcf().transFigure,loc=1)
plt.show()
