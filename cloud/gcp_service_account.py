# --- Modal Operators ---
def Diamond(p):  # Possibly p
    return f"◇({p})"

def Box(p):      # Necessarily p
    return f"□({p})"

# --- Propositions ---
propositions = {
    "p1": "Adversary has access to an OAuth token associated with a GCP service account",
    "p2": "Adversary does not have access",
    "p3": "Adversary accesses metadata server on a GCE/GKE instance",
    "p4": "Adversary compromises VM or container with attached service account",
    "p5": "Adversary obtains a leaked private key for the service account",
    "p6": "Adversary has IAM permission to impersonate service account (getAccessToken)",
    "p7": "Adversary uses SSRF to query metadata API",
    "p8": "Adversary finds credentials in CI/CD pipeline, artifacts, or container registry",
    "p9": "Adversary recovers OAuth token from source code or logs",
    "p10": "Cloud Function leaks service account token or identity",
    "p11": "Adversary abuses workload identity federation",
    "p12": "Browser-based token exfiltration via extension or local compromise"
}

# --- Mitigations (optional) ---
mitigations = {
    "p3": "Enable metadata concealment and disable legacy access",
    "p4": "Harden workloads, isolate service accounts, enforce defense-in-depth",
    "p5": "Use short-lived keys and restrict downloadability of keys",
    "p6": "Enforce least privilege; deny impersonation via org policy",
    "p7": "Use metadata concealment and SSRF-aware proxies",
    "p8": "Scan artifacts and enforce CI/CD secrets hygiene",
    "p9": "Use static analysis to detect secrets in code/logs",
    "p10": "Restrict service account bindings and enforce runtime environment separation",
    "p11": "Lock down trust configuration and audience mapping",
    "p12": "Harden endpoints, disallow token reuse in browsers"
}

# --- Possible Worlds ---
W = {
    "w0": "No access",
    "w3": "Metadata server accessed via GCE/GKE",
    "w4": "VM or container with SA compromised",
    "w5": "Service account private key obtained",
    "w6": "Impersonation via IAM permissions",
    "w7": "SSRF to metadata API",
    "w8": "Credential leakage in CI/CD",
    "w9": "OAuth token exposed in logs or code",
    "w10": "Cloud Function leaks token or identity",
    "w11": "Abuse of workload identity federation",
    "w12": "Browser-based token exfiltration",
    "w13": "Adversary has access to service account OAuth token"
}

# --- Accessibility Relations (R) ---
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

# --- Valuation (v) ---
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

# --- Modal Reasoning: Show each vector leads to token access ---
print("Modal Possibilities (◇):")
for px in range(3, 13):
    print(Diamond(f"{propositions[f'p{px}']} → {propositions['p1']}"))

# --- Final Kripke Model Object ---
model = {
    "W": W,
    "R": R,
    "v": v
}
