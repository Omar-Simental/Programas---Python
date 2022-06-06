
import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np

os.system('clear')

fifa = pd.read_csv('players_21.csv')
mc = fifa.query("club_name=='Manchester City'")
ch = fifa.query("club_name=='Chelsea'")
mi = fifa.query("club_name=='Milan'")
aj = fifa.query("club_name=='Ajax'")

print(fifa.shape, mc.shape, ch.shape, mi.shape, aj.shape)

# Gráficas cara a cara misma figura

plt.figure(figsize=(10,8))
plt.title('Histograma de Estatura')
plt.xlabel('Estatura')
plt.ylabel('Número de Jugadores')
plt.hist(mc.height_cm, color='cyan', density=False, label='RM')
plt.legend(loc='upper right')
plt.close() 

# Barras / Jugadores mas valiosos

dgrm = mc['value_eur'].sort_values(ascending=False).iloc[0:5]
dgbr = ch['value_eur'].sort_values(ascending=False).iloc[0:5]

n = dgrm.shape[0]
sp = np.arange(n)
w = 0.3

plt.figure(figsize=(0,10))
plt.title('Valor en Euros')
plt.xlabel('Jugador')
plt.ylabel('Valor Euros')
plt.bar(sp, dgrm, w, color='red', edgecolor='blue', label='RM')
plt.bar(sp + w, dgbr, w, color='blue', edgecolor='blue', label='BR')
plt.legend()
plt.xticks(sp,['Jugador 1','Jugador 2','Jugador 3','Jugador 4','Jugador 5'])
#plt.show()
plt.close()

# Boxplot / Rendimento 
plt.figure(figsize=(10,8))
plt.title('Rendimiento General de los Jugadores')
plt.ylabel('Rendimento')
sp = np.arange(2)
dg = [mc.overall, ch.overall, mi.overall, aj.overall]
plt.boxplot(dg, labels=['RM','BR','JV','LP'])
#plt.show()
plt.close()
 

# Poner graficas en un plot diferente box

# Pie / Jugadores por País

dgrm = mc.nationality.value_counts()
dgbr = ch.nationality.value_counts()
dgjv = mi.nationality.value_counts()
#print(dgrm, dgbr, dgjv)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,6))
fig.suptitle('Jugadores por País')
plt.subplots_adjust( wspace=0.3 )
ax1.title.set_text('Manchester City')
ax1.pie(labels=dgrm.index, x=dgrm.values, autopct='%1.0f%%', startangle=90, shadow=True)
ax2.title.set_text('Chelsea')
ax2.pie(labels=dgbr.index, x=dgbr.values, autopct='%1.0f%%', startangle=90, shadow=True)
ax3.title.set_text('Milan')
ax3.pie(labels=dgjv.index, x=dgjv.values, autopct='%1.0f%%', startangle=90, shadow=True)
#plt.show()
plt.close()


# scatter - Edad vs rendimiento  
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

fig, ax = plt.subplots(2,2, constrained_layout=True, figsize=(10,8))
fig.suptitle('Edad vs Rendimiento', size=18)
fig.supxlabel('Edad')
fig.supylabel('Rendimiento')
ax[0,0].set_title('Manchester City')
ax[0,0].scatter(mc.age, mc.overall)
ax[0,1].set_title('Chelsea')
ax[0,1].scatter(ch.age, ch.overall)
ax[1,0].set_title('Milan')
ax[1,0].scatter(mi.age, mi.overall) 
ax[1,1].set_title('Ajax')
ax[1,1].scatter(aj.age, aj.overall)
#plt.show()
plt.close()


# hexbin / Edad vs Potencial

fig = plt.figure(figsize=(10,8))
fig.suptitle('Edad vs Potencial')

ax1 = fig.add_subplot(2,2,1)
ax1.set_title('Manchester City')
im1 = ax1.hexbin(mc.age,mc.potential, cmap="Blues", gridsize=20)
fig.colorbar(im1)

ax2 = fig.add_subplot(2,2,2)
ax2.set_title('Chelsea')
im2 = ax2.hexbin(ch.age,ch.potential, cmap="Greens", gridsize=20)
fig.colorbar(im2)

ax3 = fig.add_subplot(2,2,3)
ax3.set_title('Milan')
im3 = ax3.hexbin(mi.age, mi.potential, cmap="Purples", gridsize=20)
fig.colorbar(im3)

ax4 = fig.add_subplot(2,2,4)
ax4.set_title('Ajax')
im4 = ax4.hexbin(aj.age, aj.potential, cmap="Oranges", gridsize=20)
fig.colorbar(im4)

plt.show()
plt.close()