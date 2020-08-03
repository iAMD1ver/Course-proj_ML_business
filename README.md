###### Итоговый проект курса "Машинное обучение в бизнесе"

Сервис позволяет предсказать курс USD на поределенную дату. 

На вход подаются следующие параметры: 
* date - дата на которую предсказывается курс USD, 
* curs_y - курс EUR на t-1 дату https://www.cbr.ru/currency_base/dynamics, 
* WA_TOD_RATE - средневзвешенный курс USD_TOD на бирже на t-2 дату https://www.cbr.ru/hd_base/micex_doc/, 
* VALUE_TOD - объем торогов на валютной бирже USD_TOD на t-2 дату https://www.cbr.ru/hd_base/micex_doc/,	
* WA_TOM_RATE - средневзвешенный курс USD_TOM на бирже на t-2 дату https://www.cbr.ru/hd_base/micex_doc/, 
* VALUE_TOM - объем торогов на валютной бирже USD_TOM на t-2 дату https://www.cbr.ru/hd_base/micex_doc/, 
* Rate - ставка Банка России по инструмента овернайт на t-1 дату https://www.cbr.ru/hd_base/overnight/, 
* value_x - LIBOR ставка 12М на t-1 дату, 
* value_y - LIBOR ставка 3М на t-1 дату,	
* Brent - котировка стоимоти Брент на t-1 дату, 
* t_1 - курс USD на t-1 дату https://www.cbr.ru/currency_base/dynamics, 
* t_2 - курс USD на t-2 дату https://www.cbr.ru/currency_base/dynamics.

Данные: с сайта ЦБР, ICE, Биржевых агрегаторов

Модель: Градиентный бустинг