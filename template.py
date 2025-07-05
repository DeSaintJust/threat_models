# Placeholder modal operators (for later logic validation or symbolic model checking)
def Diamond(p):  # Possibly p
  return f"◇({p})"

def Box(p):      # Necessarily p
  return f"□({p})"

# propositions describing conditions that are required for an attack to succeed
propositions = {
  "p1":"Adversary has administrative access to a Google Kubernetes Engine Cluster",
  "p2":"Adversary does not have access"
}

if propositions["p2"]:
  Diamond(propositions["p1"])

# mitigations that negate specific propositions
mitigations = {}

if any(m for ms in mitigations.keys()):
  Box(not p2)

W = {
  "w1":"Unauthenticated", 
  "w2":"Administrative access to Google Kubernetes Engine Cluster"
}

R = [[W["w1"], W["w2"]]]

v = {
  W["w1"]: [propositions["p2"]],
  W["w2"]: [propositions["p1"]]
}

model = [W, R, v]
