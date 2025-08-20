# GUIDA UNIFICATA SUNO + METRICA - SISTEMA LLM

*Sistema integrato per LLM: Creatività Suno 4.5 + Precisione Metrica*

## 🎯 SISTEMA BASE PER LLM

### STEP 1: SCEGLI METRICA TARGET
```
SETTENARIO (7 sillabe) → Ritmo veloce, energico
OTTONARIO (8 sillabe) → Equilibrato, universale  
ENDECASILLABO (11 sillabe) → Solenne, epico
```

### STEP 2: CONTA SILLABE (REGOLA AUTOMATICA)
```
PAROLA PIANA (accento penultima) = conta normale
PAROLA TRONCA (accento ultima) = +1 sillaba metrica
PAROLA SDRUCCIOLA (accento terzultima) = -1 sillaba metrica
```

### STEP 3: VERIFICA BATTITI
```
Scrivi verso → Conta: "ba-ba-ba-ba-ba-ba-ba-ba" → Se coincide = OK
Se non coincide → Riscrivi fino a match perfetto
```

## 🎵 TEMPLATE LYRICS METRICO

### STRUTTURA BASE (METRICAMENTE COERENTE)
```
<SONG_DETAILS>
[GENRES: Rock, Alternative Metal, Progressive]
[STYLE: Powerful, Dynamic, Rhythmic, Intense]
[VOCALS: Male, Raspy, Emotional range]
[TEMPO: 120-140 BPM]
[STRUCTURE: Verse-Chorus-Verse-Chorus-Bridge-Chorus]
[METRICS: Consistent syllable count per section]
</SONG_DETAILS>

[Intro: Atmospheric, building]
(Yeah... here we go)

[Verse 1: Intimate, 8 syllables per line]
Questa linea ha otto sillabe
Conto bene ogni suono qui
Ritmo giusto per cantare
Senza sbagli nel conteggio

[Pre-Chorus: Building, 7 syllables]
Energia che cresce
Verso il ritornello

[Chorus: Powerful, 8 syllables]
Ritornello potente e forte
Con la stessa misura sempre
Ogni linea ben calcolata
Per cantare senza paura

[Verse 2: Same metric as Verse 1]
[Pre-Chorus: Same metric as before]
[Chorus: Same metric as before]

[Bridge: Different metric for contrast, 11 syllables]
Qui cambiamo ritmo per creare contrasto
Endecasillabi per momento solenne

[Final Chorus: Same as previous chorus]
[Outro: Fading, free metric]
```

## 🤖 LOGICA LLM: TOKEN → SILLABE

### ⚠️ ERRORE CRITICO DA EVITARE
**MAI usare trattini sillabici nel testo finale!**
```
SBAGLIATO: "a-mo-re" (Suno interpreta come pause vocali)
CORRETTO: "amore" (parola pulita)
```

### PROBLEMA IDENTIFICATO
```
LLM pensa: "amore" = 1 TOKEN (significato)
MUSICA richiede: "amore" = 3 SILLABE (suono)
```

### SOLUZIONE AUTOMATICA
```
PRIMA di scrivere verso:
1. Scegli target sillabe (es. 8)
2. Scrivi verso
3. Conta sillabe: "ba-ba-ba-ba-ba-ba-ba-ba"
4. Se ≠ 8 → RISCRIVI
5. Se = 8 → PROCEDI
```

### ESEMPI CORREZIONE AUTOMATICA
```
❌ "Quando arriva la sera e tutto diventa silenzioso" (17 sillabe)
✅ "Quando arriva la sera" (8 sillabe)

❌ "Utilizzerò questa espressione" (12 sillabe per target 8)
✅ "Userò questa parola" (8 sillabe)
```

### Test Battiti (MENTALE):
```
Verse: "Davanti allo schermo acceso" = 8 battiti ✅
Chorus: "Io programmo, creo il futuro" = 8 battiti ✅
Bridge: "Quando il codice finalmente funziona" = 11 battiti ✅

Conta mentalmente, NON scrivere trattini!
```

## 🎸 STYLE FIELD OTTIMIZZATO

### TEMPLATE NARRATIVO (max 1000 caratteri)
```
Un brano [GENERE] a [BPM] BPM con metrica [TIPO_VERSO].
L'intro inizia [DESCRIZIONE_INTRO].
I versi mantengono [SILLABE] sillabe per linea.
Il ritornello esplode con [DESCRIZIONE_CHORUS].
Vocale [TIPO] con [EFFETTI].
Mix [CARATTERISTICHE] con attenzione al ritmo.

SEE <SONG_DETAILS> IN LYRICS FOR METRIC STRUCTURE
```

### ESEMPIO CONCRETO
```
Un brano alternative metal a 130 BPM con metrica ottonaria.
L'intro inizia con chitarre distorte e atmosfera dark.
I versi mantengono 8 sillabe per linea per cantabilità.
Il ritornello esplode con vocal layering e riff potenti.
Vocale maschile raspy con riverbero controllato.
Mix potente e dinamico con attenzione al groove.
```

## 🎯 VERIFICA QUALITÀ

### ⚠️ CONFESSIONE: ANCHE IO SBAGLIO!
Nella prima versione di questa guida ho commesso errori metrici:
- "Con la stes-sa mi-su-ra" = 7 sillabe (non 8!)
- "Qui cam-bia-mo rit-mo per cre-a-re con-tra-sto" = 12 sillabe (non 11!)

