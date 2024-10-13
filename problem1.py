import matplotlib.pyplot as plt


labels = ['Kisumu', 'Nakuru', 'Mombasa']
sizes = [35, 30, 35]  
colors = ['#1f77b4', '#2ca02c', '#ff7f0e']  


plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Values')
plt.axis('equal')  


plt.show()
