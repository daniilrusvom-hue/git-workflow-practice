"""
Демонстрационный скрипт для практики Git workflow
"""

from src.main import GitWorkflowManager


def practice_scenario():
    """Практический сценарий работы с Git"""
    print("🎯 Git Workflow Practice Scenario\n")
    
    # Инициализация проекта
    my_project = GitWorkflowManager("Learning Git")
    
    # Симуляция реального рабочего процесса
    print("=== День 1: Начало работы ===")
    
    # Создаем базовые файлы
    print("1. Создаем базовую структуру проекта...")
    print(my_project.add(["app.py", "config.py", "requirements.txt"]))
    print(my_project.commit("feat: initialize project with basic structure"))
    print()
    
    print("2. Добавляем модель данных...")
    print(my_project.add(["models/user.py", "models/post.py"]))
    print(my_project.commit("feat: add user and post models"))
    print()
    
    print("=== День 2: Разработка ===")
    
    print("3. Добавляем утилиты...")
    print(my_project.add(["utils/validators.py", "utils/helpers.py"]))
    print(my_project.commit("feat: add validation and helper utilities"))
    print()
    
    print("4. Исправляем баги...")
    print(my_project.add(["models/user.py"]))  # Исправляем один файл
    print(my_project.commit("fix: correct user model validation logic"))
    print()
    
    print("=== День 3: Тестирование ===")
    
    print("5. Добавляем тесты...")
    print(my_project.add([
        "tests/test_models.py", 
        "tests/test_utils.py",
        "conftest.py"
    ]))
    print(my_project.commit("test: add comprehensive test suite"))
    print()
    
    # Показываем итоговую историю
    print("📊 Итоговая статистика проекта:")
    stats = my_project.status()
    print(f"   Всего коммитов: {stats['total_commits']}")
    print(f"   Последний коммит: {stats['last_commit']['message']}")
    print()
    
    print("📜 Полная история разработки:")
    print(my_project.log())


def quick_demo():
    """Быстрая демонстрация основных команд"""
    print("\n⚡ Quick Git Commands Demo:")
    
    project = GitWorkflowManager("Quick Demo")
    
    # Быстрый цикл
    commands = [
        ("add", ["main.py"]),
        ("commit", "Initial commit"),
        ("add", ["utils.py", "config.ini"]),
        ("commit", "Add utilities and config"),
        ("add", ["README.md"]),
        ("commit", "Update documentation")
    ]
    
    for cmd, args in commands:
        if cmd == "add":
            result = project.add(args)
        elif cmd == "commit":
            result = project.commit(args)
        print(f"{cmd.upper():<10} → {result}")


if __name__ == "__main__":
    practice_scenario()
    quick_demo()
