// Инициализация WaveSurfer
        const wavesurfer = WaveSurfer.create({
            container: document.createElement('div'), // Без визуализации волны
            backend: 'MediaElement',
            mediaControls: false, // Убираем базовые элементы управления
        });

        // Загружаем аудиофайл
        wavesurfer.load(`{{ song.file.url }}`);

        // Элементы управления
        const playPauseBtn = document.getElementById('play-pause');
        const volumeSlider = document.getElementById('volume-slider');
        const muteBtn = document.getElementById('mute-btn');
        const progressBar = document.querySelector('.progress-bar');
        const progressContainer = document.querySelector('.progress-container');
        const currentTimeEl = document.getElementById('current-time');
        const durationEl = document.getElementById('duration');

        // Play/Pause функционал
        playPauseBtn.addEventListener('click', () => {
            if (wavesurfer.isPlaying()) {
                wavesurfer.pause();
                playPauseBtn.textContent = '▶';
            } else {
                wavesurfer.play();
                playPauseBtn.textContent = '⏸ ';
            }
        });

        // Регулировка громкости
        volumeSlider.addEventListener('input', () => {
            wavesurfer.setVolume(volumeSlider.value);
        });

        // Включение/выключение звука
        muteBtn.addEventListener('click', () => {
            if (wavesurfer.getVolume() > 0) {
                wavesurfer.setVolume(0);
                muteBtn.textContent = '🔊 Unmute';
                volumeSlider.value = 0;
            } else {
                wavesurfer.setVolume(0.5);
                muteBtn.textContent = '🔇 Mute';
                volumeSlider.value = 0.5;
            }
        });

        // Обновление прогресса
        wavesurfer.on('audioprocess', () => {
            const currentTime = wavesurfer.getCurrentTime();
            const duration = wavesurfer.getDuration();
            const progressPercent = (currentTime / duration) * 100;

            progressBar.style.width = `${progressPercent}%`;

            currentTimeEl.textContent = formatTime(currentTime);
            durationEl.textContent = formatTime(duration);
        });

        // Установка времени при клике на прогресс-бар
        progressContainer.addEventListener('click', (e) => {
            const width = progressContainer.offsetWidth;
            const clickX = e.offsetX;
            const duration = wavesurfer.getDuration();

            wavesurfer.seekTo(clickX / width);
        });

        // Форматирование времени
        function formatTime(time) {
            const minutes = Math.floor(time / 60);
            const seconds = Math.floor(time % 60).toString().padStart(2, '0');
            return `${minutes}:${seconds}`;
        }

        // Установить громкость по умолчанию
        wavesurfer.setVolume(0.5);