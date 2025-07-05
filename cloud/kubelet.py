# https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/
# === Propositions (TTPs) ===
p1 = "Deploy malicious container with elevated privileges"
p2 = "Escape container to gain access to the host system"
p3 = "Abuse misconfigured RBAC to escalate privileges"
p4 = "Access cloud metadata services to obtain credentials"
p5 = "Establish persistence on the host system"

# === Kripke Model ===
model = {
    "W": {
        "w0": "Malicious container deployed",
        "w1": "Container escape achieved",
        "w2": "RBAC misconfigurations exploited",
        "w3": "Cloud metadata accessed",
        "w4": "Persistence established"
    },
    "R": [
        ("w0", "w1"),
        ("w1", "w2"),
        ("w2", "w3"),
        ("w3", "w4")
    ],
    "v": {
        "w0": [p1],
        "w1": [p2],
        "w2": [p3],
        "w3": [p4],
        "w4": [p5]
    }
}
