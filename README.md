#  Network Traffic Feature Engineering

![Python](https://img.shields.io/badge/python-3.13+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub Repo Size](https://img.shields.io/github/repo-size/smitaTech30/network-traffic-feature-engineering)

A **reproducible pipeline** to extract **packet-level and flow-level features** from network traffic PCAP files. Designed for **machine learning–based network traffic analysis and anomaly detection**.

## 🔹 Project Scope

This project allows you to:

* Convert raw PCAP files into **packet-level** and **flow-level** representations.
* Aggregate flows using the **5-tuple**: `src_ip`, `dst_ip`, `src_port`, `dst_port`, `protocol`.
* Extract **statistical features** for each flow, including:

  * Number of packets
  * Total bytes
  * Flow duration
  * Average packet size
  * Variance of packet sizes
  * Entropy of packet sizes
* Produce **ML-ready datasets** for anomaly detection and traffic analysis.

## 🛠️ Tools & Technologies

* **Python 3.13+**
* [**Scapy**](https://scapy.net/) — packet processing
* [**Pandas**](https://pandas.pydata.org/) — data manipulation
* [**NumPy**](https://numpy.org/) — numerical computation

## 📂 Project Structure

```
network-traffic-feature-engineering/
├── data/
│   ├── raw_pcaps/          # Input PCAP files
│   └── features/           # Extracted flow-level CSVs
├── src/
│   ├── __init__.py
│   ├── pcap_reader.py      # PCAP loading utilities
│   ├── packet_features.py  # Packet-level feature extraction
│   └── flow_features.py    # Flow-level statistical features
├── README.md
├── .gitignore
└── requirements.txt
```

## Pipeline Overview

```
Raw PCAP Files
      │
      ▼
  Packet Extraction (src/pcap_reader.py)
      │
      ▼
Packet-Level Features (src/packet_features.py)
      │
      ▼
Flow Aggregation & Statistics (src/flow_features.py)
      │
      ▼
   ML-Ready CSV (data/features/)
```

## 🚀 How to Use (Step-by-Step)

1️⃣ Clone the repository

```bash
git clone https://github.com/smitaTech30/network-traffic-feature-engineering.git
cd network-traffic-feature-engineering
```

2️⃣ Set up a Python virtual environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```powershell
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

This will install **Scapy, Pandas, and NumPy**.

4️⃣ Run the feature extraction pipeline

```python
from src.pcap_reader import load_pcap
from src.flow_features import extract_flow_features

# Load packets from PCAP
packets = load_pcap("data/raw_pcaps/sample.pcap")

# Extract flow-level features
df_flows = extract_flow_features(packets)

# Save to CSV
df_flows.to_csv("data/features/flow_features.csv", index=False)

print("✅ Flow features saved!")
```

The CSV will be saved at: `data/features/flow_features.csv`

