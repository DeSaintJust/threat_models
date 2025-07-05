# === Propositions (APT40 TTPs) ===
p1 = "Conduct reconnaissance on target networks"
p2 = "Identify and exploit known vulnerabilities (e.g., CVE-2021-26084)"
p3 = "Gain initial access to the target network"
p4 = "Establish persistence within the network"
p5 = "Escalate privileges to gain higher access"
p6 = "Move laterally within the network"
p7 = "Exfiltrate sensitive data"
p8 = "Maintain long-term access for future operations"

# === Mitigations ===
m1 = "Harden public-facing services and limit information exposure via open-source intelligence (OSINT) or DNS records"
m2 = "Patch management program to address known CVEs promptly and continuously scan for vulnerable systems"
m3 = "Use WAFs, endpoint protection, and credential hygiene to prevent exploitation and initial access"
m4 = "Monitor for persistence mechanisms (e.g., new services, autoruns, scheduled tasks) and isolate anomalies"
m5 = "Implement PAM (Privileged Access Management) and EDRs to detect and prevent privilege escalation"
m6 = "Apply segmentation, restrict lateral movement (via firewalls and ACLs), and use microsegmentation"
m7 = "Use DLP (Data Loss Prevention), outbound traffic inspection, and TLS decryption for egress filtering"
m8 = "Rotate credentials, audit accounts, and apply zero-trust with inactivity-based account expiration"

# === Modal Logic Inference ===
# If mitigations hold, certain attack propositions are necessarily false (Box ¬p)
if m1:
    Box(not p1)
if m2:
    Box(not p2)
if m3:
    Box(not p3)
if m4:
    Box(not p4)
if m5:
    Box(not p5)
if m6:
    Box(not p6)
if m7:
    Box(not p7)
if m8:
    Box(not p8)

# === Kripke Model ===
model = {
    "W": {
        "w0": "Initial reconnaissance phase",
        "w1": "Exploitation of vulnerabilities",
        "w2": "Initial access achieved",
        "w3": "Persistence established",
        "w4": "Privilege escalation performed",
        "w5": "Lateral movement conducted",
        "w6": "Data exfiltration executed",
        "w7": "Long-term access maintained"
    },
    "R": [
        ("w0", "w1"),
        ("w1", "w2"),
        ("w2", "w3"),
        ("w3", "w4"),
        ("w4", "w5"),
        ("w5", "w6"),
        ("w6", "w7")
    ],
    "v": {
        "w0": [p1],
        "w1": [p2],
        "w2": [p3],
        "w3": [p4],
        "w4": [p5],
        "w5": [p6],
        "w6": [p7],
        "w7": [p8]
    }
}
