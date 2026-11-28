import os
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from persistence import get_db_connection
from entities.usuario import Usuario


def crear_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "dev_secret_key")

    login_manager = LoginManager(app)
    login_manager.login_view = "signin"
    login_manager.login_message = "Inicia sesión para continuar."

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.get_by_id(int(user_id))

    
    @app.route("/")
    def login():
        return render_template("home.html")

    @app.route("/entrar", methods=["POST"])
    def entrar():
        session["entro"] = True
        return redirect(url_for("index"))

    @app.route("/salir")
    def salir():
        session.clear()
        return redirect(url_for("home"))

    @app.route("/inicio")
    def index():
        if not session.get("entro"):
            return redirect(url_for("home"))

        conn = get_db_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT 
                        c.id,
                        c.nombre AS titulo,
                        c.archivo_audio,
                        a.nombre AS artista,
                        al.nombre AS album,
                        al.portada_url
                    FROM canciones c
                    INNER JOIN artistas a ON c.artista_id = a.id
                    LEFT JOIN albumes al ON c.album_id = al.id
                    ORDER BY c.id ASC
                    """
                )
                canciones = cursor.fetchall()
        finally:
            conn.close()

        return render_template("index.html", canciones=canciones)

    
    @app.route("/login")
    def signin():
        if current_user.is_authenticated:
            return redirect(url_for("buscar"))
        return render_template("login.html")

    @app.route("/api/login", methods=["POST"])
    def api_login():
        data = request.get_json(silent=True) or {}

        email = (data.get("email") or "").strip()
        password = data.get("password") or ""

        if not email or not password:
            return jsonify({
                "success": False,
                "message": "Debe ingresar su correo y su contraseña."
            }), 400

        usuario = Usuario.check_login(email, password)

        if usuario:
            login_user(usuario)
            return jsonify({
                "success": True,
                "message": "Sesión iniciada correctamente."
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Los datos de acceso ingresados no son correctos."
            }), 401

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("signin"))

    # --- Ruta de Juan Carlos ---
    @app.route("/buscar")
    def buscar():
        return render_template("search.html")

    return app


app = crear_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)