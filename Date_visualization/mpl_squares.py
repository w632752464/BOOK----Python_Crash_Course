import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

plt.title("Line",fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
