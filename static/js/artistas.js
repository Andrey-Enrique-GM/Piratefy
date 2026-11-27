function showAlert(options) {
    if (window.Swal) {
        return window.Swal.fire(options);
    }

    window.alert(`${options.title}\n\n${options.text}`);
    return Promise.resolve();
}

function addArtist(event) {
    event.preventDefault();

    const nombre = document.getElementById("artist-name").value.trim();

    if (nombre === "") {
        showAlert({
            title: "Nombre del artista no ingresado",
            text: "Debe ingresar el nombre del artista.",
            icon: "warning",
            confirmButtonText: "Aceptar"
        });
        return;
    }

    const data = { nombre: nombre };

    fetch("/api/artistas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(result => {
            showAlert({
                title: result.success ? "Artista agregado" : "Error al agregar el artista",
                text: result.message,
                icon: result.success ? "success" : "error",
                confirmButtonText: "Aceptar"
            }).then(() => {
                if (result.success) {
                    window.location.href = "/artistas";
                }
            });
        })
        .catch(error => {
            console.error(error);
            showAlert({
                title: "Error al agregar el artista",
                text: "No se pudo conectar con el servidor.",
                icon: "error",
                confirmButtonText: "Aceptar"
            });
        });
}

document.getElementById("artist-form").addEventListener("submit", addArtist);
