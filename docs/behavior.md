# ПОВЕДЕНЧЕСКИЕ МОДЕЛИ

## ПОСТАНОВКИ
![THEATRE](https://github.com/sinseiwas/PROspekt_bot/blob/507173e5827142b6157ca4b6aea5956a9b77abde/docs/diagrams/theatre_status.png)

- Idle: Начальное состояние, в котором бот ожидает команду от пользователя.
- SelectingMonth: Состояние, в котором бот предлагает пользователю выбрать месяц.
- FetchingPerformances: Состояние, в котором бот получает данные о постановках на выбранный месяц.
- DisplayingPerformances: Состояние, в котором бот отображает данные о постановках.

## ТРЕННИНГИ
![TRAININGS](https://github.com/sinseiwas/PROspekt_bot/blob/507173e5827142b6157ca4b6aea5956a9b77abde/docs/diagrams/treninngs_status.puml)

- Idle: Начальное состояние бота, когда он ожидает команду от пользователя.
- FetchingTrainings: Состояние, в котором бот получает данные о тренингах.
- DisplayingTrainings: Состояние, в котором бот отображает информацию о тренингах.

## СММ
![CONTENT PLAN](https://github.com/sinseiwas/PROspekt_bot/blob/507173e5827142b6157ca4b6aea5956a9b77abde/docs/diagrams/content_plan_status.png)

- User: Пользователь взаимодействует с ботом, нажимая кнопку "СММ".
- Bot: Телеграм бот, который принимает и отправляет сообщения.
- MessageHandler: Обработчик сообщений, который обрабатывает команды и взаимодействует с другими компонентами.
- DBConnector: Компонент для взаимодействия с базой данных, который получает данные по запросу.
- ContentRepository: Репозиторий, содержащий данные о постах, используемый для получения информации.

## ДОЛЖНОСТНЫЕ ЛИЦА
![DIRECTORS](https://github.com/sinseiwas/PROspekt_bot/blob/507173e5827142b6157ca4b6aea5956a9b77abde/docs/diagrams/director_status.png)

- Idle: Начальное состояние бота, когда он ожидает команду от пользователя.
- FetchingData: Состояние, в котором бот получает данные о должностных лицах.
- DisplayingOptions: Состояние, в котором бот отображает варианты должностных лиц для выбора.
- FetchingInfo: Состояние, в котором бот получает информацию о выбранном должностном лице.
- DisplayingInfo: Состояние, в котором бот отображает информацию о выбранном должностном лице.