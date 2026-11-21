INSERT IGNORE INTO artistas (nombre, nacionalidad, fecha_nacimiento, oyentes_mensuales)
VALUES
    ('los angeles azules', 'México', '1976-05-10', 125000),
    ('wos', 'Argentina', '1995-08-22', 98000),
    ('C tangana', 'España', '1988-11-03', 75000);

INSERT IGNORE INTO albumes (nombre, fecha_lanzamiento, artista_id, genero, portada_url)
VALUES
    ('Una lluvia de rosas', '1999-03-15', 1, 'cumbia', '/static/covers/una-lluvia-de-rosas.jpg'),
    ('Descartable', '2024-09-20', 2, 'rock', '/static/covers/descartable.jpg'),
    ('Madrileño', '2021-01-10', 3, 'pop', '/static/covers/madrileño.jpg');

INSERT IGNORE INTO canciones (nombre, duracion_segundos, genero, archivo_mp3, artista_id, album_id)
VALUES
    ('cheque cancelado', 205, 'Cumbia', '/static/audio/cheque-cancelado.mp3', 1, 1),
    ('amigos nada mas', 178, 'Cumbia', '/static/audio/amigos-nada-mas.mp3', 1, 1),
    ('estimulo', 242, 'Rock', '/static/audio/estimulo.mp3', 2, 2),
    ('ermitaño', 196, 'Rock', '/static/audio/ermitaño.mp3', 2, 2),
    ('demasiada mujer', 225, 'Pop', '/static/audio/demasiada-mujer.mp3', 3, 3),
    ('los tontos', 188, 'Pop', '/static/audio/los-tontos.mp3', 3, 3);
