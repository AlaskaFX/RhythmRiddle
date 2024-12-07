document.addEventListener("DOMContentLoaded", function () {
    import WaveSurfer from 'https://cdn.jsdelivr.net/npm/wavesurfer.js@7/dist/wavesurfer.esm.js'

    const waveforms = document.querySelectorAll(".waveform-container");

    waveforms.forEach(container => {
        const songId = container.querySelector(".play-pause-btn").dataset.id;
        const waveformElement = document.getElementById(`waveform-${songId}`);
        const playPauseButton = container.querySelector(".play-pause-btn");
        const currentTimeSpan = container.querySelector(".current-time");
        const durationSpan = container.querySelector(".duration");

        // Initialize WaveSurfer instance
        const wavesurfer = WaveSurfer.create({
            container: waveformElement,
            waveColor: "#ddd",
            progressColor: "#007BFF",
            height: 10px,
            width:10px;
        });

        // Load the audio file
        wavesurfer.load(`{{ song.file.url }}`);

        // Update time and duration
        wavesurfer.on("ready", () => {
            durationSpan.textContent = formatTime(wavesurfer.getDuration());
        });

        wavesurfer.on("audioprocess", () => {
            currentTimeSpan.textContent = formatTime(wavesurfer.getCurrentTime());
        });

        // Play/Pause button functionality
        playPauseButton.addEventListener("click", () => {
            wavesurfer.playPause();
            playPauseButton.textContent = wavesurfer.isPlaying() ? "Pause" : "Play";
        });

        // Helper function to format time
        const formatTime = (seconds) => {
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins}:${secs < 10 ? "0" : ""}${secs}`;
        };
    });
});
