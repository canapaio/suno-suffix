# Suno Prompt Suffix (Plugin CCat)

Plugin per Cheshire Cat AI progettato per aiutare a creare prompt ottimizzati per Suno AI.

## Sistema Dinamico
Questo plugin utilizza un **sistema dinamico file-comando**.
- Qualsiasi file Markdown inserito nella cartella `documents/` diventa automaticamente un comando.
- **Esempio**: `documents/mia_guida.md` -> Trigger `:mia_guida:`

## Note Didattiche
Questo plugin è progettato come risorsa di apprendimento per lo sviluppo su Cheshire Cat:
- **Hooks**: Vedi `plugin.py` per capire come `before_cat_reads_message` intercetta i prompt.
- **Settings**: Vedi `settings.py` per la configurazione basata su Pydantic.
- **Caricamento Dinamico**: Il plugin scansiona il file system per creare comandi al volo.
- **Conteggio Token**: Usa `tiktoken` (cl100k_base) per stimare l'uso dei token per il contenuto iniettato.

## Comandi Predefiniti
- `:s1:` (da `documents/s1.md`): **Guida Metrica & Testi**.
- `:s2:` (da `documents/s2.md`): **Guida Formattazione Suno**.

## Configurazione
- **commands.json**: Generato automaticamente. Modifica questo file per personalizzare trigger, istruzioni e template wrapper per ogni documento.
- **Settings**:
    - **Educational Mode**: Attiva/disattiva le istruzioni in chat.
    - **Smart Reload**: Controlla automaticamente se i file sono cambiati ad ogni messaggio (ottimizzato).

## Installazione
1. Copia la cartella `suno-suffix` nella cartella `cat/plugins/` del tuo Cheshire Cat.
2. Riavvia il Cat.

## Ringraziamenti
Un ringraziamento speciale al team di **Cheshire Cat AI** per aver creato un framework così straordinario ed estensibile.
- [Sito Web Cheshire Cat AI](https://cheshirecat.ai/)
- [Repository GitHub](https://github.com/cheshire-cat-ai/core)
