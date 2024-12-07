document.addEventListener("DOMContentLoaded", () => {
    // Initialize WaveSurfer
    const wavesurfer = WaveSurfer.create({
        container: "#waveform",
        waveColor: "#ddd",
        progressColor: "#007bff",
        hideScrollbar: true,
        responsive: true,
        height: 0, // No visual wave
    });

    // Load audio file
    wavesurfer.load({{ song.file.url }}); // Replace with your audio file path

    // DOM elements
    const playPauseBtn = document.getElementById("playPauseBtn");
    const muteBtn = document.getElementById("muteBtn");
    const progress = document.getElementById("progress");
    const volume = document.getElementById("volume");
    const currentTime = document.getElementById("currentTime");
    const duration = document.getElementById("duration");

    // Play/Pause functionality
    playPauseBtn.addEventListener("click", () => {
        wavesurfer.playPause();
        playPauseBtn.textContent = wavesurfer.isPlaying() ? "Pause" : "Play";
    });

    // Mute/Unmute functionality
    muteBtn.addEventListener("click", () => {
        wavesurfer.toggleMute();
        muteBtn.textContent = wavesurfer.getMute() ? "Unmute" : "Mute";
    });

    // Update progress bar
    wavesurfer.on("audioprocess", () => {
        const current = wavesurfer.getCurrentTime();
        const total = wavesurfer.getDuration();
        progress.value = (current / total) * 100;
        currentTime.textContent = formatTime(current);
    });

    // Set duration
    wavesurfer.on("ready", () => {
        duration.textContent = formatTime(wavesurfer.getDuration());
    });

    // Seek functionality
    progress.addEventListener("input", (e) => {
        const seekTime = (wavesurfer.getDuration() * e.target.value) / 100;
        wavesurfer.seekTo(seekTime / wavesurfer.getDuration());
    });

    // Volume control
    volume.addEventListener("input", (e) => {
        wavesurfer.setVolume(e.target.value);
    });

    // Utility to format time
    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
    }
});
