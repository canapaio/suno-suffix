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

## 🎵 SCHEMA INIZIALE CON <SONG_DETAILS>

### FASE 1: PIANIFICAZIONE METRICA
```
<SONG_DETAILS>
Genere: [MESCOLA GENERI! Es: Pop-Rock con Bridge Jazz, Indie-Folk con Chorus Elettronico]
Stile: [DINAMICO! Cambia energia tra sezioni: Intimista→Esplosivo→Epico]
Voci: [VARIA! Solista→Coro→Duetto, sperimenta effetti vocali]
Tempo: [IN MOVIMENTO! Accelera/rallenta tra sezioni per creare tensione]
Struttura: [ORIGINALE! Non solo Verse-Chorus, prova AABA, ABCB, forme ibride]

SCHEMA METRICO DINAMICO:
- Verse: [X sillabe] - Tag: [Genere A + descrizione musicale]
- Pre-Chorus: [Y sillabe] - Tag: [Transizione + build-up]
- Chorus: [Z sillabe] - Tag: [Genere B + energia esplosiva]
- Bridge: [W sillabe] - Tag: [Genere C + contrasto totale]
- Outro: [Libero] - Tag: [Fusione generi + risoluzione]

ORIGINALITÀ OBBLIGATORIA:
- EVITA cliché musicali comuni
- MESCOLA almeno 2-3 generi diversi
- CREA progressioni emotive inaspettate
- USA strumenti non convenzionali per il genere principale

TEMA CENTRALE: [Messaggio originale, evita luoghi comuni]
PAROLE CHIAVE: [Termini freschi, metafore innovative]
</SONG_DETAILS>
```

### FASE 2: IMPLEMENTAZIONE TESTO
Dopo aver definito lo schema, scrivi il testo seguendo:
1. **Rispetta le sillabe** definite nello schema
2. **Usa i tag musicali** pianificati
3. **Mantieni coerenza** metrica per sezione
4. **Integra parole chiave** naturalmente

### ESEMPIO PRATICO
```
<SONG_DETAILS>
Genere: INDIE-FOLK con Chorus ELECTRO-POP e Bridge JAZZ-FUSION
Stile: DINAMICO! Intimista→Esplosivo→Contemplativo→Trionfo finale
Voci: VARIA! Sussurro→Canto potente→Vocoder→Coro gospel
Tempo: IN MOVIMENTO! 70 BPM→120 BPM→90 BPM→140 BPM
Struttura: ORIGINALE! Intro-Verse-Pre-Chorus-Chorus-Verse-Bridge-Chorus-Outro

SCHEMA METRICO DINAMICO:
- Verse: 8 sillabe - Tag: Indie-folk intimista, fingerpicking guitar + violino
- Pre-Chorus: 7 sillabe - Tag: Transizione elettronica, synth pad crescente
- Chorus: 8 sillabe - Tag: Electro-pop esplosivo, beat trap + archi
- Bridge: 11 sillabe - Tag: Jazz-fusion contemplativo, sax solo + piano
- Outro: Libero - Tag: Fusione tutti i generi, crescendo orchestrale

ORIGINALITÀ APPLICATA:
- EVITA: "seguire i sogni", "non mollare mai"
- MESCOLA: Folk acustico + elettronica + jazz + gospel
- PROGRESSIONE: Vulnerabilità→Determinazione→Saggezza→Celebrazione
- STRUMENTI: Banjo + sintetizzatori + sassofono + coro gospel

TEMA CENTRALE: Trasformare le cicatrici in costellazioni (metafora originale)
PAROLE CHIAVE: cicatrici, costellazioni, metamorfosi, alchimia, rinascita
</SONG_DETAILS>
```

Poi implementi il testo rispettando schema e tag pianificati.

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

[Verse 1: Intimate storytelling, acoustic guitar]
Questa linea ha otto sillabe
Conto bene ogni suono qui
Ritmo giusto per cantare
Senza sbagli nel conteggio

[Pre-Chorus: Building tension, drums entering]
Energia che cresce
Verso il ritornello

[Chorus: Explosive anthem, full band]
Ritornello potente e forte
Con la stessa misura sempre
Ogni linea ben calcolata
Per cantare senza paura

[Verse 2: Confident stride, same energy as Verse 1]
[Pre-Chorus: Rising intensity, same as before]
[Chorus: Powerful declaration, same as before]

[Bridge: Epic emotional climax, orchestral swell]
Qui cambiamo ritmo per creare contrasto
Endecasillabi per momento solenne

[Final Chorus: Triumphant finale, layered vocals]
[Outro: Peaceful fade, gentle resolution]
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

## 🎵 REGOLE TAG SEZIONI (PRIORITÀ MUSICALE)

### ⚠️ PRIORITÀ ASSOLUTA: DESCRIZIONE MUSICALE PRIMA!

**❌ SBAGLIATO** (focus solo su sillabe):
```
[Bridge – Endecasillabo (11 sillabe)]  ← Troppo tecnico!
[Chorus: 8 syllables per line]         ← Noioso!
```

**✅ CORRETTO** (descrizione musicale + sillabe opzionali):
```
[Bridge: Epic, soaring, emotional climax]
[Chorus: Explosive, full band with layered vocals]
[Verse: Intimate, acoustic guitar only]
[Pre-Chorus: Building tension, drums entering]
```

