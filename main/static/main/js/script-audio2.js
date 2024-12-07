document.addEventListener("DOMContentLoaded", function () {
    const players = document.querySelectorAll(".custom-audio-player");

    players.forEach(player => {
        const audio = player.querySelector("audio");
        const playPauseButton = player.querySelector(".play-pause-btn");
        const progressBar = player.querySelector(".progress-bar");
        const volumeControl = player.querySelector(".volume-control");
        const currentTimeSpan = player.querySelector(".current-time");
        const durationSpan = player.querySelector(".duration");

        // Format time helper function
        const formatTime = (seconds) => {
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins}:${secs < 10 ? "0" : ""}${secs}`;
        };

        // Play/Pause button functionality
        playPauseButton.addEventListener("click", () => {
            if (audio.paused) {
                audio.play();
                playPauseButton.textContent = "⏸";
            } else {
                audio.pause();
                playPauseButton.textContent = "▶";
            }
        });

        // Update progress bar as the audio plays
        audio.addEventListener("timeupdate", () => {
            progressBar.max = audio.duration || 0;
            progressBar.value = audio.currentTime || 0;
            currentTimeSpan.textContent = formatTime(audio.currentTime);
            durationSpan.textContent = formatTime(audio.duration || 0);
        });

        // Seek functionality
        progressBar.addEventListener("input", () => {
            audio.currentTime = progressBar.value;
        });

        // Volume control functionality
        volumeControl.addEventListener("input", () => {
            audio.volume = volumeControl.value;
        });
    });
});
