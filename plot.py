import numpy as np 
import matplotlib.pyplot as plt 

X = ['1T','2T','4T','8T'] 
push = [2.373063,
1.654754,
1.661270,
2.175396

] 
pull = [3.471682,
1.905091,
0.965238,
0.736253

] 
push_atomic = [6.135846,
3.239259,
1.693659,
0.878245,

]

pull2 = [226.290292,
110.201709,
50.564838,
34.930343

]
push2 = [108.192203,
73.161487,
52.299620,
56.274677

]
push_atomic2 = [273.807188,
147.402898,
 76.398504,
38.963251

]

X_axis = np.arange(len(X)) 

plt.figure()
plt.bar(X_axis, push, 0.3, label='Push')           # Shift by -0.3
plt.bar(X_axis-0.3, pull, 0.3, label='Pull')                 # No shift
plt.bar(X_axis + 0.3, push_atomic, 0.3, label='Push Atomic')


plt.xticks(X_axis, X) 
plt.xlabel("Threads") 
plt.ylabel("Time (seconds)") 
plt.title("Algorithm vs Time (roadNet-CA)") 
plt.legend() 
plt.savefig("roadNet.jpg")

plt.figure()
plt.bar(X_axis, push2, 0.3, label='Push')           # Shift by -0.3
plt.bar(X_axis-0.3, pull2, 0.3, label='Pull')                 # No shift
plt.bar(X_axis + 0.3, push_atomic2, 0.3, label='Push Atomic')


plt.xticks(X_axis, X) 
plt.xlabel("Threads") 
plt.ylabel("Time (seconds)") 
plt.title("Algorithm vs Time (test_25M_50M)") 
plt.legend() 
plt.savefig("test25.jpg")

