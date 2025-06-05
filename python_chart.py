import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
values = [12, 19, 3, 5, 2, 3]

plt.figure(figsize=(6, 4))
plt.bar(months, values, color='skyblue')
plt.title('Sales')
plt.xlabel('Month')
plt.ylabel('Value')
plt.tight_layout()
plt.savefig('sales_chart.png')
print("Chart saved to sales_chart.png")
