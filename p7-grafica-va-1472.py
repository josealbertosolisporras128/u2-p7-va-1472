import matplotlib.pyplot as plt
import numpy as np
# jose solis NC 1472
no_lista=[1,2,3,17,48]
califa_ml=[20,30,80,100,90]
califa_va=[70,90,60,90,100]
plt.plot(no_lista,califa_ml,label="Calif ML")
plt.plot(no_lista,califa_va,label="Calif VA")
plt.title("calificaciones materias 1472")
plt.xlabel("numero de lista")
plt.ylabel("calificacion")
plt.legend()
plt.show()
