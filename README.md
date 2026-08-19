# calc-cli

Консольный калькулятор с историей операций и сохранением в файл.  
Реализован на Python.

[![CI](https://github.com/Belannandere/calc-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/Belannandere/calc-cli/actions/workflows/ci.yml)

---

## Возможности

- Арифметические операции: `+`, `-`, `*`, `/`
- История операций в памяти и в файле `history.txt`
- Команды:
  - `history` — показать историю
  - `clear` — очистить историю
  - `exit` — выйти
- Обработка ошибок (деление на ноль, неверный ввод)

---

### Демонстрация работы калькулятора

![Демонстрация работы калькулятора](https://raw.githubusercontent.com/Belannandere/calc-cli/main/assets/demo1.gif)

---

## Запуск локально (без Docker)

```bash
python main.py
```

## Запуск через Docker

```bash
docker build -t calc-cli .
docker run -it calc-cli
```
---