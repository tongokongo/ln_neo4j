

class response_parser():
    def __init__(self, response):
        self.response = response
        self.nodes = response.nodes
        self.edges = response.edges


    #nodes parser takes all the nodes objects and parses it into list of dicts
    def parseNodes(self):
        nodes_list = []
        for node in self.nodes:
            #print(node)
            if node.last_update:
                last_update = node.last_update
            else:
                last_update = None

            if node.alias:
                alias = node.alias
            else:
                alias = None

            if node.color:
                color = node.color
            else:
                color = None

            if node.addresses:
                if "network" in node.addresses:
                    network = node.addresses["network"]
                else:
                    network = None

                if "addr" in node.addresses:
                    addr = node.addresses["addr"]
                else:
                    addr = None
            else:
                addr = None
                network = None

            d = {
                "pubKey": node.pub_key,
                "lastUdate" : last_update,
                "alias" : alias,
                "color" : color,
                "network" : network,
                "addr" : addr
            }

            nodes_list.append(d)


        print(len(nodes_list))
        return nodes_list

    def parseEdges(self):
        edges_list = []
        for edge in self.edges:
            #print(edge)
            if edge.channel_id:
                channel_id = edge.channel_id
            else:
                channel_id = None

            if edge.chan_point:
                chan_point = edge.chan_point
            else:
                chan_point = None

            if edge.last_update:
                last_update = edge.last_update
            else:
                last_update = None

            if edge.node1_pub:
                node1_pub = edge.node1_pub
            else:
                node1_pub = None

            if edge.node2_pub:
                node2_pub = edge.node2_pub
            else:
                node2_pub = None

            if edge.capacity:
                capacity = edge.capacity
            else:
                capacity = None