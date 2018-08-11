title: Projects
template: template.html
siteroot: .

---

{% set projects = siblings['projects'].contents|dictsort %}
<div id="project-grid">
{% for _, projdir in projects %}
{% set project = projdir.contents['index.md'] %}
<div class="project-grid-item">
    <a href="{{ project.fpath }}">
    <img src="{{siteroot}}{{project.data.image}}"/><br>
    {{ project.data.title }}</a>
    <p>
        {{project.data.description}}
    </p>
</div>
{% endfor %}
