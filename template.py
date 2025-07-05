# propositions
p1 = "<e.g., Code is executed on a public-facing web server>"
p2 = "<e.g., There is an exploitable vulnerability on a public-facing web server>"

if p2:
  Diamond(p1)

# mitigations
m1 = "<mitigation description>"

if m1:
  Box(not p2)

model = {
  "W": {"w1":"Unauthenticated", "w2":"Web server"},
  "R": [["w1", "w2"]],
  "v": {
    "w1": [p2],
    "w2": [p1]
  }
}
