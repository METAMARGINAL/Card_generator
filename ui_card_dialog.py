import tkinter as tk
from tkinter import ttk
from models import Card
from config import CARD_WINDOW_SIZE, CARD_RECT, FONT_SMALL, FONT_CENTER


class CardDialog(tk.Toplevel):
    def __init__(self, parent, card: Card):
        super().__init__(parent)

        self.card = card

        self.title(f"Ваша карта: {self.card.title()}")
        self.geometry(CARD_WINDOW_SIZE)
        self.resizable(False, False)

        # делаем окно модальным
        self.transient(parent)
        self.grab_set()

        self._build_ui()

    def _build_ui(self):
        canvas = tk.Canvas(self, width=300, height=400,
                           bg="#F0F0F0", highlightthickness=0)
        canvas.pack(pady=10)

        x0, y0, x1, y1 = CARD_RECT

        # белый прямоугольник карты
        canvas.create_rectangle(
            x0, y0, x1, y1,
            outline="black",
            fill="white",
            width=2
        )

        # левый верхний угол
        canvas.create_text(
            x0 + 20,
            y0 + 20,
            text=f"{self.card.value}\n{self.card.suit_symbol}",
            fill=self.card.color,
            font=FONT_SMALL,
            anchor="nw"
        )

        # правый нижний угол
        canvas.create_text(
            x1 - 20,
            y1 - 20,
            text=f"{self.card.value}\n{self.card.suit_symbol}",
            fill=self.card.color,
            font=FONT_SMALL,
            anchor="se"
        )

        # центр – крупный символ масти
        canvas.create_text(
            (x0 + x1) / 2,
            (y0 + y1) / 2,
            text=self.card.suit_symbol,
            fill=self.card.color,
            font=FONT_CENTER,
        )

        ttk.Button(self, text="Закрыть", command=self.destroy).pack(pady=10)
