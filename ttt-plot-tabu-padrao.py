import matplotlib.pyplot as plt
import numpy as np

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
    
    
    x_points.append(ttt_tabu_padrao_data[i][-1][0])
    prob = (i - 0.5)/len(ttt_tabu_padrao_data)
    y_points.append(prob) # append no tempo de execução da ultima iteração

x_points.sort()


plt.plot(x_points, y_points, "+")


plt.savefig("ttt-tabu-padrao.png")
plt.clf()
    
    
ttt_tabu_diver_restart_data = []
file = open("ts_diver_restart.txt", "r")
while(True):
    line = file.readline().strip()
    if(not line):
        break
    line_list = line.split()
    if(line_list[0] == "Iteration"):
        ttt_tabu_diver_restart_data.append([])
    else:
        line_list = [int(x) for x in line_list]
        ttt_tabu_diver_restart_data[-1].append(line_list)

x_points = []
y_points = []

for i in range(len(ttt_tabu_diver_restart_data)):
    if(ttt_tabu_diver_restart_data[i][-1][0] == -1):
        ttt_tabu_diver_restart_data[i].pop()
    
    
    x_points.append(ttt_tabu_diver_restart_data[i][-1][0])
    prob = (i - 0.5)/len(ttt_tabu_diver_restart_data)
    y_points.append(prob) # append no tempo de execução da ultima iteração

x_points.sort()


plt.plot(x_points, y_points, "+")


plt.savefig("ttt-tabu-diver-restart.png")


    
    
