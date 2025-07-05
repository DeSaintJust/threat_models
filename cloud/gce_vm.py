# --- Modal Operators ---
def Diamond(p):  # Possibly p
    return f"◇({p})"

def Box(p):      # Necessarily p
    return f"□({p})"

# --- Propositions ---
propositions = {
    "p1": "Adversary has administrative access to Google Compute Engine VM",
    "p2": "Adversary does not have access",
    "p3": "Exploits weak or leaked SSH credentials",
    "p4": "Compromises a sudo/root user (e.g., phishing)",
    "p5": "Exploits unpatched OS or software vulnerabilities",
    "p6": "Uses stolen SSH private keys",
    "p7": "Abuses metadata server for privilege escalation or keys",
    "p8": "Misuses GCP IAM roles (OS Login or key generation)",
    "p9": "Exploits misconfigured firewall or internal network pivot",
    "p10": "Leverages malicious startup scripts or instance metadata injection",
    "p11": "Escapes container to host on GKE or GCE VM",
    "p12": "Uses compromised service accounts with OS Login or admin rights"
}

# --- Mitigations (Optional) ---
mitigations = {
    "p3": "Enforce strong SSH keys and rotate passwords",
    "p4": "Use phishing-resistant MFA and user training",
    "p5": "Regular patching and vulnerability scanning",
    "p6": "Protect SSH keys, restrict access, and monitor usage",
    "p7": "Enable metadata concealment and limit access",
    "p8": "Enforce least privilege IAM roles and monitor OS Login",
    "p9": "Harden firewall rules and use network segmentation",
    "p10": "Validate startup scripts and restrict metadata injection",
    "p11": "Implement container isolation and runtime security",
    "p12": "Restrict service account permissions and audit usage"
}

# --- Worlds ---
W = {
    "w0": "Unauthenticated / No Access",
    "w3": "Weak or leaked SSH credentials exploited",
    "w4": "Compromised sudo/root user",
    "w5": "Unpatched OS/software vulnerability exploited",
    "w6": "Stolen SSH private key used",
    "w7": "Metadata server abused",
    "w8": "Misused GCP IAM role for OS Login or keys",
    "w9": "Firewall/network pivot exploited",
    "w10": "Startup script or metadata injection exploited",
    "w11": "Container breakout to host VM",
    "w12": "Compromised service account with admin access",
    "w13": "Adversary has administrative access to GCE VM"
}

# --- Accessibility (R) ---
R = [
    [W["w0"], W["w3"]],
    [W["w0"], W["w4"]],
    [W["w0"], W["w5"]],
    [W["w0"], W["w6"]],
    [W["w0"], W["w7"]],
    [W["w0"], W["w8"]],
    [W["w0"], W["w9"]],
    [W["w0"], W["w10"]],
    [W["w0"], W["w11"]],
    [W["w0"], W["w12"]],
    [W["w3"], W["w13"]],
    [W["w4"], W["w13"]],
    [W["w5"], W["w13"]],
    [W["w6"], W["w13"]],
    [W["w7"], W["w13"]],
    [W["w8"], W["w13"]],
    [W["w9"], W["w13"]],
    [W["w10"], W["w13"]],
    [W["w11"], W["w13"]],
    [W["w12"], W["w13"]],
]

# --- Valuation function (v) ---
v = {
    W["w0"]: [propositions["p2"]],
    W["w3"]: [propositions["p3"]],
    W["w4"]: [propositions["p4"]],
    W["w5"]: [propositions["p5"]],
    W["w6"]: [propositions["p6"]],
    W["w7"]: [propositions["p7"]],
    W["w8"]: [propositions["p8"]],
    W["w9"]: [propositions["p9"]],
    W["w10"]: [propositions["p10"]],
    W["w11"]: [propositions["p11"]],
    W["w12"]: [propositions["p12"]],
    W["w13"]: [propositions["p1"]]
}

# --- Modal reasoning examples ---
print("Modal Possibilities (◇):")
for i in range(3, 13):
    print(Diamond(f"{propositions[f'p{i}']} → {propositions['p1']}"))

# --- Kripke model ---
model = {
    "W": W,
    "R": R,
    "v": v
}
