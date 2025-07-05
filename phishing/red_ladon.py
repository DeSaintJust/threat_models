# https://www.proofpoint.com/au/blog/threat-insight/chasing-currents-espionage-south-china-sea
# === Propositions (TTPs) ===
p1 = "Conduct reconnaissance on target organizations"
p2 = "Craft phishing emails impersonating Australian media entities"
p3 = "Deliver ScanBox malware via malicious websites"
p4 = "Collect victim data through ScanBox (e.g., keystrokes, browser info)"
p5 = "Deploy additional malware payloads based on reconnaissance"
p6 = "Exfiltrate sensitive information from compromised systems"
p7 = "Maintain persistent access for long-term espionage"

# === Mitigations ===
m1 = "Implement threat intelligence to monitor for reconnaissance activities"
m2 = "Educate users to recognize phishing attempts and verify sender identities"
m3 = "Deploy web filtering to block access to known malicious domains"
m4 = "Use endpoint protection to detect and prevent data collection tools"
m5 = "Monitor for unusual behavior indicative of secondary malware deployment"
m6 = "Employ data loss prevention (DLP) solutions to detect and block exfiltration"
m7 = "Regularly audit systems for unauthorized access and persistence mechanisms"

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
if m6:
    Box(not p6)
if m7:
    Box(not p7)

# === Kripke Model ===
model = {
    "W": {
        "w0": "Initial reconnaissance phase",
        "w1": "Phishing emails crafted and sent",
        "w2": "Malware delivered via malicious website",
        "w3": "Data collection through ScanBox",
        "w4": "Deployment of additional malware",
        "w5": "Data exfiltration executed",
        "w6": "Persistence established for ongoing access"
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
        "w0": [p1],
        "w1": [p2],
        "w2": [p3],
        "w3": [p4],
        "w4": [p5],
        "w5": [p6],
        "w6": [p7]
    }
}
