"""Generates animation for GitHub README."""
import time
from typing import Dict

import rich.box
import rich.console
import rich.columns
import rich.markdown
import rich.panel
import rich.progress

PRIMARY_COLOR = "#BB86FC"
SECONDARY_COLOR = "#03DAC5"

about_me_text = "\nHello, I'm Paulo — a data scientist currently at Facebook.\n"
project_text = (
    "\nHere, I work mostly on Python libraries, command-line interfaces,"
    " and tools for working with data.\n"
)
language_text = (
    "\nI dabble in a lot of different languages both here and at work."
    " But my open source work is primary focused around:\n\n"
    " [blue][/blue] Python\n"
    " [yellow][/yellow] SQL\n"
    " [magenta][/magenta] Shell\n"
)
citations_text = (
    "\nThe code used to create this animation may be found at"
    f" [{SECONDARY_COLOR}]paw-lu/paw-lu[/{SECONDARY_COLOR}]. It was"
    " made with the help of two great Python libraries:\n\n"
    f" • [{SECONDARY_COLOR}]nbedos/termtosvg[/{SECONDARY_COLOR}]\n"
    f" • [{SECONDARY_COLOR}]willmcgugan/rich[/{SECONDARY_COLOR}]\n"
)
panels = {
    "Me": about_me_text,
    "Projects": project_text,
    "Languages": language_text,
    "How this was made": citations_text,
}
console = rich.console.Console()


def render_readme(
    name: str,
    primary_color: str,
    secondary_color: str,
    panels: Dict[str, str],
    step_time: float,
) -> None:
    """
    Generate the README animation.

    Parameters
    ----------
    name : str
        The title in the animation.
    primary_color : str
        The primary color as a hex value.
    secondary_color : str
        The secondary color as a hex value.
    panels : Dict[str, str]
        A dictionary with the title as the key and text and the value.
    step_time : float
        The amount of time to wait before rendering each step.
    """
    step_size = 100 // (len(panels) + 1)
    with rich.progress.Progress(
        rich.progress.TextColumn("[progress.description]{task.description}"),
        rich.progress.BarColumn(
            complete_style=secondary_color, finished_style=secondary_color
        ),
        rich.progress.TextColumn(
            "[progress.percentage]{task.percentage:>3.0f}%", style=primary_color
        ),
        rich.progress.TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task(
            "Animation",
            total=100,
            complete_style="#03DAC5",
        )
        time.sleep(step_time)
        console.print(f"\n\n[bold]{name}[/bold]", style=primary_color)
        console.print(len(name) * "—" + "\n\n", style=secondary_color)
        progress.update(task, advance=step_size)
        time.sleep(step_time)
        for title, text in panels.items():
            console.print(
                rich.panel.Panel(
                    text,
                    box=rich.box.ROUNDED,
                    title=title,
                    title_align="left",
                    border_style=primary_color,
                )
            )
            progress.update(task, advance=step_size)
            time.sleep(step_time)


render_readme(
    name="Paulo S. Costa",
    primary_color=PRIMARY_COLOR,
    secondary_color=SECONDARY_COLOR,
    panels=panels,
    step_time=1,
)
