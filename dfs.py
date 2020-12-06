def load_graph():
        Graph = {}
        fin=open("graph.txt","r")
        lines=fin.readlines()
        is_key=True
        for x in lines:
            x=x.strip()
            if is_key:
                key=x
                is_key=False
                Graph[key]=[]
            else:
                if(x=="-1"):
                    is_key=True
                else:
                    Graph[key].append(x)
        return Graph

Graph = load_graph()
level1 = Graph['robot']
for i in Graph['robot']:
    print(i,Graph[i])
    
