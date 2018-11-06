import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, s=10, edgecolors='none', c='red')
plt.xlabel("XValue", fontsize=14)
plt.ylabel("YValue", fontsize=14)
plt.title("Square Number", fontsize=25)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig("scatter_gif", bbox_inches='tight')