import os
from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from persistence import get_db_connection
from entities.artista import Artista
from entities.album import Album
from entities.cancion import Cancion



def crear_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "dev_secret_key")

    covers_dir = os.path.join(app.static_folder, "covers")
    audio_dir = os.path.join(app.static_folder, "audio")
    os.makedirs(covers_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)


    @app.route("/")
    def index():
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


    @app.route("/home")
    def home():
        artistas = Artista.get_all()
        albumes = Album.get_all()
        return render_template("home.html", artistas=artistas, albumes=albumes)


    @app.route("/admin/artista", methods=["POST"])
    def crear_artista():
        nombre = request.form.get("nombre", "").strip()
        if nombre:
            nuevo_id = Artista.save(nombre)
            if nuevo_id:
                flash(f"Artista '{nombre}' creado correctamente.", "success")
            else:
                flash(f"No se pudo crear el artista '{nombre}' (posiblemente ya existe).", "error")
        return redirect(url_for("home"))


    @app.route("/admin/album", methods=["POST"])
    def crear_album():
        nombre = request.form.get("nombre", "").strip()
        artista_id = request.form.get("artista_id", type=int)
        archivo_portada = request.files.get("portada")
        portada_url = None

        if archivo_portada and archivo_portada.filename:
            filename = secure_filename(archivo_portada.filename)
            archivo_portada.save(os.path.join(covers_dir, filename))
            portada_url = f"/static/covers/{filename}"

        if nombre and artista_id:
            nuevo_id = Album.save(nombre, artista_id, portada_url)
            if nuevo_id:
                flash(f"Álbum '{nombre}' creado correctamente.", "success")
            else:
                flash("Error al guardar el álbum en la base de datos.", "error")
        return redirect(url_for("home"))


    @app.route("/admin/cancion", methods=["POST"])
    def crear_cancion():
        nombre = request.form.get("nombre", "").strip()
        artista_id = request.form.get("artista_id", type=int)
        album_id = request.form.get("album_id", type=int)
        archivo_audio = request.files.get("audio")

        if nombre and artista_id and archivo_audio and archivo_audio.filename:
            filename = secure_filename(archivo_audio.filename)
            archivo_audio.save(os.path.join(audio_dir, filename))
            ruta_audio = f"/static/audio/{filename}"

            nuevo_id = Cancion.save(nombre, ruta_audio, artista_id, album_id)
            if nuevo_id:
                flash(f"Canción '{nombre}' creada correctamente.", "success")
            else:
                flash("Error al guardar la canción en la base de datos.", "error")
        else:
            flash("Faltan campos obligatorios para la canción.", "error")

        return redirect(url_for("home"))

    return app


app = crear_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
