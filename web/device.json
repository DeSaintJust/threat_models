# propositions
p1 = "Access to internal corporate mail server"
p2 = "Credentials are accessible that provide access to a corporate mail server"
p3 = "A vulnerable service on the corporate mail server is accessible"

if p2 or p3:
  Diamond(p1)

# mitigations
m1 = "Credential segmentation: Ensure no shared or cached credentials exist on the web server that are valid for the mail server."
m2 = "No plaintext secrets: Avoid storing mail server credentials in environment variables, config files, or memory."
m3 = "Use Just-In-Time access controls: Credentials expire quickly and are not statically configured."
m4 = "Password vaults: Use hardware-backed secure enclaves or centralized secrets managers (e.g., HashiCorp Vault, AWS Secrets Manager)."
m5 = "Remove client tools: Don’t allow Outlook, Thunderbird, or similar mail clients to be installed or used on the web server."
m6 = "MFA and conditional access: Ensure that access to the mail server requires interactive MFA from specific trusted endpoints (not from the web server subnet)."
m7 = "TLS client authentication: Only allow mail access from devices presenting valid client certificates."
m8 = "Isolate the mail server from the DMZ or web tier."
m9 = "Enforce strict allowlists for service ports (e.g., block SMTP/IMAP from the web server)."
m10 = "All communication requires identity verification and explicit authorization."
m11 = "Only trusted internal hosts can reach mail services."
m12 = "Patch Exchange/Postfix/Dovecot/Sendmail immediately."
m13 = "Disable unused protocols and interfaces (e.g., remove legacy RPC)."
m14 = "Run intrusion detection / honeypots on the mail server subnet to detect scans."
m15 = "Don’t expose internal mail servers via the same DNS resolvers the web server uses."
m16 = "TLS enforcement, spam filtering, authentication required before mail command acceptance."

if m1 and m2 and m3 and m4 and m5 and m6 and m7:
  Box(not p2)

if m8 and m9 and m10 and m11 and m12 and m13 and m14 and m15 and m16:
  Box(not p3)

model = {
  "W": {"w1":"Access as web server as operating system administrator", "w2":"Access to internal corporate mail server"},
  "R": [["w1", "w2"]],
  "v": {
    "w1": [p2],
    "w2": [p1]
  }
}
