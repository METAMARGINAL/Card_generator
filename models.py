class Card:
    def __init__(self, value: str, suit_symbol: str, suit_name: str, color: str):
        self.value = value       # '2', '10', 'Валет', ...
        self.suit_symbol = suit_symbol  # '♥', '♦', '♣', '♠'
        self.suit_name = suit_name      # 'Черви', 'Бубны', ...
        self.color = color       # '#FF0000' или '#000000'

    def title(self) -> str:
        return f"{self.value} {self.suit_name}"
