## Копируем проект себе локально

```
git init
git remote add origin git@github.com:Aivan-Productions/jira.git
git pull origin main
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

### Структура проекта

Появиться позже
