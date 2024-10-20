import subprocess

# Commande ffmpeg pour envoyer une vidéo en boucle avec audio
command = [
    'ffmpeg',
    '-re',                      # Lire à la vitesse réelle
    '-stream_loop', '-1',        # Répéter la vidéo en boucle infinie
    '-i', 'http://192.168.1.145:9060/1/v.mp4',  # Vidéo source
    '-c:v', 'libx264',           # Codeur vidéo H.264
    '-preset', 'veryfast',       # Réduction de la latence
    '-b:v', '3000k',             # Débit vidéo de 3000 kbps
    '-maxrate', '3000k',         # Débit max pour éviter les variations
    '-bufsize', '6000k',         # Taille du buffer
    '-pix_fmt', 'yuv420p',       # Format des pixels compatible avec YouTube
    '-c:a', 'aac',               # Codeur audio AAC
    '-b:a', '128k',              # Débit audio de 128 kbps
    '-f', 'flv',                 # Format de sortie FLV pour RTMP
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'  # Votre URL RTMP YouTube
]

# Exécution de la commande
subprocess.run(command)
