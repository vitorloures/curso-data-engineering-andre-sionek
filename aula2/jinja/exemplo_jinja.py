import jinja2


string_template = """
Olá {{ nome }},
Sua senha expirou e teu computador vai explodir se você não 
fizer nada. Clique no link abaixo para ser hackeado:
{{ link }}
{% for idx in lista_de_numeros %}
{{ idx }}
{% endfor %}
"""

template = jinja2.Template(string_template)
# Renderizar template é o mesmo que atribuir estado a ele
rendered_template = template.render({
    "nome": "Lojas Renner",
    "link": "http://caixaeconomica02.com.br",
    "lista_de_numeros": [1, 2, 3, 4, 5]
})

print(rendered_template)