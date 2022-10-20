import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("data.txt", dtype=np.int)
settings = np.genfromtxt("settings.txt", dtype=np.float)

a = np.empty(len(data))

for i in range(len(data)):
    a[i] = data[i]*(3.3/256)
a_1 = np.empty(10)
for i in range(0, 10):
    a_1[i] = data[i*88]*(3.3/256)

print(len(data))
MAX = a.argmax()
print(MAX)
#y = a#np.linspace(0, 3.3, len(data))
x = np.linspace(0, settings[0]*len(data), len(data))
x_1 = np.linspace(0, settings[0]*len(data), len(a_1))
fig, ax = plt.subplots()
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепи")
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")
ax.text(8, 2.8, "Время заряда = " + str((x[MAX]//0.01)*0.01)[:4] + " с", fontsize = 10)
ax.text(8, 2.6, "Время разаряда = " + str(x[len(x) - 1]-x[MAX])[:4] + " с", fontsize = 10)
#plt.scatter(x, a)
ax.minorticks_on()
ax.grid(which='major', color = 'lightgray', linewidth = 2)
ax.grid(which='minor', color = 'lightgray', linestyle = ":")
ax.plot(x, a, label = "V(t)", color = "darkorchid")
ax.legend()
fig.set_figheight(5)
fig.set_figwidth(8)
#ax.scatter(x_1, a_1)
plt.show()
fig.savefig('V(t).svg')