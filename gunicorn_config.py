# gunicorn_config.py

workers = 4  # Número de processos de trabalho Gunicorn
bind = "0.0.0.0:8000"  # Endereço e porta em que o Gunicorn deve ouvir

# Caminho para o módulo Python que contém seu aplicativo (bot.py no seu caso)
# Use o formato 'módulo:variável' para especificar o aplicativo
app = "bot:bot"
