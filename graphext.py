
Graph={}
list_of_nodes = ["game controller","game"]

def id_extractor(search_string):
       #print(type(wikipedia.search(search_string)))
       query=""
       try:
           query = wikipedia.search(search_string)[0]
       except :
           return "-1","-1"

       #print(query)
       new_string = ""
       for i in query:
           if i == " ":
               new_string = new_string + '_'
           else:
               new_string = new_string + i
       print(["New string",new_string])
       print(type(new_string))
       #new_string = new_string.encode('ascii', 'ignore').decode('ascii').encode("utf-8")
       #print("After encoding",type(new_string))
       #new_string= str(new_string).encode('utf-8')
       print("Added to renamed_nodes {}".format(new_string))
       print("getting",new_string)
       res = requests.get("https://en.wikipedia.org/wiki/"+new_string)
       soup = bs(res.text, "html.parser")
       wikidata = []
       for link in soup.find_all("a"):
           url = link.get("href", "")
           if "//www.wikidata.org/" in url:
               wikidata.append(url)
               #print(url)
       #print(wikidata)
       count = 0
       wikidata_id  = ""
       for i in wikidata[0]:
           if i == 'Q' or i == '1' or i == '2' or i =='0' or i =='3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
               wikidata_id = wikidata_id + i
       res = requests.get(wikidata[0])
       soup = bs(res.text, "html.parser")
       #print(soup)
       node=""
       for hit in soup.findAll(attrs={'class' : 'wikibase-title-label'}):
           node= hit.text
       #TODO dont use unicode
       # UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
       #solve this ^^
       return wikidata_id.encode('ascii', 'ignore').decode('ascii').encode("utf-8"),node.encode('ascii', 'ignore').decode('ascii').encode("utf-8")



def load_graph():
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
def get_nodes():
        #TODO
        openfile=open("nodes.txt","r")
        t=openfile.readlines()
        for x in t:
            #print(x)
            x=x.encode("utf-8")
            x=re.sub(r"/[A-Z][A-Z][A-Z]*","",x)
            x=re.sub(r"/"," ",x)
            x=re.sub(r"\n","",x)
            list_of_nodes.append(x)
        list_of_nodes=list(dict.fromkeys(list_of_nodes))


def Graph_gen():
        load_graph()
        print(len(Graph))
        for node in list_of_nodes:
            id,new_node=id_extractor(node)
            if len(id)!=0 and id!="-1":
                renamed_nodes.append(new_node)
                save_graph("prev_graph.txt")
                if new_node not in Graph:
                    #print("Here")
                    chilldren(new_node,id,0)
                    parent(new_node,id,0)
                    #print(Graph)
                    save_graph("graph.txt")
        print("DONE")
#print(list_of_nodes)
Graph_gen()
load_graph()
for i in Graph["game"]:
        print(i)