### 📝 FORMULA PERFETTA PER TAG
```
[SEZIONE: DESCRIZIONE_MUSICALE, dettagli_opzionali]

Esempi:
[Intro: Atmospheric, building suspense]
[Verse: Melancholic, stripped down piano]
[Chorus: Triumphant, orchestral swell]
[Bridge: Vulnerable, whispered confession]
[Outro: Hopeful, fading into distance]
```

### 🎯 COSA DESCRIVERE NEI TAG

**ENERGIA & DINAMICA**:
- Explosive, Intimate, Building, Fading
- Powerful, Gentle, Aggressive, Calm
- Rising, Falling, Steady, Pulsing

**STRUMENTAZIONE**:
- Full band, Acoustic only, Piano driven
- Orchestral, Electronic, Stripped down
- Heavy drums, Ambient pads, Guitar solo

**EMOZIONE & ATMOSFERA**:
- Epic, Melancholic, Triumphant, Mysterious
- Vulnerable, Confident, Nostalgic, Euphoric
- Dark, Bright, Dreamy, Gritty

**STILE VOCALE**:
- Whispered, Belted, Harmonized, Spoken
- Raspy, Smooth, Falsetto, Growled

### 🔥 ESEMPI PERFETTI
```
[Intro: Ambient soundscape, distant echoes]
[Verse 1: Intimate storytelling, fingerpicked guitar]
[Pre-Chorus: Tension building, bass entering]
[Chorus: Anthemic explosion, full arrangement]
[Verse 2: Confident stride, driving rhythm]
[Bridge: Emotional breakdown, piano and strings]
[Final Chorus: Epic finale, layered vocals soaring]
[Outro: Peaceful resolution, gentle fade]
```

### 💡 SILLABE: DETTAGLIO SECONDARIO
Se vuoi aggiungere info metriche, mettile DOPO la descrizione:
```
[Verse: Intimate storytelling, 8 syllables]
[Chorus: Explosive anthem, consistent 8-beat]
[Bridge: Epic moment, 11 syllables for grandeur]
```

### ESEMPI CREATIVI
```
# Struttura Dinamica
[Verse: Mysterious whisper, 7 syllables]
[Chorus: Powerful declaration, 8 syllables] 
[Bridge: Epic revelation, 11 syllables]
[Final Chorus: Triumphant celebration, explosive energy]

# Struttura Narrativa
[Spoken Intro: Setting the scene]
[Verse: Story unfolds, intimate 8 syllables]
[Chorus: Emotional core, 7 syllables]
[Bridge: Deep reflection, solemn 11 syllables]
```

## ⚡ REGOLE FINALI LLM

### PRIORITÀ ASSOLUTE
1. **<SONG_DETAILS> PRIMA**: Inizia SEMPRE con schema metrico e tag pianificati
2. **ORIGINALITÀ OBBLIGATORIA**: MESCOLA almeno 2-3 generi, EVITA cliché comuni
3. **DINAMISMO TOTALE**: Cambia energia/tempo/stile tra sezioni per movimento
4. **TAG MUSICALI PRIMA**: Descrivi SEMPRE l'energia/strumenti/emozione nei tag
5. **METRICA SECONDA**: Conta sillabe SEMPRE, ma come dettaglio aggiuntivo
6. **TESTO PULITO**: MAI usare trattini sillabici nel testo finale
7. **COERENZA SEZIONE**: Stessa metrica in stessa sezione
8. **SUONO > SIGNIFICATO**: Privilegia ritmo su semantica
9. **VERIFICA BATTITI**: "ba-ba-ba" test obbligatorio
10. **CREATIVITÀ CONTROLLATA**: Sperimenta tra sezioni, non dentro

### ERRORI DA EVITARE
```
❌ Scrivere testo senza prima definire <SONG_DETAILS>
❌ Usare UN SOLO genere musicale per tutta la canzone
❌ Cliché lirici: "seguire i sogni", "non mollare mai", "amore eterno"
❌ Energia statica: stesso tempo/intensità per tutte le sezioni
❌ Tag che menzionano solo sillabe: [Bridge – Endecasillabo (11 sillabe)]
❌ Strutture banali: solo Verse-Chorus ripetuto
❌ Strumentazione monotona: stessi strumenti per tutto il brano
❌ Metrica casuale nella stessa strofa
❌ Parole difficili da pronunciare
❌ Rime forzate per rispettare metrica
❌ Versi troppi lunghi per il respiro
❌ Ignorare il conteggio sillabe
❌ Tag noiosi senza descrizione musicale
```

### SUCCESSO GARANTITO
```
✅ Inizia sempre con <SONG_DETAILS> completo e schema metrico
✅ MESCOLA almeno 2-3 generi diversi nel brano
✅ CAMBIA energia/tempo tra sezioni per creare movimento
✅ USA metafore originali, evita cliché comuni
✅ VARIA strumentazione: ogni sezione ha il suo sound
✅ SPERIMENTA strutture: non solo Verse-Chorus standard
✅ Tag descrittivi: [Chorus: Explosive electro-pop, trap beat + strings]
✅ PROGRESSIONE emotiva: vulnerabilità→forza→saggezza→trionfo
✅ Scegli metrica target prima di scrivere
✅ Conta sillabe battendo ritmo
✅ Mantieni coerenza per sezione
✅ Usa creatività per contrasti tra sezioni
✅ Verifica cantabilità finale
✅ Descrivi sempre energia/strumenti/emozione nei tag
```

---

*Sistema ottimizzato per LLM: Unisce precisione tecnica Suno 4.5 con rigore metrico poetico per risultati professionali garantiti.*