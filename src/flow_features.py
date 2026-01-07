import pandas as pd
import math
from collections import Counter
from collections import defaultdict
from scapy.layers.inet import IP, TCP, UDP

def extract_flow_features(packets, flow_timeout=60):
    """
    Aggregate packets into flows and compute flow-level statistical features.

    Features:
    - src_ip, dst_ip, src_port, dst_port, protocol
    - num_packets
    - total_bytes
    - duration
    - avg_packet_size
    - variance_packet_size
    - entropy_packet_size
    """

    flows = defaultdict(list)

    # Group packets into flows using 5-tuple
    for pkt in packets:
        if IP in pkt:
            ip_layer = pkt[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            proto = ip_layer.proto
            src_port = pkt.sport if TCP in pkt or UDP in pkt else 0
            dst_port = pkt.dport if TCP in pkt or UDP in pkt else 0

            flow_key = (src_ip, dst_ip, src_port, dst_port, proto)
            flows[flow_key].append(pkt)

    records = []
    for key, pkts in flows.items():
        pkt_lengths = [len(p) for p in pkts]
        total_bytes = sum(pkt_lengths)
        timestamps = [p.time for p in pkts]
        duration = max(timestamps) - min(timestamps) if len(timestamps) > 1 else 0
        avg_pkt_size = total_bytes / len(pkts)
        variance = sum((l - avg_pkt_size) ** 2 for l in pkt_lengths) / len(pkt_lengths)

        # Entropy of packet sizes
        counts = Counter(pkt_lengths)
        probs = [c / len(pkt_lengths) for c in counts.values()]
        entropy = -sum(p * math.log2(p) for p in probs) if probs else 0

        records.append({
            "src_ip": key[0],
            "dst_ip": key[1],
            "src_port": key[2],
            "dst_port": key[3],
            "protocol": key[4],
            "num_packets": len(pkts),
            "total_bytes": total_bytes,
            "duration": duration,
            "avg_packet_size": avg_pkt_size,
            "variance_packet_size": variance,
            "entropy_packet_size": entropy
        })

    return pd.DataFrame(records)
