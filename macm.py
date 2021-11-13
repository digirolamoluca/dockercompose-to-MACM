import networkx as nx
import re
from digraph import DiGraph

#creo grafo
macm=nx.DiGraph()


#inserire il path relativo alla posizione in cui salvare la query cypher
file_cypher=open("C:/Users/lucad/Desktop/microsernnn.macm","w")
file_cypher.write("CREATE\n")


class Node(DiGraph):
	def __init__(self, service, namee, type_node,  app_id, application_name):
		self.service=service
		self.namee=namee
		self.type_node=type_node
		self.app_id=app_id
		self.application_name=application_name
		
	def get_service(self):
		return self.service
	
	def get_name(self):
		return self.namee
	
	def get_type(self):
		return self.type_node
		
	def get_appid(self):
		return self.app_id
	
	def get_application_name(self):
		return self.application_name
	
	
	def addnode(self):
		macm.add_node(self)
		file_cypher.write("\t("+filtering(self.namee)+":"+self.service+" {name:'"+self.namee+"', type:'"+self.type_node+"', app_id:'"+self.app_id+"', application:'"+self.application_name+"'}),\n")

		

class Edge(DiGraph):
	def __init__(self, by_node , to_node, type_connect):
		self.by_node=by_node
		self.to_node=to_node
		self.type_connect=type_connect
		
	def get_bynode(self):
		return self.by_node
	
	def get_tonode(self):
		return self.to_node
	
	def get_type_connect(self):
		return self.type_connect
		
	
	def addedge(self,flag_end):
		macm.add_edge(self.by_node,self.to_node)
		if(flag_end==0):
			file_cypher.write("\t("+filtering(self.by_node.get_name())+")-[:"+self.type_connect+"]->("+filtering(self.to_node.get_name())+"),\n")
		if(flag_end==1):
			file_cypher.write("\t("+filtering(self.by_node.get_name())+")-[:"+self.type_connect+"]->("+filtering(self.to_node.get_name())+")\n")	
		


def getnode_fromname(self,namee):
	if self.get_name()==namee:
		return self		
				

def get_graph():
		return macm

		
def filtering(x):
	return re.sub('[- ]','',x)


