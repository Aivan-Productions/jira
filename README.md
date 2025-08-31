## Копируем проект себе локально

```
git init
git remote add origin git@github.com:Aivan-Productions/jira.git
git pull origin main
```

Создание виртуального окружения и установка необходимых библиотек

```
python -m venv .venv
. .venv/bin/activate (если у вас Linux)
.venv\Scripts\activate (если у вас Windows)
pip install -r requirements.txt
```

## Как выполнять задачи?

#### 1.Создаем ветку под свою задачу

```
git checkout -b branch_name
```

#### 2.Добавляем изменения в свою ветку
```
git add .
git commit -m "new commit"
```

#### 3.Отправляем изменения на github и создаем pull request
```
git push origin branch_name
```

*После удачного ревью выполняем следующий пункт. Если нужно внести правки повторяем 2 и 3 пункты*

#### 4.Переключаемся на основную ветку и удаляем свою

```
git checkout main
git branch -d branch_name
```

#### 5.Подтягиваем изменения с основной ветки

```
git pull origin main
```

### Как называть ветку?

Название состоит из 3-х частей

Тип: ```feat```, ```fix```, ```refactor```, ```chore```, ```build```, ```docs```

Название: Пишем похоже на название задачи (пример ```implement-logging```, ```fix-docker```)

Номер: берем номер задачи (пример ```#30```, ```#19```)

Итог: ```feat/add-uers-model/#15```

### Как называть коммит?

Название состоит из 2-х частей

Тип: ```feat```, ```fix```, ```refactor```, ```chore```, ```build```, ```docs```

Название: Пишем кратко и по делу (пример ```add config file```, ```add migrations```)

Итог: ```feat: add logging in project```

### Что мы вообще делаем?

Мы создаем аналог доски в Jira (как вы могли догадаться). Сейчас создаем каркас для дальнейшего расширения и интеграции с другими сервисами

*Если не знаете что такое [канбан-доска](https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D0%B1%D0%B0%D0%BD-%D0%B4%D0%BE%D1%81%D0%BA%D0%B0), ознакомьтесь. Это важно для понимания того, что мы будем создавать*

### Сущности проекте

```
Tasks
id primary key
title string(256)
description text
start datetime
end datetime
tags Tags
author Users
executors Users
created_at datetime
updated_at datetime
status Statuses
```

```
Tags
id primary key
title string(32)
tasks Tasks
```

```
Users
id primary key
username string(32)
role Roles
hashed_passsword string
```

```
Roles
id primary key
title enum(owner, mentor, student)
```

```
Statuses
id primary eky
title enum(backlog, todo, in_progress, review, done, canceled)
```

```
Columns
id primary key
title string(32)
statuses Statuses
broad Broads
position int
```

```
Board
id primary key
title string
author Users
created_at datetime
updaeted_at datetime
```

### Откуда брать информацию для решения задач?
- [ChatGPT](https://chatgpt.com) - ваш основной помощник для написания код и поиска необходимой информации
- [Google](https://google.com) - если у вас есть желание изучать информацию в первоисточниках, используйте google
- [Пример проекта](https://github.com/DmitryGolub/blog) - будет очень круто если вы будете ориентироваться на этот проект, т.к. он взят за основу и все что мы будем делать будет похоже на него. Поэтому ориентируйтесь на него, это будет очень полезно

*Можете использовать другие нейронки вам известные для решения задач, если у вас есть трудности с доступом к chatgpt*

### Полезные ссылки
- [Ссылка на проект](https://github.com/Aivan-Productions/jira)
- [Ссылка на задачи](https://github.com/orgs/Aivan-Productions/projects/18/views/1)
- [Ссылка на проект откуда можно брать код](https://github.com/DmitryGolub/blog)
