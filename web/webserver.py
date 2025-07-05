# propositions
p1 = "Access as administrator on web server operating system"
p2 = "There is an exploitable local privilege escalation vulnerability on the server"
p3 = "A compromised application has write access in directories ownered by the operating system administrator"
p4 = "Access elevation methods on the operating system are accessible to the application"
p5 = "Untrusted code can be injected into privileged processes"
p6 = "Privileged services are running on the web server"
p7 = "Privileged credentials are accessible to the web application"
p8 = "The compromised application is running with administrative privileges"

# mitigations
m1 = "Patch the OS and all kernel-level components regularly."
m2 = "Use a Linux hardening framework (e.g., Kernel lockdown mode, SELinux)."
m3 = "Monitor with tools like linux-exploit-suggester, syzkaller."
m4 = "Disable features not needed (e.g., unprivileged user namespaces)."
m5 = "Run the app under a dedicated low-privilege user."
m6 = "Enforce strict file system permissions (chmod, chown)."
m7 = "Use read-only mounts where appropriate."
m8 = "Audit for improper write permissions using tools like ls -alR / | grep "rw"."
m9 = "Remove or restrict tools like sudo, su, pkexec from the app environment."
m10 = "Use containerization or sandboxing (e.g., AppArmor, seccomp)."
m11 = "Audit and restrict any CLI/GUI-based elevation utilities."
m12 = "Configure PAM and policykit to block elevation from unprivileged users."
m13 = "Use process isolation: run privileged and unprivileged processes under different UIDs."
m14 = "Harden the system with SELinux or AppArmor to prevent inter-process interference."
m15 = "Disable ptrace for non-root processes (echo 1 > /proc/sys/kernel/yama/ptrace_scope)."
m16 = "Use hardened kernels with mitigations like ASLR, DEP/NX, CFI."
m17 = "Avoid co-locating sensitive services (e.g., LDAP, backup daemons) with public-facing apps."
m18 = "Run only essential services, and sandbox or containerize them."
m19 = "Use systemd hardening options (ProtectSystem, PrivateTmp, etc.)."
m20 = "Audit with tools like ps aux | grep root and disable unnecessary daemons."
m21 = "Never store root/administrator credentials in the app config or environment."
m22 = "Use secrets managers (e.g., Vault, AWS Secrets Manager)."
m23 = "Limit file access with file ACLs or separate mounts."
m24 = "Scan for credential exposure using tools like truffleHog, gitleaks."
m25 = "Run the web app as a non-root user (nobody, www-data, webapp)."
m26 = "Use User= and Group= directives in systemd unit files."
m27 = "Block privilege escalation via Linux capabilities (drop all with capsh --drop=all)."
m28 = "For Windows: run services under restricted service accounts (not SYSTEM or Administrator)."

if p2 or p3 or p4 or p5 or p6 or p7 or p8:
  Diamond(p1)

if m1 and m2 and m3 and m4:
  Box(not p2)

if m5 and m6 and m7 and m8:
  Box(not p3)

if m9 and m10 and m11 and m12:
  Box(not p4)

if m13 and m14 and m15 and m16:
  Box(not p5)

if m17 and m18 and m19 and m20:
  Box(not p6)

if m21 and m22 and m23 and m24:
  Box(not p7)

if m25 and m26 and m27 and m28:
  Box(not p8)

model = {
  "W": {"w1":"Access as web application", "w2":"Access as operating system administrator"},
  "R": [["w1", "w2"]],
  "v": {
    "w1": [p2],
    "w2": [p1]
  }
}
