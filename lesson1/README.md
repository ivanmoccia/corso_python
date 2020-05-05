# Esercizio 1

Prerequisiti:

- avere il programma `pip` installato (dovresti già averlo se hai python installato)

Nota: il programma `pip` serve per installare librerie python open source

In questo esercizio imparerai a:

- creare un _virtual environment_
- attivare e disattivare il v.e.
- installare delle dipendenze nel v.e.

Un virtual environment serve ad avere una specifica versione di python e delle librerie di cui farai uso per un progetto specifico.
L'idea è di evitare l'installazione di librerie globalmente nel computer. Piuttosto, per ogni progetto avere le corrispondenti dipendenze installate in un _ambiente virtuale_. Così facendo eviterai di far partire un programma con le versioni sbagliate di python o delle librerie dalle quali dipende.

1. Installla la libreria `virtualenv` usando `pip`. Digita `pip install virtualenv` nel terminal. Se non funziona, vuol dire che forse il tuo computer non trova il programma pip, e puoi provare `python -m pip install virtualenv`.
2. Ora che hai `virtualenv` installato puoi usarlo per creare l'ambiente virtuale. Digita `virtualenv .env` che crea una cartella dove si inizializza l'ambiente virtuale. Una pratica comune è renderla una cartella nascosta (per questo ha il punto davanti).
3. Ogni ambiente virtuale è una cartella, come quella che hai creato, e al suo interno trovi uno script che serve ad attivarlo, ovvero a dire "sto usando questo ambiente". Lo script si chiama `activate` e si trova all'interno della cartella `bin`. Ora attiva l'ambiente virtuale. Digita `source .env/bin/activate`
4. Per disattivare l'ambiente virtuale digita `deactivate`. Non farlo ora siccome lo vogliamo ancora usare.

# Installare librerie (dipendenze)

Ora che hai il tuo ambiente virtuale attivato puoi provare ad eseguire il file python che trovi nella cartella, una volta così come lo trovi, e de-commentando le righe che trovi sotto forma di commento. Cosa noti? Perchè? Risolvilo con `pip` (e ricorda di aver attivato l'ambiente virtuale).

# Occhio.. prima di fare commit..

Ora potresti fare `git add`, `git commit`, `git push`, ecc., ma aspetta, prima, siccome non vogliamo che il nostro ambiente virtuale (che può diventare bello pesante) venga salvato in github, possiamo specificare che lo vogliamo ignorare. Per fare questo, crea un file chiamato `.gitignore` e all'interno scrivici riga per riga i files o le cartelle che vuoi ignorare. Per ora il contenuto sarà semplicemente una riga con scritto `.env`.
