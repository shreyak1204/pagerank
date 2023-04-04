#page rank
import networkx as nx
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import operater
import random as rd 
graph=nx.gnp_random_graph(25,0,6,directed=true)
nx.drwa(graph,with_labels=true,font_color="pink",font_size=10,node_color="yellow")
plt.show()
count=graph.number_of_nodes()
print(list(graph.neighbors(1)))