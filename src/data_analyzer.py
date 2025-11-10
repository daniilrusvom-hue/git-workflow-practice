Git Init
git init — создаёт новый локальный репозиторий в текущей папке, инициализируя скрытую директорию .git.
Git Config
git config user.name "..." и git config user.email "..." — задают имя и email автора коммитов (можно глобально с --global).
Рабочий цикл
•    git status — показывает состояние файлов (изменены, не добавлены и т.д.).
•    git add <file> или git add . — добавляет файлы в индекс (staging).
•    git commit -m "..." — фиксирует изменения с комментарием.
•    git log --oneline --graph — компактная история коммитов с визуализацией веток.
Удалённый репозиторий
•    git remote add origin <url> — привязывает локальный репозиторий к удалённому (например, на GitHub).
•    git push -u origin main — отправляет коммиты в удалённый репозиторий и устанавливает отслеживание ветки.
README.md
Файл с описанием проекта в Markdown:
•    # Заголовок, ## Подзаголовок
•    - список, 1. нумерованный список
•    код или блоки кода с тройными апострофами.
Ветвление и слияние
•    git branch <name> — создаёт ветку.
•    git checkout -b <name> — создаёт и переключается на ветку.
•    git merge <branch> — вливает ветку в текущую.
•    Fast-forward — если нет расхождений, указатель просто перемещается.
•    Не fast-forward — создаётся коммит слияния при наличии независимых изменений.
Разрешение конфликтов
При конфликте слияния:
Вручную редактируем файл (убираем маркеры <<<<<<<, =======, >>>>>>>).
git add <file> — помечаем конфликт разрешённым.
git commit — завершаем слияние.
Просмотр истории
git log с флагами:
•    --oneline — краткий вид.
•    --graph — график ветвления.
•    --all — все ветки.
•    -p — показывает изменения в файлах.
Gitignore
Файл .gitignore содержит шаблоны файлов/папок, которые Git должен игнорировать (например, *.log, node_modules/).
контрольные вопросы:
1. Система контроля версий (VCS)
Система контроля версий — это инструмент для отслеживания изменений в исходном коде и управления ими. Ключевая проблема, которую она решает — потеря контроля над изменениями при совместной работе. Без VCS разработчики сталкиваются с:
•	Версионным хаосом ("final_final_version.zip")
•	Невозможностью отката к рабочей версии
•	Конфликтами при одновременном редактировании файлов
Раскрыть
message.txt
7 кб
Danielka — 19:42
git-workflow-practice
MIT License
Git Workflow Practice Project
🎯 Цель проекта
Освоить базовый рабочий цикл Git: status, add, commit

📚 Функциональность
Демонстрация работы с Git через GitHub интерфейс
Практика создания осмысленных коммитов
Изучение управления версиями проекта

🏗 Структура проекта
project/
├── README.md # Документация проекта
├── .gitignore # Исключаемые файлы
└── LICENSE # Лицензия MIT

👨‍💻 Разработчик
[Даниил] - Группа [Т9-ИП-24-2]
Danielka — 19:55
https://chat.deepseek.com/share/fz3x324pz5gii4zkud
Danielka — 20:10
https://chat.deepseek.com/share/zrhose566rb3om5lm5
Danielka — 20:41
Задание 2,3.
Изучить базовый рабочий цикл Git: (status, add, commit). Создать несколько осмысленных коммитов, изменяя код учебного проекта, создать удаленный репозиторий на GitHub (GitLab) и связать его с локальным репозиторием (remote, push). Оформить README.md-файл для проекта.
Boogie
БОТ
 — 20:51
