from scapy.all import rdpcap

def load_pcap(pcap_path):
    """
    Load a PCAP file and return list of packets.
    """
    packets = rdpcap(pcap_path)
    return packets
