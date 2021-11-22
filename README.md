# dockercompose-to-MACM
Con questo progetto è possibile trasformare qualsiasi docker compose in un oggetto MACM. <br>
Ciò viene effettuato tramite il parser <b>generator_cypher.py</b> con il supporto della libreria appositamente creata <b>macm.py</b>. La libreria macm creata fa riferimento a sua volta alla libreria opensource networkx.py e all'interfaccia grafica <b>gui.py</b> appositamente creata. L'oggetto MACM è possibile ottenerlo eseguendo il parser e riempiendo i campi definiti nell'interfaccia grafica. A partire dall'oggetto creato è possibile effettuare la query che definisce tale oggetto su Neo4j che permetterà di implementare e di visualizzare graficamente il MACM ottenuto.
