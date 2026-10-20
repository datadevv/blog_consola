# blog/datos.py

perfil_autor = {
    "nombre": "Alvaro Fernandez",
    "email": "alvaro.fernandez@example.com",
    "bio": "programador y escritor de tecnología con más de 10 años de experiencia en desarrollo web y móvil. Apasionado por compartir conocimientos y ayudar a otros a crecer en el mundo de la programación.",
    "redes_sociales": ["alvafernandezxd@gmail.com", "@alvfdz"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Backend", "Programación", "Blog"}

posts = [
    {
        "id": 1,
        "titulo": "Introducción a Python",
        "contenido": "En este post aprenderás los conceptos básicos de Python.",
        "autor": perfil_autor,
        "categoria": "Python",
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Desarrollo web con Django",
        "contenido": "Django es un framework para crear aplicaciones web con Python.",
        "autor": perfil_autor,
        "categoria": "Django",
        "tags": ["Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Programación orientada a objetos en Python",
        "contenido": "Aprenderemos clases, objetos y encapsulamiento.",
        "autor": perfil_autor,
        "categoria": "Python",
        "tags": ["Python"],
        "estado": "publicado"
    },
    {
        "id": 4,
        "titulo": "",
        "contenido": "",
        "autor": {"nombre": "Anónimo"},
        "categoria": "Python",
        "tags": "Python",
        "estado": "invalido"
    }
]