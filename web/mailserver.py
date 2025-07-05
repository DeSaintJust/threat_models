# propositions
p1 = "Access to internal corporate mail server"
p2 = "Read and dump inbox contents (sensitive data, legal, financial, executive communications)"
p3 = "Search for credentials in mail content (plaintext passwords, MFA tokens, etc.)"
p4 = "Export entire mailboxes (PST, EML, or MBOX formats)"
p5 = "Monitor live email communications (e.g., via journaling, mailbox rules)"
p6 = "Exfiltrate attachments (e.g., contracts, source code, HR records)"
p7 = "Create forwarding rules to exfiltrate future emails"
p8 = "Modify or delete emails to disrupt workflows or hide traces"
p9 = "Spoof internal senders to impersonate executives or HR"
p10 = "Insert malicious links or payloads into drafts, sent items, or calendar invites"
p11 = "Send internal phishing emails using a trusted mailbox"
p12 = "Abuse administrative tools (e.g., Exchange Management Shell or web admin interfaces)"
p13 = "Modify Receive/Send Connector settings to relay spam or malware"
p14 = "Create new privileged mailboxes or admin roles"
p15 = "Dump Active Directory-integrated credentials (if mail server is domain-joined)"
p16 = "Access service account credentials stored in config files or memory"
p17 = "Extract OAuth tokens, NTLM hashes, or Kerberos tickets"
p18 = "Use cached credentials or tokens to access: File shares, Domain controllers, Other internal applications (HR, finance, ERP)"
p19 = "Exploit trusted relationships with other systems (e.g., shared mailbox permissions)"
p20 = "Pivot via Exchange Web Services (EWS), MAPI, or PowerShell remoting"
p21 = "Abuse Outlook Forms, COM objects, or malicious add-ins for movement to endpoints"
p22 = "Create mailbox rules to run scripts or auto-forward"
p23 = "Register transport agents or event sinks (in Exchange)"
p24 = "Implant scheduled tasks or services on the mail server"
p25 = "Deploy backdoors via DLL sideloading, web shells, or cron jobs"
p26 = "Abuse autodiscover / autodiscover.json redirection to control client connections"
p27 = "Send high-trust phishing emails from compromised accounts"
p28 = "Craft spearphishing emails using gathered internal context"
p29 = "Impersonate executives (CEO/CFO) to perform BEC (Business Email Compromise)"
p30 = "Conduct whaling by targeting high-value individuals"
p31 = "Embed malicious macros or links in calendar invites or meeting requests"
p32 = "Turn the mail server into a spam relay"
p33 = "Send malware externally (causing blacklisting of company’s IP/domain)"
p34 = "Use mail server as a C2 infrastructure node"
p35 = "Launch DDoS or botnet activity from mail server"
p36 = "Abuse SMTP relay to send phishing/malware under company domain"
p37 = "Extract private keys or TLS certificates from mail server storage"
p38 = "Downgrade or disable TLS encryption for SMTP/IMAP"
p39 = "Intercept internal mail traffic if encryption is not enforced"
p40 = "Disable MFA policies or mailbox auditing"
p41 = "Replay or forge OAuth or SAML tokens"
p42 = "Backdoor mail server software (e.g., via plugin or DLL injection)"
p43 = "Modify integration points (e.g., with AV, DLP, archiving systems)"
p44 = "Intercept or modify mail archival/logging systems to erase traces"
p45 = "Exploit mail filtering or security gateways misconfigured to trust internal senders"
p46 = "Delete or corrupt mailboxes"
p47 = "Lock users out by changing credentials or mailbox ownership"
p48 = "Stop SMTP/IMAP/POP services"
p49 = "Flood system queues to cause DoS"
p50 = "Wipe logs to prevent detection"
p51 = "Plant false messages (e.g., fake HR directives)"
p52 = "Attack external partners or clients by sending malware/phishing from trusted addresses"
p53 = "Harvest mail headers and contacts for reconnaissance"
p54 = "Exfiltrate confidential external communications (e.g., NDAs, contracts)"

if p1:
  Diamond(any([p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40,
  p41, p42, p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54]))

# mitigations

m1 = "LSASS protected by Credential Guard or sandboxing (on Windows Server)."
m2 = "Tokens may not be stored locally; may be encrypted or in inaccessible key stores."
m3 = "Other internal systems may require MFA, device identity, or be behind ZTNA boundaries."
m4 = "Mail server may not have any established inter-service trust or RBAC permissions elsewhere."
m5 = "Outbound access from the mail server may be blocked or filtered; remoting may be disabled."
m6 = "These require client-side execution (on Outlook clients), not server-side."
m7 = "If autodiscover is managed externally (e.g., by Microsoft 365), local control has no impact."
m8 = "Egress filtering, firewall rules, or reverse proxy design may prevent outbound C2 traffic."
m9 = "The network perimeter may block unusual volumes of outbound traffic or rate-limit unknown destinations."
m10 = "Mail server may not act as a man-in-the-middle if TLS is enforced end-to-end by client policy (e.g., S/MIME or M365)."
m11 = "These typically exist outside the mail server and may not trust internal sources."
m12 = "External mail relaying may be restricted or signed emails required (DKIM/DMARC enforced)."
m13 = "These may not reside on the internal server — e.g., they could be in cloud-hosted mailboxes (like Exchange Online)."

if m1:
  Box(not p15)
if m2:
  Box(not p17)
if m3:
  Box(not p18)
if m4:
  Box(not p19)
if m5:
  Box(not p20)
if m6:
  Box(not p21)
if m7:
  Box(not p26)
if m8:
  Box(not p34)
if m9:
  Box(not p35)
if m10:
  Box(not p39)
if m11:
  Box(not p45)
if m12:
  Box(not p52)
if m13:
  Box(not p54)

model = {
  "W": {"w1":"Access to internal corporate mail server"},
  "R": [["w1", "w1"]],
  "v": {
    "w1": [p1]
  }
}
