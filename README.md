# Network Traffic Feature Engineering

A reproducible pipeline to extract **packet-level and flow-level features** from network traffic PCAP files.  
Designed for **machine learning–based network traffic analysis and anomaly detection**.

---

## 🔹 Project Scope

- Convert raw PCAP files into **packet-level** and **flow-level** representations
- Aggregate flows using **5-tuple (src_ip, dst_ip, src_port, dst_port, protocol)**
- Extract **statistical features** for each flow:
  - Number of packets
  - Total bytes
  - Flow duration
  - Average packet size
  - Variance of packet sizes
  - Entropy of packet sizes
- Produce **ML-ready datasets** for anomaly detection and traffic analysis

---

## 🛠️ Tools & Technologies

- Python 3.13+
- [Scapy](https://scapy.net/) — packet processing
- [Pandas](https://pandas.pydata.org/) — data manipulation
- [NumPy](https://numpy.org/) — numerical computation

---

## 📂 Project Structure

```text
network-traffic-feature-engineering/
│
├── data/
│   ├── raw_pcaps/          # Input PCAP files
│   └── features/           # Extracted flow-level CSVs
│
├── src/
│   ├── __init__.py
│   ├── pcap_reader.py      # PCAP loading utilities
│   ├── packet_features.py  # Packet-level feature extraction
│   └── flow_features.py    # Flow-level statistical features
│
├── README.md
├── .gitignore
└── requirements.txt
