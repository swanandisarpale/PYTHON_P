import matplotlib.pyplot as plt
subject=["m","s","c","h","b"]
marks=[40,50,30,20,47]

plt.bar(subject,marks)

plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("marks of std")
plt.show()