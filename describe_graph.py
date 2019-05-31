import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import os
import codecs
import json
from response_parse.parse_response import response_parser
from neo.neo4jobj import Neo4J


#saving nodes to the neo4j
def nodesToNeo(nodes):
    print("Parsing nodes")
    for node in nodes:
        #print(node)
        graph.saveSingleNode(node)

#saving edges to the noe4j
def edgesToNeo(edges):
    print("Parsing edges")
    count = 0
    for edge in edges:
        if count >= 0:
            #print(edge)
            print("\n\n\n")
            graph.saveSingleChannel(edge)
        count += 1


# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

# Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac
cert = open(os.path.expanduser('~/.lnd/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10009', creds, options=[('grpc.max_send_message_length', 11154485), (
    'grpc.max_receive_message_length', 11154485)])
stub = lnrpc.LightningStub(channel)

#macaroon path for linux: ~/.lnd/data/chain/bitcoin/mainnet/admin.macaroon
with open(os.path.expanduser('~/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'), 'rb') as f:
    macaroon_bytes = f.read()
    macaroon = codecs.encode(macaroon_bytes, 'hex')

#create channel graph request
request = ln.ChannelGraphRequest(
        include_unannounced=False,
    )
response = stub.DescribeGraph(request, metadata=[('macaroon', macaroon)])


#setting up neo4j connection
url = "bolt://127.0.0.1:7687"
print("Connecting...")
global graph
graph = Neo4J(url, "neo4j", "neorules")
print("Connected")


#parsing part of the script
parser = response_parser(response)
nodes = parser.parseNodes()
edges = parser.parseEdges()
print("There are " + str(len(nodes)) + " nodes and " + str(len(edges)) + " edges. \n")

nodesToNeo(nodes)
edgesToNeo(edges)


