#diverse Module importiert für bute Ausgaben und nützliche Funktionen
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import Progress
from rich.text import Text
import random
import json

#Rich-Konsole für bunte und formatierte Ausgabe erstellt
console = Console()

#Speicherfunktion des Spielstandes, um den Forschritt zu sichern und nachzuverfolgen
def save_game(state):
    with open("game_save.json", "w") as file:
        json.dump(state, file)

#Funktion zum Laden des Spielstands, falls einer bereits gespeichert wurde/falls nicht kommt None zurück
def load_game():
    try:
        with open("game_save.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

#Funktion um das Spiel jederzeit mit "quit" beenden zu können
def check_quit(input_value):
    if input_value.lower() == "quit":
        console.print("\n[red]Spiel wird beendet. Danke fürs Spielen![/red]")
        exit()

#Begrüßt den Spieler in einem schicken Titel-Panel
def create_title_panel():
    return Panel(
        Text("🌟 Willkommen zu 'Das Geheimnis des Elfenwaldes'! 🌟", justify="center", style="bold cyan"),
        style="green",
        expand=True
    )

#Auswahl-Panel erstellt damit Spieler Optionen auswählen kann
def create_choice_panel(title, options):
    panel_content = "\n".join(f"[bold magenta]{key}.[/bold magenta] {desc}" for key, desc in options.items())
    return Panel(
        f"{title}\n\n{panel_content}",
        style="bold yellow",
        expand=False
    )

#kurze Einführungsgeschichte des Spiels für Kontext zur Reise durch den Elfenwald
def introduction():
    console.print(Panel(
        "In einer längst vergangenen Zeit, als Magie und Heldenmut das Land regierten, "
        "wurde der magische Kristall des Königreichs gestohlen. "
        "Nur die mutigsten Abenteurer können den Frieden wiederherstellen.\n\n"
        "Bist du bereit, dich der Herausforderung zu stellen?\n"
        "Hinweis: Du kannst das Spiel jederzeit mit dem Wort 'quit' beenden",
        style="italic blue",
        expand=True
    ))

#das Spiel wird gestartet
#der Spieler wird zur Geschichte und gleich im Anschluss zur Charakter-Wahl geführt
def start_game():
    console.print(create_title_panel())
    introduction()
    character_selection()

#Auswahl eines Charakters: Elfenkrieger oder Elfenmagierin
def character_selection():
    console.print("\n")
    options = {
        "1": "🗡 Elfenkrieger",
        "2": "🪄 Elfenmagierin"
    }
    console.print(create_choice_panel("Wähle deinen Charakter:", options))

    choice = Prompt.ask("Gib [bold]1[/bold] oder [bold]2[/bold] ein")
    check_quit(choice)
    if choice == "1":
        console.print(Panel("[bold white]Du hast den tapferen Elfenkrieger gewählt! Möge dein Schwert dich leiten.[/bold white]", style="bold blue"))
    elif choice == "2":
        console.print(Panel("[bold white]Du hast die weise Elfenmagierin gewählt! Möge deine Magie dich schützen.[/bold white]", style="bold purple"))

    enter_forest(choice)

#Spieler kommt in den mystischen Elfenwald, der als ASCII angezeigt wird
def enter_forest(character):
    #ASCII-Kunst des Elfenwaldes
    elfenwald_ascii = """
           🌲🌳🌲
      🌳       🌳  🌲🌳
    🌲   🌲  🌳     🌲
  🌳   🌳🌲 🌳  🌲    🌳
       🌳   🌲🌳
         🌳     🌳
           🌳🌲
    """
    console.print(f"\nDu betrittst den mystischen Elfenwald. 🌳\n{elfenwald_ascii}")
    path_choice(character)

#nach Eintritt wählt der Spieler einen der zwei Wege
#Auswahl wird wiederholt, wenn der Weg gesperrt ist
def path_choice(character):
    console.print("\nVor dir liegen zwei Wege:")
    console.print("1. Der linke Pfad, der von leuchtenden Pilzen gesäumt ist. 🍄")
    console.print("2. Der rechte Pfad, der durch dichtes Unterholz führt. 🌿")
    choice = Prompt.ask("Wähle deinen Weg [1 oder 2]")
    check_quit(choice)

    if choice == "1":
        console.print("\nDer Pfad führt dich tiefer in den Wald hinein.")
        item_selection(character)
    elif choice == "2":
        console.print("\nDer Weg ist versperrt! Du musst einen Schritt zurückgehen.")
        path_choice(character)

#Spieler findet einen Schatz und je nach Charakter kann er sich nun ein Item auswählen.
def item_selection(character):
    if character == "1":
        items = {
            "1": "🗡 Verzaubertes Schwert",
            "2": "🛡 Magischer Schild"
        }
    elif character == "2":
        items = {
            "1": "🪄 Stab der Weisheit",
            "2": "📜 Verzaubertes Pergament"
        }

    console.print("\nDu findest einen verborgenen Schatz. Wähle ein Item:")
    console.print(create_choice_panel("Verfügbare Items:", items))

    choice = Prompt.ask("Wähle ein Item", choices=list(items.keys()))
    check_quit(choice)

    item = items[choice]
    console.print(f"\nDu nimmst {item} an dich.")
    fight_enemy(character, item)

#Nach der Belohnung kommt der Spieler direkt zum ersten Kampf gegen einen Gegner.
def fight_enemy(character, item):
    console.print("\nEin Schattenwolf erscheint! 🐺")
    console.print(f"Du nutzt dein {item} im Kampf.")
    
    #Erfolg hängt von Charakter und Item ab
    if character == "1" and item == "🗡 Verzaubertes Schwert":
        #garantierter Sieg für Elfenkrieger mit Schwert
        console.print("[green]Du gewinnst den Kampf mühelos dank deines verzauberten Schwertes![green]")
        elf_riddle(character, item)
    else:
        #sonst zufälliger Erfolg
        success_rate = random.randint(1, 100)
        if success_rate > 50:
            console.print("[green]Du gewinnst den Kampf![green]")
            elf_riddle(character, item)
        else:
            console.print("[red]Du verlierst den Kampf und musst fliehen![red]")
            path_choice(character)

#nach dem gewonnenen Kampf erfolgt ein Rätsel mit drei Versuchen
#Wenn erfolgreich gelöst, dann erhält man eine Belohnung - sonst wird man "bestraft"
def elf_riddle(character, item):
    console.print("\nEine weise Elfe erscheint und stellt dir ein Rätsel:")
    console.print("[italic cyan]'Ich bin nicht lebendig, aber ich wachse. Ich habe keine Lungen, aber ich brauche Luft. Was bin ich?'[/italic cyan]")
    attempts = 3
    while attempts > 0:
        answer = Prompt.ask(f"Deine Antwort ({attempts} Versuche übrig)")
        check_quit(answer)
        if answer.lower() == "feuer":
            #bei richtiger Antwort 
            console.print("\n[green]Richtig![green] Die Elfe überreicht dir einen magischen Trank. 🧪")
            rescue_character(character, item, "Magischer Trank")
            return
        else:
            #bei falscher Antwort
            attempts -= 1
            console.print("\n[red]Falsch![/red]")

    #Strafe nach 3 Fehlversuchen
    console.print("\n[red]Du hast das Rätsel nicht gelöst. Die Elfe ist enttäuscht und entzieht dir Lebensenergie.[/red]")
    console.print("\n[red]Du fühlst dich geschwächt.[/red]")
    rescue_character(character, item)

#Spieler hört Hilferufe, wenn er Hilf erhält er Informationen und einen Begleiter
#Wenn dieser nicht hilft, dann zieht er alleine weiter
def rescue_character(character, item, bonus_item=None):
    console.print("\nDu hörst Hilferufe aus der Ferne. 🆘")
    console.print("Ein Wanderer wird von Goblins angegriffen! 👺")
    choice = Prompt.ask("Möchtest du ihm helfen?", choices=["ja", "nein"])
    check_quit(choice)

    if choice == "ja":
        #Spieler hilf und gewinnt einen Begleiter zur Unterstützung
        console.print("\nDu eilst zur Hilfe und vertreibst die Goblins!")
        console.print("Der gerettete Charakter schließt sich dir an. 🤝")
        console.print("Er erzählt dir von dem gestohlenen magischen Kristall, der das Königreich retten kann.")
        final_battle(character, item, bonus_item, True)
    else:
        #Spieler ignoriert Hilferufe
        console.print("\nDu ignorierst die Hilferufe und gehst weiter.")
        final_battle(character, item, bonus_item, False)

#der große Finalkampf gegen eine dunkle Gestalt und deren Minions
#Wie der Kampf endet hängt von dem bisherigen Weg des Spielers
def final_battle(character, item, bonus_item, companion):
    #ASCII-Kunst des magischen Kristalls
    magischer_kristall_ascii = """
        ✨✨✨
       ✨  *  ✨
        * 💎 *
       ✨  *  ✨
        ✨✨✨
    """
    console.print("\nPlötzlich tauchen die Minions der dunklen Gestalt auf! ⚔️")
    console.print("Ein Kampf entbrennt...")
    
    #der KAmpf besteht aus drei Runden, wo Aktionen gewählt werden können
    for round_num in range(1, 4):
        console.print(f"\n[bold cyan]Runde {round_num} des Endkampfs![/bold cyan]")
        options = {
            "1": "Angriff mit deinem Hauptitem",
            "2": "Strategischer Rückzug",
            "3": "Den magischen Trank verwenden"
        }
        console.print(create_choice_panel("Wähle deine Aktion:", options))

        action = Prompt.ask("Deine Wahl", choices=list(options.keys()))
        
        #je nach Wahl pro Runde
        if action == "1" and item:
            if companion:
                #Spieler mit Begleiter
                console.print(f"[bold green]Du nutzt dein {item} effektiv und schadest der dunklen Gestalt! Leider wurde dein Begleiter dabei verletzt ...[/bold green]")
            else:
                #Spieler ohne Begleiter
                console.print(f"[bold green]Du nutzt dein {item} effektiv und schadest der dunklen Gestalt, aber du bist auf dich allein gestellt. Der Kampf wird schwieriger ...[/bold green]")
        elif action == "2":
            console.print("[yellow]Du ziehst dich kurz zurück, um eine bessere Position zu finden.[/yellow]")
        elif action == "3" and bonus_item:
            if companion:
                #Spieler mit Begleiter kann sich oder Begleiter stärken
                console.print("\n[bold blue]Du hast eine Wahl:[/bold blue]")
                sub_choice = Prompt.ask("Möchtest du dich oder deinen Begleiter stärken?", choices=["ich", "begleiter"])
                if sub_choice == "ich":
                    console.print(f"[bold blue]Du nutzt den {bonus_item}, um dich zu stärken![/bold blue]")
                else:
                    console.print(f"[bold blue]Du nutzt den {bonus_item}, um deinen Begleiter zu stärken![/bold blue]")
                    console.print("[italic red]'Wow danke - ich hab mich noch nie so stark gefühlt!' sagt dein Begleiter, bevor er heroisch kämpft.")
            else:
                #Spieler ohne Begleiter kann nur sich stärken
                console.print(f"[bold blue]Du nutzt den {bonus_item}, um dich selbst zu stärken. Du brauchst jede Hilfe, die du bekommen kannst ...[/bold blue]")
        else:
            #kein effektive Aktion
            console.print("[red]Deine Aktion hatte keinen Effekt... Sei vorsichtig![/red]")
        
    #Ausgang des Kampfes je nach Ressourcen und Entscheidungen
    if item and companion and bonus_item:
        console.print("\n[bold green]Mit der Hilfe deines Begleiters, deinem Item und deinem Bonus-Item besiegst du die dunkle Gestalt endgültig![/bold green]")
        console.print("✨ [bold green]Das Königreich ist gerettet![/bold green] ✨")
    elif item and companion:
        console.print("\n[bold yellow]Du und dein Begleiter besiegen die dunkle Gestalt, aber der Sieg fordert einen hohen Preis.[/bold yellow]")
    elif item:
        console.print("\n[bold red]Du kämpfst tapfer, aber ohne Unterstützung kannst du die dunkle Gestalt nicht bezwingen.[/bold red]")
    else:
        console.print("\n[bold red]Ohne Ausrüstung und Hilfe hattest du keine Chance. Die dunkle Gestalt triumphiert.[/bold red]")

    end_game()

#Ende des Spiels
def end_game():
    console.print("\nDanke fürs Spielen! 🎉")
    exit()

if __name__ == "__main__":
    start_game()
