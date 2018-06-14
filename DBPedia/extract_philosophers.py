from SPARQLWrapper import SPARQLWrapper, JSON
import networkx as nx
import matplotlib.pyplot as plt
import operator




sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT *
    WHERE {
    ?p a
    <http://dbpedia.org/ontology/Philosopher> .
    ?p <http://dbpedia.org/ontology/influenced> ?influenced.
    } 
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()


G = nx.DiGraph()

for result in results["results"]["bindings"]:
    try:
        filosofo = result["p"]["value"].split("/resource/")[1]
        influenzato = result["influenced"]["value"].split("/resource/")[1]
        
        #print(result["p"]["value"])
        #print(result["influenced"]["value"])
        #print("_____________________________________")
    
        #print("(" + filosofo + "," + influenzato + ")")
        G.add_edge(influenzato, filosofo)


    except:
        print("",end="")

'''
val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values)
plt.show()
'''

pr = nx.pagerank(G, alpha=0.85)
sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))
sorted_pr.reverse()


for i in sorted_pr:
    #print(i + " " + str(pr.get(i)))
    print(i)
