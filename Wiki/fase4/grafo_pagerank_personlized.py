from SPARQLWrapper import SPARQLWrapper, JSON
import networkx as nx
import matplotlib.pyplot as plt
import operator


f = open("modifiche_a_mano.txt","r")



G = nx.DiGraph()




for line in f:

    
    l = line.split(",")
    influenzato = l[0].split("\n")[0]
    filosofo = l[1].split("\n")[0]
    
           
    
    
    #print(result["p"]["value"])
    #print(result["influenced"]["value"])
    #print("_____________________________________")
    
    #print("(" + filosofo + "," + influenzato + ")")
    G.add_edge(influenzato, filosofo)

'''
val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values)
plt.show()
'''

pr = nx.pagerank(G, alpha=0.85,personalization={"Anaxagoras":10, "Anaximander":10, "Democritus":10, "Gorgias":10, "Heraclitus":10, "Leucippus":10, "Parmenides":10, "Protagoras":10, "Pythagoras":10, "Thales":10, "Zeno of Elea":10} )
sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))
sorted_pr.reverse()


for i in sorted_pr:
    #print(i + " " + str(pr.get(i)))
    print(i)
