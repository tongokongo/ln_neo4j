

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
        #print(len(nodes_list))
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
                "lastUpdate": edge.last_update if edge.last_update else None,
                "node1Pub": edge.node1_pub if edge.node1_pub else None,
                "node2Pub": edge.node2_pub if edge.node2_pub else None,
                "capacity": edge.capacity if edge.capacity else None
                # nodeXPolicy keys "time_lock_delta", "min_htlc", "fee_rate_milli_msat", "max_htlc_msat", optional "disabled" bool
            }
            if edge.node1_policy:
                node1= edge.node1_policy
                node1policy = {
                    "timeLockDelta1": node1.time_lock_delta if node1.time_lock_delta else None,
                    "minHtlc1": node1.min_htlc if node1.min_htlc else None,
                    "feeBaseMsat1": node1.fee_base_msat if node1.fee_base_msat else None,
                    "feeRateMilliMsat1": node1.fee_rate_milli_msat if node1.fee_rate_milli_msat else None,
                    "maxHtlcMsat1": node1.max_htlc_msat if node1.max_htlc_msat else None
                }
                d = {**d, **node1policy}

            if edge.node2_policy:
                node2= edge.node2_policy
                node2policy = {
                    "timeLockDelta2": node2.time_lock_delta if node2.time_lock_delta else None,
                    "minHtlc2": node2.min_htlc if node2.min_htlc else None,
                    "feeBaseMsat2": node2.fee_base_msat if node2.fee_base_msat else None,
                    "feeRateMilliMsat2": node2.fee_rate_milli_msat if node2.fee_rate_milli_msat else None,
                    "maxHtlcMsat2": node2.max_htlc_msat if node2.max_htlc_msat else None
                }
                d = {**d, **node2policy}

            edges_list.append(d)

        #print(len(edges_list))
        return edges_list