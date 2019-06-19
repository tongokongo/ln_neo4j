from neo4j import GraphDatabase, basic_auth

class Neo4J:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), max_retry_time=1)

    def close(self):
        self._driver.close()

    def saveSingleNode(self, node):
        with self._driver.session() as session:
            with session.begin_transaction() as tx:
                #TODO: ramake to UNWIND statement
                tx.run('''  MERGE (n:LnNode {pubkey: $dict.pubKey}) 
                            SET n.alias=$dict.alias, n.lastUpdate=$dict.lastUpdate, n.color=$dict.color, 
                            n.network=$dict.network, n.addr=$dict.addr ''',
                       dict = node)

                #print("Node saved")

    def saveSingleChannel(self, edge):
        with self._driver.session() as session:
            with session.begin_transaction() as tx:
                #TODO: remake to UNWIND statement
                tx.run('''  MERGE (n1:LnNode {pubkey: $dict.node1Pub}) 
                            MERGE (n2:LnNode {pubkey: $dict.node2Pub})
                            MERGE (e:LnChan {point: $dict.chanPoint})
                            MERGE (n1)-[r1:LnNode1Policy]->(e)
                            MERGE (e)-[r2:LnNode2Policy]->(n2)
                            SET e.id=$dict.chanID, e.capacity=$dict.capacity, e.lastUpdate=$dict.lastUpdate,\
                             r1.timeLockDelta=$dict.timeLockDelta1, r1.minHtlc=$dict.minHtlc1,
                             r1.feeBaseMsat=$dict.feeBaseMsat1, r1.feeRateMilliMsat=$dict.feeRateMilliMsat1,
                             r1.maxHtlcMsat=$dict.maxHtlcMsat1, r2.maxHtlcMsat=$dict.maxHtlcMsat2,
                             r2.timeLockDelta=$dict.timeLockDelta2, r2.minHtlc=$dict.minHtlc2,
                             r2.feeBaseMsat=$dict.feeBaseMsat2, r2.feeRateMilliMsat=$dict.feeRateMilliMsat2 ''',
                       dict = edge)

                #print("Edge saved")

    def deleteAll(self):
        with self._driver.session() as session:
            with session.begin_transaction() as tx:
                tx.run('''  MATCH (n) 
                            DETACH DELETE n ''')

                print("All nodes and relations deleted")