# MalwDetect

### Obbiettivo del progetto: 
Questo progetto punta al raggiungimento di due obbiettivi. **Il primo obbiettivo** è quello di costruire un modello di Machine learning in grado di predire,utilizzando unicamente le caratteristiche dell'url, quali sono gli url legittimi (ovvero url che indicano risorse web lecite) e quali sono gli url phishing (ovvero web page dubbie).

Il **secondo obbiettivo** è quello di mostrare la pipeline di un modello di machine learning. Ovvero di mostrare tutte le procedure e tutte le scelte che sono state prese per creare un modello di ML a partire da diversi dataset trovati online.

### Risorse contenute nella repository: 
- **Cartella dataset**: contiene 5 file .CSV. Questi sono i dataset utilizzati all'interno del progetto per estrarre gli url (di entrambe le classi).I dataset sono stati scaricati da diverse fonti come ad esempio Openphish, PhishTank e Kaggle.
- **progetto.ipynb**: è il progetto vero è proprio.In questo file è possibile vedere tutto il procedimento e tutte le scelte che sono state effettuate in fase di progettazione.
- **featureExtraction.py**: questo è il modulo che si occupa dell'estrazione delle feature.
- **generateDataset.py** questo è il modulo che viene utilizzato per generare il dataset finale.
- **finalDataset.csv** questo è il dataset finale (url + feature) generato in fase di proggettazione.
- **Demo.py** questa è una piccola demo che deve utilizza il modello creato per predire url inseriti dall'utente.

### Cone replicare il progetto:
per replicare il progetto è necessario runnare il file progetto.ipynb. Solo dopo aver finito di runnare tale file, è possibile visualizzare la demo. Questo perchè alla fine del Jupyter notebook viene creato un file (ovvero modelRF.joblib) che verrà utilizzato da Demo.py. Senza quel filela demo non può essere avviata.

### Accortenze:
1. è sconsigliato rigenerare il finalDataset.csv in quanto la sua generazione richiede molto tempo-
2. Alcune celle, nello specifico le celle che effettuano la grid search richiedono tempi molto lunghi. Tali celle possono essere saltate in quanto sono solo dimostrative.

