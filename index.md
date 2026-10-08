---
layout: default
---
<section class="hero">
  <p class="eyebrow">OT / ICS security</p>
  <h1>Securing OT, from the radio tower to the control room.</h1>
  <p class="lede">I'm Jared, an OT security practitioner from Oklahoma with 16 years across field tech work, SCADA, industrial radio and telemetry, and security. This is where I share what I build, break, and learn.</p>
  <p><a class="button" href="{{ '/notes/' | relative_url }}">Read the lab notes</a></p>
</section>

<section class="cards">
  <div class="card">
    <h2>Radio &amp; telemetry</h2>
    <p>Licensed and unlicensed radio, cellular, VSAT and point-to-point links. The remote side of OT that rarely gets talked about.</p>
  </div>
  <div class="card">
    <h2>SCADA &amp; HMI</h2>
    <p>Tags, Modbus maps, HMI graphics and historians, seen from someone who spent years building them.</p>
  </div>
  <div class="card">
    <h2>Home lab builds</h2>
    <p>A two-cell simulated plant with PLCs, an HMI, a historian, a firewall, an attacker and detections. Every step documented.</p>
  </div>
</section>

<section>
  <h2>Latest notes</h2>
  <ul class="post-list">
    {% for post in site.posts limit:5 %}
    <li><span class="meta">{{ post.date | date: "%b %-d, %Y" }}</span> <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</section>
