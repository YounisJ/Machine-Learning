import streamlit as st
import pandas as pd
import joblib
import pyshark
import numpy as np

# Load trained model
model = joblib.load('tor_detector.pkl')

# Function to extract features from PCAP file
def extract_features(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    data = []







    for packet in cap:
        try:
            features = {
                "length": int(packet.length),
                "protocol": packet.highest_layer,
                "src_ip": packet.ip.src,
                "dst_ip": packet.ip.dst,
                "src_port": int(packet[packet.transport_layer].srcport),
                "dst_port": int(packet[packet.transport_layer].dstport)
            }
            data.append(features)
        except AttributeError:
            continue

    cap.close()
    return pd.DataFrame(data)

# Streamlit UI
st.title("Dark Web Activity Detector")

uploaded_file = st.file_uploader("Upload a PCAP file", type=["pcap"])

if uploaded_file is not None:
    st.write("Processing file...")
    df = extract_features(uploaded_file)

    # Convert categorical features to numerical (dummy encoding or mapping)
    df["protocol"] = df["protocol"].astype("category").cat.codes

    # Make predictions
    predictions = model.predict(df)

    # Display results
    df["Prediction"] = predictions
    st.write(df)

    if 1 in predictions:
        st.warning("Dark web activity detected!")
    else:
        st.success("No dark web activity detected.")
