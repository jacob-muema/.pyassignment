import matplotlib.pyplot as plt


car_brands = ['BMW', 'AUDI', 'MERCEDES', 'JAGUAR', 'TESLA', 'FORD']
brand_distribution = [20, 15, 25, 10, 18, 12]


departments = ['SSET', 'Education', 'Health sci', 'Business', 'Law']
data = [25, 18, 35, 12, 28]


fig, axs = plt.subplots(2, 1, figsize=(8, 12))


axs[0].pie(brand_distribution, labels=car_brands, autopct='%1.1f%%', startangle=140)
axs[0].set_title('Car Brand Distribution')


axs[1].bar(departments, data, color='blue')
axs[1].set_xlabel('Departments')
axs[1].set_ylabel('Number of Students')
axs[1].set_title('Number of Students per Department')


plt.tight_layout()

plt.show()
