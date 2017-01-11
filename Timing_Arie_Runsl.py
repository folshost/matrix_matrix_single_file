import matplotlib.pyplot as plt
import numpy as np

open_mp_3000 = np.array([143.05, 151.05, 161.84, 173.59, 187.41, 204.97,
                         221.24, 243.53, 274.55, 306.25, 350.39, 410.56,
                         515.68, 671.71, 978.56, 1897.68])

open_mp_4000 = np.array([337.93, 360.85, 385.82, 413.28, 446.06, 479.52, 519.33,
                         576.1, 646.14, 738.22, 848.16, 977.97, 1222.42, 1584.79,
                         2320.55, 4535])

open_mp_5000 = np.array([653.97, 698.7, 747.38, 801.62, 870.1, 934.35, 1014.03,
                         1122.58, 1259.22, 1414.64, 1638.81, 1909.39, 2382.39,
                         3104.39, 4562, 8791])

hpx_3000 = np.array([24.91, 27.76, 28.37, 30.57, 32.47, 36.16, 37.85, 44.24,
                     46.43, 52.79, 60.92, 69.54, 86.36, 120.54, 189.18, 380.82])

hpx_4000 = np.array([83.49, 85.75, 94.34, 98.76, 107.91, 119.69, 130.78, 143.28,
                     138.59, 156.8, 184.28, 222.25, 269.9, 339.55, 559.62,
                     972.88])

hpx_5000 = np.array([194.63, 209.59, 221.76, 244.04, 262.07, 273.86, 343.65,
                     330.03, 313.21, 344.6, 390.23, 453.88, 574.5, 715.46,
                     1049.95, 2036.33])

omp_vs_hpx_3000 = np.array(open_mp_3000/hpx_3000)

omp_3000_vs_linear = np.array(1899/open_mp_3000)
hpx_3000_vs_linear = np.array(1899/hpx_3000)

tmp = list(reversed(range(17)))
tmp.pop(16)
range = np.array(tmp)

plt.figure(1)
line1, line2 = plt.plot(range, omp_3000_vs_linear, 'bs-', range, hpx_3000_vs_linear,'g^-')
plt.setp(line1,label='OMP')
plt.setp(line2,label='HPX')
plt.title('OMP & HPX Speed-Up vs Linear\n3000x3000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.legend(handles=[line1,line2])
plt.legend(bbox_to_anchor=(.5,.8),bbox_transform=plt.gcf().transFigure,loc=1)
plt.show()

plt.figure(2)

omp_4000_vs_linear = np.array(4494/open_mp_4000)
hpx_4000_vs_linear = np.array(4494/hpx_4000)

line3, line4 = plt.plot(range, omp_4000_vs_linear, 'bs-', range, hpx_4000_vs_linear, 'g^-')
plt.setp(line3,label='OMP')
plt.setp(line4,label='HPX')
plt.title('OMP & HPX Speed-Up vs Linear\n4000x4000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.legend(handles=[line1,line2])
plt.legend(bbox_to_anchor=(.5,.8),bbox_transform=plt.gcf().transFigure,loc=1)
plt.show()

plt.figure(3)

omp_5000_vs_linear = np.array(8763/open_mp_5000)
hpx_5000_vs_linear = np.array(8763/hpx_5000)

line5, line6 = plt.plot(range, omp_5000_vs_linear, 'bs-', range, hpx_5000_vs_linear, 'g^-')
plt.setp(line5,label='OMP')
plt.setp(line6,label='HPX')
plt.title('OMP & HPX Speed-Up vs Linear\n5000x5000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.legend(handles=[line1,line2])
plt.legend(bbox_to_anchor=(.5,.8),bbox_transform=plt.gcf().transFigure,loc=1)
plt.show()

plt.figure(6)

omp_vs_hpx_3000 = np.array(open_mp_3000/hpx_3000)

line7 = plt.plot(range, omp_vs_hpx_3000, 'bs-')
plt.title('HPX vs OMP Speed-Up\n3000x3000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.show()

plt.figure(4)

omp_vs_hpx_4000 = np.array(open_mp_4000/hpx_4000)

line7 = plt.plot(range, omp_vs_hpx_4000, 'bs-')
plt.title('HPX vs OMP Speed-Up\n4000x4000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.show()

plt.figure(5)

omp_vs_hpx_5000 = np.array(open_mp_5000/hpx_5000)

line7 = plt.plot(range, omp_vs_hpx_5000, 'bs-')
plt.title('HPX vs OMP Speed-Up\n5000x5000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.show()

