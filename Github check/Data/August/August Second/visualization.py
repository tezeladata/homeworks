import numpy as np
import matplotlib.pyplot as plt

data = [('გურგენიძე', 98.37398374, 307.5), ('ზაბახიძე', 94.08695652, 287.5),('ისაკაძე', 98.88888889, 180), ('ძინძიბაძე', 98.28571429, 175), ('მელიქჯანიანი', 97.07317073, 102.5), ('მოწონელიძე', 95.45454545, 165), ('გუჯაბიძე', 94.76923077, 162.5),('ვანიშვილი', 92.38095238, 315), ('გიორგელაშვილი', 91.56862745, 255),('მოთიაშვილი', 91.48387097, 387.5), ('სამსონიძე', 88.52459016, 305), ('აბაშიძე', 86.05042017, 297.5), ('აბრამიანი', 85.29411765, 340),('ხმალაძე', 100, 7.5), ('ჭიტაძე', 100, 50),('ყვავაძე', 92.47058824, 212.5), ('ფოფხაძე', 91.75257732, 242.5), ('შავაძე', 91.70212766, 235), ('ნუკრაძე', 88.57142857, 140),('ქიმერიძე', 90.66666667, 75),('შუბითიძე', 82.47619048, 262.5), ('პაპუნაშვილი', 77.00598802, 417.5), ('გრძელიშვილი', 73.79746835, 790), ('ნარიმანიძე', 71.84, 312.5), ('ვახტანგაშვილი', 69.19642857, 560),('კილასონია', 84.35897436, 195), ('ხუსკივაძე', 80.83333333, 180), ('აკოფიანი', 62.55319149, 117.5), ('დოლიძე', 59.11111111, 225), ('ფილიშვილი', 45.33333333, 112.5), ('ნავროზაშვილი', 42.90322581, 155),('სვანიძე', 85, 80), ('ბექაური', 79.31034483, 72.5), ('ვარადაშვილი', 77.2972973, 92.5), ('ჯალაღონია', 72.30769231, 65), ('წითლაური', 67.33333333, 75), ('გვრიტიშვილი', 66.06060606, 82.5), ('ვარაზაშვილი', 62.66666667, 75), ('თირქია', 58.0952381, 52.5), ('კვარაცხელია', 50.52631579, 95)]

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