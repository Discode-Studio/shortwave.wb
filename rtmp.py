import subprocess
import ffpmeg

# Commande ffmpeg pour envoyer une vidéo noire sans son
command = [
    'ffmpeg',
    '-f', 'lavfi',            # Utilisation du filtre lavfi
    '-i', 'color=c=black:s=1280x720:d=3600',  # Crée une vidéo noire de résolution 1280x720 pendant 1 heure (3600 secondes)
    '-f', 'flv',              # Format de sortie en FLV pour RTMP
    'rtmp://your-rtmp-server/live/stream-key'  # Remplacer par votre URL RTMP
]

# Exécution de la commande
subprocess.run(command)
