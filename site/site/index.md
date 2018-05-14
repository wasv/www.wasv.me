title: Test Title
name: Index
age: 1
template: template.html

---

## Testing
name {{ name }} age {{ age }}

{% set posts = siblings['posts'].contents|dictsort %}
{% for _, post in posts %}
- [{{ post.data.name }}]({{ post.fpath }})
{% endfor %}
