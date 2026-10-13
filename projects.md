---
layout: default
title: Projects
permalink: /projects/
description: "OT Triage: Now / Next / Never triage for OT/ICS vulnerabilities. Open source, offline-first."
---
# Projects

## OT Triage

<p class="eyebrow">Now / Next / Never triage for OT/ICS vulnerabilities</p>

Most vulnerability scores come from IT thinking: a high CVSS number means "patch it". In an OT environment the better question is *what do I do about this one, on this asset, given what protects it*. I built OT Triage to answer that question and to show its work.

You give it a CVSS score or a full CVSS vector, optionally a CVE, and what you know about the asset: how critical it is, how exposed, whether a patch exists and what controls protect it. It answers **NOW**, **NEXT** or **NEVER**, and lists the reasons in plain language. It also shows the single change that would move the answer, so the logic is easy to explain to someone else.

<img class="shot" src="{{ '/assets/img/ot-triage/assess-dark.png' | relative_url }}" alt="The Assess view: a crown-jewel asset with an actively exploited vulnerability is NOW, with the reasons, CISA's required action and its reference links">
<p class="caption">An actively exploited CVE on an exposed crown-jewel asset: NOW, with the reasons and CISA's own guidance.</p>

### What it does

<ul class="facts">
  <li><strong>Threat intelligence built in.</strong> Looks a CVE up in CISA's Known Exploited Vulnerabilities catalog and in EPSS. It shows CISA's required action, its reference links (only plain HTTPS links are clickable, and you always see the real domain), and the forensic-triage flag.</li>
  <li><strong>CVSS vectors.</strong> Paste a CVSS 3.0, 3.1 or 4.0 vector and the score is filled in. Every possible base vector was checked against FIRST's official calculators.</li>
  <li><strong>CISA ICS advisories.</strong> Shows which of CISA's published ICS advisories name a CVE, with a link to each one, what it says about a fix (a vendor fix, a mitigation only, or nothing yet) and the vendor's own steps in the vendor's words: the firmware to install, the setting to change, the workaround. This is context: it never changes the answer.</li>
  <li><strong>Batch mode.</strong> Load a CSV of findings, filter by bucket, search, sort and export the ranked results. An asset inventory fills in criticality, exposure and controls, and an earlier export shows what is new, what moved and what was resolved.</li>
  <li><strong>By asset.</strong> OT assets get patched in short outage windows, so one view groups the findings by asset: the worst bucket on each, and what could be handled on one visit. With a vendor, product and version in the inventory it also points at the advisories that may apply, and says which of them list your version as affected.</li>
  <li><strong>Command line.</strong> The same ranking from a script or a scheduled job, with an exit code you can gate on.</li>
  <li><strong>Offline first.</strong> The only network access is a threat-data update that you start yourself, over HTTPS, to three public sources: CISA's KEV catalog, EPSS and CISA's advisory repository. Nothing about your assets or findings ever leaves the machine.</li>
  <li><strong>Explainable rules.</strong> The decisions behind the rules, and the reasons for each, are written down in the project's policy document, and the scoring thresholds are adjustable.</li>
</ul>

<div class="shots">
  <figure>
    <img class="shot" src="{{ '/assets/img/ot-triage/batch-dark.png' | relative_url }}" alt="The Batch view ranking fifteen findings, with the selected row's reasons, CISA references and the ICS advisories that name its CVE">
    <figcaption>Batch: rank a whole spreadsheet and see the references behind each row.</figcaption>
  </figure>
  <figure>
    <img class="shot" src="{{ '/assets/img/ot-triage/batch-assets-dark.png' | relative_url }}" alt="The Batch view grouped by asset: the worst bucket on each asset and what could be handled on one outage window">
    <figcaption>By asset: the worst thing on each asset, and what to handle on one visit.</figcaption>
  </figure>
  <figure>
    <img class="shot" src="{{ '/assets/img/ot-triage/advisory-steps-dark.png' | relative_url }}" alt="The Assess view for an actively exploited firewall flaw on a crown-jewel asset, with the CISA ICS advisory that names it and the vendor's own mitigations and fix">
    <figcaption>CISA's advisory for the CVE, with what the vendor says to do about it.</figcaption>
  </figure>
  <figure>
    <img class="shot" src="{{ '/assets/img/ot-triage/assess-light.png' | relative_url }}" alt="The Assess view in the light theme">
    <figcaption>A light theme, adjustable text size and keyboard shortcuts.</figcaption>
  </figure>
</div>

### Built to be trusted

It is a security tool, so it is tested like one. The project has a written security test plan with archived reports, tests that feed it hostile files and hostile network responses, property-based fuzzing, and automated checks on every change (Linux and Windows, static analysis and a secret scan). It is pure Python with no third-party dependencies, so there is no dependency tree to audit.

The Now / Next / Never categories come from the framing Dragos has used in its annual ICS/OT Year in Review. The definitions and scoring rules here are my own and are documented in the repository.

<div class="actions">
  <a class="button" href="{{ site.links.ot_triage }}">View on GitHub</a>
  <a class="button secondary" href="{{ site.links.ot_triage }}#readme">Read the README</a>
</div>

### Get it

The current version is **0.8.0**. Each [release]({{ site.links.ot_triage }}/releases/latest) has a portable bundle (`ot-triage-0.8.0.zip`) with a checksum file next to it. Unzip it anywhere and, on Windows, double-click **OT Triage.pyw**; everywhere else run `python3 ot_triage_gui.py`. It needs Python 3.12 or newer with Tkinter, and nothing else: no third-party packages and no `.exe`. The bundle is reproducible, so anyone can rebuild it from the tag and compare the checksum.

If you are looking for places to learn more about OT security, there is also a [curated list of free OT/ICS resources]({{ '/resources/' | relative_url }}).

MIT licensed code. The OkieOTSec name and logo are not part of that license.
