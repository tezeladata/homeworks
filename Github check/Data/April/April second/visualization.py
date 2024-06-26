import numpy as np
import matplotlib.pyplot as plt

data = [
    ('თეზელაშვილი', 99.33884298, 302.5), ('გრძელიშვილი', 99.05405405, 370), ('მოთიაშვილი', 95.96330275, 272.5), ('ზაბახიძე', 93.39622642, 265), ('ბაბაჯანაშვილი', 97.77777778, 180), ('საზანდრიშვილი', 97.10843373, 207.5), ('ფოფხაძე', 96.20253165, 197.5), ('ჯანაშია', 96.09756098, 205), ('დიასამიძე', 94.83870968, 155), ('ნუცუბიძე', 93.63636364, 110), ('თირქია', 93.33333333, 112.5), ('ვახტანგაშვილი', 92.7027027, 185), ('ვანიშვილი', 92.30769231, 292.5), ('გიორგელაშვილი', 91.29251701, 367.5), ('ჯანეზაშვილი', 87.3015873, 315), ('გურგენიძე', 100, 85), ('შავაძე', 100, 30), ('სიხარულიძე', 100, 7.5), ('მოწონელიძე', 100, 7.5), ('ხუსკივაძე', 100, 37.5), ('სვანიძე', 100, 37.5), ('ბერკაცაშვილი', 96.96969697, 82.5), ('ქიმერიძე', 96.19047619, 52.5), ('მოლოდინი', 95.55555556, 90), ('რაზმაძე', 91.89189189, 185), ('ნავროზაშვილი', 87.04225352, 177.5), ('გაგნიძე', 77.17647059, 212.5), ('ბერიძე', 75.40540541, 185), ('ფილიშვილი', 73.33333333, 142.5), ('თინიკაშვილი', 69.75609756, 102.5), ('ლევერაშვილი', 84.44444444, 45), ('დოლიძე', 80, 15), ('ტყეშელაშვილი', 73.33333333, 7.5), ('არღუთაშვილი', 70.90909091, 27.5), ('ამონაშვილი', 58.66666667, 75), ('თაქთაქიძე', 52.38095238, 52.5)   
]

# Extracting individual lists from the data
names = [item[0] for item in data]
coefficients = [item[1] for item in data]
salaries = [item[2] for item in data]

# Plotting
plt.figure(figsize=(12, 8))
plt.barh(names, coefficients, color='#634234')
plt.xlabel('Work Coefficient')
plt.ylabel('Squad Leaders')
plt.title('Work Coefficient by Leader')
plt.suptitle("From best to worst")
plt.gca().invert_yaxis()
plt.grid(axis="x", lw=1)
plt.show()