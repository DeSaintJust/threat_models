# --- Modal Logic Operators ---
def Diamond(p):
    return f"◇({p})"

def Box(p):
    return f"□({p})"

# --- Propositions ---
propositions = {
    "p1": "Adversary has access as Organization Administrator in Google Cloud Platform",
    "p2": "Adversary does not have access",
    "p3": "Adversary compromises Google Workspace super admin account",
    "p4": "Adversary compromises GCP IAM user with orgAdmin role",
    "p5": "Adversary obtains OAuth token from service account with org scope",
    "p6": "Adversary phishes a user with organization-level permissions",
    "p7": "Adversary abuses misconfigured Identity Federation (OIDC/SAML)",
    "p8": "Adversary escalates via overly broad custom IAM role",
    "p9": "Adversary exploits IaC (Terraform, Deployment Manager) with org bindings",
    "p10": "Adversary abuses CI/CD pipeline with org-level permissions",
    "p11": "Adversary compromises trusted third-party org-level service",
    "p12": "Adversary inherits org-admin through IAM misconfiguration"
}

# --- Mitigations (Optional) ---
mitigations = {
    "p3": "Enable 2FA and alerting for Google Workspace admins",
    "p4": "Rotate and audit IAM keys and bindings regularly",
    "p5": "Use service account scoping and limit Org-level bindings",
    "p6": "Enforce phishing-resistant MFA (e.g., FIDO2)",
    "p7": "Harden identity federation and restrict subject claim mappings",
    "p8": "Validate IAM custom roles and remove privilege escalation paths",
    "p9": "Use org policy constraints on deployment systems",
    "p10": "Isolate CI/CD secrets and validate least privilege",
    "p11": "Audit third-party access and require VPC-SC or org policy",
    "p12": "Enforce IAM policy hierarchy review and folder inheritance constraints"
}

# --- Possible Worlds ---
W = {
    "w0": "No GCP access",
    "w3": "Compromised Workspace super admin",
    "w4": "Compromised IAM user with orgAdmin",
    "w5": "Service account token with org scope",
    "w6": "Phished org-level IAM user",
    "w7": "Exploited identity federation",
    "w8": "Privilege escalation via custom role",
    "w9": "IaC with org-wide permission abused",
    "w10": "CI/CD compromise with org access",
    "w11": "Compromised third-party service",
    "w12": "Inherited org-admin via IAM misconfig",
    "w13": "Adversary has Org Admin access"
}

# --- Transitions (R): Attack paths ---
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

# --- Valuation Function ---
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
    W["w13"]: [propositions["p1"]],
}

# --- Modal Reasoning ---
print("Modal Possibilities (◇):")
for px in range(3, 13 + 1):
    print(Diamond(f"{propositions[f'p{px}']} → {propositions['p1']}"))

# --- Model Object ---
model = {
    "W": W,
    "R": R,
    "v": v
}
