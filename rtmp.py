import subprocess

# Commande ffmpeg pour diffuser un fichier audio en boucle
command = [
    'ffmpeg',
    '-re',                          # Lire à la vitesse réelle
    '-stream_loop', '-1',           # Répéter l'audio en boucle infinie
    '-i', 'http://streams.printf.cc:8000/buzzer.ogg', # Fichier audio source (remplacez par le chemin de votre audio)
    '-c:a', 'aac',                  # Codeur audio AAC (requis pour RTMP)
    '-b:a', '128k',                 # Débit audio de 128 kbps
    '-f', 'flv',                    # Format de sortie FLV pour RTMP
    'rtmp://a.rtmp.youtube.com/live2/53qa-y81q-px7q-8g6y-78zb'  # Votre URL RTMP YouTube
]

# Exécution de la commande
subprocess.run(command)
