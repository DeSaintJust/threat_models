# === Propositions (TTPs) ===
p1 = "Identify and compromise legacy test OAuth application with elevated access"
p2 = "Create additional malicious OAuth applications with high privileges"
p3 = "Grant consent to malicious OAuth applications using a new user account"
p4 = "Assign 'full_access_as_app' role to malicious OAuth applications"
p5 = "Authenticate to Exchange Online using malicious OAuth applications"
p6 = "Access corporate email accounts via Exchange Web Services"

# === Mitigations ===
m1 = "Implement strong authentication mechanisms for all accounts"
m2 = "Regularly audit and remove unnecessary OAuth applications"
m3 = "Enforce least privilege access for OAuth applications"
m4 = "Monitor and alert on unusual OAuth consent grants"
m5 = "Restrict permissions granted to OAuth applications"

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

# === Kripke Model ===
model = {
    "W": {
        "w0": "Initial access achieved",
        "w1": "Legacy test OAuth application compromised",
        "w2": "Malicious OAuth applications created",
        "w3": "Consent granted to malicious OAuth applications",
        "w4": "Elevated permissions assigned to OAuth applications",
        "w5": "Authentication via malicious OAuth applications",
        "w6": "Access to corporate email accounts obtained"
    },
    "R": [
        ("w0", "w1"),
        ("w1", "w2"),
        ("w2", "w3"),
        ("w3", "w4"),
        ("w4", "w5"),
        ("w5", "w6")
    ],
    "v": {
        "w0": [],
        "w1": [p1],
        "w2": [p2],
        "w3": [p3],
        "w4": [p4],
        "w5": [p5],
        "w6": [p6]
    }
}
