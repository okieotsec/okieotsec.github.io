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
  <li><strong>Batch mode.</strong> Load a CSV of findings, filter by bucket, search, sort and export the ranked results.</li>
  <li><strong>Offline first.</strong> The only network access is a threat-data update that you start yourself, over HTTPS, to two public sources. Nothing about your assets or findings ever leaves the machine.</li>
  <li><strong>Explainable rules.</strong> The decisions behind the rules, and the reasons for each, are written down in the project's policy document, and the scoring thresholds are adjustable.</li>
</ul>

<div class="shots">
  <figure>
    <img class="shot" src="{{ '/assets/img/ot-triage/batch-dark.png' | relative_url }}" alt="The Batch view ranking six findings, with the selected row's reasons and CISA references">
    <figcaption>Batch: rank a whole spreadsheet and see the references behind each row.</figcaption>
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

MIT licensed. Python 3.12 or newer with Tkinter, then `python3 ot_triage_gui.py`.
