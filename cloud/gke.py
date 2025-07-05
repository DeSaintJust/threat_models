# --- Modal Operators for Temporal/Modal Logic ---
def Diamond(p):  # Possibly p
    return f"◇({p})"

def Box(p):      # Necessarily p
    return f"□({p})"

# --- Propositions: Attack Goals and Paths ---
propositions = {
    "p1": "Adversary has administrative access to a Google Kubernetes Engine Cluster",
    "p2": "Adversary does not have access",
    "p3": "Adversary obtains GCP IAM credentials with Kubernetes Admin role",
    "p4": "Adversary compromises a CI/CD pipeline with kubeconfig or service account tokens",
    "p5": "Adversary exploits a vulnerable workload with GCP API permissions (metadata API access)",
    "p6": "Adversary escalates privileges inside the cluster to cluster-admin",
    "p7": "Adversary gains access via exposed Kubernetes Dashboard with weak/no auth",
    "p8": "Adversary uses stolen SSH keys to access nodes and extract kubeconfig",
    "p9": "Adversary exploits a misconfigured GKE RBAC policy granting admin rights",
    "p10": "Adversary uses a supply chain attack to inject code that leads to cluster access"
}

# --- Mitigations Against Each Attack Path ---
mitigations = {
    "p3": "Use IAM least privilege and enable 2FA",
    "p4": "Secure CI/CD secrets and rotate service account keys",
    "p5": "Restrict metadata API access from pods",
    "p6": "Use RBAC appropriately; enable PodSecurityPolicies or Admission Controllers",
    "p7": "Disable or secure Kubernetes Dashboard",
    "p8": "Disable SSH to nodes or audit key usage",
    "p9": "Audit RBAC policies regularly",
    "p10": "Verify integrity of third-party dependencies"
}

# --- Possible Worlds (W): Different attack stages ---
W = {
    "w0": "No access",  # Initial world
    "w1": "Adversary obtains IAM credentials",
    "w2": "Compromised CI/CD with kubeconfig",
    "w3": "Exploited workload with GCP API access",
    "w4": "Privilege escalation in-cluster",
    "w5": "Exposed Kubernetes Dashboard",
    "w6": "SSH access to node, extracted kubeconfig",
    "w7": "Misconfigured RBAC",
    "w8": "Supply chain compromise",
    "w9": "Full admin access to GKE"
}

# --- Accessibility Relations (R): Paths between worlds ---
# Each step is a possible transition between worlds
R = [
    [W["w0"], W["w1"]],
    [W["w0"], W["w2"]],
    [W["w0"], W["w3"]],
    [W["w0"], W["w4"]],
    [W["w0"], W["w5"]],
    [W["w0"], W["w6"]],
    [W["w0"], W["w7"]],
    [W["w0"], W["w8"]],
    # All lead to admin access eventually
    [W["w1"], W["w9"]],
    [W["w2"], W["w9"]],
    [W["w3"], W["w9"]],
    [W["w4"], W["w9"]],
    [W["w5"], W["w9"]],
    [W["w6"], W["w9"]],
    [W["w7"], W["w9"]],
    [W["w8"], W["w9"]],
]

# --- Valuation Function (v): Propositions true in each world ---
v = {
    W["w0"]: [propositions["p2"]],
    W["w1"]: [propositions["p3"]],
    W["w2"]: [propositions["p4"]],
    W["w3"]: [propositions["p5"]],
    W["w4"]: [propositions["p6"]],
    W["w5"]: [propositions["p7"]],
    W["w6"]: [propositions["p8"]],
    W["w7"]: [propositions["p9"]],
    W["w8"]: [propositions["p10"]],
    W["w9"]: [propositions["p1"]],
}

# --- Modal Logic: Can adversary possibly gain admin access? ---
print("Modal Possibilities (◇):")
attack_paths = ["p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]
for p in attack_paths:
    print(Diamond(f"{propositions[p]} → {propositions['p1']}"))

# --- Optional: Display available mitigations ---
print("\nMitigations:")
for p, m in mitigations.items():
    print(f"If {propositions[p]} then mitigation: {m}")

# --- Full Model Output (for symbolic checking or export) ---
model = {
    "W": W,
    "R": R,
    "v": v
}
