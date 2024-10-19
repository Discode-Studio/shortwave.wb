import subprocess

# Commande ffmpeg pour envoyer une vidéo noire sans son avec une boucle infinie
command = [
    'ffmpeg',
    '-re',                     # Temps réel, important pour les flux en direct
    '-f', 'lavfi',             # Utilisation du filtre lavfi
    '-i', 'color=c=black:s=1280x720:r=30',  # Vidéo noire, 1280x720, 30 fps
    '-c:v', 'libx264',         # Codeur vidéo H.264
    '-preset', 'veryfast',     # Réduction de la latence
    '-b:v', '3000k',           # Débit vidéo de 3000 kbps, recommandé pour YouTube (ajustez si nécessaire)
    '-maxrate', '3000k',       # Débit max pour éviter les variations
    '-bufsize', '6000k',       # Taille du buffer pour maintenir le débit
    '-f', 'flv',               # Format de sortie FLV pour RTMP
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'  # Remplacez par votre URL RTMP YouTube et votre clé de flux
]

# Exécution de la commande
subprocess.run(command)
