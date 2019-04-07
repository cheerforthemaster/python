from mininet.topo import Topo

class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        Topo.__init__(self)

        oneHost=self.addHost('h1')
        twoHost=self.addHost('h2')
        threeHost=self.addHost('h3')
        fourHost=self.addHost('h4')

        oneSwitch=self.addSwitch('s1')
        twoSwitch=self.addSwitch('s2')
        threeSwitch=self.addSwitch('s3')

        self.addLink(oneHost,oneSwitch)
        self.addLink(twoHost,twoSwitch)
        self.addLink(threeHost,threeSwitch)
        self.addLink(fourHost,threeSwitch)

        self.addLink(oneSwitch,twoSwitch)
        self.addLink(oneSwitch,threeSwitch)
        self.addLink(twoSwitch,threeSwitch)

topos={'mytopo':(lambda :MyTopo())}

