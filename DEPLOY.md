# Инструкция по развертыванию на Vercel

Код уже загружен в GitHub: https://github.com/znn-cmd/asp_rera.git

## Шаги для развертывания на Vercel:

### Вариант 1: Через веб-интерфейс Vercel

1. Перейдите на https://vercel.com и войдите в систему
2. Нажмите "Add New" → "Project"
3. Подключите GitHub аккаунт (если еще не подключен)
4. Найдите репозиторий `znn-cmd/asp_rera` и выберите его
5. Настройки:
   - **Framework Preset**: Other
   - **Root Directory**: оставьте пустым или укажите `.`
   - **Build Command**: оставьте пустым
   - **Output Directory**: `docs`
   - **Install Command**: оставьте пустым
6. Нажмите "Deploy"

### Вариант 2: Через Vercel CLI

```bash
# Установите Vercel CLI глобально
npm i -g vercel

# Войдите в Vercel
vercel login

# Разверните проект
vercel

# Для production deployment
vercel --prod
```

### Альтернатива: Используйте GitHub Pages

Если хотите использовать GitHub Pages вместо Vercel:

1. Перейдите в Settings репозитория на GitHub
2. Найдите "Pages" в левом меню
3. Source: выберите "Deploy from a branch"
4. Branch: `main`
5. Folder: `/docs`
6. Нажмите "Save"

Сайт будет доступен по адресу:
`https://znn-cmd.github.io/asp_rera/`

## Настройки для Vercel

Для правильной работы сайта на Vercel убедитесь, что в `vercel.json` указаны правильные пути.

Если структура работает некорректно, обновите `vercel.json`:

```json
{
  "version": 2,
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/docs/$1"
    }
  ]
}
```

## Проверка

После развертывания проверьте:
- Главная страница: `https://ваш-сайт.vercel.app/`
- Русская версия: `https://ваш-сайт.vercel.app/ru/`
- Английская версия: `https://ваш-сайт.vercel.app/en/`

## Обновление сайта

После внесения изменений в код:

```bash
git add .
git commit -m "Update content"
git push
```

Vercel автоматически пересоберет и развернет новую версию сайта.

