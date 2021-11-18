import yaml
import os
from config import *
from macm import *


node_container = []
node_networks = []
edge_uses = []
edge_connects = []
edge_connects_default_networks = []
edge_hosts = []

container_name = []

networks = []
networks_connects = []

depends_on = []

ports = []
ports_container = []



script_dir = os.path.dirname(__file__)
dockercompose=dockercompose_name+".yml"
abs_file_path = os.path.join(script_dir, dockercompose)
fp=open(abs_file_path,"r")
fp2=fp.read()



#converto yml in dizionario:
docker_composeObj=(yaml.safe_load(fp2))



#ottengo i container name
for key,value in docker_composeObj['services'].items():
	container_name.append(key)



#NETWORKS: ottengo le networks associate ai singoli container per le relazioni di uses	
ind=0
for x in container_name:
	for key,value in docker_composeObj['services'][x].items():
		#definiamo l'if siccome networks può non essere presente nel docker compose
		if(key=='networks'):
			ind+=1
			networks_connects.append(docker_composeObj['services'][x]['networks'])
if ind==0:
	print("Non è presente alcuna 'networks' nel docker compose\n")



#NETWORKS: ottengo le networks(uno per tipo non replicato) per la creazione di nodi networks(se presenti)
if(len(networks_connects)!=0):
	for key in docker_composeObj['networks'].keys():
		networks.append(key)
	
	
	
#DEPENDS_ON: ottengo le depends_on associate ai singoli container per le relazioni di connects
ind=0
for x in container_name:
	for key,value in docker_composeObj['services'][x].items():
		#definiamo l'if siccome depends_on può non essere presente nel docker compose
		if(key=='depends_on'):
			ind+=1
			depends_on.append(docker_composeObj['services'][x]['depends_on'])
if ind==0:
	print("Non è presente nessuna 'depends_on' nel docker compose\n")	



#ottieni ports container e associa asset type
ind00=0
net00 = []
properties0 = []
for x in container_name:
	properties0.append(list(docker_composeObj['services'][x].keys()))

for j in range(0,len(container_name),1):
	ind00=0	
	for i in range(0,len(properties0[j]),1):
		if(properties0[j][i]=='ports'):
			net00.insert(j,1)
		if(properties0[j][i]!='ports'):
			ind00+=1
		if(ind00==len(properties0[j])):
			net00.insert(j,0)

ind01=0
for x in container_name:
	for key,value in docker_composeObj['services'][x].items():
		#definiamo l'if siccome depends_on può non essere presente nel docker compose
		if(key=='ports'):
			ind01+=1
			ports.append(docker_composeObj['services'][x]['ports'])
if(ind01==0):
	print("Non è presente alcun 'ports' nel docker compose")

if(ind01!=0): #mi assicuro che esistano ports
	net3 = [] #verifico quanto numeri di porti associati ai container ci sono
	temp = ""
	for j in range(0,len(ports),1):	
		net3.insert(j,len(ports[j]))
		for k in range(0,len(ports[j]),1):
			flag=0
			for i in range(0,len(ports[j][k]),1):
				a=1
				if(flag==1):
					temp=temp+ports[j][k][i]
				if(ports[j][k][i]==':'):
					flag=1

			ports_container.append(temp)
			temp = ""

for j in range(0,len(net00),1):
	#nei container che non è presente la chiave ports inserire '?' per trasferirlo poi all'asset type
	if(net00[j]==0):
		ports_container.insert(j,'?')
	
if(ind01!=0):	
	#definisco gli asset_type secondo i porti noti
	asset_type = []
	for x in range(0,len(container_name),1):
		flag2=0
		for y in range(0,net00[x],1):
			if(ports_container[x]=='20' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='21' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='22' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='23' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='25' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='53' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='67' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='68' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='69' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='80' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='88' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='104' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='110' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='113' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='119' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='123' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='143' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='443' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='465' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='563' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='587' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='591' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='636' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='993' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='995' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='1883' and flag2==0):
				asset_type.append('Service.MQTTBroker?')
				flag2=1
			if(ports_container[x]=='1433' and flag2==0):
				asset_type.append('Service.DB?')
				flag2=1
			if(ports_container[x]=='1434' and flag2==0):
				asset_type.append('Service.DB?')
				flag2=1
			if(ports_container[x]=='3050' and flag2==0):
				asset_type.append('Service.DB?')
				flag2=1
			if(ports_container[x]=='3128' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='3306' and flag2==0):
				asset_type.append('Service.DB?')
				flag2=1
			if(ports_container[x]=='3389' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='4662' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='4672' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='4711' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='5000' and flag2==0):
				asset_type.append('Service.DB?')
				flag2=1
			if(ports_container[x]=='5222' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='5269' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='5432' and flag2==0):
				asset_type.append('Service.DB?')
				flag2=1
			if(ports_container[x]=='8080' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='8118' and flag2==0):
				asset_type.append('Service.Web?')
				flag2=1
			if(ports_container[x]=='8883' and flag2==0):
				asset_type.append('Service.MQTTBroker?')
				flag2=1
				
		if(flag2==0):
			asset_type.append('?')




