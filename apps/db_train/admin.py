from django.contrib import admin

# Зарегистрируйте свои модели в админ панели здесь
from django.contrib import admin
from .models import Author

admin.site.register(Author)

def __str__(self):
    initials = None  # Инициалы
    if self.first_name and self.middle_name:
        initials = f"{self.first_name.upper()[0]}.{self.middle_name.upper()[0]}."
    return f"{self.username} - {self.last_name} {initials}"