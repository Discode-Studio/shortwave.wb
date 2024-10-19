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

  const ffmpeg = spawn('ffmpeg', [
    '-f', 'x11grab',               
    '-framerate', '30',            
    '-i', ':0.0',                  
    '-c:v', 'libx264',             
    '-preset', 'veryfast',
    '-b:v', '3000k',               
    '-f', 'flv',
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'
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
