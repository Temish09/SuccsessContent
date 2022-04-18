"""Module with custom cards."""

from datetime import datetime
import calendar

from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

class CustomCard(MDCard, RoundedRectangularElevationBehavior):
    """Base class for scrollable cards in screens."""

    def __init__(self, **kwargs):
        """Init this class. Sets radius for card, and independence of size from window."""
        super().__init__(**kwargs)
        self.radius = [20]
        self.size_hint_y = None
        self.size_hint_x = 0.8

class LabelUnderIconWidget(MDBoxLayout):
    """Widget to paste IconButton and Label vertically."""

    def change_icon(self, new_icon: str) -> None:
        """Change button icon to new icon.

        Args:
        new_icon: str - new icons kivymd name.

        Returns:
        None.
        """
        print("Day is marked")
        self.image.icon = new_icon

    def __init__(self, icon, text, new_icon_on_action=None, **kwargs):
        """Init this widget.

        Adds MDIconButton and MDLabel vertically.
        Sets on_press to MDIconButton.
        """
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.image = MDIconButton(
            icon=icon,
            pos_hint={"center_x": 0.5},
        )

        if new_icon_on_action:
            self.image.on_press = lambda *x: \
                self.change_icon(new_icon_on_action)

        self.label = MDLabel(
            text=text,
            halign="center"
        )

        self.add_widget(self.image)
        self.add_widget(self.label)

class CurrentDayCard(CustomCard):
    """Card with icon, current date and some message."""

    def __init__(self, icon="emoticon-outline", msg="", **kwargs):
        """Init this card.

        Sets 'emoticon-outline' icon as default.
        Sets empty message as default.
        """
        super().__init__(**kwargs)

        self.height = 60

        today = datetime.now()
        self.day = today.day
        self.weekday = today.strftime("%A")
        self.month = today.strftime("%b")

        self.icon = icon
        self.msg = msg

        left_icon = MDIconButton(
            icon=self.icon,
            pos_hint={"center_y": 0.5}
        )

        date_cheer_label = MDLabel(
            text=str(self.weekday) + ", " + \
                str(self.day) + " " + str(self.month) + \
                "\n" + self.msg,
        )

        self.add_widget(left_icon)
        self.add_widget(date_cheer_label)

class DaysInRowCard(CustomCard):
    """Card with title and list of 6 last days, their states, and current day with empty state."""

    def __init__(self, storage=None, **kwargs):
        """Init card."""
        if not storage:
            print("TODO storage")

        super().__init__(**kwargs)

        self.orientation = "vertical"

        title = MDLabel(
            text="Days in a Row",
            size_hint_y=None,
            height=40,
            padding=(15, 0)
        )

        days_layout = MDBoxLayout(
            orientation="horizontal",
            padding=(0, 0, 0, 15)
        )

        today = datetime.now().weekday()
        days = [calendar.day_name[today - i] for i in range(6, 0, -1)]

        for day in days:
            days_layout.add_widget(
                LabelUnderIconWidget(
                    icon="check-circle-outline",
                    text=day[:3]
                )
            )

        today_widget = LabelUnderIconWidget(
            icon="checkbox-blank-circle-outline",
            text=calendar.day_name[today][:3],
            new_icon_on_action="check-circle-outline"
        )

        days_layout.add_widget(today_widget)

        self.add_widget(title)
        self.add_widget(days_layout)

class RateHabit(CustomCard):
    """Card to rate your habit today."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Тут должен оцениваться сегодняшний habit")

class Chart(CustomCard):
    """MatPlot of habbit."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Тут должен рисоваться график чего-то")

class Achievements(CustomCard):
    """Card with achievements."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Можно ачивки сделать, и их здесь выводить")

class Count(CustomCard):
    """Count statistics."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Здесь просто выводится статистика " + \
            "по каждой оценке: сколько раз оценка 5, ...")

class Calendar(CustomCard):
    """Simply Calendar."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Просто каледнарь с отметками о днях")