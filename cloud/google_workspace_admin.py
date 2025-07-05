# --- Modal Operators ---
def Diamond(p):
    return f"◇({p})"

def Box(p):
    return f"□({p})"

# --- Propositions: States in the attack chain ---
propositions = {
    "p1": "Adversary has super admin access to a Google Workspace",
    "p2": "Adversary does not have access",
    "p3": "Adversary steals credentials of a super admin (password reuse, keylogger)",
    "p4": "Adversary bypasses MFA or hijacks an authenticated session",
    "p5": "Adversary phishes super admin via malicious OAuth consent",
    "p6": "Adversary exploits trusted OAuth apps with domain-wide delegation",
    "p7": "Adversary compromises federated identity provider (SAML/OIDC)",
    "p8": "Insider with existing admin role elevates or misuses privileges",
    "p9": "Adversary escalates from GCP IAM to Google Workspace admin due to cross-platform bindings",
    "p10": "Adversary hijacks session via browser-based XSS",
    "p11": "Supply chain compromise of browser extension or endpoint software",
    "p12": "OAuth app with delegated access is abused"
}

# --- Mitigations (Optional but realistic) ---
mitigations = {
    "p3": "Use strong, unique passwords and password managers; detect credential reuse",
    "p4": "Enforce phishing-resistant MFA (FIDO2, passkeys)",
    "p5": "Review and restrict third-party app access; use OAuth token restrictions",
    "p6": "Disable domain-wide delegation unless required; audit OAuth client IDs",
    "p7": "Secure IdP with MFA and monitor SAML/OIDC configs",
    "p8": "Enforce admin role separation and audit logs",
    "p9": "Avoid privilege sharing between GCP and Workspace accounts",
    "p10": "Enable CSP headers and isolate admin UIs from injection",
    "p11": "Restrict unverified extensions; use managed devices",
    "p12": "Review delegated scopes and revoke unused app access"
}

# --- Possible Worlds (States) ---
W = {
    "w0": "Unauthenticated/No access",
    "w3": "Stolen credentials",
    "w4": "MFA bypass or session hijack",
    "w5": "Phished via malicious OAuth app",
    "w6": "OAuth abuse via trusted app",
    "w7": "Federated IdP compromised",
    "w8": "Malicious or negligent insider admin",
    "w9": "Escalation from GCP IAM",
    "w10": "Browser session hijack (XSS)",
    "w11": "Supply chain compromise",
    "w12": "OAuth app with delegated access",
    "w13": "Super admin access achieved"
}

# --- Accessibility: Transitions between states ---
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

# --- Valuation: Propositions true in each world ---
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

# --- Modal Logic: Is access to p1 possible from each vector?
print("Modal Possibilities (◇):")
for i in range(3, 13):
    print(Diamond(f"{propositions[f'p{i}']} → {propositions['p1']}"))

# --- Full Kripke model object ---
model = {
    "W": W,
    "R": R,
    "v": v
}
