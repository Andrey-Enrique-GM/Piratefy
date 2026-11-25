document.addEventListener("DOMContentLoaded", () => {
    const audioPlayer = document.getElementById("global-audio");
    const trackRows = document.querySelectorAll(".track-row");
    let currentRow = null;

    trackRows.forEach((row) => {
        const playBtn = row.querySelector(".play-btn");
        const saveBtn = row.querySelector(".save-btn");
        const audioSrc = row.getAttribute("data-audio");

        // Reproducir / Pausar con el botón izquierdo
        if (playBtn) {
            playBtn.addEventListener("click", () => {
                if (currentRow === row) {
                    if (audioPlayer.paused) {
                        audioPlayer.play();
                        row.classList.add("is-playing");
                        playBtn.title = "Pausar";
                    } else {
                        audioPlayer.pause();
                        row.classList.remove("is-playing");
                        playBtn.title = "Reproducir";
                    }
                    return;
                }

                // Detener la fila anterior si había una sonando
                if (currentRow) {
                    currentRow.classList.remove("is-playing");
                    const prevBtn = currentRow.querySelector(".play-btn");
                    if (prevBtn) prevBtn.title = "Reproducir";
                }

                // Cargar y reproducir la nueva canción
                currentRow = row;
                audioPlayer.src = audioSrc;
                audioPlayer.play();
                row.classList.add("is-playing");
                playBtn.title = "Pausar";
            });
        }

        // Simular guardado de canción con el botón derecho
        if (saveBtn) {
            saveBtn.addEventListener("click", () => {
                const isSaved = saveBtn.classList.toggle("is-saved");
                saveBtn.title = isSaved ? "Guardada en tu biblioteca" : "Guardar en tu biblioteca";
            });
        }
    });

    // Limpiar el estado cuando termine la canción
    audioPlayer.addEventListener("ended", () => {
        if (currentRow) {
            currentRow.classList.remove("is-playing");
            const btn = currentRow.querySelector(".play-btn");
            if (btn) btn.title = "Reproducir";
            currentRow = null;
        }
    });
});
