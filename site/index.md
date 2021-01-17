title: Projects
template: template.html

---

{% set projdirs = parent.contents['projects'].contents|dictsort %}
{% set projects = [] %}
{% for _, projdir in projdirs %}{% set _ = projects.append(projdir) %}{% endfor %}
<div id="project-grid">
<div class="project-grid-item">
    <a href="https://okay.wasv.me">
        <img src="{{parent.data.siteroot}}/img/okay.png"/><br>
        okay.wasv.me
    </a>
    <p>
        An exercise in mindfulness for stress relief.
    </p>
</div>
{% for project in projects|sort(attribute='data.priority') %}
<div class="project-grid-item">
    <a href="{{ project.contents['index.md'].fpath }}">
        <img src="{{parent.data.siteroot}}{{project.data.image}}"/><br>
        {{ project.contents['index.md'].data.title }}
    </a>
    <p>
        {{project.contents['index.md'].data.description}}
    </p>
</div>
{% endfor %}
</div>