Nothing Playing
No track is currently playing. load a track to get started;)
To disable this feature use /settings
More Features...
Danielka — 20:58
feature/new-functionality
Danielka — 21:30
src/data_analyzer.py
"""
Data Analysis Module - New feature for Python Git project
Advanced data analysis capabilities using pandas and numpy
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Union
import json

class DataAnalyzer:
    """
    Advanced data analysis tool for statistical operations
    and data visualization preparation
    """
    
    def __init__(self, data_source: str = None):
        self.data_source = data_source
        self.dataset = None
        self.analysis_results = {}
        
    def load_csv_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from CSV file into pandas DataFrame
        
        Args:
            file_path (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Loaded dataset
        """
        try:
            self.dataset = pd.read_csv(file_path)
            print(f"✅ Successfully loaded data from {file_path}")
            print(f"📊 Dataset shape: {self.dataset.shape}")
            return self.dataset
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None
    
    def generate_sample_data(self, rows: int = 100) -> pd.DataFrame:
        """
        Generate sample dataset for demonstration
        
        Args:
            rows (int): Number of rows to generate
            
        Returns:
            pd.DataFrame: Generated sample data
        """
        np.random.seed(42)
        
        data = {
            'user_id': range(1, rows + 1),
            'age': np.random.randint(18, 65, rows),
            'salary': np.random.normal(50000, 15000, rows).round(2),
            'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], rows),
            'experience_years': np.random.randint(0, 20, rows),
            'performance_score': np.random.uniform(0.5, 1.0, rows).round(3)
        }
        
        self.dataset = pd.DataFrame(data)
        print(f"🎯 Generated sample dataset with {rows} rows")
        return self.dataset
    
    def basic_statistics(self) -> Dict:
        """
        Calculate basic statistical metrics for numerical columns
        
        Returns:
            Dict: Statistical summary
        """
        if self.dataset is None:
            print("❌ No dataset loaded. Generate or load data first.")
            return {}
        
        numerical_cols = self.dataset.select_dtypes(include=[np.number]).columns
        
        stats = {}
        for col in numerical_cols:
            stats[col] = {
                'mean': float(self.dataset[col].mean()),
                'median': float(self.dataset[col].median()),
                'std': float(self.dataset[col].std()),
                'min': float(self.dataset[col].min()),
                'max': float(self.dataset[col].max()),
                'count': int(self.dataset[col].count())
            }
        
        self.analysis_results['basic_stats'] = stats
        return stats
    
    def group_analysis(self, group_by: str, target_column: str) -> Dict:
        """
        Analyze data grouped by specific column
        
        Args:
            group_by (str): Column to group by
            target_column (str): Column to analyze
            
... (осталось: 126 строк)
Свернуть
message.txt
8 кб
﻿
"""
Data Analysis Module - New feature for Python Git project
Advanced data analysis capabilities using pandas and numpy
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Union
import json

