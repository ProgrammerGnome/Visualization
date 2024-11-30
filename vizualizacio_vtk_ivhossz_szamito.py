import numpy as np
import pyvista as pv

# A görbét tartalmazó VTK fájl betöltése
line = pv.read("custom_curve.vtk")
points = line.points  # A görbe pontjainak kinyerése a fájlból

# Az ívhossz kiszámítása: összeadjuk a két egymást követő pont közötti távolságokat
length = 0
for i in range(
    len(points) - 1
):  # Végigiterálunk a pontokon, kivéve az utolsó előtti pontot
    p1 = points[i]  # Az i-edik pont
    p2 = points[i + 1]  # A következő pont
    length += np.linalg.norm(
        p2 - p1
    )  # A két pont közötti távolság kiszámítása és hozzáadása az összhozhoz

# Az összesített ívhossz kiírása
print("Total curve length:", length)
