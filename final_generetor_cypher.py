#nelle liste without abbiamo i valori con i caratteri non supportati da cypher eliminati
import yaml
import re #per eliminare caratteri non supportati nella query cypher
print("Insert Application name:")
application_name=input()

print("Insert app_id:")
app_id=input()

container_name = []
container_name_without = []

networks = []
networks_without = []
networks_connects = []

depends_on = []

fp=open("C:/Users/lucad/Desktop/ingegneria/Tesi Rak/newway/docker-compose.yml","r")
fp2=fp.read()

#converto yml in dizionario:
docker_composeObj=(yaml.safe_load(fp2))

#ottengo i container name
for key,value in docker_composeObj['services'].items():
	container_name.append(key)
	container_name_without.append(re.sub('[- ]','',key))

#ottengo le networks del docker-compose
for key in docker_composeObj['networks'].keys():
	networks.append(key)
	networks_without.append(re.sub('[- ]','',key))

#ottengo le networks associate ai singoli container	
for x in container_name:
	for key in docker_composeObj['services'][x]['networks']:
		networks_connects.append(key)

#ottengo le depends_on associate ai singoli container
for x in container_name:
	#ind=0
	#for key,value in docker_composeObj['services'][x]['depends_on']:
	for key,value in docker_composeObj['services'][x].items():
		#definiamo l'if siccome depends_on non è presente in tutti i container
		if(key=='depends_on'):
			depends_on.append(docker_composeObj['services'][x]['depends_on'])
	

file_cypher=open("C:/Users/lucad/Desktop/ingegneria/Tesi Rak/newway/cypher.txt","w")
file_cypher.write("CREATE\n")



#create node
ind=0
for x in container_name:
    file_cypher.write("\t("+container_name_without[ind]+":service {name:'"+x+"', type:'TDB', app_id:'"+app_id+"', application:'"+application_name+"'}),\n")
    ind+=1   

ind=0
for x in networks:
    file_cypher.write("\t("+networks_without[ind]+":service {name:'"+x+"', type:'TDB', app_id:'"+app_id+"', application:'"+application_name+"'}),\n")
    ind+=1  

file_cypher.write("\n")

#create uses
ind=0
for x in container_name:
	for key in docker_composeObj['services'][x].keys():
		#definiamo l'if siccome depends_on non è presente in tutti i container
		if(key=='depends_on'):
			#itero nella lista di liste
			for i in range(0,len(depends_on[ind]),1):
				file_cypher.write("\t("+re.sub('[- ]','',x)+")-[:uses]->("+re.sub('[- ]','',depends_on[ind][i])+"),\n")
			ind+=1

file_cypher.write("\n")
		
#create connects
#il valore q lo utilizziamo per non inserire la virgola nell'ultima connect
ind=0
for x in container_name_without:
	q=len(container_name_without)-1
	if ind!=q:
		file_cypher.write("\t("+x+")-[:connects]->("+networks_connects[ind]+"),\n")
	if ind==q:
		file_cypher.write("\t("+x+")-[:connects]->("+networks_connects[ind]+")\n")
	ind+=1
