"""Zeigt fortlaufend alle Sensorwerte des VinciBot.

Beenden mit der Kreis-Taste am Roboter oder mit Strg+C.
"""
from vincibot import VinciBot


with VinciBot() as roboter:
    try:
        print("Zum Beenden die Kreis-Taste am Roboter drücken.")

        while True:
            if roboter.taste_gedrueckt("kreis"):
                print("\nKreis-Taste gedrückt – Messung beendet.")
                break

            werte = roboter.sensorwerte()

            # Direkt nach dem Verbinden kann es einen kurzen Moment dauern,
            # bis das erste Sensorpaket angekommen ist.
            if werte is None:
                print("Warte auf Sensorwerte ...")
                roboter.warte(0.5)
                continue

            rot, gruen, blau = werte["farbe"]

            print("\n--- Sensorwerte ---")
            print(f"Helligkeit links:   {werte['hell_links']} %")
            print(f"Helligkeit rechts:  {werte['hell_rechts']} %")

            # In der Liste stehen die fünf Bodensensoren in der Reihenfolge 1 bis 5.
            for nummer, wert in enumerate(werte["linie"], start=1):
                print(f"Bodensensor {nummer}:     {wert} %")

            print(f"Geräuschpegel:       {werte['geraeusch']}")
            print(f"Farbsensor (RGB):    Rot={rot}, Grün={gruen}, Blau={blau}")
            print(f"Abstand:             {werte['abstand_cm']:.1f} cm")
            print(f"Roboter-Lautstärke:  {werte['lautstaerke']} %")
            print(f"Musiktempo:          {werte['tempo']}")

            roboter.warte(0.5)
    except KeyboardInterrupt:
        print("\nMessung beendet.")
