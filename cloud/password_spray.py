# === Propositions (TTPs) ===
p1 = "Conduct password spray attacks using common passwords"
p2 = "Target legacy, non-production test tenant accounts without MFA"
p3 = "Utilize distributed residential proxy infrastructure to evade detection"
p4 = "Successfully authenticate to a test tenant account"

# === Mitigations ===
m1 = "Implement account lockout policies to deter password spraying"
m2 = "Enforce multi-factor authentication (MFA) on all accounts, including test tenants"
m3 = "Monitor for authentication attempts from residential proxy IP ranges"
m4 = "Audit and secure legacy test tenant accounts"

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
        "w0": "Initiate password spray attack",
        "w1": "Target legacy test tenant accounts",
        "w2": "Employ residential proxies for obfuscation",
        "w3": "Gain access to test tenant account"
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
