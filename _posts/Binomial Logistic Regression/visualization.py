x = np.arange(0,10,.1)
y = model.weight.item()*x + model.bias.item()

plt.plot(x, 1/(1 + np.exp(-y)), color="green")

plt.xlim(0,10)
plt.scatter(blue_x, blue_y, color="blue")
plt.scatter(red_x, red_y, color="red")

plt.show()