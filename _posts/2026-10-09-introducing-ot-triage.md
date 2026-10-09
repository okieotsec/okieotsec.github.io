---
layout: post
title: "Introducing OT Triage: Now, Next or Never for OT vulnerabilities"
description: "An open-source tool that tells you what to fix now, what can wait, and why."
---

Every OT security team I know has the same spreadsheet: hundreds of vulnerabilities, a CVSS number next to each, and no good way to decide what to do first. A 9.8 on an isolated, non-critical box and a 6.5 on an exposed controller that attackers are already using are very different problems, and the number alone doesn't tell you that.

So I built a tool to help with that decision. It's called **OT Triage**, and it's open source.

## How it works

You give it a CVSS score (or paste the full CVSS vector), optionally a CVE, and what you know about the asset: how critical it is, how exposed it is, whether a patch exists, and what controls protect it. It answers **NOW**, **NEXT** or **NEVER**, and then it shows its work: the reasons in plain language, and the single change that would move the answer.

If you give it a CVE, it checks CISA's Known Exploited Vulnerabilities catalog and EPSS, and it shows CISA's own required action and reference links right next to the result. You can also load a whole CSV and get a ranked list back.

## Choices I made on purpose

- **Offline first.** The only network access is an update you start yourself, from two public sources, over HTTPS. Your asset data never leaves your machine.
- **Explainable over clever.** The rules are simple enough to read and argue with, and each decision is written down with its reasoning in the project's policy document.
- **Tested like a security tool.** Hostile-input tests, fuzzing, a written security test plan, and automated checks on every change. No third-party dependencies, so there's nothing to audit but the code.

I built it with an AI coding assistant doing much of the typing, and I kept the decisions, such as the rules, the policies and what the tool will and won't do, as mine. The commit history shows that openly.

## Try it

The code, the screenshots and the documentation are on [GitHub]({{ site.links.ot_triage }}), and there's a short write-up on the [projects page]({{ '/projects/' | relative_url }}). It needs Python 3.12 or newer with Tkinter. If you work in OT and something about the rules is wrong for your environment, that's exactly the feedback I want: open an issue, or email me at [{{ site.email }}](mailto:{{ site.email }}).
