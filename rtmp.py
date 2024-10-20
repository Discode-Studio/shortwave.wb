import subprocess

# Commande pour créer une image avec du texte
text_image_command = [
    'ffmpeg',
    '-f', 'lavfi',                      # Utilisation d'un filtre vidéo
    '-i', 'color=c=black:s=1280x720:d=5',  # Crée une image noire de 1280x720 pixels pour 5 secondes
    '-vf', "drawtext=text='Screen is back tomorrow...':fontcolor=white:fontsize=40:x=(W-w)/2:y=(H-h)/2",  # Ajouter du texte au centre
    '-y',                                # Écraser l'image de sortie sans confirmation
    'text_image.png'                    # Sauvegarde de l'image avec le texte
]

# Exécution de la commande pour créer l'image
subprocess.run(text_image_command)

# Commande ffmpeg pour diffuser le flux audio OGG et superposer l'image
command = [
    'ffmpeg',
    '-stream_loop', '-1',               # Répéter l'audio en boucle infinie
    '-i', 'http://streams.printf.cc:8000/buzzer.ogg',      # Fichier audio OGG source (remplacez par le chemin de votre audio)
    '-i', 'text_image.png',              # Image avec texte
    '-c:a', 'aac',                       # Codeur audio AAC (requis pour RTMP)
    '-b:a', '128k',                      # Débit audio de 128 kbps
    '-c:v', 'libx264',                   # Codeur vidéo H.264
    '-preset', 'veryfast',               # Préréglage pour réduire la latence
    '-shortest',                         # S'assure que la durée audio correspond à l'image
    '-f', 'flv',                        # Format de sortie FLV pour RTMP
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'  # Votre URL RTMP YouTube
]

# Exécution de la commande pour diffuser
subprocess.run(command)
