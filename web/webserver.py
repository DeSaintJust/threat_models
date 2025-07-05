# propositions
p1 = "Access as administrator on web server operating system"
p2 = "There is an exploitable local privilege escalation vulnerability on the server"
p3 = "A compromised application has write access in directories ownered by the operating system administrator"
p4 = "Access elevation methods on the operating system are accessible to the application"
p5 = "Untrusted code can be injected into privileged processes"

if p2 or p3 or p4:
  Diamond(p1)

# mitigations


if m1 and m2 and m3 and m4 and m5:
  Box(not p2)

if m6 and m7 and m8 and m9 and m10:
  Box(not p3)

if m11 and m12 and m13 and m14 and m15 and m16:
  Box(not p4)

model = {
  "W": {"w1":"Web server", "w2":"Operating system administrator"},
  "R": [["w1", "w2"]],
  "v": {
    "w1": [p2],
    "w2": [p1]
  }
}
