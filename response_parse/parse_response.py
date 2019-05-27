

class response_parser():
    def __init__(self, response):
        self.response = response
        self.nodes = response.nodes
        self.edges = response.edges


    #nodes parser takes all the nodes objects and parses it into list of dicts
    def parseNodes(self):
        nodes_list = []
        for node in self.nodes:
            dic = {}

            d = {
                "pubKey": node.pub_key,
                "lastUpdate" : node.last_update if node.last_update else None,
                "alias" : node.alias if node.alias else None,
                "color" : node.color if node.color else None
                #addresses keys "network, "addr"
                }
            if node.addresses:
                network = []
                addr = []
                for pair in node.addresses:
                    if pair.network: network.append(pair.network)
                    if pair.addr: addr.append(pair.addr)

                addresses = {
                    "network": network if len(network)>0 else None,
                    "addr": addr if len(addr)>0 else None
                }
                d = {**d, **addresses}

            nodes_list.append(d)
        print(len(nodes_list))
        return nodes_list

    '''channel_id: 635198862672003073
    chan_point: "f1bcc3df0ddf3a49f1e58c6b17935e4d8f1fe806055e5870a19719889216c5c0:1"
    last_update: 1558788122
    node1_pub: "02a04446caa81636d60d63b066f2814cbd3a6b5c258e3172cbdded7a16e2cfff4c"
    node2_pub: "036a33e92cda2679ac91ac0467acb1ba33396c0df1119521653e0f269c275dd6bf"
    capacity: 4000000
    node1_policy {
      time_lock_delta: 29
      min_htlc: 1000
      fee_rate_milli_msat: 1
      max_htlc_msat: 3960000000
    }
    node2_policy {
      time_lock_delta: 40
      min_htlc: 1000
      fee_base_msat: 1000
      fee_rate_milli_msat: 1
      max_htlc_msat: 3960000000
    }'''
    def parseEdges(self):
        edges_list = []
        for edge in self.edges:
            #print(edge)
            d = {
                "chanID": edge.channel_id,
                "chanPoint": edge.chan_point if edge.chan_point else None,
                "lastUdate": edge.last_update if edge.last_update else None,
                "node1Pub": edge.node1_pub if edge.node1_pub else None,
                "node2Pub": edge.node2_pub if edge.node2_pub else None,
                "capacity": edge.capacity if edge.capacity else None,
                "node1Policy": edge.node1_policy if edge.node1_policy else None,
                "node2Policy": edge.node2_policy if edge.node2_policy else None
                # nodeXPolicy keys "time_lock_delta", "min_htlc", "fee_rate_milli_msat", "max_htlc_msat", optional "disabled" bool
            }
            edges_list.append(d)
        print(len(edges_list))
        return edges_list