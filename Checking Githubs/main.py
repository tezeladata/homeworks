def calculate_work(work_coefficient, salary, name):
    if salary > 250:
        salary_range = "high_salary"
    elif 100 < salary <= 250:
        salary_range = "mid_salary"
    else:
        salary_range = "low_salary"

    if work_coefficient > 92.5:
        efficiency_range = "high_eff"
    elif 85 < work_coefficient <= 92.5:
        efficiency_range = "mid_eff"
    else:
        efficiency_range = "low_eff"



    if salary_range == "high_salary":
        if efficiency_range == "high_eff":
            high_salary_high_eff.append((name, work_coefficient, salary))
        elif efficiency_range == "mid_eff":
            high_salary_mid_eff.append((name, work_coefficient, salary))
        else:
            high_salary_low_eff.append((name, work_coefficient, salary))
    elif salary_range == "mid_salary":
        if efficiency_range == "high_eff":
            mid_salary_high_eff.append((name, work_coefficient, salary))
        elif efficiency_range == "mid_eff":
            mid_salary_mid_eff.append((name, work_coefficient, salary))
        else:
            mid_salary_low_eff.append((name, work_coefficient, salary))
    else:  # low_salary
        if efficiency_range == "high_eff":
            low_salary_high_eff.append((name, work_coefficient, salary))
        elif efficiency_range == "mid_eff":
            low_salary_mid_eff.append((name, work_coefficient, salary))
        else:
            low_salary_low_eff.append((name, work_coefficient, salary))

    return (salary_range, efficiency_range)

high_salary_high_eff = []
mid_salary_high_eff = []
high_salary_mid_eff = []
low_salary_high_eff = []
mid_salary_mid_eff = []
low_salary_mid_eff = []
high_salary_low_eff = []
mid_salary_low_eff = []
low_salary_low_eff = []

calculate_work(100, 75, 'Nutsubidze')
calculate_work(100, 22.5, 'Qimeridze')
calculate_work(99, 355, 'Tezelashvili')
calculate_work(97.7, 497.5, 'Grdzelishvili')
calculate_work(96.1, 297.5, 'Zabakhidze')
calculate_work(95.6, 370, 'Giorgelashvili')
calculate_work(95.3, 257.5, 'Babajanashvili')
calculate_work(93.7, 312.5, 'Vanishvili')

calculate_work(90.1, 247.5, 'Tinikashvili')
calculate_work(87.7, 142.5, 'Filishvili')
calculate_work(87.6, 52.5, 'Vakhtangashvili')
calculate_work(87.3, 232.5, 'Razmadze')
calculate_work(87, 585, 'Molodini')
calculate_work(86.6, 247.5, 'Beridze')
calculate_work(86.4, 185, 'Motiashvili')
calculate_work(86.1, 302.5, 'Gagnidze')

calculate_work(83.3, 162.5, 'Tirkia')
calculate_work(82.1, 297.5, 'Diasamidze')
calculate_work(81.8, 265, 'Khoperia')
calculate_work(80.3, 152.5, 'Chxikvadze')
calculate_work(79.3, 315, 'Janezashvili')
calculate_work(77.7, 202.5, 'Tarieladze')
calculate_work(77.5, 302.5, 'Ekseulidze')
calculate_work(46.6, 7.5, 'Tkeshelashvili')

calculate_work(31.3, 75, 'Amonashvili')
calculate_work(95.3, 182.5, 'Navrozashvili')
calculate_work(92.1, 300, 'Sazandrishvili')
calculate_work(73.8, 177.5, 'Leverashvili')
calculate_work(90.6, 90.6, 'Janashia')

high_salary_high_eff.sort(key=lambda x: x[1], reverse=True)
mid_salary_high_eff.sort(key=lambda x: x[1], reverse=True)
high_salary_mid_eff.sort(key=lambda x: x[1], reverse=True)
low_salary_high_eff.sort(key=lambda x: x[1], reverse=True)
mid_salary_mid_eff.sort(key=lambda x: x[1], reverse=True)
low_salary_mid_eff.sort(key=lambda x: x[1], reverse=True)
high_salary_low_eff.sort(key=lambda x: x[1], reverse=True)
mid_salary_low_eff.sort(key=lambda x: x[1], reverse=True)
low_salary_low_eff.sort(key=lambda x: x[1], reverse=True)

print([
    high_salary_high_eff,
    mid_salary_high_eff,
    high_salary_mid_eff,
    low_salary_high_eff,
    mid_salary_mid_eff,
    low_salary_mid_eff,
    high_salary_low_eff,
    mid_salary_low_eff,
    low_salary_low_eff
])