## Время работы workflow

### Установка зависимостей:
1.	С кешем: 10с.
2.	Без кеша: 8c.
### Запуск тестов:
1.	С кешем: 1с.
2.	Без кеша: ~0c.
### Анализ SonarQube:
1.	С кешем: 53с.
2.	Без кеша: 51с.
### Общее время:
1.	С кешем: 1м12с. (Python CI/CD Pipeline #8)
2.	Без кеша: 1м8с. (Python CI/CD Pipeline #9)
### Итоги
На маленьком проекте кэширование показывает небольшое ускорения работы пайплайна. Вероятно, на больших проектах это поможет сильно сократить время сборки.
Ссылка на результаты пайплайнов: https://github.com/frog016/Mihalyov_practice_205/actions.
