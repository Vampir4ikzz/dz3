import colorama
import inspect
colorama.init()
print("=== інтроспекція модуля COLORAMA ===\n")
print(f"Тип об'єкта: {type(colorama)}")
print(f"Документація модуля:\n{colorama.__doc__}\n")
print(f"Шлях до файлу модуля: {colorama.__file__}\n")
print("-" * 50)
print("Найважливіші атрибути та класи в colorama:")
print("-" * 50)
all_attributes = dir(colorama)
key_components = ['Fore', 'Back', 'Style', 'init', 'deinit', 'reinit']
for name in key_components:
    if name in all_attributes:
        obj = getattr(colorama, name)
        if inspect.isclass(obj):
            obj_type = "Клас"
        elif callable(obj):
            obj_type = "Функція/Метод"
        else:
            obj_type = "Атрибут"
        print(f"\n[ {obj_type} ] colorama.{name}")
        doc = obj.__doc__ if obj.__doc__ else "Документація відсутня"
        print(f"Опис: {doc.strip()}")
        if inspect.isclass(obj):
            colors = [attr for attr in dir(obj) if not attr.startswith('__')]
            print(f"Доступні властивості класу {name}: {', '.join(colors)}")
print("\n" + "=" * 50)
print("=== демонстрацыя роботи наважливыших методів ===")
print("=" * 50)
print(colorama.Fore.GREEN + "Цей текст став зеленим завдяки Fore.GREEN")
print(colorama.Back.YELLOW + "А цей має жовтий фон завдяки Back.YELLOW")
print(colorama.Style.BRIGHT + "Текст став яскравішим завдяки Style.BRIGHT")
print(colorama.Style.RESET_ALL + "Скидання стилів наступний текст знову звичайний.")

colorama.deinit()