import pandas as pd

def extract_packet_features(packets):
    """
    Convert list of packets into a DataFrame with basic features:
    - timestamp
    - length
    - protocol
    """
    records = []

    for pkt in packets:
        record = {
            "timestamp": float(pkt.time),
            "length": len(pkt),
            "protocol": pkt.summary().split()[0]
        }
        records.append(record)

    return pd.DataFrame(records)