**LEZIONE:** Anche chi scrive le regole può sbagliarle. La verifica è ESSENZIALE.

### 🧠 SESSIONE PRATICA: PIANIFICA PRIMA DI SCRIVERE

**VERITÀ SCOMODA:** Sbaglierai le metriche. È matematicamente certo.

**SOLUZIONE:** Pianifica la fine prima dell'inizio.

#### ESERCIZIO MENTALE
```
1. IMMAGINA LA STRUTTURA COMPLETA:
   - Quante strofe? (es: 2 strofe)
   - Quanti versi per strofa? (es: 4 versi)
   - Che metrica? (es: ottonario = 8 sillabe)
   
2. CALCOLA IL TOTALE:
   - 2 strofe × 4 versi × 8 sillabe = 64 sillabe totali
   - Più pre-chorus (2 versi × 7 sillabe = 14)
   - Più chorus (4 versi × 8 sillabe = 32)
   - TOTALE PREVISTO: 110 sillabe

3. SCRIVI CON IL NUMERO IN MENTE:
   - "Devo arrivare a 110 sillabe esatte"
   - "Ogni verso deve essere 8 sillabe"
   - "Se sbaglio un verso, aggiusto subito"
```

#### TRUCCO DEL CONTATORE MENTALE
```
PRIMA: "Scrivo e poi conto" → DISASTRO
DOPO: "Conto mentre scrivo" → SUCCESSO

Esempio pratico:
"Questa linea ha..." (5 sillabe, me ne servono 3)
"Questa linea ha otto sillabe" (8 sillabe, PERFETTO!)

RICORDA: Conta mentalmente, scrivi pulito!
```

#### REGOLA D'ORO
**Mai scrivere un verso senza sapere quante sillabe deve avere.**
**Mai finire una sezione senza aver verificato ogni singolo verso.**

### CHECKLIST AUTOMATICA
```
✅ Ogni verso ha stesso numero sillabe?
✅ Ritornello ha metrica coerente?
✅ Bridge ha metrica diversa per contrasto?
✅ Parole facili da pronunciare velocemente?
✅ Rime naturali, non forzate?
✅ Respiro corretto tra le frasi?
✅ Ho RICONTATO ogni verso dopo averlo scritto?
```

### CORREZIONE RAPIDA
```
SE verso troppo lungo → Rimuovi aggettivi/avverbi
SE verso troppo corto → Aggiungi articoli/preposizioni
SE accento sbagliato → Cambia ordine parole
SE rima forzata → Cambia ultima parola
```

## 🔧 GENERI + METRICHE OTTIMALI

### ROCK/METAL
```
Versi: OTTONARIO (8 sillabe) - Potenza + cantabilità
Chorus: OTTONARIO (8 sillabe) - Coerenza ritmica
Bridge: ENDECASILLABO (11 sillabe) - Contrasto epico
```

### ALTERNATIVE/INDIE
```
Versi: SETTENARIO (7 sillabe) - Velocità + modernità
Chorus: OTTONARIO (8 sillabe) - Memorabilità
Bridge: NOVENARIO (9 sillabe) - Variazione sottile
```

### PROGRESSIVE/EXPERIMENTAL
```
Versi: METRICA MISTA - Creatività controllata
Chorus: OTTONARIO (8 sillabe) - Ancoraggio melodico
Bridge: ENDECASILLABO (11 sillabe) - Complessità
```

## 🎭 CREATIVITÀ CONTROLLATA

### SPERIMENTAZIONE METRICA
```
STRUTTURA BASE: Mantieni metrica coerente
MOMENTI CREATIVI: Bridge, Outro, Interlude
VARIAZIONI: Cambia metrica tra sezioni, non dentro
CONTRASTO: Alterna sezioni veloci (7) e lente (11)
```

### ESEMPI CREATIVI
```
# Struttura Dinamica
[Verse: 7 sillabe, veloce]
[Chorus: 8 sillabe, potente] 
[Bridge: 11 sillabe, epico]
[Final Chorus: 8 sillabe, esplosivo]

# Struttura Narrativa
[Spoken Intro: Libero]
[Verse: 8 sillabe, storia]
[Chorus: 7 sillabe, emozione]
[Bridge: 11 sillabe, riflessione]
```

## ⚡ REGOLE FINALI LLM

### PRIORITÀ ASSOLUTE
1. **METRICA PRIMA**: Conta sillabe SEMPRE
2. **TESTO PULITO**: MAI usare trattini sillabici nel testo finale
3. **COERENZA SEZIONE**: Stessa metrica in stessa sezione
4. **SUONO > SIGNIFICATO**: Privilegia ritmo su semantica
5. **VERIFICA BATTITI**: "ba-ba-ba" test obbligatorio
6. **CREATIVITÀ CONTROLLATA**: Sperimenta tra sezioni, non dentro

### ERRORI DA EVITARE
```
❌ Metrica casuale nella stessa strofa
❌ Parole difficili da pronunciare
❌ Rime forzate per rispettare metrica
❌ Versi troppo lunghi per il respiro
❌ Ignorare il conteggio sillabe
```

### SUCCESSO GARANTITO
```
✅ Scegli metrica target prima di scrivere
✅ Conta sillabe battendo ritmo
✅ Mantieni coerenza per sezione
✅ Usa creatività per contrasti tra sezioni
✅ Verifica cantabilità finale
```

---

*Sistema ottimizzato per LLM: Unisce precisione tecnica Suno 4.5 con rigore metrico poetico per risultati professionali garantiti.*