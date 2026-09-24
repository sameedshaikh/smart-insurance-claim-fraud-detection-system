import streamlit as st
import pandas as pd
import numpy as np

# Set up page layout
st.set_page_config(page_title="Insurance Fraud Detector", page_icon="🛡️", layout="centered")

# App Header
st.title("🛡️ Insurance Claim Fraud Detection App")
st.write("Enter the claim and policy details below to check for potential fraudulent activity.")

# Input Form for Data Collection
with st.form("prediction_form"):
    st.subheader("📋 Claim & Policy Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Insured Age", min_value=18, max_value=100, value=35)
        policy_deductable = st.selectbox("Policy Deductible ($)", [500, 1000, 2000])
        umbrella_limit = st.number_input("Umbrella Limit ($)", min_value=0, max_value=10000000, step=100000, value=0)
        capital_gains = st.number_input("Capital Gains ($)", min_value=0, value=0)
    
    with col2:
        incident_type = st.selectbox("Incident Type", ["Single Vehicle Collision", "Multi-vehicle Collision", "Parked Car", "Vehicle Theft"])
        collision_type = st.selectbox("Collision Type", ["Rear Collision", "Front Collision", "Side Collision", "Unknown"])
        incident_severity = st.selectbox("Incident Severity", ["Trivial Damage", "Minor Damage", "Major Damage", "Total Loss"])
        total_claim_amount = st.number_input("Total Claim Amount ($)", min_value=0, value=5000)
        
    submitted = st.form_submit_button("Analyze Claim")

# Risk Assessment Logic
if submitted:
    st.subheader("📊 Analysis Results")
    
    # Simple rule-based validation logic for UI demonstration
    risk_score = 0
    reasons = []
    
    if incident_severity in ["Major Damage", "Total Loss"]:
        risk_score += 40
    if total_claim_amount > 50000:
        risk_score += 30
        reasons.append("High claim amount requested")
    if incident_type == "Vehicle Theft" and collision_type != "Unknown":
        risk_score += 20
        reasons.append("Mismatched incident and collision profiles")
        
    # Baseline normal variation
    risk_score = min(100, max(5, risk_score + int(age % 10 * 2)))
    
    # Display results according to calculated threshold
    if risk_score >= 60:
        st.error(f"⚠️ High Risk of Fraud Detected! (Risk Score: {risk_score}%)")
        st.write("**Flagged Indicators:**")
        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("- Severity and claim dynamics closely match high-risk fraud profiles.")
    elif risk_score >= 30:
        st.warning(f"⚡ Medium Risk: Verification recommended. (Risk Score: {risk_score}%)")
    else:
        st.success(f"✅ Low Risk: Safe to process standard payout. (Risk Score: {risk_score}%)")
        
    # Visual Progress Indicator
    st.progress(risk_score / 100)
