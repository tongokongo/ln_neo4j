from neo4j import GraphDatabase, basic_auth

class Neo4J:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), max_retry_time=1)

    def close(self):
        self._driver.close()

    def saveSingleNode(self, node):
        with self._driver.session() as session:
            with session.begin_transaction() as tx:


                tx.run('''  MERGE (n:LnNode {pubkey: $dict.pubKey}) 
                            SET n.alias=$dict.alias, n.lastUpdate=$dict.lastUpdate, n.color=$dict.color, 
                            n.network=$dict.network, n.addr=$dict.addr ''',
                       dict = node)

                print("Node saved")