import tkinter as tk
from tkinter import ttk, messagebox

from models import Card
from config import VALUES, SUITS, MAIN_WINDOW_TITLE, MAIN_WINDOW_SIZE
from ui_card_dialog import CardDialog


class CardApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(MAIN_WINDOW_TITLE)
        self.root.geometry(MAIN_WINDOW_SIZE)
        self.root.resizable(False, False)

        # список мастей для комбобокса (только имена)
        self.suit_names = list(SUITS.keys())

        self._create_widgets()

    def _create_widgets(self):
        # значение карты
        ttk.Label(self.root, text="Выберите значение карты:").pack(pady=(20, 5))

        self.value_combobox = ttk.Combobox(
            self.root,
            values=VALUES,
            state="readonly"
        )
        self.value_combobox.pack()

        # масть карты
        ttk.Label(self.root, text="Выберите масть карты:").pack(pady=(20, 5))

        self.suit_combobox = ttk.Combobox(
            self.root,
            values=self.suit_names,
            state="readonly"
        )
        self.suit_combobox.pack()

        # кнопка
        ttk.Button(
            self.root,
            text="Показать карту",
            command=self._on_show_card
        ).pack(pady=30)

    def _on_show_card(self):
        value = self.value_combobox.get()
        suit_name = self.suit_combobox.get()

        if not value or not suit_name:
            messagebox.showerror("Ошибка", "Выберите значение и масть карты!")
            return

        suit_symbol, color = SUITS[suit_name]
        card = Card(value=value,
                    suit_symbol=suit_symbol,
                    suit_name=suit_name,
                    color=color)

        CardDialog(self.root, card)
