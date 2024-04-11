import matplotlib.pyplot as plt

ttt_tabu_padrao_data = []
file = open("ts_padrao_final.txt", "r")
while(True):
    line = file.readline().strip()
    if(not line):
        break
    line_list = line.split()
    if(line_list[0] == "Iteration"):
        ttt_tabu_padrao_data.append([])
    else:
        line_list = [int(x) for x in line_list]
        ttt_tabu_padrao_data[-1].append(line_list)

x_points = []
y_points = []

for i in range(len(ttt_tabu_padrao_data)):
    if(ttt_tabu_padrao_data[i][-1][0] == -1):
        ttt_tabu_padrao_data[i].pop()
    
    if(ttt_tabu_padrao_data[i][-1][1] < 1000):
        continue
    else:
        x_points.append(i)
        y_points.append(ttt_tabu_padrao_data[i][-1][0]) # append no tempo de execução da ultima iteração

y_points.sort()

plt.plot(x_points, y_points)
plt.show()



    
    
