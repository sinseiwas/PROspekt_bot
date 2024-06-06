[![CI/CD GitHub Actions](https://github.com/sinseiwas/PROspekt_bot/actions/workflows/main.yml/badge.svg)](https://github.com/sinseiwas/PROspekt_bot/actions/workflows/test-action.yml)
[![Coverage Status](https://coveralls.io/repos/sinseiwas/PROspekt_bot/badge.svg?branch=main)](https://coveralls.io/github/sinseiwas/PROspekt_bot?branch=main)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sinseiwas_PROspekt_bot&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sinseiwas_PROspekt_bot)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=sinseiwas_PROspekt_bot&metric=code_smells)](https://sonarcloud.io/dashboard?id=sinseiwas_PROspekt_bot)


# PROJECT
TG BOT


## Описание
Проект представляет собой телеграм бота, который выводит информацию о театре ПРОспект. В проекте реализован набор алгоритмов, использующих условные и циклические операторы.

## Алгоритмы
1. Программа достаёт из файла exel нужную ячейку и выводит мероприятия на день
3. Программа достаёт из файла exel нужные ячейки и выводит описание должностного лица(конкретного человека)
4. Программа достаёт из файлв exel нужные ячейки на цказанный период времени и выводит постановки на этот период

## Функциональности
Пользователь может:
1. Нажать на кнопку должностные лица, выбрать кого-то конкретного. Программа отобразит о нём информацию
2. Нажать на кнопку постановки, выбрать месяц. Программа отобразит постановки на этот месяц
3. Нажать на кнопку треннинги. Программа отобразит информацию о треннингах на текущий месяц
4. Нажать на кнопку СММ. Программа отобразит список постов, которые нужно сделать


Краткие описания сценариев работы:
- Пользователь запускает бота
- Приложение выбирает команды
- Пользователь узнаёт то, что нужно

- [Функциональные модели](docs/functions.md)
- [Структурные модели](docs/struct.md)
- [Поведенческие модели](docs/behavior.md)