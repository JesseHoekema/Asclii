import os
import sys
import random
import time
from typing import List, Optional

try:
    import pyfiglet
    import pyperclip
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.align import Align
    from rich.rule import Rule
except ImportError as e:
    print(f"Oops! You're missing a required package: {e}")
    print("You can fix that by running:")
    print("pip3 install pyfiglet pyperclip rich")
    sys.exit(1)


class ASCIIArtGenerator:

    def __init__(self):
        self.console = Console()
        self.available_fonts = [
            "slant", "block", "standard", "digital", "big", "small",
            "banner", "doom", "ghost", "gothic", "graffiti", "isometric1",
            "larry3d", "mini", "script", "shadow", "speed", "starwars"
        ]
        self.random_art_patterns = [
            "★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆",
            "◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇",
            "▲ ▼ ▲ ▼ ▲ ▼ ▲ ▼ ▲ ▼",
            "♦ ♢ ♦ ♢ ♦ ♢ ♦ ♢ ♦ ♢",
            "▒░▒░▒░▒░▒░▒░▒░▒░▒░▒░",
            "═══════════════════════",
            "┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐",
            "╔═╦═╦═╦═╦═╦═╦═╦═╦═╦═╗"
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        banner_text = pyfiglet.figlet_format("ASCII ART", font="slant")
        banner_panel = Panel(
            Align.center(Text(banner_text, style="bold cyan")),
            title="[bold white]ASCII Art Generator[/bold white]",
            subtitle="[dim]Turn text into art, the fun way[/dim]",
            border_style="bright_blue"
        )
        self.console.print(banner_panel)
        self.console.print()

    def show_main_menu(self) -> str:
        menu_table = Table(show_header=False, box=None, padding=(0, 2))
        menu_table.add_column("Option", style="bold cyan")
        menu_table.add_column("Description", style="white")

        menu_table.add_row("1", "Create ASCII art from text")
        menu_table.add_row("2", "Get a random ASCII art surprise")
        menu_table.add_row("3", "Exit")

        menu_panel = Panel(
            menu_table,
            title="[bold white]Main Menu[/bold white]",
            border_style="bright_blue"
        )

        self.console.print(menu_panel)

        return Prompt.ask(
            "\n[bold cyan]What would you like to do?[/bold cyan]",
            choices=["1", "2", "3"],
            default="1"
        )

    def show_font_menu(self) -> str:
        self.console.print(Rule("[bold cyan]Pick a Style[/bold cyan]"))

        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("", style="bold yellow")
        table.add_column("", style="white")
        table.add_column("", style="bold yellow")
        table.add_column("", style="white")

        for i in range(0, len(self.available_fonts), 2):
            left_font = f"{i+1:2d}. {self.available_fonts[i]}"
            right_font = f"{i+2:2d}. {self.available_fonts[i+1]}" if i + 1 < len(self.available_fonts) else ""
            table.add_row(left_font, "", right_font, "")

        font_panel = Panel(
            table,
            title="[bold white]Font Styles[/bold white]",
            border_style="bright_blue"
        )

        self.console.print(font_panel)

        while True:
            try:
                choice = Prompt.ask(
                    f"\n[bold cyan]Choose a font (1-{len(self.available_fonts)})[/bold cyan]",
                    default="1"
                )
                font_index = int(choice) - 1
                if 0 <= font_index < len(self.available_fonts):
                    return self.available_fonts[font_index]
                else:
                    self.console.print("[bold red]Invalid number. Try again![/bold red]")
            except ValueError:
                self.console.print("[bold red]Please enter a number, not text.[/bold red]")

    def generate_text_ascii(self, text: str, font: str) -> str:
        try:
            return pyfiglet.figlet_format(text, font=font)
        except Exception as e:
            self.console.print(f"[bold red]Whoops! Couldn't use that font: {e}[/bold red]")
            return pyfiglet.figlet_format(text, font="standard")

    def generate_random_ascii(self) -> str:
        patterns = [random.choice(self.random_art_patterns) for _ in range(5)]
        word = random.choice(["AWESOME", "COOL", "AMAZING", "GREAT", "NICE", "WOW"])
        font = random.choice(self.available_fonts)
        ascii_text = self.generate_text_ascii(word, font)
        patterns.append(ascii_text)
        return "\n".join(patterns)

    def display_ascii_preview(self, ascii_art: str):
        preview_panel = Panel(
            ascii_art,
            title="[bold white]Here’s Your ASCII Art[/bold white]",
            border_style="bright_green"
        )
        self.console.print(preview_panel)

    def show_action_menu(self) -> str:
        action_table = Table(show_header=False, box=None, padding=(0, 2))
        action_table.add_column("Option", style="bold cyan")
        action_table.add_column("Action", style="white")

        action_table.add_row("1", "Copy to clipboard")
        action_table.add_row("2", "Make another one")
        action_table.add_row("3", "Back to main menu")
        action_table.add_row("4", "Exit")

        action_panel = Panel(
            action_table,
            title="[bold white]Next Steps[/bold white]",
            border_style="bright_blue"
        )

        self.console.print(action_panel)

        return Prompt.ask(
            "\n[bold cyan]Choose what to do next[/bold cyan]",
            choices=["1", "2", "3", "4"],
            default="1"
        )

    def copy_to_clipboard(self, text: str):
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
                transient=True
            ) as progress:
                task = progress.add_task("Copying to clipboard...", total=None)
                time.sleep(1)
                pyperclip.copy(text)
                progress.update(task, description="✓ All set! Copied successfully.")
                time.sleep(0.5)

            self.console.print("[bold green]✓ Your ASCII art is now on the clipboard![/bold green]")
        except Exception as e:
            self.console.print(f"[bold red]Couldn't copy to clipboard: {e}[/bold red]")

    def text_to_ascii_flow(self):
        while True:
            font = self.show_font_menu()

            self.console.print(Rule("[bold cyan]Your Text[/bold cyan]"))
            text = Prompt.ask(
                "\n[bold cyan]What text do you want to turn into ASCII art?[/bold cyan]",
                default="Hello World"
            )

            if not text.strip():
                self.console.print("[bold red]Oops! Looks like you didn’t enter anything.[/bold red]")
                continue

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
                transient=True
            ) as progress:
                task = progress.add_task("Creating ASCII art...", total=None)
                time.sleep(0.5)
                ascii_art = self.generate_text_ascii(text, font)
                progress.update(task, description="Done! Here's your art.")
                time.sleep(0.3)

            self.console.print()
            self.display_ascii_preview(ascii_art)

            while True:
                action = self.show_action_menu()

                if action == "1":
                    self.copy_to_clipboard(ascii_art)
                    time.sleep(1)
                elif action == "2":
                    self.clear_screen()
                    self.show_banner()
                    break
                elif action == "3":
                    return
                elif action == "4":
                    sys.exit(0)

    def random_ascii_flow(self):
        while True:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=self.console,
                transient=True
            ) as progress:
                task = progress.add_task("Generating something random...", total=None)
                time.sleep(0.8)
                ascii_art = self.generate_random_ascii()
                progress.update(task, description="Surprise ready!")
                time.sleep(0.3)

            self.console.print()
            self.display_ascii_preview(ascii_art)

            while True:
                action = self.show_action_menu()

                if action == "1":
                    self.copy_to_clipboard(ascii_art)
                    time.sleep(1)
                elif action == "2":
                    self.clear_screen()
                    self.show_banner()
                    break
                elif action == "3":
                    return
                elif action == "4":
                    sys.exit(0)

    def run(self):
        try:
            while True:
                self.clear_screen()
                self.show_banner()

                choice = self.show_main_menu()

                if choice == "1":
                    self.clear_screen()
                    self.show_banner()
                    self.text_to_ascii_flow()
                elif choice == "2":
                    self.clear_screen()
                    self.show_banner()
                    self.random_ascii_flow()
                elif choice == "3":
                    self.console.print("\n[bold cyan]Thanks for using the ASCII Art Generator![/bold cyan]")
                    self.console.print("[dim]See you next time 👋[/dim]\n")
                    break

        except KeyboardInterrupt:
            self.console.print("\n\n[bold yellow]Cancelled. No worries![/bold yellow]")
            self.console.print("[dim]See you next time 👋[/dim]\n")
            sys.exit(0)
        except Exception as e:
            self.console.print(f"\n[bold red]Something went wrong: {e}[/bold red]")
            sys.exit(1)


def main():
    if not sys.stdout.isatty():
        print("This tool is meant to run in a terminal.")
        sys.exit(1)

    app = ASCIIArtGenerator()
    app.run()


if __name__ == "__main__":
    main()
