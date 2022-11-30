import matplotlib.pyplot as plt 

dpi = plt.rcParams['figure.dpi']
canvas = plt.figure(figsize=(960/dpi, 540/dpi))

with open("DS8.txt", "r") as file:
    for i in file:
        if i == "":
            break

        dot = i.split()
        plt.plot(int(dot[1]), int(dot[0]), ".r")

plt.savefig("Mandryko_8.png")
plt.close()