title: Projects
template: template.html
siteroot: .

---

{% set projects = siblings['projects'].contents|dictsort %}
<div id="project-grid">
{% for _, projdir in projects %}
{% set project = projdir.contents['index.md'] %}
<div class="project-grid-item">
    <img src="{{siteroot}}/img/{{projdir.fpath}}.png"/><br>
    <a href="{{ project.fpath }}">{{ project.data.title }}</a>
    <p>
        {{project.data.description}}
    </p>
</div>
{% endfor %}
