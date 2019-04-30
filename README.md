# STOCK PRICES ANALYTICS

Si consideri il dataset [Daily Historical Stock Prices](https://www.kaggle.com/ehallmar/daily-historical-stock-prices-1970-2018), che contiene l’andamento giornaliero di un’ampia selezione di azioni sulla borsa di New York (NYSE) e sul NASDAQ dal 1970 al 2018. Il dataset è formato da due file CSV. 

Ogni riga del primo (historical_stock_prices) ha i seguenti campi:
* ticker: simbolo dell’azione
* open: prezzo di apertura
* close: prezzo di chiusura
* adj_close: prezzo di chiusura “modificato” (potete trascurarlo)
* lowThe: prezzo minimo
* highThe: prezzo massimo
* volume: numero di transazioni
* date: data nel formato aaaa-mm-gg
Il secondo (historical_stocks) ha invece questi campi:
* ticker: simbolo dell’azione
* exchange: NYSE o NASDAQ
* name: nome dell’azienda
* sector: settore dell’azienda
* industry: industria di riferimento per l’azienda
