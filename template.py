# propositions describing conditions that are required for an attack to succeed
p1 = "<e.g., Code can be executed on a public-facing web server>"
p2 = "<e.g., There is an exploitable vulnerability on a public-facing web server>"

if p2:
  Diamond(p1)

# mitigations that negate specific propositions
m1 = "<e.g., Regularly patch and update all software (OS, web apps, libraries).>"

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
