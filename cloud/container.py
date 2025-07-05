# https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/
# === Propositions (TTPs) ===
p1 = "Scan internal network for unsecured kubelets using masscan"
p2 = "Identify additional containers across nodes"
p3 = "Establish reverse shells to newly discovered containers"
p4 = "Deploy cryptomining payloads across compromised containers"

# === Mitigations ===
m1 = "Implement network segmentation to limit internal scanning"
m2 = "Enforce authentication on kubelet APIs to prevent unauthorized access"
m3 = "Monitor for unusual reverse shell connections within the cluster"
m4 = "Deploy runtime security tools to detect and block unauthorized payloads"

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
        "w0": "Initial foothold in compromised container",
        "w1": "Internal network scanning initiated",
        "w2": "Additional containers identified",
        "w3": "Reverse shells established on new containers",
        "w4": "Cryptomining payloads deployed cluster-wide"
    },
    "R": [
        ("w0", "w1"),
        ("w1", "w2"),
        ("w2", "w3"),
        ("w3", "w4")
    ],
    "v": {
        "w0": [],
        "w1": [p1],
        "w2": [p2],
        "w3": [p3],
        "w4": [p4]
    }
}
