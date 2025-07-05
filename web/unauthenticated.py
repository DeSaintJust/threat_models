p1 = "Code is executed on a public-facing web server"
p2 = "There is an exploitable vulnerability on a public-facing web server"
p3 = "Repository trusted by a public-facing web server is compromised"
p4 = "Credentials of a user with acccess to a public-facing web server are compromised"

if p2 or p3 or p4:
  Diamond(p1)

model = {
  "W": {"w1":"Unauthenticated", "w2":"Web server"},
  "R": [["w1", "w2"]],
  "v": {
    "w1": [p2],
    "w2": [p1]
  }
}
