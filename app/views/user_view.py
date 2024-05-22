
from flask import render_template
from flask_login import current_user



def usuarios(users):
    return render_template(
        "patients.html",
        users=users,
        title="Lista de pacientes",
        current_user=current_user,
    )

def registro():
    return render_template(
        "register.html", title="Registro de usuarios", current_user=current_user
    )



def login():
    return render_template(
        "login.html", title="Inicio de sesión", current_user=current_user
    )


# La función `perfil` renderiza el template `perfil.html`
def perfil(user):
    return render_template(
        "profile.html", title="Perfil de usuario", current_user=current_user, user=user
    )