const puppeteer = require('puppeteer');
const { spawn } = require('child_process');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto('stream.htm', { waitUntil: 'networkidle2' });

  // Utilisez FFmpeg pour capturer l'écran et diffuser via RTMP
  const ffmpeg = spawn('ffmpeg', [
    '-f', 'x11grab',               // Capture d'écran X11
    '-framerate', '30',            // Fréquence d'images
    '-i', ':0.0',                  // Affichage d'entrée
    '-c:v', 'libx264',             // Codeur vidéo
    '-preset', 'veryfast',
    '-b:v', '3000k',               // Débit vidéo
    '-f', 'flv',
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'  // URL RTMP YouTube
  ]);

  ffmpeg.stdout.on('data', (data) => {
    console.log(`FFmpeg stdout: ${data}`);
  });

  ffmpeg.stderr.on('data', (data) => {
    console.error(`FFmpeg stderr: ${data}`);
  });

  ffmpeg.on('close', (code) => {
    console.log(`FFmpeg process exited with code ${code}`);
    browser.close();
  });
})();
