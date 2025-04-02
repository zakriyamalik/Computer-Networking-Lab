import ns.applications as apps
import ns.core as core
import ns.internet as internet
import ns.network as network
import ns.point_to_point as p2p

#this part creates nodes
nodes = network.NodeContainer()
nodes.Create(2)  # creating nodes n0 and n1

pointToPoint = p2p.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate", core.StringValue("5Mbps"))
pointToPoint.SetChannelAttribute("Delay", core.StringValue("2ms"))

devices = pointToPoint.Install(nodes.Get(0), nodes.Get(1))

internet_stack = internet.InternetStackHelper()
internet_stack.Install(nodes)

# Assigning IP Addresses
address = internet.Ipv4AddressHelper()
address.SetBase("10.1.1.0", "255.255.255.0")
interfaces = address.Assign(devices)

port = 9  # port num

# UDP Sink/Receiver at node1
udp_sink = apps.PacketSinkHelper("ns3::UdpSocketFactory",
                                 network.InetSocketAddress(network.Ipv4Address.GetAny(), port))
sinkApp = udp_sink.Install(nodes.Get(1))
sinkApp.Start(core.Seconds(0.0))
sinkApp.Stop(core.Seconds(10.0))

# UDP Client/Sender at node0
udp_client = apps.OnOffHelper("ns3::UdpSocketFactory",
                              network.InetSocketAddress(interfaces.GetAddress(1), port))
udp_client.SetAttribute("OnTime", core.StringValue("ns3::ConstantRandomVariable[Constant=1]"))
udp_client.SetAttribute("OffTime", core.StringValue("ns3::ConstantRandomVariable[Constant=0]"))
udp_client.SetAttribute("DataRate", core.StringValue("1Mbps"))
udp_client.SetAttribute("PacketSize", core.UintegerValue(1024))

clientApp = udp_client.Install(nodes.Get(0))
clientApp.Start(core.Seconds(1.0))
clientApp.Stop(core.Seconds(9.0))

# packet capture
pointToPoint.EnablePcapAll("file")

core.Simulator.Run()
core.Simulator.Destroy()