#creo nodo VM che fa da host per tutti i container
VM=Node("IaaS:service","VM1","VM",app_id,application_name)
VM.addnode()


#se c'è qualche container privo di networks creo nodo default-network
if(len(networks_connects) != len(container_name)):
	default_network=Node("network","default-network","?",app_id,application_name)
	default_network.addnode()


#creato i nodi container
ind=0
for x in container_name:
	node_container.append(Node("service",x,asset_type[ind],app_id,application_name))
	node_container[ind].addnode()
	ind+=1   



#per pulizia di codice in output:
file_cypher.write("\n")



#creo i nodi networks(se presenti)
if(len(networks_connects)!=0):
	ind=0
	for x in networks:
		node_networks.append(Node("network",x,"?",app_id,application_name))
		node_networks[ind].addnode()
		ind+=1  



#per pulizia di codice in output:
file_cypher.write("\n")



#creo gli archi uses se le depends_on sono presenti nel docker compose
if(len(depends_on)!=0):
	ind=0
	count=0
	count_edge=0
	for x in container_name:
		for key in docker_composeObj['services'][x].keys():
			#definiamo l'if siccome depends_on non è presente in tutti i container
			
			if(key=='depends_on'):
				#itero nella lista di liste
				for i in range(0,len(depends_on[ind]),1):
					
					#di seguito vado ad ottenere il to_node(nodo destinazione in cui punta l'arco) a partire dal nome del container del nodo destinazione
					ind2=0
					to_node = None
					while to_node == None:
						to_node=getnode_fromname(node_container[ind2],depends_on[ind][i])
						ind2+=1
					
					#il nodo da cui parte l'arco è sempre corretto grazie all'if che abbiamo inserito	
					edge_uses.append(Edge(node_container[count],to_node,"uses"))
					edge_uses[count_edge].addedge(0)
					count_edge+=1
					
				ind+=1
		count+=1		



#per pulizia di codice in output:
file_cypher.write("\n")



#creo gli archi connects per connettere alla default-network quando il container non ha una network associata
properties = []
ind=0
net = []
for x in container_name:
	properties.append(list(docker_composeObj['services'][x].keys()))

	
for j in range(0,len(container_name),1):
	ind=0	
	for i in range(0,len(properties[j]),1):
		if(properties[j][i]=='networks'):
			net.insert(j,1)
		if(properties[j][i]!='networks'):
			ind+=1
		if(ind==len(properties[j])):
			net.insert(j,0)

count=0	
for j in range(0,len(net),1):
	if(net[j]==0):
		edge_connects_default_networks.append(Edge(node_container[j],default_network,"connects"))
		edge_connects_default_networks[count].addedge(0)
		count+=1


#per pulizia di codice in output:
file_cypher.write("\n")



#creo gli archi connects se le networks sono presenti nel docker compose
#il valore q lo utilizziamo per non inserire la virgola nell'ultima connect
if(len(networks_connects)!=0):
	ind=0
	count=0
	count_edge=0
	for x in container_name:
		for key in docker_composeObj['services'][x].keys():
			if(key=='networks'):
				#q=len(container_name)-1
				for i in range(0,len(networks_connects[ind]),1):
					ind2=0
					to_node = None
					while to_node == None:
						to_node=getnode_fromname(node_networks[ind2],networks_connects[ind][i])
						ind2+=1
					
					#il nodo da cui parte l'arco è corretto grazie all'if che abbiamo inserito	
					edge_connects.append(Edge(node_container[count],to_node,"connects"))
					edge_connects[count_edge].addedge(0)
					count_edge+=1
				ind+=1
		count+=1		



#per pulizia di codice in output:
file_cypher.write("\n")



#creo gli archi hosts da VM per tutti i container
count_edge=0
ind=0
q=len(container_name)-1	
for i in range(0,len(container_name),1):
	ind2=0
	to_node = None
	while to_node == None:
		to_node=getnode_fromname(node_container[ind2],container_name[i])
		ind2+=1
	
	edge_hosts.append(Edge(VM,to_node,"hosts"))
	
	#l'if seguente viene utilizzato per alzare l'end:flag (e quindi in sostanza non inserire la virgola nella parte finale della query)
	if ind!=q:
		edge_hosts[count_edge].addedge(0)
		count_edge+=1
	if ind==q:	
		edge_hosts[count_edge].addedge(1)
		count_edge+=1
	
	ind+=1
	
	
	
print("\n")



#segnalo in output quali container non presentano le depends_on (nel caso in cui le presentano tutte non ha alcun effetto)
ind=0
net2 = []
for x in container_name:
	properties.append(list(docker_composeObj['services'][x].keys()))

	
for j in range(0,len(container_name),1):
	ind=0	
	for i in range(0,len(properties[j]),1):
		if(properties[j][i]=='depends_on'):
			net2.insert(j,1)
		if(properties[j][i]!='depends_on'):
			ind+=1
		if(ind==len(properties[j])):
			net2.insert(j,0)

for j in range(0,len(net2),1):
	if(net2[j]==0):
		print("Il container "+container_name[j]+" non presenta depends_on")





			
#stampa dell'oggetto grafo finale
print("\nL'oggetto grafo finale è il seguente:")
print(get_graph())
