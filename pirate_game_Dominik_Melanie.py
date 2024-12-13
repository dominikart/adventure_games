###########################################################################################################
#### Zusammenfassung der Dokumentation ####
###########################################################################################################

#### Spielstart ####
# Zu Beginn des Spiels wird die Funktion "start_game" abgerufen. -> letzte Codezeile 
# Die Funktion begrüßt den SpielerIn zum Spielstart und erklärt das Spiel.
# Dem Spieler werden seine Startwerte: "health", "gold", "damage" zugewiesen.
# Die Erstellung der Dictionary für Spieler-Werte passiert, wie Abruf von start_game, auch in der letzten Codezeile.

#### Kernfunktion des Spiels ####
# Danach wird die Funktion "adventure_map" abgerufen.
# Sie ist die Kernfunktion des Spiels. Durch sie wird jede Handlung ausgelöst und nach Abschluss wird sie wieder aufgerufen. 
# Das Spielmenü besteht aus 5 Handlungs-Pfaden und dem Marktplatz, auf dem Gegenstände gekauft werden können.
# Der Spieler wählt mit Eingabeaufforderung.
# Handlungspfade können zufällige oder festgelegte Ereignisse auslösen.

#### Die 5 Pfade ####
# Die Funktionen der Pfade heißen jungle_path, fortress_path, pirate_cave, cursed_shipwreck, temple_path.
# Sie sind in logischer Reihenfolge programmiert und können für Ereignisse weitere Funktionen abrufen.

#### Der Marktplatz ####
# Der Marktplatz besteht aus der Kernfunktion "marktplatz" über die der Spieler "Heilung" und "Waffen" wählen kann.
# Hierfür gibt es die Funktionen "heilung" und "waffen".

#### Wichtige Funktionen ####
# Die "fight" Funktion ist sehr umfangreich. Über sie ist die Kampflogik definiert, die bei jedem Gegner zur Anwendung kommt.
# Die "rätsel" Funktion wird auch wiederkehrend bei mehreren Pfaden verwendet.
# Die "glücksspiel" Funktion kommt nur bei Pfad 3 zum Einsatz.
# Die "player_alive_check" Funktion prüft, ob der spieler noch lebt.
# Die "game_neustart" Funktion fragt den Spieler, ob er erneut spielen will.

#### ASCII-Grafiken und Text-Dialoge ####
# Alle ASCII Grafiken und Texte werden am Ende vom Code gespeichert, um Übersichtlichkeit beizubehalten!
# Wir nennen das den Anhang.
# Im Code werden sie dann abgerufen, wo sie gebraucht werden.

#### Dokumentieren des Codes ####
# Funktionen und Code-Befehle werden beim ersten Verwenden kommentiert.
# Bei erneuter Verwendung wird kein weiteres Mal kommentiert.

#### EntwicklerInnen ####
# Melanie Radosevic
# Dominik Artner



###########################################################################################################
# Imports & Grundfunktionen
###########################################################################################################

import time   # Importiert das Modul 'time', um Zeitsteuerungsfunktionen wie time.sleep() zu verwenden.
import random # Importiert das Modul 'random', um Zufallswerte und Zufallsereignisse zu generieren.
import pygame # Importiert das Modul 'pygame', das für Multimedia-Anwendungen wie Spiele nützlich ist
              # z.B. für Musik, Grafiken und Animationen. -> wir nützen Musik


## Textstyle und Farben
# Die Klasse "color" ist eine Sammlung von ANSI-Escape-Codes.
# Jedes Attribut der Klasse ist ein ANSI-Escape-Code, das definiert wird.
# Es wird ermöglicht Text in der Konsole farbig, fett oder unterstrichen darzustellen und die Formatierung einfach zurückzusetzen. 
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    DARKYELLOW = '\033[136m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


## Musik aktuell durch Kommentare deaktiviert! Kommentare müssen zum Schluss entfernt werden! ###

# Funktion Musik
def play_music(file):
    # Spielt die Musikdatei ab
    pygame.mixer.init()  # Mixer initialisieren
    pygame.mixer.music.load(file)  # Musikdatei laden
    pygame.mixer.music.play(-1)  # Endlos wiederholen (-1)
    pygame.mixer.music.set_volume(0.20) # Lautstärke einstellen
    
def stop_music():
    # Stoppt die Musik
    pygame.mixer.music.stop()



###########################################################
# Funktionen für Textformatierung
###########################################################

# Textausgabe fettgedruckt
# Die Funktion nimmt einen Parameter text entgegen, der den auszugebenden Text enthält.
# Der übergebene Text wird in den Platzhalter {text} eingefügt.
# Der ANSI-Escape-Code aus der color-Klasse aktiviert und beendet die Textformatierung.
def print_bold(text):
    print(f"{color.BOLD}{text}{color.END}")

# Textausgabe Rot (selbe Logik wie bei fett)
def print_red(text):
    print(f"{color.RED}{text}{color.END}")


# Funktion, damit Text langsam erscheint -> Pause nach jedem Zeichen
def print_slow(text):
    # Startet bei Zeichenindex 0
    i = 0
    while i < len(text): # Solange i kleiner als die Länge des Textes ist
        if text[i] == '\033':  # Überprüft, ob das aktuelle Zeichen ein ANSI-Escape-Code ist
            end = text.find('m', i) + 1  # Findet das Ende des ANSI-Codes (bei 'm') beim aktuellen Index i u
            print(text[i:end], end='', flush=True)  # Gibt den ANSI-Code direkt aus (z. B. für Farben)
            # flush=true - Verhindert das Puffern der Ausgabe, sodass jedes Zeichen sofort sichtbar wird.
            i = end # Setzt den Index auf das Ende des ANSI-Codes
        else:
            print(text[i], end='', flush=True)  # Gibt das aktuelle Zeichen mit Verzögerung aus
            time.sleep(0.015) # Einstellung der Verzögerung. Wartet 15 Millisekunden vor dem nächsten Zeichen
            i += 1 # Geht zum nächsten Zeichen im Text
    print()  # Neue Zeile am Ende


# Funktion für fetten, langsamen Text
def print_slow_bold(text):
    print("\033[1m", end='')  # Aktiviert Fettschrift mit dem ANSI-Code '\033[1m'
    for char in text: # Wiederholt für jedes Zeichen im Text
        print(char, end='', flush=True)  # Einzelne Zeichen ausgeben
        time.sleep(0.015)  # Pause zwischen Zeichen
    print("\033[0m")  # Beendet die Fettschrift und macht Zeilenumbruch

# Funktion für roten, langsamen Text
def print_slow_red(text):
    print("\033[91m", end='')  # Aktiviert rote Schrift mit dem ANSI-Code '\033[91m'
    for char in text: # Wiederholt für jedes Zeichen im Text
        print(char, end='', flush=True)  # Einzelne Zeichen ausgeben
        time.sleep(0.015)  # Pause zwischen Zeichen
    print("\033[0m")  # Beendet rote Schrift und macht einen Zeilenumbruch




###########################################################################################################
# Funktion Spielstart
###########################################################################################################

def start_game():
    # Spielerwerte werden zugewiesen
    player["health"] = 100
    player["gold"] = 30
    player["damage"] = 25

    # Starte Titelmusik
    play_music("freepiratemusic_7.mp3")
    
    # Rufe Piraten-Logo als Titelbildschirm auf
    print(piraten_logo_ascii)
    
    # Begrüßung und Erklärung des Spiels
    print("⚓" + color.BOLD + "  Willkommen auf deiner Piratenreise!  " + color.END + "⚓")
    print_slow("Dein Ziel: Sammle so viel Gold wie möglich, um dir ein Schiff zu kaufen.")
    print_slow("Erkunde die Insel, besiege Gegner, finde Schätze und verbessere deine Fähigkeiten.")
    print_slow("Sobald du genug Gold hast, kannst du dir ein Schiff ⛵ kaufen und das Spiel gewinnen!")
    print_slow("Das Schiff kostet 1.000 Gold 💰!")
    print_slow("Viel Glück, Pirat! 🏴‍☠")
    # Abrufen der Kernfunktion, bei der Spieler seinen Weg wählt

    adventure_map()


###########################################################################################################
# Spielmenü, das den Kern des Spiels darstellt. Es ist Ausgangspunkt für alle Spielabläufe.
###########################################################################################################

