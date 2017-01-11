import matplotlib.pyplot as plt
import numpy as np

open_mp_2000 = np.array([14.34,15.32,16.32,17.55,18.98,20.54,21.99,24.4,27.32,
                         31.12,34.44,41.1,51.23,67.99,96.55,191.68])

open_mp_4000 = np.array([112.04,119.67,127.89,137.67,149.13,162.13,173.77,
                         191.91,215.28,245.84,271.91,324.36,404.59,538.48,
                         769.54,1520.67])

open_mp_5000 = np.array([218.83,233.08,249.68,271.13,292.06,316.04,338.61,
                         374.78,419.99,479.47,529,634.29,790.46,1052.3,1494.31,
                         2972.09])

hpx_2000 = np.array([1.43,1.48,1.52,1.59,1.64,1.75,1.92,2.12,2.37,2.63,3.05,
                     3.47,4.28,5.4,7.96,14.83])

hpx_4000 = np.array([10.37,11.17,11.53,12.19,13.14,14.42,15.58,16.81,18.35,
                     20.72,23.8,27.49,33.69,42.29,62.51,116.04])

hpx_5000 = np.array([20.31,21.1,22.51,24.57,25.94,27.55,30.94,32.78,36.13,
                     40.53,46.69,53.58,66.09,82.85,121.51,225.84])

Linear2000 = 192.7
Linear4000 = 1541.53
Linear5000 = 2985.52

omp_vs_hpx_2000 = np.array(open_mp_2000/hpx_2000)

omp_2000_vs_linear = np.array(Linear2000/open_mp_2000)
hpx_2000_vs_linear = np.array(Linear2000/hpx_2000)

tmp = list(reversed(range(17)))
tmp.pop(16)
range = np.array(tmp)

plt.figure(1)
line1, line2 = plt.plot(range, omp_2000_vs_linear, 'bs-', range, hpx_2000_vs_linear,'g^-')
plt.setp(line1,label='OMP')
plt.setp(line2,label='HPX')
plt.title('OMP & HPX Speed-Up vs Linear\n3000x3000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.legend(handles=[line1,line2])
plt.legend(bbox_to_anchor=(.5,.8),bbox_transform=plt.gcf().transFigure,loc=1)
plt.show()

plt.figure(2)

omp_4000_vs_linear = np.array(Linear4000/open_mp_4000)
hpx_4000_vs_linear = np.array(Linear4000/hpx_4000)

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

omp_5000_vs_linear = np.array(Linear5000/open_mp_5000)
hpx_5000_vs_linear = np.array(Linear5000/hpx_5000)

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

omp_vs_hpx_3000 = np.array(open_mp_2000/hpx_2000)

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