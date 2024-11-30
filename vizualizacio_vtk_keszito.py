import numpy as np
import pyvista as pv

# Paraméterek
num_points = 100  # Mintavételi pontok száma
# t paraméter a [0, 1] tartományban
t = np.linspace(0, 1, num_points)

# Képlet szerinti koordináták generálása
x = t * (1 - t)  # x(t) = t(1-t)
y = t**2 * (1 - t) ** 3  # y(t) = t^2(1-t)^3
z = np.zeros_like(x)  # 2D síkban: z = 0

# Pontok definiálása
points = np.column_stack((x, y, z))

# PyVista PolyData objektum
line = pv.PolyData()
line.points = points

# Csatlakozó élek létrehozása
# Az éleknek 3 értéket kell tartalmaznia: 2 (értékek száma), majd az index
lines = np.zeros((num_points, 3), dtype=int)
for i in range(num_points):
    lines[i, 0] = 2  # Két pontot összekapcsol
    lines[i, 1] = i  # Az i-edik pont
    # A következő pont (körbefordulva az utolsó pont az elsővel összekapcsolódik)
    lines[i, 2] = (i + 1) % num_points

# Létrehozott élek hozzárendelése
line.lines = lines

# VTK fájl mentése
line.save("custom_curve.vtk")

print("A görbe VTK fájlba mentve: custom_curve.vtk")
