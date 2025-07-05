# https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/
# === Propositions (TTPs) ===
p1 = "Scan for exposed Kubernetes kubelets with anonymous access"
p2 = "Gain access to Kubernetes cluster via misconfigured kubelet"
p3 = "Deploy tmate reverse shell for command and control (C2)"
p4 = "Establish IRC channel for persistent C2 communication"

# === Mitigations ===
m1 = "Disable anonymous access to Kubernetes kubelets"
m2 = "Implement authentication and authorization for kubelet APIs"
m3 = "Monitor for unauthorized reverse shell connections"
m4 = "Inspect network traffic for unauthorized IRC communications"

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

# === Kripke Model ===
model = {
    "W": {
        "w0": "Scanning phase",
        "w1": "Access gained to Kubernetes cluster",
        "w2": "Reverse shell deployed",
        "w3": "IRC channel established"
    },
    "R": [
        ("w0", "w1"),
        ("w1", "w2"),
        ("w2", "w3")
    ],
    "v": {
        "w0": [p1],
        "w1": [p2],
        "w2": [p3],
        "w3": [p4]
    }
}