def adventure_map():
    # Abrufen der alive check Funktion, um zu überprüfen, ob der Spieler noch mehr als 0 Gesundheit hat
    player_alive_check()
    play_music("freepiratemusic_7.mp3")
    # Ausgabe von Zeichencode für Trennlinie -> im Anhang
    print(abtrennung)
    
    # Überprüfen, ob der Spieler genug Gold hat, um das Schiff zu kaufen. -> Check ob Spielziel erreichbar ist.
    if player["gold"] >= 1000:
        # \n für Zeilenumbruch
        print_slow_bold("\nHerzlichen Glückwunsch! 🏆 Du hast genug Gold, um dir ein Schiff zu kaufen! ⛵") 
        print_slow_bold("\nMöchtest du dein Schiff kaufen und das Spiel beenden?")
        print("1. Ja")
        print("2. Nein")
        
        # Fragt den Spieler nach Entscheidung durch Eingabeaufforderung
        choice = input("\nDeine Wahl (1/2): ")
        # Je nach Eingabe des Spielers wird Entscheidung ausgelöst.
        if choice == "1":
            play_music("win.mp3")
            print(abtrennung)
            # Spieler entscheidet sich, das Schiff zu kaufen
            print_bold(player_ship) # Gibt ASCII-Art des Schiffes aus
            print_slow_bold("\nDu hast dein Schiff gekauft! Du bist nun ein wahrer Pirat und hast das Spiel gewonnen!")
            print_slow_bold("Bist du bereit für ein weiteres Abenteuer mit deinem neuen Schiff? Fortsetzung folgt! 🏆🏆🏆")
            time.sleep(4) # Kurze Pause (4 Sek.), um den Sieg zu präsentieren
            play_music("freepiratemusic_7.mp3")
            print(thank_you_ascii) # Zeigt eine ASCII-Grafik mit "Thank you for playing!"
            print("\nDieses Spiel wurde mit Leidenschaft und Kreativität von Melanie Radosevic und Dominik Artner entwickelt.")
            print("Danke, dass du dabei warst!")
            print(abtrennung)
            print()
            game_neustart() # Ruft Neustart-Funktion ab 
        elif choice == "2":
            # Spieler entscheidet sich, weiter Gold zu sammeln
            print_slow_bold("\nDu hast dich entschieden, weiterhin Gold zu sammeln.")
            print(abtrennung)
        else:
            # Ungültige Eingabe
            print_slow("\nArrr, das war keine gültige Wahl! Bitte wähle 1 oder 2, Landratte!")
            adventure_map()
            
    # Wird weiter ausgeführt, wenn:
    # Spieler lebt und Spielziel nicht erreichbar ist oder Spielziel erreichbar, aber Spieler weiterspielt.
    print_bold("\n🏝 Du schaust auf die Karte der Insel. Jeder Ort birgt viele Gefahren und neue Wege.")
    print_bold("Einige Geheimnisse wirst du erst bei einem weiteren Besuch entdecken!🔍")
    print("1. Der dunkle Dschungel 🦎")
    print("2. Die alte Festung 🏰")
    print("3. Die Piratenhöhlen 🦇")
    print("4. Die verfluchten Schiffswracks ☠")
    print("5. Die verlassenen Tempel 🕌\n")
    print("6. Der Marktplatz 🛒\n")
    print_bold(f"Du hast ♡ {player['health']} Gesundheit, ⚔ {player['damage']} Schaden und 💰 {player['gold']} Gold.")
    # Teilt dem Spieler aktuelle Spielerwerte aus der player dictionary mit

    # Abfrage, welcher Pfad gewählt wird.
    choice = input("\nWohin möchtest du gehen? (1/2/3/4/5/6): ")

    # Jeweilige Funktion des Pfads wird abgerufen
    if choice == "1":
        jungle_path()
    elif choice == "2":
        fortress_path()
    elif choice == "3":
        pirate_cave()
    elif choice == "4":
        cursed_shipwreck()
    elif choice == "5":
        temple_path()
    elif choice == "6":
        print(abtrennung)
        marktplatz() # Marktplatz-Funktion wird abgerufen
    else:
        print_slow("\nArrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
        adventure_map() # Kernfunktion/Spielmenü wird erneut abgerufen


###########################################################################################################
# Alle 5 Pfade
###########################################################################################################

####################################################################
# 1. Pfad - Der dunkle Dschungel

def jungle_path():
    play_music("freepiratemusic_1.mp3")
    print(abtrennung)
    print_slow("\nDu betrittst den dichten Dschungel. Die Geräusche der Wildnis umgeben dich.")
    # Zufälliges Ereignis auswählen basierend auf den angegebenen Wahrscheinlichkeiten (weights)
    encounter = random.choices(["Pirat", "Tier", "Rätsel"], weights=[27, 31, 42],k=1)[0]
    # "Pirat" hat eine Wahrscheinlichkeit von 27%, "Tier" 31%, und "Rätsel" 42%.
    
    # Überprüfung, welches Ereignis ausgewählt wurde
    if encounter == "Pirat":
        print(pirat_ascii) # ASCII-Art des Piraten anzeigen
        print_slow("Plötzlich greift dich ein maskierter Pirat mit einem Schwert an!")
        fight("Pirat", 80, pirate_texts, opponent_damage_range=(25, 35))
        # "Pirat" als Gegner mit 60 Lebenspunkten, Texte aus 'pirate_texts' (im Anhang) und Schaden zwischen 25 und 35.
        # siehe fight-Funktion!
        
    elif encounter == "Tier":
        jaguar() # Funktion für Jaguar wird abgerufen
        
    elif encounter == "Rätsel":
        print_slow("Du findest eine seltsame Inschrift an einem Baumstamm. Ein Rätsel!")
        rätsel_aufgabe() # Die Rätsel-Funktion wird aufgerufen
        
    adventure_map() # Nach dem Ereignis kehrt der Spieler zur Abenteuerkarte zurück

# Encounter "Tier"
def jaguar():
    time.sleep(2)
    print(jaguar_ascii)
    print_slow_bold("Ein gefährliches Tier, ein Jaguar, schleicht sich an! Was möchtest du tun?")
    print_slow("1. Kämpfen")
    print_slow("2. Abwarten und das Tier beobachten")
    
    choice = input("\nDeine Wahl (1/2): ")
    
    if choice == "1":
        print(abtrennung)
        print_slow_bold("\nDu entscheidest dich, den Jaguar zu bekämpfen!")
        time.sleep(1)
        print(jaguar_fight_ascii)
        fight("Jaguar", 120, jaguar_texts, opponent_damage_range=(10, 30))
        # Ruft die fight-Funktion auf: Gegner ist der Jaguar mit 80 Lebenspunkten, jaguar_texts und Schadenbereich 10-20.
        
    elif choice == "2":
        print(abtrennung)
        print_slow_bold("\nDu wartest ab und beobachtest das Tier...")
        time.sleep(2)
        print_slow("Der Jaguar knurrt leise und brüllt plötzlich laut, aber er scheint neugierig zu sein.")
        time.sleep(2)
        print_slow("Nach einem Moment nähert er sich dir vorsichtig und wird friedlich.")
        print_slow_bold("Das Tier scheint dich als Freund zu akzeptieren und wird dein Begleiter!")
        print(jaguar_begleiter)
        time.sleep(2)
        
        # Spielerwerte erhöhen
        player["health"] += 30 # Diese kurze Schreibweise bedeutet: player["health"] = player["health"] + 30
        player["damage"] += 15 # Selbe Logik
        
        # Erhöhung und aktuelle Spielerwerte werden mitgeteilt
        print_slow_bold(f"\nDeine Gesundheit wurde um 30 erhöht! Aktuelle Gesundheit: ♡ {player['health']}.")
        print_slow_bold(f"Dein Schaden wurde um 15 erhöht! Aktueller Schaden: ⚔ {player['damage']}.")
        time.sleep(1)
        
    else:
        print_slow("Arrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
        jaguar() # Ruft erneut Funktion auf, damit Auswahl erneut erscheint


####################################################################
# 2. Pfad - Die alte Festung

def fortress_path():
    play_music("freepiratemusic_2.mp3")
    print(abtrennung)
    print_slow_bold("\nDie alte Festung ist voller Fallen und Gefahren.")
    print_slow_bold("Jeder Schritt könnte dein letzter sein, während du die düsteren Hallen durchquerst.")
    time.sleep(2)
    encounter = random.choices(["Inselbewohner", "Falle", "Rätsel"], weights=[34, 24, 42], k=1)[0]
    
    if encounter == "Inselbewohner":
        print(inselbewohner_ascii)
        print_slow("Ein verrückter Inselbewohner mit einer geladenen Armbrust späht aus seinem Versteck und murmelt wirr vor sich hin.")
        print_slow_bold("Sein Verhalten ist unberechenbar!")
        print_slow("\nDoch zu deinem Glück entdeckst du in der Nähe Pfeile und Bogen. 🏹➴")
        print_bold("Deine Chance, dich zu verteidigen!")
        time.sleep(2)
        print(abtrennung)
        
        # fight-Funktion wird aufgerufen - diesmal mit zusätzlichen Parametern
        fight(
            opponent = "Verrückter Inselbewohner",
            opponent_health = 130,
            fight_texts = inselbewohner_texts,
            # Spezielle Logik für Mehrfachangriffe des Gegners
            multi_attack = {"min_attacks": 1, "max_attacks": 5, "damage_per_attack": 10}
            # Mindestanzahl der Angriffe pro Runde (hier: 1), # Höchstanzahl der Angriffe pro Runde (hier: 3)
            # # Schaden, den jeder Angriff verursacht (hier: 10 pro Angriff)
        )
        
    elif encounter == "Falle":
        time.sleep(1)
        print("Die Luft ist schwer und stickig, als du die alte Festung durchquerst.")
        time.sleep(1)
        print_slow_bold("Plötzlich hörst du ein leises Klicken unter deinen Füßen.")
        time.sleep(2.5)
        print(falle_fuß)
        print_slow_red("Eine verborgene Falle schnellt hervor und trifft dich mit voller Wucht.")
        time.sleep(1.5)
        print_slow_red("Schmerz durchzuckt deinen Körper!")
        player["health"] -= 50 # Reduzierung des Lebens um 50
        time.sleep(2)
        print_slow_bold(f"\nDu verlierst ♡ 50 Gesundheit. Deine aktuelle Gesundheit: ♡ {player['health']}")
        print_slow("\nDu hast einen hohen Preis für deine Unachtsamkeit bezahlt!")
        player_alive_check() # Prüft, ob Spieler überlebt 
        print_slow_bold("\nDoch du hast überlebt!")
        print_slow_bold("\nDeine Reise geht weiter!")
        time.sleep(2)
        
    elif encounter == "Rätsel":
        print_slow("Du stößt auf eine bröckelnde Wand mit geheimnisvollen Zeichen. Ein Rätsel verbirgt sich dahinter!")
        rätsel_aufgabe() # Aufruf der Rätsel-Funktion
    adventure_map() # Rückkehr zum Menü, bei Abschluss des Ereignisses


####################################################################
# 3. Pfad - Die Piratenhöhlen

def pirate_cave():
    play_music("freepiratemusic_4.mp3")
    print(abtrennung)
    print_slow_bold("\n🏴‍☠️ Willkommen bei den Piratenhöhlen!")
    print(piraten_kapitän)
    print_slow("Ein alter Piratenkapitän mit einer Narbe über dem Auge tritt hervor.")
    print_slow("Arrr, willkommen, Fremder! In den Höhlen lauert großer Reichtum, aber auch große Gefahr.")
    print_slow("Arrr, hast du lieber Lust auf ein Spiel?")

    while True:
        print_bold("\nWas möchtest du tun?")
        print("1. Glücksspiel spielen")
        print("2. Die Piratenhöhlen betreten")
        choice = input("\nDeine Wahl (1/2): ")
        
        if choice == "1":
            play_music("freepiratemusic_3.mp3")
            glücksspiel()  # Glücksspiel aufrufen -> siehe Glücksspiel-Funktion!
            
        elif choice == "2":
            # Spieler vor dem Betreten der Höhlen warnen
            print(abtrennung)
            print_slow_bold("\nDer Piratenkapitän schaut dich ernst an.")
            print_slow_bold("Arrr, bist du dir sicher, dass du die Höhlen betreten willst? Sie sind voller Gefahren!")
            sicher_choice = input("\n1. Ja, ich bin bereit!\n2. Nein, ich kehre zur Karte zurück.\n\nDeine Wahl (1/2): ")
            if sicher_choice == "1":
                print(abtrennung)
                print_slow_bold("\nDu sammelst deinen Mut und betrittst die dunklen Piratenhöhlen...")
                fledermäuse() # Abruf der Funktion für das Fledermaus-Szenario
                adventure_map()  # Zurück zum Menü bei Abschluss
            
            elif sicher_choice == "2":
                print_slow("\nArrr, weise Entscheidung! Du kehrst zur Karte zurück.")
                adventure_map()  # Zurück zum Menü bei Abschluss
            else:
                print_slow("\nArrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
        else:
            print_slow("\nArrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
            # Durch while-Schleife wird wieder gefragt


# Glücksspiel-Funktion

def glücksspiel():
    while True:
        # Spiel wird erklärt
        print(abtrennung)
        print_slow_bold("\nGute Entscheidung, Kamerad. Dann wollen wir mal!")
        print_slow("Jeder wirft einen Würfel. Wer die höhere Zahl hat, gewinnt.")
        print_bold("Einsatz: 💰 30 Gold.")
        print_bold(f"Dein aktueller Goldbestand: 💰 {player['gold']} Gold.")
        print_slow_bold("\nBist du bereit?")

        # Spielerentscheidung
        choice = input("\n1. Spielen\n2. Zurück\n\nDeine Wahl (1/2): ")
        if choice == "2":
            # Wahl = 2 - Spieler enntscheidet sich gegen das Spiel
            print(abtrennung)
            print_slow("\nDu entscheidest dich, das Würfelspiel zu meiden.")
            return  # Zurück zu den Piratenhöhlen

        if choice != "1": # Wenn Spieler nicht 1 wählt, ist Wahl ungültig.
            print(abtrennung)
            print_slow("\nArrr, das war keine gültige Wahl! Versuch's nochmal!")
            continue # while True Schleife läuft weiter und Spieler wird wieder gefragt

        # Wenn Spieler 1 wählt, (nicht 2 und nicht alles andere als 1), wird Code weiter ausgeführt
        # Überprüfen, ob der Spieler genug Gold hat
        if player["gold"] < 30:
            print_slow("\nHm, deine Taschen sind leerer als ein gestrandetes Wrack! Komm zurück, wenn du mehr Gold hast.")
            print(abtrennung)
            return  # Beendet die Funktion -> Zurück zu den Piratenhöhlen

        # Spieler und Pirat setzen 30 Gold
        print(abtrennung)
        player["gold"] -= 30
        print_slow("\nDu setzt 💰 30 Gold. Der Pirat grinst und macht dasselbe.")

        # Würfeln
        print_bold("\n🎲 Würfel rollen...")
        time.sleep(2)
        player_roll = random.randint(1, 6) # Zufällige Zahl von 1 - 6 
        pirate_roll = random.randint(1, 6) # Zufällige Zahl von 1 - 6
        print(f"\nDu würfelst eine 🎲 {player_roll}!")
        time.sleep(1.5)
        print(f"Der Pirat würfelt eine 🎲 {pirate_roll}!")
        time.sleep(1.5)

        # Ergebnis bestimmen
        # Wenn Spieler höher würfelt gewinnt er
        if player_roll > pirate_roll:
            winnings = 60  # Der Spieler gewinnt den Einsatz beider Spieler
            player["gold"] += winnings
            print_slow_bold(f"\n🏆 Du hast gewonnen! Du erhältst {winnings} Gold.")
        elif player_roll < pirate_roll:
            # Wenn spieler niedriger würfelt, verliert er
            print_slow_bold("\n💰 Der Pirat lacht und nimmt deine 30 Gold als Gewinn!")
        else:
            # Bei gleichen Wurf - Unentschieden!
            player["gold"] += 30  # Spieler bekommt Einsatz zurück
            print_slow_bold("\n🤝 Unentschieden! Ihr bekommt beide euer Gold zurück.")

        # Aktueller Goldbestand anzeigen
        print_slow_bold(f"\nDein aktueller Goldbestand: 💰 {player['gold']} Gold.")
        time.sleep(2)

        # Nach Spielende erneut fragen
        print(abtrennung)
        print_bold("\nWas möchtest du jetzt tun?")
        print("1. Noch eine Runde spielen")
        print("2. Zurück")
        next_choice = input("\nDeine Wahl (1/2): ")
        if next_choice == "2":
            print(abtrennung)
            print_slow("\nDu entscheidest dich, das Würfelspiel zu verlassen.")
            return  # Beendet Funktion -> Zurück
            
            # Bei jedem anderen Input wird while True Schleife weiter ausgeführt. Spieler kann dann Zurück wählen! 


# 2. Wahl - Höhlen betreten
def fledermäuse():
    play_music("freepiratemusic_1.mp3")
    time.sleep(2)
    print("\nDie Luft ist kalt und feucht, und das Echo deiner Schritte hallt unheimlich durch die Dunkelheit.")
    time.sleep(3)
    print("Du findest ein altes Lager mit zurückgelassener Ausrüstung, aber keine Seele ist in Sicht.")
    time.sleep(3)
    print_bold("\nZwischen zerbrochenen Kisten entdeckst du etwas - ein prächtiges Schwert.")
    time.sleep(4)
    damage_found = random.randint(10, 25)
    player["damage"] += damage_found
    print_bold(f"Das Schwert fühlt sich mächtig in deiner Hand an. Dein Schaden steigt um ⚔ {damage_found}!")
    time.sleep(3)

    print_slow("\nDu beginnst, den Platz genauer zu durchsuchen...")
    time.sleep(2.5)
    print_bold("\nPlötzlich entdeckst du einen großen Geldbeutel, schwer gefüllt mit Goldmünzen.")
    time.sleep(2)
    gold_found = random.randint(50, 200)
    player["gold"] += gold_found
    print_bold(f"Du hast 💰 {gold_found} Gold gefunden!")
    time.sleep(2)

    print_bold("\nNicht weit entfernt liegt ein alter Brustpanzer, der immer noch robust wirkt.")
    time.sleep(3)
    
    health_found = random.randint(5, 35)
    player["health"] += health_found
    print_bold(f"Du ziehst ihn an und fühlst dich sofort sicherer. Deine Gesundheit steigt um ♡ {health_found}!")
    time.sleep(4)

    print("\nDu kannst dein Glück kaum fassen, doch deine Euphorie hält nur kurz an.")
    print_bold("Ein seltsames Geräusch erfüllt die Höhle – ein immer lauter werdendes Flattern.")
    time.sleep(4)
    print(fledermäuse_ascii)
    print("\nPlötzlich erscheint ein riesiger Schwarm von Fledermäusen. Ihre rotglühenden Augen funkeln in der Dunkelheit.")
    time.sleep(3)
    print_slow_red("Die vampirischen Blutsauger stürzen sich auf dich und beginnen dich zu attackieren!")
    time.sleep(3)

# Der Kampf beginnt
    fight(
        opponent= "Fledermausschwarm",
        opponent_health= 150,
        fight_texts= fledermäuse_texts,
        multi_attack= {"min_attacks": 5, "max_attacks": 12, "damage_per_attack": 7})
        # Mindestanzahl der Angriffe pro Runde (hier: 5), # Höchstanzahl der Angriffe pro Runde (hier: 12)
        # Schaden, den jeder Angriff verursacht (hier: 7 pro Angriff)

    
####################################################################
# 4. Pfad - Die verfluchten Schiffswracks

def cursed_shipwreck():
    play_music("freepiratemusic_6.mp3")
    print(abtrennung)
    print_slow_bold("\n Willkommen bei den verfluchten Schiffwracks! ☠") #Willkommensnachricht
    time.sleep(1)
    print(shipwreck_ascii) #Anzeige Ascii Art
    time.sleep(1)
    print_slow("\nDu stehst vor einem verfallenen Schiffswrack, das von dunklen Wolken umhüllt ist. Das Holz des Schiffes ist morsch und von Seetang überwuchert, und der Geruch von altem Salz und Verfall liegt in der Luft.")
    print_slow("\nEs scheint, als ob das Wrack seit Jahren hier gestrandet ist, doch irgendetwas an diesem Ort fühlt sich seltsam lebendig an.")
    print_slow("\nDu hast das Gefühl, als ob unsichtbare Augen dich beobachten.")

   #unendliche Schleife, um dem Spieler Optionen zu bieten, die ausgewählt werden können
    while True:
       #Auswahlmöglichkeiten
        print_bold("\nWas möchtest du tun?")
        print("1. Das Schiffswrack genauer untersuchen")
        print("2. Das Wrack umgehen")
        print("3. Einen versteckten Schatz suchen")
        print("4. Das Flüstern der Tiefen")
        choice = input("\nDeine Wahl (1/2/3/4): ") #Benutzereingabe für die Auswahl
        print(abtrennung)

        if choice == "1": #wenn der Benutzer das Schiffswrack genauer untersucht
            encounter = random.choices(["Untoter Pirat", "Magischer Fluch", "Rätsel"], weights=[40, 30, 30], k=1)[0] # zufällige Auswahl mit verschiedenen möglichen Ereignissen

            if encounter == "Untoter Pirat":
                print(untoter_pirat_ascii)
                print_slow("\nEin untoter Pirat erhebt sich aus den Schatten und greift dich an!")
                fight("Untoter Pirat", 150, untoter_pirat_texts, opponent_damage_range=(20, 80)) #Kampf mit untotem Piraten
                # Gegner: Untoter Pirat mit 70 Lebenspunkten und Schadensbereich von 20 - 80

            elif encounter == "Magischer Fluch":
                print_slow("\nEin leuchtender Nebel umgibt dich plötzlich und du spürst eine eisige Kälte.")
                time.sleep(2)
                print_slow_red("\nEin magischer Fluch trifft dich und raubt dir Energie!") #Anzeige des Fluchs
                player["health"] -= 40 #Gesundheitsverlust durch den Fluch
                print_slow_bold(f"\nDu verlierst ♡ 40 Gesundheit. Deine aktuelle Gesundheit: ♡ {player['health']}.")
                time.sleep(3)
                player_alive_check() #Überprüfung ob der Spieler noch lebt
                print_slow_bold("\nDeine Reise geht weiter!")
            
            elif encounter == "Rätsel":
                print_slow("\nEin altes Pergament flattert im Wind. Ein Rätsel verbirgt sich dahinter!")
                rätsel_aufgabe() # Aufruf der Rätsel-Funktion

        #Wenn der Spieler sich entscheidet das Wrack zu umgehen
        elif choice =="2":
            print_slow("\nDu entscheidest dich, das Wrack zu umgehen und deine Reise sicher fortzusetzen.") #Keine Aktion, einfach Weiterreise
            
        elif choice == "3":
            while True:
                #zufällige Auswahl eines Schatzes der gefunden werden kann
                treasure = random.choices(["Geheime Vorrichtung", "Goldmünzen", "Glücksrad"], weights=[25, 35, 40], k=1)[0]
                if treasure == "Geheime Vorrichtung":
                    print_slow("\nDu entdeckst eine mysteriöse Vorrichtung im Inneren des Wracks, die von Seetang und Rost bedeckt ist.")
                    print_slow_bold("\nDu drückst vorsichtig auf einen Hebel und plötzlich öffnet sich ein geheimer Gang, der in die Dunkelheit führt. Vielleicht führt er zu etwas noch Gefährlicherem...")
                    time.sleep(2)
                    print_slow("\nDu schlenderst vorsichtig den dunken Gang entlang. Der geheime Gang endet jedoch in einer Sackgasse und du musst umkehren.") #Keine Aktion, es ist eine Sackgasse und man wird wieder auf die Adventure Map geworfen
                    time.sleep(3)
                    
                    cursed_shipwreck()
                
                elif treasure == "Goldmünzen":
                    print_slow("\nDu findest eine kleine Truhe mit Goldmünzen, die im Dunkeln schimmern!")
                    time.sleep(2)
                    print(goldmünzen_ascii) #Ascii Art Schatztruhe mit Gold
                    time.sleep(2) 
                    player["gold"] += 50 #Spieler erhält Goldmünzen
                    print_slow_bold(f"\nDu sammelst 💰 50 Goldmünzen. Dein Goldvorrat: 💰 {player['gold']} Münzen.")
                    break
                
                elif treasure == "Glücksrad":
                    while True:
                        print_slow("\nDu findest ein mystisches Glücksrad, das in der Nähe des Wracks steht. Es scheint eine alte Magie zu beinhalten.")
                        print_slow_bold("\nDas Glücksrad hat viele Felder und jedes verspricht entweder einen Gewinn oder Verlust.")
                        print_slow_bold("Möchtest du dein Glück versuchen und das Rad drehen?")
                        print("1. Ja")
                        print("2. Nein")
                        choice = input("\nDeine Wahl (1/2): ")
                        print(abtrennung)

                        if choice == "1":
                            print_slow("\nDu trittst vor das mystische Glücksrad und bereitest dich darauf vor, es zu drehen...")
                            time.sleep(1)
                            print_slow("\nDas Glücksrad beginnt sich zu drehen...") #textbasiertes Glücksrad
                        
                            time.sleep(2)
                        

                            # Glücksrad mit mehreren Feldern und verschiedenen Ergebnissen
                            wheel = ["Großer Gewinn", "Verlust", "Gesundheit gewinnen", "Gold verlieren"]
                            result = random.choice(wheel)

                            print_slow("\nDas Glücksrad stoppt...") #Glücksrad hält an
                            time.sleep(2)

                            #verschiedene mögliche Ereignisse nach Drehen des Rads
                            if result == "Großer Gewinn":
                                print_slow("\nDas Glücksrad bleibt bei einem großen Gewinn stehen!")
                                print_slow("\nDu erhältst 💰 100 Goldmünzen und ein seltenes Amulett, das deine Gesundheit verbessert!")
                                player["gold"] += 100
                                player["health"] += 20
                                print_slow_bold(f"\nDu sammelst 💰 100 Goldmünzen. Dein Goldvorrat: 💰 {player['gold']} Münzen.")
                                print_slow_bold(f"\nDeine Gesundheit wurde um ♡ 20 verbessert. Deine aktuelle Gesundheit: ♡ {player['health']}.")
                                time.sleep(2)
                            
                            elif result == "Verlust":
                                print_slow("\nDas Glücksrad bleibt bei Verlust stehen... Oh nein, du verlierst etwas!")
                                player["health"] -= 30 #Verlust Gesundheit
                                player["gold"] -= 20 #Verlust Gold
                                print_slow_bold(f"\nDu verlierst ♡ 30 Gesundheit und 💰 20 Goldmünzen. Deine aktuelle Gesundheit: ♡ {player['health']}, Dein Goldvorrat: 💰 {player['gold']} Münzen.")
                                time.sleep(2)
                                player_alive_check() #Check ob Pirat noch lebt
                                

                            elif result == "Gesundheit gewinnen":
                                print_slow("\nDas Glücksrad bleibt bei 'Gesundheit gewinnen' stehen!")
                                print_slow("\nDu gewinnst ♡ 50 Gesundheitspunkte!")
                                player["health"] += 50 #Gewinn von 50 Gesundheitspunkten
                                print_slow_bold(f"\nDu gewinnst ♡ 50 Gesundheit! Deine aktuelle Gesundheit: ♡ {player['health']}.")
                                time.sleep(2)

                            elif result == "Gold verlieren":
                                print_slow("\nDas Glücksrad bleibt bei 'Gold verlieren' stehen!")
                                print_slow("\nDu verlierst 💰 50 Goldmünzen!")
                                player["gold"] -= 50 #Verlust Goldmünzen
                                print_slow_bold(f"\nDu verlierst 💰 50 Goldmünzen. Dein Goldvorrat: 💰 {player['gold']} Münzen.")
                                time.sleep(2)
                            break
                                
                                     
                       
                        elif choice == "2":
                            print_slow("\nDu entscheidest dich, das Glücksrad nicht zu drehen und das Abenteuer fortzusetzen.")
                            cursed_shipwreck()
                        
                        else:
                            print_slow("\nArrr, das war keine gültige Wahl! Bitte wähle 1 oder 2, Landratte!")
                            time.sleep(1)
                            continue # Führt while-Schleife fort
                break
                        


         #Das Wetter für sich nutzen        
        elif choice == "4":
            #Zufällige Wetterbedingungen werden mit unterschiedlicher Wahrscheinlichkeit ausgewählt
            weather = random.choices(["Sturm", "Sonnenschein", "Dunkle Wolken"], weights=[33, 33, 34], k=1)[0]
            if weather == "Sturm":
                print_slow("\nPlötzlich zieht ein gewaltiger Sturm auf! Die Wellen schlagen gegen das Schiffswrack, und der Wind heult durch die Ritzen.")
                time.sleep(2) #kurze Pause, um die Atmosphäre zu verstärken
                print(storm_ascii)
                time.sleep(3)
                print_slow_red("\nDer Sturm verstärkt den Fluch des Ortes und du fühlst eine Welle kalter Energie!")
                player["health"] -= 20 #Spieler verliert Gesundheit aufgrund des Sturms
                print_slow_bold(f"\nDu verlierst ♡ 20 Gesundheit. Deine aktuelle Gesundheit: ♡ {player['health']}.")
                time.sleep(2) #Pause vor der Gesundheitsüberprüfung
                player_alive_check() #Überprüfen ob der Spieler noch lebt
            
            elif weather == "Sonnenschein":
                print_slow("\nDie Sonne bricht durch die Wolken und erhellt das Wrack. Du fühlst dich für einen Moment sicherer.")
                time.sleep(2)
                print(sun_ascii)
                time.sleep(3) 
                print_slow("\nDu erhältst einen Moment der Ruhe und deine Gesundheit wird um ♡ 20 geheilt.")
                player["health"] += 20 #Spieler erhält Gesundheit durch den Sonnenschein
                print_slow_bold(f"\nDu gewinnst ♡ 20 Gesundheit. Deine aktuelle Gesundheit: ♡ {player['health']}.")
                time.sleep(2)
            
            elif weather == "Dunkle Wolken":
                print_slow("\nDunkle Wolken ziehen am Himmel auf und ein bedrohlicher Schatten schleicht sich über das Schiffswrack.")
                time.sleep(2)
                print(clouds_ascii)
                print_slow_red("\nEine unheimliche Stille breitet sich aus. Etwas ist hier nicht richtig...")
                # Der mysteriöse Schatten erscheint
                print_slow("\nEin gigantisches Seeungeheuer taucht plötzlich aus den Tiefen des Ozeans auf!")
                print_slow("Seine Augen glühen und seine Zähne glänzen scharf im Licht.")
                print(seeungeheuer_ascii)
                time.sleep(2)
                print_slow_red("\nDas Ungeheuer greift dich an!")
                # Kampf mit dem Seeungeheuer beginnen
                fight("Seeungeheuer", 200, seeungeheuer_texts, opponent_damage_range=(30, 50))
                # Gegner: Seeungeheuer mit 100 Lebenspunkten und Schadensbereich von 30-50
                
        else:
            print_slow("\nArrr, das war keine gültige Wahl! Bitte wähle 1, 2, 3 oder 4 Landratte!")
            time.sleep(1)
            continue # Führt while-Schleife fort
        
        adventure_map()
        


####################################################################
# 5. Pfad - Die verlassenen Tempel

def temple_path():
    # Funktion, die verschiedene Szenarien im Tempel behandelt
    play_music("freepiratemusic_8.mp3")
    print(abtrennung)  # Trennt den Text visuell
    print_slow_bold("\n Willkommen bei den verlassenen Tempeln!")  # Begrüßt den Spieler im Tempelbereich
    print(temple_ascii)  # Zeigt eine ASCII-Darstellung des Tempels
    print_slow("\nDu stehst vor einem uralten Tempel, dessen steinerne Fassade von Moos und Efeu überwuchert ist.")
    print_slow("\nEtwas in der Luft fühlt sich geheimnisvoll und magisch an!")

    # Zufällige Auswahl eines Szenarios mit festgelegten Wahrscheinlichkeiten
    encounter = random.choices(["Tempelwächter", "Rätsel", "Goldfund", "Friedhof", "Eingesperrt"], 
                               weights=[15, 15, 20, 35, 15 ], k=1)[0]

    if encounter == "Tempelwächter":
        # Szenario: Spieler begegnet einem Tempelwächter
        print(wächter_ascii)  # Zeigt die ASCII-Darstellung des Tempelwächters
        print_slow_bold("\nEin gewaltiger Tempelwächter aus Stein und Metall erwacht zum Leben und stürzt sich auf dich!")
        print_slow_red("\nWie kannst du es wagen unsere Ruhestätte zu stören? Das wirst du Büßen!")
        time.sleep(4)
        print(sword_ascii) #Zeigt die ASCII Darstellung vom Schwert des Tempelwächters und symbolisisert den Kampf
        fight("Tempelwächter", 200, tempelwaechter_texts, opponent_damage_range=(20, 60))  # Startet den Kampf mit dem Wächter

    elif encounter == "Rätsel":
        # Szenario: Spieler entdeckt ein Rätsel
        print_slow("\nDu entdeckst eine steinerne Tafel, die mit mystischen Zeichen bedeckt ist. Ein Rätsel verbirgt sich dahinter!")
        rätsel_aufgabe()  # Ruft die Funktion auf, die das Rätsel behandelt
        

    elif encounter == "Goldfund":
        # Szenario: Spieler findet einen Goldschatz
        time.sleep(2)
        print_slow("\nDu findest eine versteckte Kammer im Tempel. Darin liegt ein goldener Kelch, der glänzend im Dunkeln schimmert.")
        time.sleep(2)
        print_slow_bold("\nDu nimmst den Kelch in die Hand und entdeckst, dass er mit 💰 200 Goldmünzen gefüllt ist!")
        time.sleep(2)
        player["gold"] += 200 
        print_slow_bold(f"\nDu erhältst 💰 200 Gold. Dein aktueller Goldbestand: 💰 {player['gold']}.")
        time.sleep(3)
        
    elif encounter == "Friedhof":
        # Szenario: Spieler wird zum Friedhof gebracht und kämpft gegen einen Geist
        time.sleep(2)
        print_slow_bold("\nAls du versuchst den Tempel zu betreten, packen dich plötzlich eiserne Hände!")
        time.sleep(2)
        print_slow("\nDu wirst von zehn Wächtern aus dem Tempel getragen und zu einem uralten Friedhof gebracht.")
        print(graveyard_ascii)
        time.sleep(3)
        print_slow("\nDort triffst du auf einen Geist, dessen Augen im Dunkeln leuchten.")
        print_slow_red("\nDer Geist schreit: \"Du hast die Ruhe der Verstorbenen gestört! Jetzt wirst du gegen mich kämpfen!\"")
        time.sleep(2.5)

        # Zeigt den Geist dreimal schnell hintereinander mit Pausen dazwischen

        for _ in range(3):  # Wiederholt den Effekt dreimal
            print(ghost_ascii)  # Zeigt die ASCII-Darstellung des Geistes
            time.sleep(2)  # Wartet 2 Sekunden, um den Effekt zu erzeugen
            
            
        
        print_slow("Die Luft wird kalt, und der Kampf beginnt!")  # Bereitet den Spieler auf den Kampf vor
        play_music("fight_music.mp3")


        geist_health = 200  # Lebenspunkte des Geistes
        while geist_health > 0:  # Solange der Geist noch Lebenspunkte hat
            print_bold(f"\nDeine Gesundheit: ♡ {player['health']} Dein Schaden: ⚔ {player['damage']} | Gesundheit des Gegners: ♡ {geist_health}")
            print_bold("\nWas willst du tun?")
            print("1. Angriff\n2. Ausweichen\n3. Spezialfähigkeit einsetzen")  # Optionen für den Spieler
            choice = input("\nDeine Wahl (1/2/3): ")  # Spieler wählt eine Aktion
            print(abtrennung)

            if choice == "1":
                # Spieler greift den Geist an
                damage = player['damage']
                print_slow_red(f"\nDu stürmst auf den Geist zu und fügst ihm ⚔ {player['damage']} Schaden zu!")
                geist_health -= damage  # Abziehen des Schadens von den Lebenspunkten des Geistes
            elif choice == "2":
                # Spieler weicht aus
                print_slow("\nDu weichst geschickt den Angriffen des Geistes aus und wartest auf eine bessere Gelegenheit.")
                continue  # Überspringt den Rest des Loops
            elif choice == "3":
                # Spieler setzt eine Spezialfähigkeit ein
                print_slow("\nDu konzentrierst dich und setzt eine verheerende Spezialfähigkeit ein!")
                special_damage = random.randint(50, 70)  # Zufälliger Spezialschaden zwischen 50 und 70
                print_slow_red(f"\nDer Geist schreit auf, als du ihm ⚔ {special_damage} Schaden zufügst!")
                geist_health -= special_damage  # Abziehen des Schadens von den Lebenspunkten des Geistes
            else:
                # Ungültige Eingabe
                print_slow("\nUngültige Wahl. Bitte versuche es erneut.")
                continue  # Überspringt den Rest des Loops

            if geist_health > 0:  # Wenn der Geist noch lebt
                geist_action = random.choice(geist_actions)  # Wählt zufällig eine Aktion des Geistes
                print_slow(f"\n{geist_action}")  # Zeigt die Aktion des Geistes an
                if "Schaden" in geist_action or "absaugt" in geist_action:
                    geist_damage = random.randint(15, 30)  # Zufälliger Schaden zwischen 15 und 30
                    print_slow_red(f"\nDu erleidest {geist_damage} Schaden!")  # Zeigt den erlittenen Schaden an
                elif "schwächen" in geist_action:
                    print(more_ghosts_ascii)
                    print_slow("\nDein nächster Angriff wird weniger effektiv sein.")  # Reduziert die Effektivität des nächsten Angriffs
                    

        print_slow("\nMit einem letzten Schrei verschwindet der Geist in einem Wirbel aus Dunkelheit. Du hast gewonnen!")  # Spieler besiegt den Geist
        play_music("win.mp3")
        gold_found = random.randint(80, 150) # Zufällige Goldbelohnung im Intervall 80 - 150
        player["gold"] += gold_found # # Gold dem Spieler hinzufügen
        print_slow_bold(f"\nDu hast 💰 {gold_found} Goldmünzen gefunden!")
        health_gain = random.randint(10, 40) # Spieler regeneriert Gesundheit
        player["health"] += health_gain # Leben hinzufügen
        print_slow_bold(f"Der überstandene Kampf erfüllt dich mit neuer Kraft!")
        print_slow_bold(f"Deine Gesundheit steigt um ♡ {health_gain}!")
        time.sleep(4)
        print_slow_bold("\nDeine Reise geht weiter!")

    elif encounter == "Eingesperrt":
        play_music("freepiratemusic_1.mp3")
        # Szenario: Spieler wird im Tempel eingesperrt und muss Münzen zahlen, um zu entkommen
        time.sleep(2)
        print_slow_bold("\nPlötzlich fällt ein schweres Gitter herunter und schließt den Ausgang des Tempels!")
        time.sleep(2)
        print(gitter)
        time.sleep(3)
        if player["gold"] >= 200:
            while True:
                print_slow_bold("Eine Stimme hallt: 'Bezahle 💰 200 Goldmünzen, um deine Freiheit zu erkaufen!'\n")
                print_slow("1. Bezahlen und freikommen")
                print_slow("2. Verweigern und eingesperrt bleiben")
                print_slow("3. Fliehen (50% Erfolgsquote)")

                # Spieler trifft seine Wahl
                choice = input("\nWas tust du? (1/2/3): ")
                print(abtrennung)

                if choice == "1":
                    player["gold"] -= 200  # Zieht 200 Münzen vom Goldbestand des Spielers ab
                    print_slow_bold("\nDu bezahlst 💰 200 Gold und das Gitter hebt sich langsam. Du bist frei!")
                    time.sleep(3)
                    break  # Beendet die Schleife, da der Spieler frei ist

                elif choice == "2":
                    print_slow_bold("\nDu verweigerst die Zahlung und bleibst eingesperrt. Vielleicht schaffst du es zu fliehen...\n")
                    continue

                elif choice == "3":
                    # 50% Chance auf Erfolg
                    if random.random() < 0.5:
                        print_slow("\nDu fliehst erfolgreich und entkommst aus dem Tempel!")
                        break  # Spieler ist frei, Schleife endet hier
                    else:
                        print_slow_bold("\nDein Fluchtversuch scheitert...")
                        time.sleep(2)
                        print_slow("\nPlötzlich verdunkelt sich der Raum und ein tiefer, grollender Donner ertönt.")
                        time.sleep(2)
                        print_slow("\nEine mächtige Stimme hallt wider: 'Du wagst es, den Willen der Götter zu hintergehen?'")
                        time.sleep(2)
                        print_slow("\nDie Stimme verkündet: 'Für deinen unehrlichen Versuch wird dir das Kostbarste genommen: dein Leben.'")
                        time.sleep(2)
                        print_slow("\nDu fühlst, wie deine Lebensenergie schwindet und mit einem letzten Atemzug geht deine Reise hier zu Ende.")
                        time.sleep(2)
                        play_music("lose.mp3")
                        print(rip_ascii)
                        print_slow_bold("GAME OVER. Die Götter haben dich bestraft.")
                        print(abtrennung)
                        print()
                        time.sleep(2)
                        print(lose_ascii)
                        time.sleep(4)
                        game_neustart()
                else:
                    print_slow("\nArrr, das war keine gültige Wahl! Bitte wähle 1, 2 oder 3 Landratte!\n") 
            
        else:
            # Spieler hat nicht genug Gold
            print_slow_bold("Eine Stimme hallt: 'Bezahle 💰 200 Goldmünzen, um deine Freiheit zu erkaufen!'\n")
            time.sleep(2)
            print_slow("\nDu suchst verzweifelt in deinen Taschen nach Münzen, doch es ist nicht genug...")
            time.sleep(2)
            print_slow_bold(f"\nDu hast nicht genug Gold, um zu entkommen! Goldbestand: 💰 {player['gold']}")
            time.sleep(2)
            print_slow("\nEine donnernde Stimme hallt wider: 'Du wagst es, uns mit deinem Mangel zu beleidigen?'")
            time.sleep(2)
            print_slow("\nEin grelles Licht erhellt den Raum, und ein unsichtbarer Druck zwingt dich auf die Knie.")
            time.sleep(2)
            print_slow("\nDie Stimme verkündet: 'Für deinen Hochmut nimmst du die Bürde deiner Armut mit ins Jenseits!'")
            time.sleep(2)
            print_slow("\nEin Schatten erhebt sich vor dir und du spürst, wie dir all deine Kraft entzogen wird.")
            time.sleep(2)
            play_music("lose.mp3")
            print(rip_ascii)
            print_slow_bold("\nGAME OVER. Deine Seele gehört nun den Göttern.")
            print(abtrennung)
            print()
            time.sleep(2)
            print(lose_ascii)
            time.sleep(5)
            game_neustart()  # Startet das Spiel neu

    adventure_map()  # Führt den Spieler zurück zur Abenteuerkarte

###########################################################################################################
# Kampfsystem
###########################################################################################################

def fight(opponent, opponent_health, fight_texts, opponent_damage_range=(30, 40), multi_attack=None):
    # Parameter:
      # opponent (str): Name des Gegners, z. B. "Pirat"
      # opponent_health (int): Lebenspunkte des Gegners
      # fight_texts (dict): Wörterbuch mit Kampftexten
        # fight_texts greift auf die jeweilige Dictionary des Gegners zu.
        # Diese beinhaltet Schlüssel für verschiedene Szenarien "attack", "flee", "special_event", "win", "lose".
        # Die Schlüssel beinhalten eine Liste an strings.
      # opponent_damage_range (tuple): Schaden des Gegners bei einem Angriff -> tuple = Unveränderliche Liste
        # Ist Standard Range, falls keine Range bei Gegner angegeben ist. Als (min, max). Standard: (30, 40)
      #  multi_attack (dict, optional): Enthält die Mehrfachangriff-Parameter:
        # - "min_attacks" (int): Minimale Anzahl Angriffe pro Runde.
        # - "max_attacks" (int): Maximale Anzahl Angriffe pro Runde.
        # - "damage_per_attack" (int): Schaden pro Angriff.
        # Kommt nur zum Einsatz, wenn Parameter angegeben ist -> z.B. bei "Inselbewohner" oder "Fledermäuse"
      

    play_music("fight_music.mp3")  # Kampfmusik abspielen

    # Gibt eine Einleitung zum Kampf aus
    print_slow_bold(f"\n⚔️ Der Kampf beginnt! Dein Gegner ist ein {opponent}.")
    
    # Hauptkampfschleife: Läuft, solange Spieler und Gegner am Leben sind
    while player["health"] > 0 and opponent_health > 0:
        # Zeigt die aktuellen Werte des Spielers und des Gegners an
        print_slow_bold(f"\nDeine Gesundheit: ♡ {player['health']} Dein Schaden: ⚔ {player['damage']} | Gesundheit des Gegners: ♡ {opponent_health}\n")
        print_slow("1. Angreifen") # Option zum Angriff
        print_slow("2. Fliehen (50% Erfolgsquote)\n") # Option zur Flucht
        
        # Spieler trifft seine Wahl
        choice = input("Was tust du? (1/2): ")
        
        # Prüft, ob die Eingabe gültig ist
        if choice not in ["1", "2"]:
            print_slow("Arrr, das war keine gültige Wahl! Bitte wähle 1 oder 2, Landratte!")
            print(abtrennung)
            continue # Springt zurück zum Anfang der Schleife
        
         # Spieler wählt Angriff
        if choice == "1":  
            print(abtrennung)
            print()
            damage = player["damage"] # Schaden des Spielers
            opponent_health -= damage # Gegner verliert entsprechend Schaden
            attack_text = random.choice(fight_texts["attack"]) # Zufälliger Angriffstext aus fight_texts
            print_slow_red(attack_text.replace("{opponent}", opponent).replace("{damage}", str(damage)))
            # Ersetzt den Namen des Gegners und den verursachten Schaden im Text mit den zutreffenden Werten

        # Spieler wählt Flucht
        elif choice == "2":  
            print(abtrennung)
            print()
            # random.random() generiert eine Zufallszahl zwischen 0.0 und 1.0
            # Wenn die Zufallszahl kleiner als 0.5 ist, ist die Flucht erfolgreich
            if random.random() < 0.5:  # 50% Chance, erfolgreich zu fliehen
                flee_text = random.choice(fight_texts["flee"])  # Zufälliger Fluchttext
                print_slow(flee_text.replace("{opponent}", opponent)) # Ersetzt wieder den Gegner Namen
                print_slow_bold("Du bist erfolgreich geflohen!")
                time.sleep(2.5)
                print_slow_bold(f"Du regenerierst langsam deine Kräfte!")
                health_gain = random.randint(20, 40) # Spieler regeneriert Gesundheit
                player["health"] += health_gain # Leben hinzufügen
                print_slow_bold(f"Deine Gesundheit steigt um ♡ {health_gain}!")
                return  # Beendet den Kampf und kehrt zur nächsten Funktion zurück
            else:
                print_slow_bold("Deine Flucht ist fehlgeschlagen! Der Kampf geht weiter.\n")
                # Wenn Flucht nicht gelingt, geht Kampf weiter und Gegner greift an

        # Sieg/Niederlage prüfen
        # Wenn Gegner Gesundheit kleiner gleich 0, dann ist Kampf gewonnen
        if opponent_health <= 0:
            win_text = random.choice(fight_texts["win"]) # Zufälliger Siegtext
            print_slow(win_text.replace("{opponent}", opponent))
            print(win_ascii)
            play_music("win.mp3")
            gold_found = random.randint(80, 150) # Zufällige Goldbelohnung im Intervall 80 - 150
            player["gold"] += gold_found # # Gold dem Spieler hinzufügen
            print_slow_bold(f"\nDu hast 💰 {gold_found} Goldmünzen gefunden!")
            health_gain = random.randint(10, 40) # Spieler regeneriert Gesundheit
            player["health"] += health_gain # Leben hinzufügen
            print_slow_bold(f"Der überstandene Kampf erfüllt dich mit neuer Kraft!")
            print_slow_bold(f"Deine Gesundheit steigt um ♡ {health_gain}!")
            time.sleep(4)
            print_slow_bold("\nDeine Reise geht weiter!")
            time.sleep(2)
            break # Beendet die Kampfschleife
        

        # Gegner greift nach jedem Zug an
        # Gegner mit mehrfachen Angriffen -> Wenn multi_attack Parameter hinterlegt ist
        if multi_attack:  
            min_attacks = multi_attack["min_attacks"] # Minimale Angriffe pro Runde
            max_attacks = multi_attack["max_attacks"] # Maximale Angriffe pro Runde
            damage_per_attack = multi_attack["damage_per_attack"] # Schaden pro Angriff
            anzahl_angriffe = random.randint(min_attacks, max_attacks) # Zufällige Anzahl der Angriffe
            print(f"{opponent} greift {anzahl_angriffe} Mal an!") # Ausgabe der Angriffszahl
            # for-Schleife, um jeden Angriff durchzuführen
            # Wiederholt den Angriff des Gegners basierend auf der Anzahl der Angriffe
            for i in range(anzahl_angriffe): 
                player["health"] -= damage_per_attack # Spieler verliert Leben in Höhe des Schadens
                # Für jeden Angriff (Nr) wird Schaden mitgeteilt
                print_red(f"Angriff {i + 1}: {opponent} verursacht {damage_per_attack} Schaden! 💥")
                time.sleep(0.5)
        else:  # Standardgegner, ohne Multiattack Parameter greift an
            # Entpackt die minimale und maximale Schadenswerte aus dem Tuple opponent_damage_range
            min_damage, max_damage = opponent_damage_range
            # Generiert einen zufälligen Schadenswert zwischen min_damage und max_damage
            opponent_damage = random.randint(min_damage, max_damage)
            player["health"] -= opponent_damage
            print_slow_red(f"Der {opponent} greift an und verursacht {opponent_damage} Schaden! 💥")

        # Zusätzliche Ereignisse
        if random.random() < 0.7:  # 70% Chance auf ein Ereignis
            event_text = random.choice(fight_texts["special_event"]) # Text aus special_event
            print_slow(event_text.replace("{opponent}", opponent))
            time.sleep(2)
            

        # Überprüfen, ob der Spieler gestorben ist -> Gesundheit kleiner gleich 0
        # player_alive_check wird hier nicht verwendet, weil lose-Text ausgegeben werden muss
        if player["health"] <= 0: 
            lose_text = random.choice(fight_texts["lose"]) # Zufälliger lose-Text aus Liste-lose-Texten des Gegners
            print_slow(lose_text.replace("{opponent}", opponent)) # Gibt lose-Text für den jeweiligen Gegner aus
            play_music("lose.mp3")
            print_slow("\nDeine Reise endet hier! Spiel beendet.")
            print_slow(lose_ascii)
            time.sleep(3)
            
            # Spieler nach Neustart fragen
            game_neustart()

      

###########################################################################################################
# Prüfung, ob Spieler lebt. Eingebunden in adventure_map(). -> Auch für Fallen/Events mit Schaden
def player_alive_check():
        # Überprüfen, ob der Spieler gestorben ist -> Gesundheit kleiner gleich 0
    if player["health"] <= 0:
        play_music("lose.mp3")
        print(abtrennung)
        print_slow("\nDeine Reise endet hier! Spiel beendet.")
        print_slow(lose_ascii)
        time.sleep(2)
        
        # Spieler nach Neustart fragen
        game_neustart()

        
        # Funktion um Spieler nach Neustart zu fragen
def game_neustart():
    while True:
        stop_music()
        print_slow_bold("Möchtest du erneut spielen?")
        print_slow("1. Ja")
        print_slow("2. Nein")
        play_again = input("\nDeine Wahl (1/2): ")
        
        if play_again == "1":
            # Spiel neustarten
            start_game()
        elif play_again == "2":
            print(abtrennung)
            print_slow("\nVielen Dank fürs Spielen! Bis zum nächsten Mal!")
            exit()
        else:
            print(abtrennung)
            print_slow("\nArrr, das war keine gültige Wahl! Bitte wähle 1 oder 2, Landratte!\n")


###########################################################################################################
# 6. Markplatz
###########################################################################################################

def marktplatz():
    print_slow_bold("\n🛒 Willkommen auf dem Marktplatz! 🛒")
    print("Hier kannst du tolle Gegenstände kaufen, die dir auf deiner Reise sehr hilfreich sein werden.")
    print("Wofür interessierst du dich?")
    print("1. Heilung")
    print("2. Waffen")
    print_bold("\n3. Marktplatz verlassen\n")  
    
    choice = input("Deine Wahl (1/2/3): ")
    
    # Wahl des Spielers
    if choice == "1":
        heilung() # Ausführen Funktion heilung
    elif choice == "2":
        waffen() # Ausführen Funktion waffen
    elif choice == "3":
        print_slow("\nDu verlässt den Marktplatz und setzt deine Reise fort.")
        adventure_map() # Aufrufen der Kernfunktion
    else:
        print(abtrennung)
        print_slow("\nArrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
        marktplatz() # Erneutes Aufrufen der Funktion

###########################
# 1. Heilung

# Funktion zum Kauf von Heilung

def heilung():
    print(abtrennung)
    # Liste der Items
    # Jedes Item ist eine Dictionary mit:
    # Name, Heilungseffekt in Lebenspunkten, Kosten und Symbol/Emoji
    heilung_items = [
        {"name": "Verband", "heilung": 20, "kosten": 50, "emoji": "🩹"},
        {"name": "Heiltrank", "heilung": 50, "kosten": 100, "emoji": "🧪"},
        {"name": "Wundsalbe der Weisen", "heilung": 100, "kosten": 200, "emoji": "🍾"},
        {"name": "Krakenblut-Elixier", "heilung": 150, "kosten": 350, "emoji": "🧴"},
        {"name": "Essenz der Tiefsee", "heilung": 300, "kosten": 500, "emoji": "🔮"} 
    ]

    # Zeigt die Items mit Beschreibung
    print_slow_bold("\nDu betrachtest die Heilungsoptionen:")
    # for-Schleife iteriert durch die Liste und erzeugt automatisch eine nummerierte Liste
    # i: Laufende Nummer (startet bei 1 durch den zweiten Parameter von enumerate)
    # item: Das aktuelle Dictionary aus der Liste der items
    for i, item in enumerate(heilung_items, 1):
        # Auflistung der Items mit allen Eigenschaften
        print(f"{i}. {item['name']} {item['emoji']} - Heilt ♡ {item['heilung']} Gesundheit für 💰 {item['kosten']} Gold")
    # Zeigt aktuelle Spielerwerte an
    print_bold(f"\nDu hast derzeit ♡ {player['health']} Gesundheit, ⚔ {player['damage']} Schaden und 💰 {player['gold']} Gold.")
    print_bold("\n6. Zurück zur Übersicht")  
    
    # Abfrage, welcher Gegenstand gekauft werden soll
    choice = input("\nWie entscheidest du dich? (1/2/3/4/5/6): ")
    print(abtrennung)

    # Gültige Auswahl
    if choice in ["1", "2", "3", "4", "5"]:
        index = int(choice) - 1  # Index des gewählten Gegenstands
        item = heilung_items[index]
        # Prüft, ob Spieler genug Gold hat
        if player["gold"] >= item["kosten"]: 
            print(f"\nSicher, dass du {item['name']} kaufen willst? ")
            print("1. Ja")
            print("2. Nein")
            confirm = input("\nDeine Wahl: ")
            if confirm == "1": # Bestätigung des Kaufs
                player["gold"] -= item["kosten"] # Gold abziehen
                player["health"] = player["health"] + item["heilung"] # Leben hinzufügen
                print_slow_bold(f"\nDu hast {item['name']} gekauft! Deine aktuelle Gesundheit: ♡ {player['health']}, dein Gold: 💰 {player['gold']}.")
            else:
                # Abbruch des Kaufs
                print_slow("Arrr, der Handel ist geplatzt! Vielleicht beim nächsten Mal, Kamerad.")
        else:
            # Spieler hat nicht genug Gold
            print_slow("Hm, dein Geldbeutel ist leerer als die Kassen eines gesunkenen Schiffes! Hol dir mehr Gold und komm zurück.")
    # Zurück zur Übersicht
    elif choice == "6":
        marktplatz()
    else:
        # Ungültige Eingabe, Funktion wird erneut aufgerufen
        print_slow("Arrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
        heilung()

    heilung() # Funktion erneut aufrufen, falls keine gültige Auswahl getroffen wurde

###########################
# 2. Waffen

# Funktion zum Kauf von Waffen
def waffen():
    print(abtrennung)
    # Liste der Waffen
    # Jede Waffe ist eine Dictionary mit:
    # Name, Schadenerhöhung, Kosten und Symbol/Emoji
    waffen_items = [
        {"name": "Rostiges Schwert", "schaden": 10, "kosten": 40, "emoji": "⸸"},
        {"name": "Piraten-Säbel", "schaden": 20, "kosten": 70, "emoji": "🗡"},
        {"name": "Doppelklingen-Axt", "schaden": 35, "kosten": 150, "emoji": "🪓🪓"},
        {"name": "Kapitäns-Degen", "schaden": 50, "kosten": 200, "emoji": "▬|════ﺤ"},
        {"name": "Verfluchte Schattenklinge", "schaden": 80, "kosten": 300, "emoji": "▬▬|≡≡≡≡≡≡≡ﺤ"}
    ]
    
    # Zeigt die Waffen mit Beschreibung
    print_slow_bold("\nDu betrachtest die Waffenoptionen:")
    # for-Schleife iteriert durch die Liste und erzeugt automatisch eine nummerierte Liste
    # i: Laufende Nummer (startet bei 1 durch den zweiten Parameter von enumerate)
    # item: Das aktuelle Dictionary aus der Liste der items
    for i, item in enumerate(waffen_items, 1):
        # Auflistung der Waffen mit allen Eigenschaften
        print(f"{i}. {item['name']} {item['emoji']} - Erhöht ⚔ Schaden um {item['schaden']} für 💰 {item['kosten']} Gold")
    # Zeigt aktuelle Spielerwerte an
    print_bold(f"\nDu hast derzeit ♡ {player['health']} Gesundheit, ⚔ {player['damage']} Schaden und 💰 {player['gold']} Gold.")
    print_bold("\n6. Zurück zur Übersicht")  

    # Spieler trifft Entscheidung
    choice = input("\nWie entscheidest du dich? (1/2/3/4/5/6): ")
    print(abtrennung)

    # Gültige Auswahl
    if choice in ["1", "2", "3", "4", "5"]:
        index = int(choice) - 1 # Index der gewählten Waffe
        item = waffen_items[index]
        # Prüft, ob Spieler genug Gold hat
        if player["gold"] >= item["kosten"]:
            print(f"\nSicher, dass du {item['name']} kaufen willst? ")
            print("1. Ja")
            print("2. Nein")
            confirm = input("\nDeine Wahl: ")
            # Bestätigung des Kaufs
            if confirm == "1":
                player["gold"] -= item["kosten"] # Gold abziehen
                player["damage"] += item["schaden"] # Schaden hinzufügen
                print_slow_bold(f"\nDu hast {item['name']} gekauft! Dein aktueller Schaden: ⚔ {player['damage']}, dein Gold: 💰 {player['gold']}.")
            else:
                # Abbruch des Kaufs
                print_slow("Arrr, der Handel ist geplatzt! Vielleicht beim nächsten Mal, Kamerad.")
        else:
            # Spieler hat nicht genug Gold
            print_slow("Hm, dein Geldbeutel ist leerer als die Kassen eines gesunkenen Schiffes! Hol dir mehr Gold und komm zurück.")
    # Zurück zur Übersicht
    elif choice == "6":
        marktplatz()
    else:
        # Ungültige Eingabe, Funktion wird erneut aufgerufen
        print_slow("Arrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")
        waffen()

    waffen() # Funktion erneut aufrufen, falls keine gültige Auswahl getroffen wurde

###########################################################################################################
# Rätsel-Funktion
###########################################################################################################

def rätsel_aufgabe():
    # Zufälliges Rätsel aus der Liste auswählen
    ausgewähltes_rätsel = random.choice(rätsel)
    frage = ausgewähltes_rätsel["frage"] # Die Frage des Rätsels 
    antworten = ausgewähltes_rätsel["antworten"] # Mögliche Antworten des Rätsels
    
    # Antworten zufällig mischen, damit die richtige Antwort nicht immer an derselben Stelle steht
    # "antworten" ist die ursprüngliche Liste mit den möglichen Antworten
    # len(antworten) gibt die Anzahl der Antworten in der Liste an
    # random.sample erstellt eine neue Liste, in der alle Antworten zufällig angeordnet sind
    zufällige_antworten = random.sample(antworten, len(antworten))
    
    # Die richtige Antwort ist immer das erste Element in der ursprünglichen Antwortliste
    richtige_antwort = antworten[0]
    
    # Endlosschleife, um den Spieler bei falschen Eingaben nicht rauszuwerfen
    while True:  
        # Frage stellen
        print()
        print_slow_bold(frage)
        # for-Schleife listet Antworten auf und beginnt bei 1
        for i, antwort in enumerate(zufällige_antworten, 1):
            print(f"{i}. {antwort}")
        
        # Antwort abfragen
        choice = input("\nWähle die richtige Antwort (1/2/3/4): ")
        # Überprüfen, ob die Eingabe eine gültige Zahl im Bereich 1-4 ist
        if choice.isdigit() and 1 <= int(choice) <= 4:
            # Die Antwort des Spielers wird aus der Liste der zufälligen Antworten entnommen
            # choice ist die Eingabe des Spielers, z. B. "1", "2", "3" oder "4"
            # int(choice)` wandelt die Eingabe von einem String in eine Ganzzahl um
            # - 1 wird subtrahiert, weil Listen in Python bei Index 0 starten, der Spieler aber ab 1 zählt
            # Dadurch wird die Eingabe des Spielers korrekt mit dem Listenindex abgeglichen
            gewählte_antwort = zufällige_antworten[int(choice) - 1]
            # Überprüfung auf richtige Antwort
            if gewählte_antwort == richtige_antwort:
                play_music("riddle_correct.mp3")
                print(abtrennung)
                # Zufälliger Erfolgstext wird ausgewählt und ausgegeben
                antwort_erfolg = random.choice(rätsel_erfolg)
                print_slow_bold("\n" + antwort_erfolg)
                
                # Zufällige Belohnungstext wird ausgewählt und ausgegeben
                antwort_belohnung = random.choice(gold_fund_varianten)
                print_slow_bold("\n" + antwort_belohnung)
                
                # Zufällige Menge an Gold wird hinzugefügt
                gold_found = random.randint(50, 120)
                player["gold"] += gold_found
                print_slow_bold(f"Du hast {gold_found} Goldmünzen gefunden! 💰")
                time.sleep(2)
                print_slow_bold("\nDeine Reise geht weiter!\n")
                return True # Beendet die Funktion, da die richtige Antwort gegeben wurde
            
            # Wenn die Antwort falsch ist
            else:
                play_music("riddle_fail.mp3")
                print(abtrennung)
                print_slow_bold("\nArrr, das war wohl nix! Beim nächsten Mal hast du vielleicht mehr Glück, Landratte!")
                time.sleep(2)
                return False # Beendet die Funtion, da die falsche Antwort gegeben wurde
        else:
            # Ungültige Eingabe: Spieler wird erneut aufgefordert
            print(abtrennung)
            print_slow("Arrr, das war keine gültige Wahl! Versuch's nochmal, Landratte!")



###########################################################################################################
###########################################################################################################
# ASCII-Grafiken und Texte
###########################################################################################################
###########################################################################################################


###########################################################################################################
# Dialoge für Kämpfe
###########################################################################################################

# Alle Dialoge für Kämpfe mit fight-Funktion sind hier definiert.
# Jeder Gegner hat seine eigene Dictionary.
# Die Schlüssel sind die Kategorien "attack", "flee", "special_event", "win" und "lose".
# Die Werte der Schlüssel sind eine Liste von Texten.

########################################################################
# 1. Pfad

pirate_texts = {
    "attack": [
        "Du schwingst dein Schwert und triffst den Piraten mitten ins Ziel, was {damage} Schaden verursacht!",
        "Mit einem kraftvollen Schlag streifst du den Piraten und er erleidet {damage} Schaden!",
        "Dein Angriff trifft die linke Seite des Piraten und verursacht {damage} Schaden."
    ],
    "flee": [
        "Du rennst so schnell du kannst und entkommst dem Piraten!",
        "Mit einem geschickten Sprung landest du außer Reichweite des Piraten und fliehst.",
    ],
    "special_event": [
        "Der Pirat wirbelt sein Schwert durch die Luft und ruft: 'Arrr, das wird dein Ende sein!'",
        "Mit einem wütenden Kampfschrei stürmt der Pirat auf dich zu und erhöht sein Tempo.",
        "Der Pirat stolpert über eine herumliegende Planke, verliert kurz das Gleichgewicht, aber fängt sich wieder."
    ],
    "win": [
        "Mit einem letzten Schlag wirfst du den Piraten zu Boden. Der Sieg gehört dir!",
        "Der Pirat lässt sein Schwert fallen und sinkt geschlagen zu Boden.",
        "Du besiegst den Piraten und seine letzte Worte sind: 'Du bist ein würdiger Gegner!'"
    ],
    "lose": [
        "Der Pirat trifft dich mit einem gezielten Schlag, und du gehst zu Boden. Deine Reise endet hier.",
        "Mit einem harten Angriff überwindet dich der Pirat. Du verlierst das Bewusstsein.",
        "Der Pirat triumphiert mit einem lauten 'Arrr!' und du liegst besiegt im Staub."
    ]
}

jaguar_texts = {
    "attack": [
        "Du schlägst mit deinem Schwert auf den Jaguar ein, was {damage} Schaden verursacht!",
        "Mit einem geschickten Hieb triffst du den Jaguar und verursachst {damage} Schaden!",
        "Dein Angriff trifft den Jaguar an der Schulter und verursacht {damage} Schaden."
    ],
    "flee": [
        "Du versuchst zu fliehen, aber der Jaguar verfolgt dich noch kurz, bevor er aufgibt.",
        "Mit einem schnellen Sprint entkommst du knapp den Klauen des Jaguars!",
    ],
    "special_event": [
        "Der Jaguar springt mit einem mächtigen Satz auf dich zu, verfehlt dich aber knapp!",
        "Ein lautes Brüllen des Jaguars lässt dich kurz erstarren, aber du bleibst standhaft.",
        "Der Jaguar umkreist dich, beobachtet jede deiner Bewegungen, bevor er angreift."
    ],
    "win": [
        "Mit einem letzten Schlag besiegst du den Jaguar. Du hast gewonnen!",
        "Der Jaguar gibt auf und verschwindet langsam in den Schatten.",
        "Der mächtige Jaguar liegt besiegt vor dir. Du hast den Kampf gewonnen!"
    ],
    "lose": [
        "Der Jaguar greift mit seinen Krallen an und du gehst zu Boden. Deine Reise endet hier.",
        "Mit einem mächtigen Sprung überwältigt dich der Jaguar. Du verlierst das Bewusstsein.",
        "Der Jaguar triumphiert mit einem lauten Brüllen, während du geschlagen am Boden liegst."
    ]
}


########################################################################
# 2. Pfad

inselbewohner_texts = {
    "attack": [
        "Du spannst deinen Bogen und schießt einen Pfeil ab, der den Inselbewohner trifft und {damage} Schaden verursacht!",
        "Mit einem gezielten Schuss triffst du den Inselbewohner an der Schulter, was {damage} Schaden verursacht!",
        "Dein Pfeil zischt durch die Luft und trifft den Inselbewohner – {damage} Schaden!",
        "Der verrückte Inselbewohner ruft: 'Du willst mich kriegen? Ha! Niemals!' während dein Pfeil ihn trifft und {damage} Schaden anrichtet.",
        "Während der Inselbewohner wirr lacht, nutzt du die Gelegenheit und triffst ihn mit einem Pfeil. {damage} Schaden!"
    ],
    "flee": [
        "Du lässt Pfeil und Bogen zurück und rennst so schnell du kannst, während der Inselbewohner wild schreiend hinter dir bleibt.",
        "In einer panischen Flucht entkommst du knapp, doch dein Bogen zerbricht und ist nicht mehr zu gebrauchen.",
        "Mit einem mutigen Sprung entkommst du den Bolzen, doch du lässt deinen Bogen zurück – er ist zerstört."
    ],
    "special_event": [
        "Der Inselbewohner lädt seine Armbrust und schreit: 'Die Insel gehört mir! Du wirst sehen!'",
        "Ein Bolzen pfeift knapp an dir vorbei, während der Inselbewohner laut lacht: 'Ich bin der König dieser Insel!'",
        "Der verrückte Inselbewohner murmelt: 'Die Stimmen... Sie sagen, du bist ein Feind!' und zielt auf dich.",
        "Plötzlich stürzt der Inselbewohner über eine Wurzel, doch er fängt sich und zielt erneut mit seiner Armbrust.",
        "Während er zielt, ruft der Inselbewohner: 'Die Schätze sind MEINS! Keiner kommt hier vorbei!'"
    ],
    "win": [
        "Mit einem letzten gezielten Schuss triffst du den Inselbewohner, der schließlich zu Boden geht. Doch dein Bogen ist zerstört und nicht mehr zu gebrauchen.",
        "Der Inselbewohner stürzt nach deinem letzten Pfeil zu Boden. Du hast gewonnen, doch dein Bogen ist völlig kaputt.",
        "Mit einem gezielten Pfeil besiegst du den Inselbewohner. Er bleibt regungslos, doch dein Bogen zerbrach im Kampf.",
    ],
    "lose": [
        "Der Inselbewohner schießt mit seiner Armbrust einen Bolzen, der dich trifft. Deine Reise endet hier.",
        "Mit einem letzten Schrei feuert der Inselbewohner auf dich und du gehst zu Boden. Der Wahnsinn hat gesiegt.",
        "Der verrückte Inselbewohner lacht laut, während du nach seinem letzten Bolzen geschlagen am Boden liegst."
    ]
}


########################################################################
# 3. Pfad

fledermäuse_texts = {
    "attack": [
        "Du schwingst dein Schwert inmitten des Schwarms und triffst mehrere Fledermäuse, was {damage} Schaden verursacht!",
        "Mit einem gezielten Hieb vertreibst du einige der Fledermäuse, sie erleiden {damage} Schaden!",
        "Du wirbelst dein Schwert durch die Luft und triffst den Schwarm. Sie verlieren {damage} Gesundheit!",
    ],
    "flee": [
        "Du rennst in die Dunkelheit, doch die Fledermäuse umkreisen dich weiterhin.",
        "Mit einem schnellen Sprint entkommst du den flatternden Angreifern – gerade noch rechtzeitig!",
    ],
    "special_event": [
        "Ein besonders große Fledermaus stößt einen durchdringenden Schrei aus und schüchtert dich kurz ein!",
        "Die Fledermäuse ziehen sich zurück und umkreisen dich aus der Dunkelheit, bevor sie erneut angreifen.",
        "Ein Teil des Schwarms stürzt sich mit unglaublicher Geschwindigkeit auf dich zu!",
    ],
    "win": [
        "Mit einem letzten Schlag vertreibst du den Schwarm! Die Höhle gehört dir!",
        "Die Fledermäuse flüchten kreischend in die Dunkelheit. Du hast den Schwarm besiegt!",
        "Der Schwarm löst sich langsam auf, während du triumphierend in der Höhle stehst.",
    ],
    "lose": [
        "Die Fledermäuse attackieren unaufhaltsam. Du gehst geschlagen zu Boden. Deine Reise endet hier.",
        "Der Schwarm überwältigt dich und du verlierst das Bewusstsein in der Dunkelheit der Höhle.",
        "Mit ihren scharfen Krallen und Zähnen setzen dir die Fledermäuse so stark zu, dass du keine Kraft mehr hast.",
    ]
}


########################################################################
# 4. Pfad

untoter_pirat_texts = {
    "attack": [
        "Du schwingst dein Schwert gegen den untoten Piraten und triffst ihn mit einem mächtigen Schlag, was {damage} Schaden verursacht!",
        "Mit einem gezielten Hieb durchtrennst du die verdorrte Haut des Piraten, er erleidet {damage} Schaden!",
        "Du triffst den Piraten mit einem kräftigen Schlag, seine Knochen knirschen, und er verliert {damage} Gesundheit!",
    ],
    "flee": [
        "Du ziehst dich zurück und entkommst dem untoten Piraten.",
        "Mit einem schnellen Sprint fliehst du und lässt den Verfolger hinter dir.",
    ],
    "special_event": [
        "Der untote Pirat stößt einen unheimlichen Schrei aus, seine Kehle klingt wie das Klirren von rostigem Metall. Du fühlst dich kurz schwach!",
        "Der Pirat erhebt sich aus seiner knöchernen Hülle, seine verdorbenen Gliedmaßen ergreifen dich für einen Moment!",
        "Seine leeren Augen glühen plötzlich rot auf, und du spürst eine lähmende Kälte, die deine Bewegungen hemmt!",
    ],
    "win": [
        "Mit einem letzten, kräftigen Schlag zerbrichst du den Piraten in Stücke! Das Schiff gehört dir!",
        "Der untote Pirat zerfällt zu Staub, und du stehst triumphierend über den Überresten des Fluchs.",
        "Du besiegst den Piraten und das Geisterschiff gibt einen markerschütternden Schrei von sich, bevor es sich langsam auflöst.",
    ],
    "lose": [
        "Der untote Pirat schlägt mit seinen knöchernen Fäusten zu. Du gehst zu Boden und verlierst das Bewusstsein.",
        "Der Pirat packt dich mit übermenschlicher Kraft, seine eisige Berührung lähmt dich, und du verlierst alles.",
        "Der Pirat drückt sein verrottetes Schwert in deine Seite, und du spürst, wie das Leben aus dir entweicht.",
    ]
}

seeungeheuer_texts = {
    "attack": [
        "Du wirfst dich in die Schlacht und schlägst mit deinem Schwert auf das Seeungeheuer ein, was {damage} Schaden verursacht!",
        "Mit einem kräftigen Hieb durchtrennst du die zähflüssige Haut des Ungeheuers, es erleidet {damage} Schaden!",
        "Du triffst das Seeungeheuer mit einem gezielten Angriff, und es brüllt vor Schmerz, verliert dabei {damage} Gesundheit!"
    ],
    "flee": [
        "Du ziehst dich zurück und entkommst dem Seeungeheuer.",
        "Mit einem Sprung fliehst du, und das Seeungeheuer verliert deine Spur.",
    ],
    "special_event": [
        "Das Seeungeheuer blubbert laut und stößt eine gewaltige Welle aus, die dich fast vom Schiff fegt!",
        "Mit einem gewaltigen Sprung verschwindet das Seeungeheuer unter der Oberfläche des Wassers, nur um dann mit voller Wucht zurückzuspringen!",
        "Ein riesiger Tentakel schlägt aus dem Wasser und trifft dich und bringt dich aus dem Gleichgewicht!"
    ],
    "win": [
        "Mit einem letzten, entschlossenen Schlag schlägst du das Seeungeheuer zurück und es sinkt in die Tiefen des Ozeans!",
        "Du zerschmetterst die monströsen Tentakel des Ungeheuers, und es gibt einen letzten verzweifelten Schrei, bevor es stirbt!",
        "Mit einem letzten Angriff besiegst du das Seeungeheuer und das Schiff wird von seiner schrecklichen Präsenz befreit!"
    ],
    "lose": [
        "Das Seeungeheuer trifft dich mit einem mächtigen Schlag, du wirst in die Tiefe gerissen und verlierst das Bewusstsein.",
        "Mit seinen schrecklichen Tentakeln packt das Seeungeheuer dich und zerrt dich in die dunklen Tiefen des Meeres!",
        "Ein riesiger Tentakel trifft dich mit voller Wucht, und du verlierst das Bewusstsein, als das Ungeheuer dich in die Tiefen zieht."
    ]
}

########################################################################
# 5. Pfad
tempelwaechter_texts = {
     "attack": [
        "Mit einem blitzschnellen Schlag wehrt der Wächter deine Attacke ab und kontert!",
        "Seine heilige Waffe glüht auf und trifft dich mit einer mächtigen Energie!"
    ],
    "flee": [
        "Du fliehst erfolgreich vor dem Wächter.",
        "Die Wächteraugen verlieren dich in der Dunkelheit.",
    ],
    "special_event": [
        "Mit erhobenem Hammer nähert er sich dir, der Boden vibriert bei jedem Schritt.",
        "Ein bedrohliches Grollen füllt die Luft, während er langsam auf dich zukommt."
    ],
    "win": [
        "Du hast den Wächter überzeugt und darfst eintreten.",
        "Mit großer Mühe besiegst du den Wächter und gewinnst Zugang zum Tempelinneren."
    ],
    "lose": [
        "Der Wächter ist zu stark. Du liegst am Boden und kannst dich nicht mehr rühren.",
        "Die heilige Kraft des Tempels vertreibt dich."
    ]
}

geist_actions = [
            "Der Geist stößt einen eisigen Schrei aus, der dich für einen Moment lähmt und Schaden verursacht!",
            "Der Geist greift in deine Gedanken und erzeugt Illusionen, die dich verwirren und deinen nächsten Angriff schwächen!",
            "Plötzlich verschwindet der Geist und taucht hinter dir auf, um dir mit seiner geisterhaften Waffe Schaden zuzufügen!",
            "Ein dunkler Nebel umhüllt dich, der langsam deine Lebensenergie absaugt!"
        ]

###########################################################################################################
# Dialoge für Rätsel
###########################################################################################################

# Die Dialoge für Rätsel sind jeweils als Liste von strings abgespeichert.

# Rätsel-Erfolg
rätsel_erfolg = [
    "Arrr! Du bist ein schlauer Seefahrer! Das Rätsel hast du geknackt wie eine harte Nuss!",
    "Ahoi, du kluger Kopf! Du hast das Rätsel gemeistert wie ein wahrer Piratenkapitän!",
    "Gut gemacht, du scharfsinnige Landratte! Dieses Rätsel hatte keine Chance gegen dich!",
    "Arrr, dein Verstand ist so scharf wie ein Piratensäbel! Das Rätsel ist gelöst!",
    "Bravo, Kamerad! Dein schlauer Kopf ist ein wahrer Schatz auf dieser Reise!",
    "Hehe, das war ein Kinderspiel für einen cleveren Piraten wie dich!",
    "Gut gemacht! Dein Verstand leuchtet heller als ein Leuchtturm im Sturm!",
    "Arrr! Deine Klugheit wird bald in allen Tavernen erzählt, mein Freund!"
]

# Gold-Belohnung
gold_fund_varianten = [
    "Arrr! Du hast das Rätsel gelöst und einen verborgenen Schatz gefunden!",
    "Glückwunsch, cleverer Seefahrer! Ein Beutel voller Gold gehört jetzt dir!",
    "Fantastisch! Das Rätsel ist gelöst und du hast kostbares Gold entdeckt!",
    "Gut gemacht, Landratte! Deine Klugheit hat dir eine Truhe voller Gold eingebracht!",
    "Arrr! Deine Schläue hat dir einen Schatz voller Gold beschert!"
]



###########################################################################################################
# Alle Rätsel
###########################################################################################################

# "rätsel" ist eine Liste von Dictionaries der Rätsel
# Jedes Rätsel ist eine Dictionary mit den zwei Schlüsseln "frage" und "antworten".
# "frage" enthält den Text der Frage
# "antworten" enthält eine Liste der Antwortmöglichkeiten, wobei die 1. immer die richtige ist.

rätsel = [
    {
        "frage": "Ich kann verloren gehen, aber niemals gefunden werden, und doch bin ich immer um dich herum. Was bin ich?",
        "antworten": ["Die Zeit", "Der Wind", "Der Horizont", "Eine Erinnerung"]
    },
    {
        "frage": "Was hat Zähne, aber kann nicht beißen?",
        "antworten": ["Ein Schlüssel", "Ein Blauwal", "Ein Steuerrad", "Ein alter Schatztruhendeckel"]
    },
    {
        "frage": "Ich bin immer hungrig, ich muss stets gefüttert werden. Jede Hand, die ich berühre, wird bald rot. Was bin ich?",
        "antworten": ["Ein heißes Feuer", "Eine Laterne", "Eine Sanddüne", "Ein heißer Stein"]
    },
    {
        "frage": "Hoch bin ich jung, klein bin ich alt, während ich mit Leben glühe, ist Wind mein Feind. Was bin ich?",
        "antworten": ["Eine Kerze", "Eine Lampe", "Ein Leuchtturm", "Ein Lagerfeuer"]
    },
    {
        "frage": "Ich habe Tasten, die Musik machen, aber keine, die Türen öffnen. Was bin ich?",
        "antworten": ["Ein Piraten-Akkordeon", "Eine Schatztruhe", "Eine alte Schreibmaschine", "Eine Muschel"]
    },
    {
        "frage": "Was hat einen Ring, aber keinen Finger?",
        "antworten": ["Eine Schatzkarte", "Ein Piratenkompass", "Ein Goldring", "Ein Fernrohr"]
    },
    {
        "frage": "Was hat einen Hals, aber keinen Kopf?",
        "antworten": ["Eine Flasche Rum", "Ein Fass Bier", "Ein verfluchtes Skelett", "Ein Fernrohr"]
    },
    {
        "frage": "Was ist immer vor dir, aber du kannst es nicht sehen?",
        "antworten": ["Die Zukunft", "Der Wind", "Ein Piratenschiff im Nebel", "Der Horizont auf See"]
    },
    {
        "frage": "Ich spreche ohne Mund und höre ohne Ohren. Ich habe keinen Körper, aber ich lebe auf, wenn der Wind weht. Was bin ich?",
        "antworten": ["Eine Piratenflagge", "Ein Segel", "Ein Papagei", "Eine Glocke"]
    },
    {
        "frage": "Was kommt einmal in einer Minute, zweimal in einem Moment, aber nie in tausend Jahren?",
        "antworten": ["Der Buchstabe „M“", "Der Buchstabe „N“", "Ein Piratenschwert", "Ein Kanonenschuss"]
    },
    {
        "frage": "Du kaufst mich, um zu essen, aber isst mich nie. Was bin ich?",
        "antworten": ["Ein Teller", "Salz", "Ein Piratenkrug", "Sardinen"]
    },
    {
        "frage": "Ich gehe hoch und runter, bewege mich aber nie. Was bin ich?",
        "antworten": ["Ein Anker", "Eine Welle", "Eine Hängematte", "Ein Steuerrad"]
    },
    {
        "frage": "Was kann um die Welt reisen, während es in einer Ecke bleibt?",
        "antworten": ["Eine Briefmarke", "Eine Schatzkarte", "Ein Anker", "Eine Kompassnadel"]
    },
    {
        "frage": "Ein Pirat hat drei Kisten voller Schätze: Eine mit Gold, eine mit Silber und eine mit Edelsteinen. Jede Kiste hat ein anderes Gewicht, aber insgesamt wiegen sie 120 Kilogramm. Das Gold wiegt doppelt so viel wie das Silber, und die Edelsteine wiegen so viel wie das Silber und das Gold zusammen. Wie viel wiegt die Kiste mit den Edelsteinen?",
        "antworten": ["80 Kilogramm", "40 Kilogramm", "60 Kilogramm", "100 Kilogramm"]
    }
    
]

###########################################################################################################
# ASCII-Grafiken 
###########################################################################################################

# Alle ASCII-Grafiken sind als ein- oder mehrzeilige strings gespeichert.

## Spielmenü/Event-Grafiken

# Titelbildschirm
piraten_logo_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡔⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣯⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⡙⢿⣿⣿⣿⣿⣿⣿⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⠿⠿⢟⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡏⠉⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡿⡍⠳⣄⡀⢀⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢿⡄⠸⡿⢄⠛⣘⢠⣼⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣼⡻⡄⠳⡤⠽⠾⠿⠿⠿⢛⣻⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣄⠙⢶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⢉⣁⣀⣀⣀⣀⣀⣉⡉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣯⣻⣍⡲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⢀⡀⣶⣤⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣁⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣈⠛⢿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⡿⠟⠛⠛⠁⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣝⢿⣿⣿⣿⣿⣿⣿⣟⣡⣶⠿⢛⣛⣉⣭⣭⣤⣤⡴⠶⠶⠶⠶⢲⣴⣤⠭⠭⡭⣟⠻⠦⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣀⣠⣶⣿⣆⠀⠀
⠹⣿⣿⣿⣿⣿⣿⣙⠻⣿⣮⣛⠿⣿⣿⣿⣫⣵⡶⠟⣛⣋⣭⣭⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣮⣽⣿⣿⣿⠿⠟⠛⠉⢀⣴⣿⣿⣿⣿⣿⣿⣶⡀
⠀⠈⠙⠋⠁⠀⠈⠉⠛⠳⣭⣛⢷⣦⣸⣿⣯⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⡟⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⠿⢿⣹⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡏⣀⣴⣾⣿⣿⠿⠛⠉⠀⠀⠀⠈⠛⠛⠉⠀
⠀⠀⠀⠀⢀⣴⠿⠛⠋⠁⠀⠀⠀⢀⣯⢿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠣⣟⡻⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⠈⡿⣿⠃⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠀⠈⠉⠛⣿⣽⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⣻⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⢹⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣰⣿⢣⡇⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠟⠋⠙⠛⠻⣿⣿⣿⣿⣿⠏⠀⠈⢿⣿⣿⣿⣦⣄⣀⣀⣀⣠⣴⣿⣏⡞⢻⣸⣿⣷⣄⠀⠀⣀⣤⠴⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠃⠀⠀⠀⠈⢿⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣶⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⠀⠀⠀⠀⠀⣀⣼⣿⡛⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣡⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⢠⣶⣿⣿⣯⣿⡇⠀⢹⣿⣿⣿⣿⣷⣤⣤⣦⣶⣿⣿⣿⣿⣿⡇⠀⣿⣿⢸⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣠⣴⣾⣿⣟⣿⠟⠁⣿⡇⠀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡇⢀⣿⣿⠙⢮⣛⠿⣷⣦⣄⣀⣀⣀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣶⣾⣿⣿⡿⣛⣽⠞⠋⠀⠀⠀⣿⣷⠀⣍⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠉⡄⣸⣿⡿⠀⠀⠈⠙⠮⣟⠿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣹⣿⣿⣿⢵⡿⠋⠀⠀⠀⠀⠀⠀⢿⣿⣦⣿⡷⣄⠙⠿⣿⢹⣿⣿⢼⡿⠋⣡⣶⣳⣿⣿⣿⠃⠀⠀⠀⠀⠀⠈⠿⠬⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣻⢿⣶⣬⣈⣉⣉⣤⣴⣿⣻⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡇⣿⣇⣿⢹⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")


abtrennung = ("------------------------------------------------------------------------")

player_ship = ("""
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
         """)

# Thank you for playing
thank_you_ascii = ("""
 _____ _                 _                           __                   _             _               _ 
|_   _| |               | |                         / _|                 | |           (_)             | |
  | | | |__   __ _ _ __ | | __  _   _  ___  _   _  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _  | |
  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | | |
  | | | | | | (_| | | | |   <  | |_| | (_) | |_| | | || (_) | |    | |_) | | (_| | |_| | | | | | (_| | |_|
  \_/ |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, | (_)
                                 __/ |                             | |             __/ |         __/ |    
                                |___/                              |_|            |___/         |___/
""")


# Win-Ascii
win_ascii = ("""
        █▄█ █▀█ █░█   █░█░█ █▀█ █▄░█ 
        ░█░ █▄█ █▄█   ▀▄▀▄▀ █▄█ █░▀█
""")

# Lose-Ascii
lose_ascii = ("""
        █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█ 
        █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄
""")


#############################################
# 1. Pfad
pirat_ascii = ("""
                ⣴⣾⣿⣿⣿⣿⣷⣦ 
                ⣿⣿⣿⣿⣿⣿⣿⣿           
                ⡟⠛⠽⣿⣿⠯⠛⢻            
                ⣧⣀⣀⡾⢷⣀⣀⣼           
                 ⡏⢽⢴⡦⡯⢹                
                 ⠙⢮⣙⣋⡵⠋
""")


jaguar_ascii = ("""
⠀⠀⠀⠀⠀⣀⠀⠀⠀⣤⣤⣤⣄⡀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣬⠄⠩⣽⣾⣧⣄⠀⠀⠈⠁⠒⠢⠉⠁⠀⠒⠠⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡔⠋⢫⣷⣶⣤⣴⣿⣟⡻⣷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠐⠢⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢶⡖⡟⢉⣷⠀⣸⣏⡭⣽⣙⣻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡀⠉⠀⠂⠄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⣮⣿⠞⠉⠀⠀⠀⡀⢉⡻⡿⠿⣷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⠀⠂⠄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠁⠀⠀⣠⠒⠁⣈⣉⣉⣉⣉⣉⣉⠉⠀⠀⠀⠀⣲⣶⣴⣄⣄⣠⣠⣶⣶⣶⣤⣄⣀⡉⠀⠀⠀⠈⠐⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠁⠀⣾⠏⠉⠀⠾⣉⡹⠿⢿⡿⣶⣷⣿⡿⠉⠿⢹⠿⡿⢿⠿⠿⠉⠉⢉⣿⣿⣶⡀⠀⠀⠀⠀⠰⡉⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠊⠶⠁⠀⠀⠀⠀⠀⠈⠉⠑⠒⠢⠛⠛⠙⠳⠶⠶⠶⠴⠶⠶⠚⠛⠛⠓⠻⢿⣿⣷⣄⠀⠀⠀⠀⠰⣤⣄⣁⠢⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⠀⠀⠈⠛⠿⠿⠦⢌⣐⡢⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡟⡿⠶⢦⠤⣤⢤⡤⠭⢭⣅⣀⠀⠐⢬⣐⠠⡀⡀⠀⠀⢀⣀⡄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠪⠤⠥⠦⠕⠚⠓⠒⠪⠽⣳⣤⡀⠻⣿⣲⣬⣙⣚⣉⣴⡶⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢿⣶⣬⣁⣧⠁⠈⠈⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠘⠂⠉⠀⠀⠀⠀⠀⠀
""")

jaguar_fight_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⡴⣶⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣷⣿⣶⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⠿⠿⠛⠛⠛⠋⠉⠉⠉⠛⠛⠛⠛⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⣻⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀⣀⣤⣄⢴⣖⣒⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣟⡁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠟⠋⠀⠀⠀⣀⣤⣦⣿⣿⣿⣿⣿⣯⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠿⠿⠿⣿⣿⣷⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⣀⣶⣿⣿⡟⠯⠍⠋⢁⣀⣠⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣄⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣦⣤⣴⣿⣿⣟⣋⣡⣤⠴⠖⠋⢉⣽⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⡀
⠀⠀⢠⣿⠟⠉⠁⠈⠉⠉⠙⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⢠⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠽⠟⠛⠉⠀⢀⣀⣥⣴⣶⣶⣶⣶⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣷⣶⣦⣤⣤⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠁⠂⠈⢉⠛⠿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠘⢿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠁⠀⠂⠽⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣴⣿⣿⣄⠀⠀⠀⠀⠀⣀⣠⣴⠶⣿⣿⠋⠉⠉⠉⠙⢻⣿⡆⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⡍⠛⠻⢷⣶⣶⣶⠟⢿⣿⠗⠀⠹⠃⡀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢀⣴⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⡇⠀⠀⠀⢻⣽⣿⠀⠈⠛⠀⠀⠀⢹⠇⠀⠀⠀⠀⢶⣿⠇⠀⢀⣴⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠁⠀⠀⠀⠀⠹⡇⠀⠀⠀⠀⠀⣀⡾⠀⠀⠀⠀⠀⢸⡿⠀⣠⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⣦⠀⠀⢠⣿⢳⠀⠀⠀⠙⣿⣿⠁⢰⣿⡿⣻⡿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣷⡾⠿⠃⢸⣷⣀⠀⢀⣾⠃⢀⣿⣿⣻⣿⡿⡯⣻⣣⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠻⠷⢾⣿⣿⣷⡿⠁⠀⢸⣿⣟⡿⣏⣿⣿⣿⣯⣿⣗⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣷⣄⠀⠀⠉⠛⠀⠀⠀⢸⣿⡇⠈⠉⠛⢧⣝⣟⣯⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣦⣄⡀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠉⠙⠯⣯⣿⣿⣷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣶⣶⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠻⠯⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠃⠀⠀⠀⠀⠀
""")

jaguar_begleiter = ("""
      ("`-''-/").___..--''"`-._
       `6_ 6  )   `-.  (     ).`-.__.`)
       (_Y_.)'  ._   )  `._ `. ``-..-'
     _..`--'_..-_/  /--'_.' ,'
    (il),-''  (li),'  ((!.-'
""")

#############################################
# 2. Pfad

inselbewohner_ascii = ("""

⠀⠀⠀⠈⢙⣶⣤⣬⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣀⠴⠚⠋⠉⠉⠀⠀⠉⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠙⠓⠋⠙⠛⠿⢿⣿⣿⣿⣿
⠁⢀⣠⣴⣶⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣤⣤⣌⡙⠉
⣴⣾⠟⠋⠀⠀⠀⠈⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠀⠉⠻⣿⣄
⣿⠃⠀⠀⣠⣾⣿⣷⡄⠠⢹⡀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⣰⣶⡿⢶⡄⠀⠈⣿
⠿⣦⠤⠤⠿⠿⠿⢿⣇⣀⣰⡇⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⢿⣻⣿⣿⢇⣀⣀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣄⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠀⠀⠀⠀⠀
⡆⠀⠀⠀⠀⠀⠙⢿⣿⣟⠛⠛⠻⠿⠿⠿⠿⠿⠛⠛⢛⣿⡿⠟⠋⠀⠀⠀⠀⢠
⣿⣄⠀⠀⠀⠀⠀⠀⠈⠩⢝⡛⠒⠒⠲⠶⠶⠖⠒⢒⡯⠃⠀⠀⠀⠀⠀⠀⣠⣿
⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠒⠒⠂⠐⠋⠁⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣶⣿⣿⣿⣿⣿

""")


falle_fuß = ("""

⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠀⠀⣾⡆⠀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⡄⠀⠀⠀⠀
⠀⠀⣾⣆⣼⣿⣧⣤⣴⣿⣇⠀⢀⣾⠀⠀⢀⣆⠀⠀⣸⣧⠀⠀⢰⣷⠀⠀⡀⠀
⠀⣸⡟⠋⠉⠉⠉⠙⠛⠻⠿⣿⣿⠟⢀⡀⠘⣿⣶⣶⣿⣿⣶⣶⣾⣿⣤⣼⡇⠀
⠀⣿⠁⠀⣼⠀⠀⠀⠀⠀⠀⠀⠈⠀⠛⠛⠀⠛⠉⠉⠉⠉⠉⠉⠉⠉⠛⢿⣇⠀
⠀⢻⣧⣴⣿⠀⠀⠀⣰⠀⠀⠀⢶⣶⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⢀⣇⠀⢸⣿⠀
⠀⠈⠻⣿⣿⣤⣀⣼⣿⠀⠀⠀⡀⠉⣉⠉⠉⠁⠀⠀⢠⣇⠀⠀⢸⣿⣤⣼⠇⠀
⠀⠀⠀⠀⠙⠻⢿⣿⣿⣤⣀⣾⡇⠀⠻⠀⢠⣧⠀⠀⣼⣿⣤⣴⣿⣿⠿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠟⠀⣶⣶⡄⢸⣿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")


#############################################
# 3. Pfad

piraten_kapitän = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⣄⠀⠀⣠⣾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠹⣿⠟⠛⠛⠻⣿⠏⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣷⣦⠀⡰⢿⡿⢆⠀⣴⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠿⠀⢳⠚⠓⡞⠀⠻⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⡛⠉⣤⣴⣷⣤⣉⣉⣤⣾⣦⣤⠉⢛⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⠿⠒⢋⣉⣡⣤⣤⣤⣤⣌⣉⡙⠒⠻⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⠿⠏⠀⠛⠛⠋⠉⠉⣉⣉⡉⠉⠙⠛⠛⠀⠻⠿⣿⣿⣆⠀⠀⠀
⠀⠀⢾⣯⣠⠄⢀⡄⢰⣾⠿⠿⠿⢿⡿⠿⠛⣉⣤⣶⣶⡆⢠⡀⠠⣄⣽⡷⠀⠀
⠀⠀⠀⠉⣁⣴⠟⠁⠈⡀⠀⠀⠀⠀⣴⣶⣎⠉⠉⣠⣿⠇⢈⣻⣦⡈⠉⠀⠀⠀
⠀⠀⢤⣾⣋⣁⣠⣴⠀⣿⣄⣀⣤⠞⠛⠛⠻⣿⣿⣿⣿⠀⣿⠉⣿⠙⢶⡄⠀⠀
⠀⠀⠀⠈⠉⢉⣿⠃⠀⢹⣿⣿⠿⠋⢁⡈⠙⠿⣿⣿⡏⠀⠙⠿⣿⠿⠛⠁⠀⠀
⠀⠀⠀⢀⣴⡟⠁⠀⠀⠈⠉⠀⢀⠀⠈⠁⠀⡀⠀⠉⠁⠀⠀⠀⠹⣧⡀⠀⠀⠀
⠀⠀⠶⠿⣯⣤⣤⣤⣤⣄⠐⠾⣿⠟⠁⠈⠻⣿⠷⠂⣠⣤⣤⣤⡶⠿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")


fledermäuse_ascii = ("""

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⠟⠉  ‿	෴🦇෴‿ 		🦇
  🦇     ‿෴🦇෴‿ ⠀⠀⠀  ⠀⢿⣿⣿⣿⣿⣿⣿⣇
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⡀⠈⣿⣿⣿⣿⣿⠟⠋
        ⠀⠀⠀⠀⠀⣀⣄⠀⠀⢿⣶⣾⣿⣿⣇⣼⣿⣿⣿⣿⡃   		🦇		‿෴🦇෴‿ 
        ⠀⠀⢀⣰⣾⣿⣿⣷⣄⣈⣉⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆
    🦇  ⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅  🦇 
        ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣦
        ⢸⡟⠋⠉⠉⠙⠋⠀⠀⠉⠛⠋⠉⠛⠿⣿⡟⠻⠅⠈⠷⠆   ‿෴🦇෴‿ 
        ⠘⠀   ⠀           ⠀⠈⣧⠄
        ⠀⠀⠀‿෴🦇෴‿ ⠀⠀⠀⠀⠀⠈
""")







#############################################
# 4. Pfad

shipwreck_ascii = ("""⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣿⣿⣷⣄⠙⢷⣾⠟⣷⣄⠀⠀⠀⠀⣠⣿⣦⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣄⠙⢿⣏⣹⣷⣄⠀⢴⣿⣿⠃⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠀⠸⣦⡙⠻⣿⣿⣿⣿⣷⣄⠙⢿⣤⡿⢷⣄⠙⠃⠀⠀⠀⠀⣀⡈⠻⠂⠀
⠀⠀⠀⠀⠈⠻⣦⡈⠻⣿⣿⣿⣿⣷⣄⠙⢷⣾⠛⣷⣄⠀⠀⢀⣴⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣦⡈⠛⠛⠻⣿⣿⣷⣄⠙⠛⠋⢹⣷⣄⠈⠻⠛⠃⠀⠀⠀
⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀
⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀
⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀
⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀
""")

untoter_pirat_ascii = ("""
⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠁⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠁⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⠇⢀⣷⠘⢿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⢟⣯⣿⡿⢻⠏⣦⠉⠋⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢀⣾⣿⣄⠈⢻⡓⠟⢻⣿⣇⣧⣸⡿⢿⣿⡇⣻⣿⠞⢿⣧⠏⣼⣷⣄⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠃⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣼⣿⣿⣿⣷⡀⠈⢸⣀⢸⣿⣿⠿⡃⣼⣿⣻⢻⣿⣠⠟⣣⣾⣿⣷⣿⡆⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡅⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢰⣿⣾⡟⠀⠻⡿⣦⡀⠈⠉⠙⢺⢸⣏⣿⢣⣟⡚⠛⣀⣾⡿⠛⠁⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿
⣿⡿⠃⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⢿⣿⣧⡀⠸⠿⠞⠻⣦⣀⣠⢟⣿⣿⣿⣈⡁⣠⣾⠟⠛⣿⣤⣾⣿⡿⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⢻⡝⣿⣿⣿⣿⣿
⡏⠁⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠹⠿⣿⣷⣶⣶⣶⡿⣿⣷⡿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⠟⠟⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠹⣟⠻⣿⣿⣿
⠂⠀⣰⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⣠⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠈⠙⠲⣿⣿⣿⠃⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠰⣄⠀⢹⣿⣿⣿⣿⣿⣿⣿⡅⢸⠀⠙⣆⢻⣿⣿
⢀⣴⣿⡿⢃⣼⢛⣿⣿⢟⣿⣿⣿⣿⣿⢀⣞⡥⠚⠀⠀⠀⠀⣀⣠⠤⠄⠀⠀⢠⣾⣿⣿⣧⡄⠀⠀⠰⠲⢦⣀⠀⠀⠀⠈⠉⢑⣺⣷⡌⣿⣿⣿⣿⣿⣿⣿⡇⣿⠂⠀⠘⢯⣿⣿
⣾⣿⠟⢁⣼⡏⣸⣿⡟⢲⢈⣿⣿⣿⡏⣾⣿⣷⡶⢶⣶⣶⣿⣿⠿⣶⢦⡀⠀⠈⠛⠿⣿⡿⠃⠀⣀⣴⡶⢺⣿⣹⣷⣾⣿⡿⣿⣿⣿⡇⢻⣿⡏⢿⣿⣿⣿⣇⣿⡄⠀⠀⣼⣿⣿
⠟⠁⠀⢸⣿⠁⣿⡿⣰⣡⣿⢇⣿⣿⠁⢻⣯⣿⣍⠻⠭⣹⣿⣿⣿⣧⣼⣿⣦⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⠵⣿⡏⡇⠸⣿⣿⠘⣧⣿⣿⣿⣾⠄⠀⣴⣿⣿⣿
⠀⠀⠀⢸⣿⣈⣿⠃⣧⣯⣿⣸⢉⣗⠀⢸⢸⢹⣏⢳⣤⣈⠙⠲⢿⣿⣿⣻⢿⣷⣶⣤⣴⣶⣾⣿⡿⣿⣿⠿⠟⠛⣉⡤⠚⡇⢸⣟⢧⡇⠀⣿⣿⡄⢻⣸⡯⣿⣸⡇⢤⣿⣿⣿⣿
⡀⠀⠀⠀⣿⣿⣷⣸⣿⠀⣬⣿⣿⣯⡀⠸⣿⡆⢿⡎⣇⠈⢹⠓⠦⢤⣄⣉⠉⠉⠉⠉⠉⠉⠉⠉⣉⣡⡤⠖⢺⣿⣿⠀⣀⣤⣿⣸⢸⠃⢰⣿⣿⠇⢼⣿⣿⣿⡿⣀⣾⣿⣿⣿⣿
⠁⡆⠀⠸⣿⣿⣿⣿⡏⢰⣿⣿⣿⣿⣿⡀⢿⢻⠘⣿⣿⣄⡀⠀⠀⠀⠘⡌⠉⠙⢻⠞⠉⠉⢙⣿⣿⣿⠀⢀⣸⣯⣿⣿⣿⣿⡇⡟⣾⠀⣾⣿⣿⠦⣙⡙⠍⣿⣇⣼⣿⣿⣿⣿⣟
⡀⢹⣤⣤⣟⣿⣯⣿⡿⠸⣾⣿⣯⣿⣾⣧⢘⣏⢧⠸⣿⣿⣛⣷⣦⣤⣤⣧⣀⣀⣘⣆⣀⣀⣸⡿⣿⡌⣿⡟⠛⣿⣷⠿⣿⡿⠸⢧⠏⢼⣿⣿⢹⣀⠸⢧⠀⣿⣿⣿⣿⣿⣿⣧⣹
⡇⢸⣿⣿⣿⣯⣿⠟⠁⠀⠀⠀⣷⡇⣿⣿⣼⡆⠀⠀⢹⣿⠻⣿⣟⠛⠉⠿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠛⡹⠃⠀⣿⠟⣯⣿⠇⠈⢠⣌⣿⣿⣿⡿⢸⢶⠈⠣⣾⣿⣿⣿⡽⢻⡜⡟
⡇⢸⡟⣿⣿⣿⡟⠀⠀⠀⠀⠀⣬⣿⣿⣽⡿⣷⣢⠀⠀⢿⣷⠙⢿⣦⣀⡀⠐⠿⣿⣿⣶⣷⣿⡗⠄⢂⣃⡤⠚⠉⣇⡟⡟⠀⢀⣼⣿⣿⣻⣍⢃⠘⠀⠀⠀⣿⣿⣿⢿⣧⠀⢿⣷
⣇⠀⡧⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⡇⠿⠛⠧⠙⢿⣆⡀⠘⡎⢧⣨⠀⠈⢹⡀⠀⠉⣾⠿⠯⠿⢲⡋⠉⠀⢹⠀⢠⡟⣸⠁⢀⢺⡿⠛⠙⢿⣿⢸⣴⣀⠀⣰⣿⣿⣿⢸⣿⡄⠘⣧
⣿⠀⣇⣿⡿⠁⠀⠀⠀⠀⠀⠀⠁⠁⠀⠀⠀⠀⠸⢿⣿⣀⠹⡌⠻⢦⣀⠘⣿⣶⣶⣿⠀⠀⠀⠨⡇⠀⣀⣸⣴⡟⢡⠇⢀⣿⣿⠁⠀⠀⠈⢻⡎⣿⣿⣿⣿⣿⡏⢹⢸⣿⣧⠀⢹
⡏⢰⣿⡇⠀⠀⢀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢾⣿⣿⡄⠙⢦⡀⠈⠉⠛⠻⠿⠛⠿⢶⠾⠿⠛⠟⠛⠉⣁⣤⠟⢀⣾⣿⣿⠀⠀⠀⠀⠀⠁⠙⣿⣿⣿⣿⡆⠸⣿⡼⣿⡄⠈
⡇⢸⣾⢣⣄⣴⢾⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣿⣷⣦⠀⠉⠓⣶⡤⠤⣤⣤⣤⢤⣤⣤⣤⣶⣶⣿⡍⠀⢀⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣯⣧⡄⣿⣇⢻⣷⠀
⡷⢸⣿⣿⡟⣇⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣶⣆⣒⣿⣧⣿⣿⣿⠟⢸⣿⠟⣿⣿⡿⣇⣦⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣏⠹⣿⣿⡇⣿⣿⠀⢻⣇
⢃⣾⣼⣿⣇⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣦⣼⣿⣶⣾⣯⣷⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠈⠻⣿⣷⣿⣇⠀⢯
⣾⣿⣥⣿⣿⡿⠀⣄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⣿⡴⣿⡆⠈
⣿⣿⣿⣿⣿⡷⠸⢿⠰⢻⡷⡆⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⢸⣸⣿⣿⡏⠀
⠉⠿⣿⣿⣿⠛⢦⣼⣿⣿⡍⣇⡈⡙⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⣾⣟⣿⣿⣟⣹⡷⢿⣿⡀
""")

seeungeheuer_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⡄⠉⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣶⣷⠄⠀⢀⣧⣀⡾⢿⠀⠀⠀⡇⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⣿⣿⡿⠿⠿⢻⣿⣴⣖⡺⢧⣧⣠⣞⣄⣀⡠⠟⡚⢹⠃⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⡿⠟⠋⠉⠀⠀⣠⠞⠉⠀⠀⠀⠉⠳⣝⣧⣟⡭⣽⡻⡿⣄⡘⠒⢒⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⢰⠃⠀⠀⢀⣤⣤⡀⠀⣹⣯⡟⠀⠀⠹⣟⣎⠙⣭⠹⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⠟⠁⠀⠀⢀⣠⠴⠒⠒⠾⣄⠀⠀⠈⠻⠟⠃⢠⠏⡿⠻⡄⠀⠀⠘⣾⣆⠈⢻⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡟⠁⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⢀⡏⣼⣧⠀⠀⠀⠀⠀⠹⡽⡏⠁⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠏⠀⢀⣀⣀⣸⠃⠀⠀⢰⣿⣷⠀⠀⠀⢳⢤⣤⣴⣟⡿⣧⡉⠃⠀⠀⠀⠀⠀⢧⢹⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⣿⢏⣴⠞⠉⠀⠀⢸⠀⠀⠀⠀⠉⠉⠀⠀⢀⣿⠁⣡⣿⣿⡀⠀⠁⠀⠀⠀⠀⠀⠀⢸⡈⡇⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⠃⠀⠀⢀⣄⡈⠳⣄⡀⠀⠀⠀⢀⣠⣾⣾⣞⣿⡁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢻⠻⢤⡼⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡦⠤⣾⢯⠀⠀⠀⠻⣿⡟⠀⠈⣿⠽⣶⣿⡿⠛⣩⣷⣏⠙⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢸⠀⠲⠂⣧⠀⠀⠀⠀⠀⠀
⠀⠀⣀⠀⣀⣰⠇⣳⠾⡜⢦⡀⠀⠀⠀⠀⣀⣴⡿⠖⣋⣥⡶⢿⡇⠈⠛⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠖⣞⡛⣻⢸⠀⠀⠀⢾⠀⠀⠀⠀⠀⠀
⠀⣰⡏⠀⢹⠘⡶⠃⡴⣛⣶⣿⣷⢶⣿⡿⣿⡿⠻⣿⡉⠳⡇⠀⠁⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⣦⣽⡏⡼⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀
⢀⡇⠙⠦⠼⢳⠇⠀⡇⢧⠘⢧⢻⠀⠙⠧⠈⠓⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⣤⡰⣶⡼⢋⡼⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀
⠈⣇⡀⠀⠀⢸⡄⠀⢸⡜⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠡⣄⠀⣶⡼⠟⢉⡴⠋⠀⠀⠀⠀⢀⣀⣇⠀⠀⠀⠀⠀
⠀⠀⠉⢹⣯⠴⢧⢀⣀⠳⡌⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢺⣦⡀⣿⣦⠟⠛⣁⡤⠞⠁⠀⠀⠀⠀⠀⠀⣠⣈⣿⠀⠀⠀⠀⠀
⠀⠀⠰⠟⠛⣇⣼⡌⠧⣄⠙⣆⠳⣄⠀⠀⡄⢀⡀⠀⣦⠀⣄⡈⣷⣄⣶⡦⠗⠛⣉⣤⠴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣿⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠞⢫⡿⡇⠶⠌⠁⠈⠳⣌⡓⠦⠿⣮⣿⣦⡿⠷⠿⡛⣋⣉⡴⠶⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀
⠀⠀⣠⡞⠀⣞⣠⡇⠀⠀⠀⠀⠀⠀⢉⠓⠲⠶⠶⠶⠚⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣇⠀⠒⠈⠀⠀
⠀⠀⠉⠉⠁⠀⠈⠉⠩⢭⣉⣉⣉⠉⠉⠉⠉⠉⠉⠉⠛⠒⠒⠒⣒⣒⣒⣶⣶⣶⣶⣶⣖⣒⣶⠶⠶⠖⠉⠉⠉⠩⠭⢤⣀⣀⣀⠤⠤⠤⠒⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠒⠒⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

goldmünzen_ascii = ("""
⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠿⠿⠿⢿⣿⣷⣶⣶⣶⣦⣤⣤⣤⣤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣶⣦⠀⣶⣤⣤⣤⣤⣍⣉⣉⣉⡙⠛⠛⠛⠛⠏⣰⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣆⠸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⢸⣿⣿⣿⣿⣿⣿⣿⡏⠀⠹⠟⠙⣿⣿⣿⠄⢻⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠊⣉⡉⢋⣩⡉⠻⠛⠁⣾⣀⣴⡀⢛⡉⢠⣷⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⣷⣿⠀⢿⣿⣿⣿⡿⢁⠚⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠤⠾⠿⣿⡿⠛⣿⣿⣿⣿⣿⣷⣦⣌⣉⣉⣠⣾⡷⠂⣠⠀⠀⠀⠀
⠀⠀⠀⣿⢰⣶⣶⣶⣦⠀⠀⣤⣌⣉⠉⣉⡙⠛⠛⠛⠻⠟⢁⣴⣾⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣆⠻⣿⣿⢇⣸⠀⣯⢉⣿⠀⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣷⡔⠐⣾⣿⠀⠛⠚⠿⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠿⠋⠀⠀⠀⠀
⠀⠀⠰⣦⡄⠀⠀⠈⠉⠉⠉⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠀⠛⢁⣀⡀⠲⠖⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀
""")

storm_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⡿⠿⠭⠤⠀⠀⠀⠈⠉⠉⠙⠛⠷⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⠟⠋⠁⠀⠀⠀⠒⠒⠲⠶⠶⢶⣶⣶⣤⣤⣤⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣾⣿⣿⣿⣿⡿⠶⠶⠤⠤⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠘⣿⣿⡿⠋⠉⣀⣀⣠⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣴⣶⡿⠛⠋⠉⣁⣀⣀⣀⣀⣀⣀⣀⣀⠰⣿⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣏⠀⠀⠀⠀⠈⠉⠉⣉⣉⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⠿⢿⣦⡀⠀⠀⠀⠈⠉⠉⠉⠉⢉⠉⠛⠻⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢈⣻⣶⣶⡶⠿⠟⠛⠛⠛⠛⠛⠛⠛⢿⣿⣶⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠿⣦⡀⠀⠀⠀⣀⣀⡀⠠⣤⣸⡟⠋⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣈⣻⣦⣤⣤⣄⣉⣛⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠂⠈⠉⠉⠉⠉⠙⢿⣍⠛⠛⠻⠿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⢀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣇⠀⢀⣼⠿⠟⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀
""")

sun_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡻⣤⡀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⣠⢞⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠈⠻⣦⣀⠀⠀⠀⣰⠟⠁⠀⠀⠹⣧⡀⠀⠀⠀⣀⣴⠞⠁⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠉⠛⠒⠚⠁⠀⠀⠀⠀⠀⠈⠛⠲⠖⠚⠋⠀⠀⢀⢸⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡷⢤⣄⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⢀⣤⠶⣻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠈⠙⠓⠒⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠒⠒⠛⠉⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠶⠚⠉⠉⠉⠉⠉⠉⠉⠛⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠰⣷⣤⣤⣀⣀⠀⢀⣀⣴⠏⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣄⠀⠀⠀⠀⠀⠀⠀⠈⠻⣤⣀⠀⠀⠀⠀⠀⣀⡀⠀⠀
⠀⠀⠀⠈⠻⣦⡀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⢉⡿⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⣰⠖⠋⠉⠳⢦⡀⠀⠀⠀⢀⣴⠟⠉⠉⠛⢶⡄⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⢰⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⢀⢸⠃⠀⣀⣀⡀⠈⢿⠀⠀⢀⣾⠃⢀⣤⣀⣀⠀⢿⡀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⢸⣿⠀⣾⡇⠀⢹⡆⢸⠇⠀⠸⣿⠀⣟⢁⡌⣽⡄⣸⡇⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀
⠀⣀⣀⣠⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠘⠸⣧⠙⠷⣤⠾⢡⡾⠀⠀⠀⠹⣇⠙⠿⠷⠟⣠⠟⠀⠀⠀⠀⠀⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣄⣀⠀
⠙⠛⠿⠶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠈⠻⠶⠶⠾⠋⠀⠀⠀⠀⠀⠈⠛⠶⠶⠟⠉⠀⠀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠿⠛⠁
⠀⠀⠀⠀⠀⠈⠙⠳⣦⡀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢘⡷⠀⠀⠀⠀⠀⠀⠹⣇⠀⠀⠀⠀⠰⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣶⡤⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠈⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠤⠤⠤⠤⠶⠛⠋⠀⠀⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⣋⣁⣤⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠙⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠛⠁⠀⠀⠀⠀⠀⠀⢀⣠⡤⠤⠤⠤⢤⣝⣶⣄⠀⠀⠀
⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢤⣄⣀⣀⠀⠀⠀⢀⣀⣀⡤⠴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠁⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣁⡤⠖⠛⠉⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠉⠛⠶⣄⡸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⠟⠁⠀⠀⠀⠀⠀⠀⢘⡇⠀⠀⠀⣀⣠⡤⣄⡀⠀⠀⠀⠀⠀⠀⣀⣤⢤⣄⡀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠙⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣠⠞⠋⠁⠀⠈⠻⣄⠀⠀⠀⢀⡼⠋⠀⠀⠈⠙⢶⣄⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣣⠞⠁⠀⠀⠀⠀⠀⠀⠹⡆⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠙⢦⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

clouds_ascii = ("""
⣿⣿⣿⣿⣿⣿⣿⣛⣻⡻⣷⣦⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣴⣾⣿⣿
⣿⣿⣷⣾⣾⠿⡯⣿⣿⣿⣪⢿⡿⠿⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣹⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣾⣿⡔⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠿⣻⢟⠟⢻⡆⠿⢿⣿⡿⢛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡰⣾⣿⢟⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣭⣭⣽⣯⣯⠜⣻⠿⢿⠿⢟⣛⣛⣛⣩⣽⣒⡿⢿⡿⠷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣶⣙⣛⣭⣴⣶⣌⣛⣛⣛
⣿⣿⣿⣿⣿⣿⠿⣛⣵⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣐⣪⠻⣿⣿⠟⢫⠶⠶⣬⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣭⣥⣭⣭⣭⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠈⣭⣾⣿⣿⡘⣡⣾⢆⣭⣽⣹⣟⠙⢨⢴⣒⠲⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⡀⠘⠾⢵⣙⣻⣿⡿⢃⣿⣿⣿⣿⣿⣿⢩⡶⠦⢄⢺⡇⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⢄⠀⠏⢗⣒⣛⣿⣷⣾⣿⣿⠿⢟⣻⣿⠿⠚⠄⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣒⣠⣚⣞⣮⣧⣴⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⢻⣻⠻⢿⣿⣿⣿⠿⠏⡴⠬⢍⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠣⢨⡝⢻⣿⣆⠟⠩⠚⠻⢻⢛⣞⡙⠲⠄⣶⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⣿⣿⣿⣿⢘⠪⢹⣙⣐⣒⣾⣿⣿⣿⣿⣿⣶⣶⣾⣿⣼⣶⣌⢹⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣈⣬
⣿⣿⣿⣿⣜⢶⣘⢀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⡆⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢻⣫⣼⠾⣹⣶⣿
⣿⣿⣿⣿⣿⣶⣜⡲⢜⢶⢌⣹⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⠟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⡰⠶⢾⠷⠶⠪⣍⣍⣴⡶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣮⣤⣔⣒⣚⣛⣟⣻⣛⣛⣭⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣓⣊⣟⡋⣼⡶⣣⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⢶⠤⠼⠭⢯⣷⣷⣿⣿⣴⣿⣿⡿⡿⠿⠿⢟⣛⡛⠿⣿⣿⣿⡿⢋
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢛⣛⣛⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⢰⣶⢪⡭⣠⢨⣤⣤⣀⡈⢓⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡀⢴⠊⢠⣶⣦⡰⠻⠻⢿⣻⣿⢿⣿⣬⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣢⣾⢸⣿⣿⣿⣿⣿⣿⣿⣟⣟⣟⣟⠯⠴⡔⢉⠛⠿⠿⠿⢟⣛⡛⠿⢿⣿⣿⣿⣿
⠿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡩⢠⢚⣒⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠿⢿⣷⣷⣷⣿⣷⣶⡸⣶⡏⣿⣷⡮⠹⢿⣿
⣝⣣⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⡾⣸⣷⣾⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣋⠇⠜⢟⡛⡿⡿⡟⣸⣿⣶⣛⣫⣽⠰⣾⣿
⣯⣭⣛⣓⣊⢭⣛⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⡨⢼⢨⢯⢷⢿⣮⠦⠼⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⢃⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣦⣰⣽⣛⠿⣿⣿⣿⣿⣿⣿⣧⣐⢲⠤⣴⠵⠷⢖⣒⣒⣋⣴⣾⣿⣿⣿⣶⣶⣭⣝⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⡺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣬⣭⣭⣭⣭⣭⣴⣶⣿⣿⣿⣿⣿⣿⣿
⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣻⣩⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣶⣬⣽⣽⣭⣬⣽⣭⣿⣵⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

#############################################
# 5. Pfad
temple_ascii = ("""
 `,.      .   .        *   .    .      .  _    ..          .
     \,~-.         *           .    .       ))       *    .
          \ *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_\_.       .       .   ,-'
  -                 `-_.,     |n|     .      .       ;
    -                    \ ._/_,_\_.  .          . ,'         ,
     -                    `-.|.n.|      .   ,-.__,'         -
      -                   ._/_,_,_\_.    ,-'              -
      -                     |..n..|-`'-'                -
       -                 ._/_,_,_,_\_.                 -
         -               ,-|...n...|                  -
           -         ,-'._/_,_,_,_,_\_.              -
             -  ,-=-'     |....n....|              -
              -;       ._/_,_,_,_,_,_\_.         -
             ,-          |.....n.....|          -
           ,;         ._/_,_,_,_,_,_,_\_.         -
  `,  '.  `.  ".  `,  '.| n   ,-.   n |  ",  `.  `,  '.  `,  ',
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][
                     |     //=====\\     |
                     |____//=======\\____|
                         //=========\\
""")

wächter_ascii=(r"""
  ,   A           {}
 / \, | ,        .--.
|    =|= >      /.--.\
 \ /` | `       |====|
  `   |         |`::`|
      |     .-;`\..../`;-.
     /\\/  /  |...::...|  \
     |:'\ |   /'''::'''\   |
      \ /\;-,/\   ::   /\--;
      |\ <` >  >._::_.<,<__>
      | `""`  /   ^^   \|  |
      |       |        |\::/
      |       |        |/|||
      |       |___/\___| '''
      |        \_ || _/
      |        <_ >< _>
      |        |  ||  |
      |        |  ||  |
      |       _\.:||:./_
      |      /____/\____\
""")

sword_ascii = ("""
 n                                                                 :.
 E%                                                                :"5
z  %                                                              :" `
K   ":                                                           z   R
?     %.                                                       :^    J
 ".    ^s                                                     f     :~
  '+.    #L                                                 z"    .*
    '+     %L                                             z"    .~
      ":    '%.                                         .#     +
        ":    ^%.                                     .#`    +"
          #:    "n                                  .+`   .z"
            #:    ":                               z`    +"
              %:   `*L                           z"    z"
                *:   ^*L                       z*   .+"
                  "s   ^*L                   z#   .*"
                    #s   ^%L               z#   .*"
                      #s   ^%L           z#   .r"
                        #s   ^%.       u#   .r"
                          #i   '%.   u#   .@"
                            #s   ^%u#   .@"
                              #s x#   .*"
                               x#`  .@%.
                             x#`  .d"  "%.
                           xf~  .r" #s   "%.
                     u   x*`  .r"     #s   "%.  x.
                     %Mu*`  x*"         #m.  "%zX"
                     :R(h x*              "h..*dN.
                   u@NM5e#>                 7?dMRMh.
                 z$@M@$#"#"                 *""*@MM$hL
               u@@MM8*                          "*$M@Mh.
             z$RRM8F"                             "N8@M$bL
            5`RM$#                                  'R88f)R
            'h.$"                                     #$x*
""")

more_ghosts_ascii = ("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠈⠈⠈⠀⠀⠛⠀⠀⠙⠃⠀⠈⠋⠄⠀⠙⠁⠀⠘⠃⠀⠀⠚⠀⠀⠀⠀⠀⠀⠂⠀⠀⠙⠁⠀⠈⠂⠀⠀⠛⠀⠀⠈⠀⠀⠀⠂⠀⠀⠙⠁⠀⠈⠊⠀⠀⠛⠀⠀⠘⠃⠀⠀⠋⠀⠀⠁⠀⠀⠈⠀⠀⠀⠐⠀⠀⠐⠁⠀⠀⠐⠀⠀⠐⠀⠀⠐⠉⠀⠀⠈⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀⠀⠠⠀⠀⠀⡄⠀⠀⠠⠀⠀⠀⠄⠀⠀⠄⠀⠀⠠⠀⠀⠀⡄⠀⠀⢠⠀⠀⠀⠄⠀⠀⠄⠀⠀⠠⠀⢀⣠⣶⣼⣿⣿⣿⣿⣿⣿⣶⣤⣤⠀⠀⠠⠀⠀⠀⠄⠀⠀⢠⠀⠀⠀⠄⠀⠀⠠⠀⠀⠠⠀⠀⠀⠄⠀⠀⢠⠀⠀⠀⡆⠀⠈⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣾⣿⣿⣿⠿⠛⠛⠛⠛⠛⠛⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⡀⠀⠀⠌⠿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⡀⣀⢀⡀⢀⠀⠀⠀⠀⠀⣠⣼⣿⣿⡿⢋⣡⣴⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⡿⠋⢀⣼⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣤⣶⣿⣿⣿⠿⠿⠛⠫⠙⠉⠙⠉⠛⠟⠿⠿⠿⠿⠟⡉⠀⡀⢼⢿⣿⣿⡿⠻⠋⠀⠀⠠⣀⣤⣶⣦⣤⠀⢰⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⢀⡀⠀⠀⡀⠀⢀⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠐⠀⠀⠀⠂⡀⢣⣿⣿⣿⡿⠟⡉⠉⠘⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠐⠈⠀⠀⠀⠉⠀⠀⠀⡀⢳⣿⣿⣿⣿⣿⡇⢻⣿⣿⡗⡙⠀⠀⠂⠀⠀⠂⠀⠀⠀⠀⢁⠘⠀⠃⠀⠀⠀⠀⠀⠂⠈⠀⠀⢀⠀⡀⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⣿⣿⣿⠏⠁⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣠⣴⣌⣀⠀⠀⣿⣿⣿⣿⣿⡿⢨⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣵⣿⣿⠃⠀⣀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣿⣿⣿⣿⣿⡆⠀⢹⣿⣿⣿⠏⣥⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⠃⢠⣾⣿⣿⣿⣿⣧⠀⣠⣴⣤⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⣿⠇⠀⠀⠈⠉⠀⣼⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣟⣸⣿⣿⡟⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠈⠿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⡀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⡏⠀⠐⣿⣿⣿⣿⣿⡏⣾⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡿⠏⠀⠀⠀⠻⢿⡿⠿⠋⢀⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡿⠟⠛⠙⠛⠛⠿⣿⣿⣿⣶⣄⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠿⠁⠀⠀⠈⢂⠁⠀⠀⠀⠙⢻⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠛⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠂⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠏⠀⠀⠀⠐⡀⣀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠋⠀⠘⣿⣿⣿⣠⣴⣶⣦⡄⠀⠀⠰⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡏⠀⠀⡀⠀⠀⠀⠀⠂⠀⢤⣶⣿⣶⣄⠸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣇⠀⣼⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢈⣿⣿⣿⠀⢠⣾⣿⣷⣎⠠⠐⡀⠀⣿⣿⣿⣿⣿⡆⢹⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⢺⣿⣿⡄⠀⠀⠀⠀⠉⠁⠀⢈⣿⣿⣿⣸⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢸⣿⣿⡇⠀⣿⣿⣿⣿⣿⠂⠁⠀⠀⢽⣿⣿⣿⣿⣿⠈⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣤⡀⠀⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⢈⣿⣿⣿⣿⣿⠃⠈⠄⠀⠀⢻⣿⣿⣿⡟⠀⣿⣿⣿⣴⣦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⣀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⢸⣿⣿⡇⠀⢿⣿⣿⣿⠇⠀⡈⢀⡀⡀⠀⠙⠛⠛⠁⠀⠈⠛⠻⠿⣿⢿⣿⣿⣿⣿⣶⣆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⣦⠀⢻⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⡃⠀⠈⠙⠟⠁⠀⢀⣱⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⢿⣿⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣇⠸⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⡿⠁⠀⠀⠀⠀⠀⠐⢠⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⢦⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡿⠁⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢀⠨⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⣧⡄⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠟⢀⣴⣾⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡄⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡏⢰⣾⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡀⠀⠀⠀⠘⢿⣿⣿⡿⠃⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⣤⣴⣸⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⣻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⣀⣤⣄⣀⡀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠈⠁⠀⠀⣠⣰⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⣼⣿⣿⣿⣿⣷⠀⣽⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣦⡀⠀⣼⣿⣿⣿⣿⣿⣦⣿⣿⣿⠄⠀⠀⠀⠀⠀⢠⣼⣿⣿⣿⡿⠟⠛⠉⠉⠉⠁⠁⠈⠀⠁⠀⠀⠀⠀⠙⠻⠟⠋⠈⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣏⠀⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡟⠛⣿⣿⣿⣷⣿⣿⡟⠈⠛⣿⣿⣿⣿⣿⠂⠀⠀⠀⣠⣾⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣤⣄⠀⠀⠀⠼⣿⣿⣿⣿⠇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣀⠀⠀⠈⠀⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣇⠀⠀⠙⠻⠿⠿⠋⠀⠀⠀⠘⣿⣿⣿⠏⠀⠀⣀⣾⣿⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⠀⠀⠀⠻⠿⠟⠃⠀⣰⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣺⣿⣿⡿⠂⠀⠀⠀⣀⣀⣤⢘⣿⣿⡟⣿⣿⣿⣄⠀⢀⠠⣔⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⣤⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⢿⣿⣇⡀⠀⣰⣿⣿⣿⣿⣼⣿⣿⣷⠈⢿⣿⣿⣶⡀⠀⠹⢿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣟⢹⣿⣿⠀⢘⣿⣿⡟⢻⣿⣿⣿⣿⣿⠁⠀⠻⣿⣿⣷⣦⡀⠈⠹⠿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⣀⣤⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠂⢼⣿⡇⢨⣿⣿⣧⠀⠙⠿⠿⠟⠃⠀⠀⠀⠈⠿⣿⣿⣿⣧⣄⠀⠉⠻⠿⣷⣤⣄⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣿⣿⣿⢿⣿⣿⣷⠀⠀⢀⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣧⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⡤⢿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣷⣦⣀⡀⠀⠉⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⠀⠀⢸⣿⣿⣿⡿⠋⠀⠀⣿⣿⣿⣴⣾⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣤⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⣿⣶⣶⣤⣦⣤⣤⣤⣤⣶⣶⣶⣤⣤⣄⡀⠹⢿⣿⣿⣇⠀⠀⠈⠻⠿⠟⠀⠀⠀⠀⠘⠿⣿⣿⠿⠟⠋⠁⣻⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣶⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠈⠁⠉⠙⠻⢿⣿⣿⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⠶⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⡷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠉⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⣠⣄⣤⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⢠⣼⣿⣿⡿⠋⣼⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⡗⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⠟⠛⠁⠀⠀⠀⠀⢤⠶⡿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⡿⠋⠀⣸⣿⣿⣟⣴⣿⣿⣿⣧⡀⠀⠀⠀⣸⣿⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⡟⠋⢀⣀⣄⣤⣠⣀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⠿⠉⠀⠀⠀⢿⣿⣿⣿⣿⣿⠻⣿⣿⡧⠀⠀⢰⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⢇⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠋⠀⢸⣿⣿⡇⠀⢠⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠛⠋⠁⠁⠈⠈⠉⠛⠛⠿⣿⢿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠁⣠⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⢇⣴⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣾⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

ghost_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀
⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀
⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀
⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀
⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

graveyard_ascii = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⣿⠛⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠛⣿⣶⣤⡀⠀⠀⠀
⠀⠀⠀⢸⠛⠛⠛⠀⠛⠛⠛⡇⠀⠀⠀⠀⠀⠀⢸⠛⠛⠛⠀⠛⠛⠛⡇⠀⠀⠀
⠀⣤⣀⡈⠳⢶⣶⠀⣶⡶⠞⢁⣀⣤⣤⣤⣤⣀⡈⠳⢶⣶⠀⣶⡶⠞⢁⣀⣤⠀
⠀⣿⣿⣿⡆⠘⣿⠀⣿⠃⢰⣿⣿⣿⡏⢹⣿⣿⣿⡆⠘⣿⠀⣿⠃⢰⣿⣿⣿⠀
⠀⣀⣀⣸⡇⠀⣿⠀⣿⠀⢸⣇⣀⣀⡀⢀⣀⣀⣸⡇⠀⣿⠀⣿⠀⢸⣇⣀⣀⠀
⠀⣿⣿⠟⠃⢀⣉⣉⣉⡀⠘⠻⣿⣿⡇⢸⣿⣿⠟⠃⢀⣉⣉⣉⡀⠘⠻⣿⣿⠀
⠀⡟⢡⣶⣿⣿⣿⠛⣿⣿⣿⣶⡌⢻⡇⢸⡟⢡⣶⣿⣿⣿⠛⣿⣿⣿⣶⡌⢻⠀
⠀⡇⢸⡿⠛⠛⠛⠀⠛⠛⠛⢿⡇⢸⡇⢸⡇⢸⡿⠛⠛⠛⠀⠛⠛⠛⢿⡇⢸⠀
⠀⠃⢸⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠘⠛⠛⠃⢸⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠘⠀
⠀⠀⢸⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣤⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣤⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀
""")


gitter = ("""

⠀⣤⣤⠀⠀⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⠀⠀⠀⣤⣤⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⣾⣿⣿⣷⣄⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⢿⣿⣿⣿⣿⡿⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣙⣛⣛⣋⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⠀⠸⠿⠀⣿⣿⣿⣿⣿⣿⠀⠿⠇⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⢠⣶⡖⠂⠈⢻⣿⣿⡿⠁⠐⢲⣶⡄⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡟⠛⠃⢸⣿⣿⡇⠘⠛⢻⣿⣿⠀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⢀⠘⢿⣿⠟⢁⣼⣿⣿⣷⡀⠻⣿⡿⠃⡀⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⣸⡇⢠⣤⠀⣿⣿⣿⣿⣿⣿⠀⣤⡄⢸⣇⠀⠀⠀⠀⣿⣿⠀
⠀⣿⣿⠀⠀⠀⠀⣿⡇⢸⣿⠀⣿⣿⣿⣿⣿⣿⠀⣿⡇⢸⣿⠀⠀⠀⠀⣿⣿⠀
⠀⠛⠛⠀⠀⠀⠀⠛⠃⠘⠛⠀⠛⠛⠛⠛⠛⠛⠀⠛⠃⠘⠛⠀⠀⠀⠀⠛⠛⠀

""")


rip_ascii = ("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣤⣶⣶⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣶⣶⣶⣶⣦⣭⣭⣉⠙⠛⠛⠿⣿⣷⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣶⣿⣿⠿⠿⠛⠉⠉⠉⠉⠉⠉⠉⠉⠛⠻⠿⢿⣿⣿⣿⣶⣦⣄⡈⠩⣟⡿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣿⣿⣮⣿⢷⣯⡻⢿⢿⣷⣦⡀⠀⠀⠀
⣰⣿⡿⠋⠀⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣝⢿⣿⣷⡾⣿⣿⣦⡀⠀
⣿⣿⠀⠘⠢⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣝⢿⣛⣈⣿⣿⣷⡄
⢸⣿⡇⠀⠀⠀⢀⣠⣴⣶⣶⣶⣄⡀⠀⢀⣄⣀⠀⣀⠀⠀⠀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⢿⣻⣿⡿⠃
⠈⣿⣷⠀⠀⠀⡟⠋⠉⠁⠈⠉⢿⣷⠀⠀⠈⣿⠛⠛⠁⠀⢸⣇⠀⠈⠉⠻⣿⣦⠀⠀⠀⠀⢀⣿⣿⠙⣿⢿⣿⡿⠁⠀
⠀⢿⣿⡄⠀⠀⣿⡄⠀⠀⠀⠀⣸⣿⠀⠀⠀⣿⡄⠀⠀⠀⢸⣿⠀⠀⠀⠀⣹⣿⠀⠀⠀⢀⣾⡿⢻⣷⣿⣾⡿⠁⠀⠀
⠀⠘⣿⣧⠀⠀⢸⣇⢀⣀⣀⣴⣿⠏⠀⠀⠀⣿⡇⠀⠀⠀⢸⣿⠀⠀⠀⣠⣿⡏⠀⠀⠀⣼⣿⣏⢿⣿⣽⣿⠃⠀⠀⠀
⠀⠀⣿⣿⠀⠀⠘⣿⠘⠿⢿⣿⡁⠀⠀⠀⠀⣿⡇⠀⠀⠀⢸⣿⣦⣴⣾⡿⠋⢠⡀⠘⣰⣿⣏⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⢸⣿⡇⠀⠀⢹⡆⠀⠀⠹⣿⡄⠀⠀⠀⣿⡇⠀⠀⠀⢸⣿⡍⠉⠁⠀⠀⠀⠉⢀⣿⣿⣽⣿⣧⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠘⣿⣧⠀⠀⠈⣿⡀⠀⠀⠹⣿⡄⠀⠀⣿⡇⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⣼⣿⣙⣿⢿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡀⠀⠀⢻⡇⠀⠀⠀⠹⠿⠀⠴⣿⣿⣿⠿⠀⠸⡿⠁⠀⠀⠀⠀⠀⢠⣿⣯⡸⣿⣷⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣿⡇⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⣮⣿⣿⣾⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⠐⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⠆⠀⠀⠀⠀⠀⢠⣿⡷⣬⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡳⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⣿⡿⣿⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⡇⠀⢄⡈⠂⠀⠀⠐⠶⠶⠤⠤⠴⠤⠤⠤⠤⠀⠀⠀⠀⠀⠀⣿⢁⣮⣿⣃⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣿⣧⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⢰⣿⣀⣽⣿⡿⠏⠘⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⣍⣛⣋⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⣉⣤⣶⣾⣟⣿⣧⡀⠀⠀⠀⠀
⠀⠀⣾⠀⠀⠉⠉⠉⠉⠛⠛⠛⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡿⠛⣏⣹⣾⣿⢛⢿⣿⡀⠀⠀⠀
⠀⣼⡏⠀⣀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠒⠲⠶⠶⠶⠤⠤⠀⠀⠀⠘⣿⠻⡿⣿⣷⣴⣿⠿⠟⠀⠀⠀⠀
⠀⠿⣶⣤⣤⣭⣭⣟⣛⣛⣛⣛⣓⣂⣀⠀⠀⠀⠛⠒⠓⠒⠲⠄⠀⠀⠀⠀⠀⠀⠀⣻⣿⣷⡾⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")


###########################################################################################################
# Spiel starten - muss am Ende stehen, damit die definierten Funktionen zuvor ausgeführt werden.
###########################################################################################################

# Leere Dictionary für Spieler-Werte -> Startwerte werden in start_game-Funktion zugewiesen.
player = {
    "health": 0,   # Schlüssel: "health", Wert: 0
    "gold": 0,     # Schlüssel: "gold", Wert: 0
    "damage": 0    # Schlüssel: "damage", Wert: 0
}

# Auslösen der start_game-Funktion

start_game()


