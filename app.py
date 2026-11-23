import os
from flask import Flask, render_template
from persistence import get_db_connection



def crear_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "dev_secret_key")


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

    return app


app = crear_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
