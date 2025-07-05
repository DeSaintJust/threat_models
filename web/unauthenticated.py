# propositions
p1 = "Code is executed on a public-facing web server"
p2 = "There is an exploitable vulnerability on a public-facing web server"
p3 = "Repository trusted by a public-facing web server is compromised"
p4 = "Credentials of a user with acccess to a public-facing web server are compromised"

if p2 or p3 or p4:
  Diamond(p1)

# mitigations
m1 = "Regularly patch and update all software (OS, web apps, libraries)."
m2 = "Conduct continuous vulnerability scanning and penetration testing."
m3 = "Use WAFs, input validation, and memory safety techniques."
m4 = "Remove or disable unused services and features (reduce attack surface)."
m5 = "Adopt memory-safe languages (e.g., Rust over C) where possible."
m6 = "Use pinned hashes or signed packages (e.g., sha256, GPG) instead of "latest"."
m7 = "Use verified third-party package registries (e.g., Sigstore, PyPI trusted publishers)."
m8 = "Mirror critical dependencies internally and control updates manually."
m9 = "Scan for supply chain threats using SBOM (Software Bill of Materials) tooling."
m10 = "Monitor public feeds for compromised packages (e.g., Sonatype, Snyk)."
m11 = "Enforce MFA and passwordless authentication (e.g., FIDO2)."
m12 = "Use least privilege: restrict who can access the server and what they can do."
m13 = "Regularly rotate credentials and monitor access logs."
m14 = "Use hardware-backed key storage (e.g., YubiKeys)."
m15 = "Enforce zero-trust network access (ZTNA) — no implicit trust for credentials."
m16 = "Monitor for credential reuse via dark web exposure alerts."

if m1 and m2 and m3 and m4 and m5:
  Box(not p2)

if m6 and m7 and m8 and m9 and m10:
  Box(not p3)

if m11 and m12 and m13 and m14 and m15 and m16:
  Box(not p4)

model = {
  "W": {"w1":"Unauthenticated", "w2":"Web server"},
  "R": [["w1", "w2"]],
  "v": {
    "w1": [p2],
    "w2": [p1]
  }
}