class DataAnalyzer:
    """
    Advanced data analysis tool for statistical operations
    and data visualization preparation
    """
    
    def __init__(self, data_source: str = None):
        self.data_source = data_source
        self.dataset = None
        self.analysis_results = {}
        
    def load_csv_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from CSV file into pandas DataFrame
        
        Args:
            file_path (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Loaded dataset
        """
        try:
            self.dataset = pd.read_csv(file_path)
            print(f"✅ Successfully loaded data from {file_path}")
            print(f"📊 Dataset shape: {self.dataset.shape}")
            return self.dataset
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None
    
    def generate_sample_data(self, rows: int = 100) -> pd.DataFrame:
        """
        Generate sample dataset for demonstration
        
        Args:
            rows (int): Number of rows to generate
            
        Returns:
            pd.DataFrame: Generated sample data
        """
        np.random.seed(42)
        
        data = {
            'user_id': range(1, rows + 1),
            'age': np.random.randint(18, 65, rows),
            'salary': np.random.normal(50000, 15000, rows).round(2),
            'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], rows),
            'experience_years': np.random.randint(0, 20, rows),
            'performance_score': np.random.uniform(0.5, 1.0, rows).round(3)
        }
        
        self.dataset = pd.DataFrame(data)
        print(f"🎯 Generated sample dataset with {rows} rows")
        return self.dataset
    
    def basic_statistics(self) -> Dict:
        """
        Calculate basic statistical metrics for numerical columns
        
        Returns:
            Dict: Statistical summary
        """
        if self.dataset is None:
            print("❌ No dataset loaded. Generate or load data first.")
            return {}
        
        numerical_cols = self.dataset.select_dtypes(include=[np.number]).columns
        
        stats = {}
        for col in numerical_cols:
            stats[col] = {
                'mean': float(self.dataset[col].mean()),
                'median': float(self.dataset[col].median()),
                'std': float(self.dataset[col].std()),
                'min': float(self.dataset[col].min()),
                'max': float(self.dataset[col].max()),
                'count': int(self.dataset[col].count())
            }
        
        self.analysis_results['basic_stats'] = stats
        return stats
    
    def group_analysis(self, group_by: str, target_column: str) -> Dict:
        """
        Analyze data grouped by specific column
        
        Args:
            group_by (str): Column to group by
            target_column (str): Column to analyze
            
        Returns:
            Dict: Grouped analysis results
        """
        if self.dataset is None:
            print("❌ No dataset loaded.")
            return {}
        
        if group_by not in self.dataset.columns or target_column not in self.dataset.columns:
            print("❌ Specified columns not found in dataset.")
            return {}
        
        grouped = self.dataset.groupby(group_by)[target_column].agg([
            'count', 'mean', 'std', 'min', 'max'
        ]).round(3)
        
        result = grouped.to_dict()
        self.analysis_results[f'grouped_{group_by}'] = result
        
        print(f"📈 Grouped analysis by '{group_by}':")
        print(grouped)
        
        return result
    
    def detect_outliers(self, column: str, method: str = 'iqr') -> List[int]:
        """
        Detect outliers in specified column
        
        Args:
            column (str): Column to analyze
            method (str): Method for outlier detection ('iqr' or 'zscore')
            
        Returns:
            List[int]: Indices of outlier rows
        """
        if self.dataset is None or column not in self.dataset.columns:
            return []
        
        data = self.dataset[column]
        
        if method == 'iqr':
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = self.dataset[(data < lower_bound) | (data > upper_bound)].index.tolist()
        
        elif method == 'zscore':
            z_scores = np.abs((data - data.mean()) / data.std())
            outliers = self.dataset[z_scores > 3].index.tolist()
        
        print(f"🔍 Found {len(outliers)} outliers in '{column}' using {method} method")
        self.analysis_results['outliers'] = outliers
        
        return outliers
    
    def export_results(self, file_path: str = 'analysis_results.json'):
        """
        Export analysis results to JSON file
        
        Args:
            file_path (str): Path for output file
        """
        if not self.analysis_results:
            print("❌ No analysis results to export.")
            return
        
        try:
            with open(file_path, 'w') as f:
                # Convert numpy types to Python native types for JSON serialization
                def convert_types(obj):
                    if isinstance(obj, (np.integer, np.floating)):
                        return float(obj)
                    elif isinstance(obj, np.ndarray):
                        return obj.tolist()
                    elif isinstance(obj, dict):
                        return {k: convert_types(v) for k, v in obj.items()}
                    elif isinstance(obj, list):
                        return [convert_types(item) for item in obj]
                    return obj
                
                json.dump(convert_types(self.analysis_results), f, indent=2)
            print(f"💾 Analysis results exported to {file_path}")
        except Exception as e:
            print(f"❌ Error exporting results: {e}")


def demo_data_analysis():
    """
    Demonstration function for the DataAnalyzer class
    """
    print("🚀 Data Analysis Module Demonstration")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = DataAnalyzer()
    
    # Generate sample data
    print("\n1. Generating sample dataset...")
    dataset = analyzer.generate_sample_data(150)
    print(f"   Columns: {list(dataset.columns)}")
    
    # Basic statistics
    print("\n2. Calculating basic statistics...")
    stats = analyzer.basic_statistics()
    for col, metrics in stats.items():
        print(f"   {col}: mean={metrics['mean']:.2f}, std={metrics['std']:.2f}")
    
    # Group analysis
    print("\n3. Performing group analysis...")
    analyzer.group_analysis('department', 'salary')
    
    # Outlier detection
    print("\n4. Detecting outliers...")
    outliers = analyzer.detect_outliers('salary')
    print(f"   Found {len(outliers)} outliers in salary data")
    
    # Export results
    print("\n5. Exporting results...")
    analyzer.export_results('demo_analysis.json')
    
    print("\n🎉 Data analysis demonstration completed!")


if __name__ == "__main__":
    demo_data_analysis()
