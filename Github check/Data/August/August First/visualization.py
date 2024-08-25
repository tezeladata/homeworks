import numpy as np
import matplotlib.pyplot as plt

data = [('გიორგელაშვილი', 97.4137931, 290), ('ზაბახიძე', 95.03875969, 322.5), ('ვანიშვილი', 94.44444444, 315), ('გურგენიძე', 93.49593496, 307.5), ('აბრამიანი', 92.72727273, 330),('ისაკაძე', 100, 200), ('ნუცუბიძე', 100, 117.5), ('ძინძიბაძე', 95.65217391, 230), ('მოწონელიძე', 93.01587302, 157.5),('სამსონიძე', 92, 362.5), ('მოთიაშვილი', 88.23529412, 297.5), ('ფოფხაძე', 85.5, 300),('შუბითიძე', 92.32323232, 247.5), ('გუჯაბიძე', 92, 175), ('ნუკრაძე', 88.57142857, 140), ('ფილიშვილი', 88.23529412, 127.5),('კვარაცხელია', 90.52631579, 95), ('თირქია', 90.47619048, 52.5), ('სვანიძე', 86.28571429, 87.5),('პაპუნაშვილი', 82.26190476, 420), ('აბაშიძე', 78.11965812, 292.5), ('ნარიმანიძე', 72.0610687, 327.5), ('ვახტანგაშვილი', 70, 560), ('გრძელიშვილი', 52.53164557, 790),('კილასონია', 82.79569892, 232.5), ('შავაძე', 80.97560976, 205), ('ყვავაძე', 79.54545455, 220), ('იოანე დოლიძე', 70.87719298, 142.5), ('ხუსკივაძე', 64.52830189, 132.5), ('ჯალაღონია', 49.52380952, 105), ('ნავროზაშვილი', 44.51612903, 155), ('მათე დოლიძე', 38.57142857, 210), ('აკოფიანი', 10.625, 160),('გვრიტიშვილი', 83.88888889, 90), ('ვარაზაშვილი', 66.66666667, 75), ('ბექაური', 60, 72.5), ('ვარადაშვილი', 52.43243243, 92.5), ('წითლაური', 37.94871795, 97.5)]

names = [item[0] for item in data]
coefficients = [item[1] for item in data]
salaries = [item[2] for item in data]

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(names, coefficients, color='#004225')
plt.xlabel('Work Coefficient')
plt.ylabel('Squad Leaders')
plt.title('Work Coefficient by Leader')
plt.suptitle("From best to worst")
plt.gca().invert_yaxis()
plt.grid(axis="x", lw=1)

# Font size
plt.yticks(fontsize=7)

plt.show()