import matplotlib.pyplot as plt
import numpy as np

open_mp_2000 = np.array([1.46,1.57,1.61,1.74,1.85,1.98,2.11,2.35,2.56,2.8,
                         3.22,3.83,4.77,5.99,8.92,15.71])

open_mp_4000 = np.array([10.67,11.51,12.1,12.81,13.67,14.33,15.7,17.36,19.24,
                         21.08,24.14,28.57,35.46,45.14,67.12,120.98])

open_mp_5000 = np.array([20.67,21.5,22.67,24.77,26.59,28.1,30.63,33.18,37.37,
                         41.99,46.87,54.8,68.52,89.79,130.35,234.26])

open_mp_10000 = np.array([221.16,250.18,254.2,253.98,269.03,297.76,306.22,
                          342.16,378.35,412.56,474.18,595.39,726.79,859.03,
                          1215.14,2074.07])

hpx_2000 = np.array([1.43,1.48,1.52,1.59,1.64,1.75,1.92,2.12,2.37,2.63,3.05,
                     3.47,4.28,5.4,7.96,14.83])

hpx_4000 = np.array([10.37,11.17,11.53,12.19,13.14,14.42,15.58,16.81,18.35,
                     20.72,23.8,27.49,33.69,42.29,62.51,116.04])

hpx_5000 = np.array([20.31,21.1,22.51,24.57,25.94,27.55,30.94,32.78,36.13,
                     40.53,46.69,53.58,66.09,82.85,121.51,225.84])

hpx_10000 = np.array([168.31,174.08,184.36,199.36,210.22,233.32,251.37,282.17,
                      298.23,335.08,383.09,441.63,542.64,677.97,996.58,
                      1835.05])

Linear2000 = 15.71
Linear4000 = 121.52
Linear5000 = 236.05
Linear10000 = 1877.84

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

omp_vs_hpx_10000 = np.array(open_mp_10000/hpx_10000)

omp_10000_vs_linear = np.array(Linear10000/open_mp_10000)
hpx_10000_vs_linear = np.array(Linear10000/hpx_10000)

plt.figure(7)
line10, line11 = plt.plot(range, omp_10000_vs_linear, 'bs-', range, hpx_10000_vs_linear,'g^-')
plt.setp(line10,label='OMP')
plt.setp(line11,label='HPX')
plt.title('OMP & HPX Speed-Up vs Linear\n10000x10000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.legend(handles=[line10,line11])
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

line8 = plt.plot(range, omp_vs_hpx_4000, 'bs-')
plt.title('HPX vs OMP Speed-Up\n4000x4000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.show()

plt.figure(5)

omp_vs_hpx_5000 = np.array(open_mp_5000/hpx_5000)

line9 = plt.plot(range, omp_vs_hpx_5000, 'bs-')
plt.title('HPX vs OMP Speed-Up\n5000x5000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.show()

plt.figure(8)

omp_vs_hpx_10000 = np.array(open_mp_10000/hpx_10000)

line9 = plt.plot(range, omp_vs_hpx_10000, 'bs-')
plt.title('HPX vs OMP Speed-Up\n10000x10000')
plt.xlabel('Number of Cores')
plt.ylabel('Speed up multiplier')
plt.show()





