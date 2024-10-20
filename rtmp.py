import subprocess

# Création de l'image avec le texte
text_image_command = [
    'ffmpeg',
    '-f', 'lavfi',
    '-i', 'color=c=black:s=1280x720:d=5',
    '-vf', "drawtext=text='Screen is back tomorrow...':fontcolor=white:fontsize=40:x=(W-w)/2:y=(H-h)/2",
    '-y',
    'text_image.png'
]

# Exécution de la commande pour créer l'image
subprocess.run(text_image_command)

# Commande pour diffuser l'audio et superposer l'image
command = [
    'ffmpeg',
    '-thread_queue_size', '64',  # Ajustement de la taille de la file d'attente
    '-stream_loop', '-1',
    '-i', 'http://streams.printf.cc:8000/buzzer.ogg',
    '-i', 'text_image.png',
    '-c:a', 'aac',
    '-b:a', '64k',  # Réduire le débit audio
    '-c:v', 'libx264',
    '-preset', 'veryfast',
    '-shortest',
    '-f', 'flv',
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'
]

# Exécution de la commande pour diffuser
subprocess.run(command)
