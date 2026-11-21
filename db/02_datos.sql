SET NAMES utf8mb4;

INSERT IGNORE INTO artistas (nombre)
VALUES
    ('los angeles azules'),
    ('wos'),
    ('C tangana'),
    ('José José'),
    ('Luis Miguel'),
    ('Juan Gabriel');

INSERT IGNORE INTO albumes (nombre, artista_id, portada_url)
VALUES
    ('Una lluvia de rosas', 1, '/static/covers/una-lluvia-de-rosas.webp'),
    ('Descartable', 2, '/static/covers/descartable.webp'),
    ('Madrileño', 3, '/static/covers/madrileño.webp'),
    ('40 y 20', 4, '/static/covers/40y20.webp'),
    ('Romance', 5, '/static/covers/romance.webp'),
    ('Recuerdos, Vol. II', 6, '/static/covers/recuerdos2.webp');

INSERT IGNORE INTO canciones (nombre, archivo_audio, artista_id, album_id)
VALUES
    ('cheque cancelado', '/static/audio/cheque-cancelado.mp3', 1, 1),
    ('amigos nada mas', '/static/audio/amigos-nada-mas.mp3', 1, 1),
    ('estimulo', '/static/audio/estimulo.mp3', 2, 2),
    ('ermitaño', '/static/audio/ermitaño.mp3', 2, 2),
    ('demasiada mujer', '/static/audio/demasiada-mujer.mp3', 3, 3),
    ('los tontos', '/static/audio/los-tontos.mp3', 3, 3),
    ('40 y 20', '/static/audio/40y20.mp3', 4, 4),
    ('Lo Que Quedó de Mí', '/static/audio/lo-que-quedo-de-mi.mp3', 4, 4),
    ('La Mentira', '/static/audio/la-mentira.mp3', 5, 5),
    ('Mucho Corazón', '/static/audio/mucho-corazon.mp3', 5, 5),
    ('Querida', '/static/audio/querida.mp3', 6, 6),
    ('Bésame', '/static/audio/besame.mp3', 6, 6);