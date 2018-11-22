title: Projects
template: template.html

---

{% set projdirs = parent.contents['projects'].contents|dictsort %}
{% set projects = [] %}
<div id="project-grid">

{% for _, projdir in projdirs %}
    {% set _ = projects.append(projdir) %}
{% endfor %}

{% for project in projects|sort(attribute='data.priority') %}
<div class="project-grid-item">
    <a href="{{ project.contents['index.md'].fpath }}">
    <img src="{{parent.data.siteroot}}{{project.data.image}}"/><br>
    {{ project.contents['index.md'].data.title }}</a>
    <p>
        {{project.contents['index.md'].data.description}}
    </p>
</div>
{% endfor %}
