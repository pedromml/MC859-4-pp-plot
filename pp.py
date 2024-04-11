import matplotlib.pyplot as plt

file = open("pp-data.txt", 'r')
pp_data = {}
for _ in range(6):
  execution = file.readline().strip()
  if(not execution): break
  pp_data[execution] = []
  for _ in range(7):
    line = file.readline().strip().split()
    if(not line): break
    line = [int(x) for x in line]
    pp_data[execution].append(line[1])

config_target = [-1, -1, -1, -1, -1 , -1, -1]
for config in pp_data:
  for j in range(7):
    if(config_target[j] < pp_data[config][j]):
      config_target[j] = pp_data[config][j]

pp_tau = {}
for config in pp_data:
  pp_tau[config] = [-1, -1, -1, -1, -1 , -1, -1]
  for i in range(7):
    pp_tau[config][i] = config_target[i] / pp_data[config][i] 
  pp_tau[config].sort()

pp_prob = {}
for config in pp_data:
  pp_prob[config] = [[],[]]
  pp_prob[config][0] = list(dict.fromkeys(pp_tau[config]))
  pp_prob[config][1] = [0 for x in range(len(pp_prob[config][0]))]
  for i in range(7):
    for j in range(len(pp_prob[config][0])):
      if (pp_tau[config][i] <= pp_prob[config][0][j]):
        pp_prob[config][1][j] += 1

  for k in range(len(pp_prob[config][1])):
    pp_prob[config][1][k] = pp_prob[config][1][k] / len(pp_tau[config])
   
max_tau = -1
for config in pp_tau:
  for i in range(7):
    if(pp_tau[config][i] > max_tau):
      max_tau = pp_tau[config][i]

color = ["red", "blue", "green"]
linestyle = ["-", "--"]

for i in range(len(pp_prob)):
  config = list(pp_prob.keys())[i]
  x_axis = pp_prob[config][0]
  x_axis.append(max_tau)
  y_axis = pp_prob[config][1]
  y_axis.append(y_axis[-1])
  plt.plot(pp_prob[config][0], pp_prob[config][1], drawstyle='steps-post', linestyle=linestyle[i%2], color=color[i//2],  label=config)

#plt.axis([1, max_tau, 0, 1])

plt.legend(title='Metaheurística:')
plt.title("Performance Profile")
plt.xlabel("tau")
plt.ylabel("P(tau)")
plt.show()

