# GUIDA SUNO 4.5 - SISTEMA LLM OTTIMIZZATO

*Sistema integrato per LLM: Creatività + Precisione Metrica*
*Flusso lineare 0→A→B→C→D*

## 🔧 FASE 0: ADVANCED OPTIONS

### CONFIGURAZIONI SUNO
```
🎵 TITOLO: [NON DIMENTICARE!]
- Evocativo e memorabile (5-6 parole max)
- Coerente con tema/mood
- Senza caratteri speciali

🎛️ ADVANCED OPTIONS:
- Vocal Gender: Male/Female/Auto
- Weirdness: 0% (safe) → 100% (experimental)
- Style Influence: 0% (loose) → 100% (strong)
- Exclude Styles: "generi da evitare"
```

### ESEMPIO CONFIGURAZIONE
```
Titolo: "Digital Echoes"
Vocal Gender: Female
Weirdness: 50% (bilanciato)
Style Influence: 34% (moderato)
Exclude Styles: "country, classical, opera, folk, bluegrass, gospel, traditional, orchestral, chamber music, baroque, romantic, medieval, gregorian, polka, waltz, tango, mariachi, flamenco, klezmer, bagpipe, didgeridoo, sitar, gamelan, throat singing, yodeling, sea shanty, military march, funeral dirge, lullaby, nursery rhyme, christmas carol, hymn, chant, ambient drone, field recording, nature sounds, white noise, silence"

💡 **STRATEGIA**: Lista estesa forza Suno a selezionare generi più moderni e creativi
```

---

## 🎯 SISTEMA BASE

### METRICHE ESSENZIALI
```
SETTENARIO (7 sillabe) → Ritmo veloce, energico
OTTONARIO (8 sillabe) → Equilibrato, universale  
ENDECASILLABO (11 sillabe) → Solenne, epico
```

### CONTEGGIO AUTOMATICO
```
PAROLA PIANA (accento penultima) = conta normale
PAROLA TRONCA (accento ultima) = +1 sillaba metrica
PAROLA SDRUCCIOLA (accento terzultima) = -1 sillaba metrica

Verifica: Conta "ba-ba-ba-ba-ba-ba-ba-ba" → Se coincide = OK
```

---

## 🎵 FASE A: <SONG_DETAILS>

### TEMPLATE OBBLIGATORIO
```
<SONG_DETAILS>
[GENERI: MESCOLA ALMENO 2-3! Es: Indie-Folk + Jazz + Ambient]
[VOCI: VARIA! Sussurro→Potente→Coro, sperimenta effetti]
[TEMPO: DINAMICO! 70→120→90→140 BPM tra sezioni]
[STRUTTURA: ORIGINALE! Non solo Verse-Chorus, prova AABA, ABCB]
[TEMA: Messaggio originale, evita cliché comuni]
[PAROLE CHIAVE: Metafore innovative, termini freschi]
</SONG_DETAILS>
```

**🚨 IMPORTANTE:** Chiudi sempre con `</SONG_DETAILS>` - il tag di chiusura è obbligatorio!

### ORIGINALITÀ OBBLIGATORIA
- **EVITA:** "seguire sogni", "non mollare mai", "amore eterno"
- **MESCOLA:** Almeno 2-3 generi diversi per sezione
- **CREA:** Progressioni emotive inaspettate
- **USA:** Strumenti non convenzionali per il genere

### ESEMPIO FASE A
```
<SONG_DETAILS>
[GENERI: Indie-Folk + Electro-Pop + Jazz-Fusion]
[VOCI: Female (breathy to powerful) + Vocoder + Gospel choir]
[TEMPO: 70 BPM→120 BPM→90 BPM→140 BPM]
[STRUTTURA: Intro-Verse-Pre-Chorus-Chorus-Verse-Bridge-Chorus-Outro]
[TEMA: Trasformare cicatrici in costellazioni]
[PAROLE CHIAVE: metamorfosi, alchimia, rinascita, stelle, guarigione]
</SONG_DETAILS>
```

---

## 🎸 FASE B: STYLE

### 🎯 STYLE SEMANTICO: LA RIVOLUZIONE NARRATIVA

#### 🌍 LINGUA RACCOMANDATA: INGLESE PER LO STYLE
**Perché inglese**: Training LLM superiore + terminologia musicale precisa  
**Limite**: 1000 caratteri massimi  
**Focus**: Storia della MUSICA (✅), non trama della canzone (❌)

**🎤 IMPORTANTE TESTO CANZONE:** Lo STYLE è in inglese, ma il TESTO della canzone deve essere in ITALIANO (a meno che non sia specificato diversamente). Suno è per cantautrici/cantautori italiani che cantano in italiano.

#### 🚨 EVITA CRASH - PAROLE PERICOLOSE
❌ "come se", "sembra", "storia", "scena", "all'inizio", "poi"  
❌ Riferimenti culturali ("Black Mirror", "anni '80")  
❌ Ellissi (...), trattini lunghi (—), parentesi complesse  
✅ Terminologia musicale diretta e atmosfera

```
A melancholic trap ballad with female vocals
floating over deep 808s and ethereal synths.
Every beat tells a story of urban solitude.
```

#### 🔧 SEMANTIC STYLE TECHNIQUES
1. **Musical Storytelling:** Describe as "narrative"
2. **Sound Metaphors:** "Notes like raindrops"
3. **Emotional Progression:** "Starts shy, explodes into passion"
4. **Cinematic Atmosphere:** "Like a sunset scene"
5. **Descriptive Layering:** Instruments + emotions + dynamics

#### 📝 TEMPLATE STYLE SICURO

🚨 **FORMATO CRITICO STYLE:**
```
✅ UN SOLO PARAGRAFO senza a capo
✅ Frasi separate da punti, non da invii
✅ Massimo 1000 caratteri
❌ NO multiple righe o paragrafi
❌ NO elenchi puntati
```

**Esempio Style Semantico:**
```
Indie folk melancholic with guitar strings like whispered secrets. Intimate atmosphere building to cathartic release. Nostalgic and contemplative.
```

### 🏗️ ARCHITETTURA DUE CAMPI
```
🚨 SEPARAZIONE CRITICA:
LYRICS FIELD = Solo testo + meta-tag strutturali (IN ITALIANO)
STYLE FIELD = Descrizioni musicali + atmosfera (IN INGLESE)

❌ LYRICS BLEED (Errore):
[Verse] "This song has trap drums and reverb"

✅ CORRETTO:
LYRICS: [Verse] "Cammino per strade vuote" (ITALIANO)
STYLE: "Trap drums, heavy reverb, urban atmosphere" (INGLESE)
```

### 🎭 REGOLA D'ORO: STYLE vs TESTO
```
🎵 STYLE FIELD (Inglese):
- Descrizioni strumentali
- Atmosfere musicali  
- Tecniche di produzione
- Energia e dinamiche

🎤 LYRICS FIELD (Italiano):
- Testo della canzone
- Tag delle sezioni [Verse], [Chorus], etc.
- Parole che canta l'artista
- Contenuto lirico
```

### 📋 SONG_DETAILS: CONTROLLO AVANZATO

#### ✅ QUANDO USARE SONG_DETAILS
- **Progetti Professionali:** Controllo massimo necessario
- **Limite Style Field:** Quando 1000 caratteri non bastano
- **Generi Complessi:** Layering avanzato e fusioni
- **Collaborazioni:** Specifiche precise richieste

#### ⚠️ COME USARE SONG_DETAILS (BENE)
**❌ Troppo Rigido:**
```
[GENERI: Indie-Folk + Jazz-Fusion]
[VOCI: Female (breathy)]
[TEMPO: 75 BPM]
```

**✅ Integrato e Naturale:**
```
<SONG_DETAILS>
[GENERI: Indie-Folk con sfumature Jazz-Fusion e tocchi Ambient]
[ATMOSFERA: Intima e crescente, come un risveglio emotivo]
[VOCE: Femminile, inizia sussurrata e si rafforza progressivamente]
[DINAMICA: 75 BPM → esplosione a 102 BPM → ritorno calmo a 94 BPM]
</SONG_DETAILS>
```

#### 🎯 PRINCIPI SONG_DETAILS
1. **Flessibilità:** Non sempre tutte le categorie
2. **Integrazione:** Mescolare con descrizioni poetiche
3. **Necessità:** Usare solo quando serve davvero
4. **Naturalezza:** Linguaggio fluido, non "etichette"

### BLUEPRINT PROMPTING (Tecnica Avanzata)
```
[Intro]: Ambient wind, distant vinyl crackle
[Verse 1]: Sparse piano, soft kick drum enters
[Pre-Chorus]: Strings swell, tension builds
[Chorus]: Full arrangement, soaring vocals
[Bridge]: Stripped back, intimate whisper
[Outro]: Fade with echoing vocals
```

### META-TAG AVANZATI V4.5
```
STRUTTURA: [Intro][Verse][Pre-Chorus][Chorus][Bridge][Outro]
STRUMENTI: [Guitar Solo][Piano Solo][808 Drop][Orchestral Build]
EFFETTI: [Reverb Heavy][Auto-Tune][Tape Saturation][Sidechain]
VOCALI: [Male Vocal][Female Vocal][Duet][Whisper][Growl]
ATMOSFERA: [Dark Mood][High Energy][Nostalgic Glow][Spacey]
```

### LAYERING AVANZATO
```
[Intro][Lo-fi Filter][Tape Hiss]
[Distant crackle, muffled piano notes]

[Verse][Male Vocal][Dark Mood]
City lights fade, I walk alone

[Chorus][Female Vocal][Euphoric Swell]
We rise above the noise tonight
```

### TRUCCO ASTERISCHI
```
[Intro](*Vinyl Crackle*)
I sat and watched the sunrise die
(*Thunder in distance*)
```

### PRINCIPI DINAMICI
- **Ogni sezione = energia diversa**
- **Strumentazione variabile**
- **Progressione emotiva chiara**
- **Contrasti marcati**

### ESEMPIO FASE B
```
STILE DINAMICO:
- Verse: Intimo, fingerpicked guitar + violino sussurrato
- Pre-Chorus: Crescendo elettronico, synth pad + batteria
- Chorus: Esplosivo electro-pop, beat trap + archi orchestrali
- Bridge: Contemplativo jazz-fusion, sax solo + piano
- Outro: Fusione tutti generi, crescendo gospel finale
```

---

## 📐 FASE C: SCHEMA STRUCTURE

### REGOLE METRICHE UNIFICATE
```
1. SCEGLI target sillabe per sezione
2. SCRIVI verso
3. CONTA battendo ritmo mentalmente
4. Se ≠ target → RISCRIVI
5. Se = target → PROCEDI
```

### STRUTTURE PER GENERE
```
ROCK/METAL:
- Verse: 8 sillabe (potenza + cantabilità)
- Chorus: 8 sillabe (coerenza ritmica)
- Bridge: 11 sillabe (contrasto epico)

INDIE/ALTERNATIVE:
- Verse: 7 sillabe (velocità + modernità)
- Chorus: 8 sillabe (memorabilità)
- Bridge: 9 sillabe (variazione sottile)
```

### REGOLE SPECIFICHE CHORUS/RITORNELLO
```
🎵 CHORUS = CUORE DELLA CANZONE:
✅ RIME OBBLIGATORIE: Almeno ABAB o AABB
✅ SEMPLICITÀ: Parole comuni, facili da ricordare
✅ ORECCHIABILITÀ: Melodia che "si attacca" subito
✅ RIPETIBILITÀ: Facile da cantare insieme
✅ IMPATTO EMOTIVO: Il momento più forte del brano

ESEMPI RIME CHORUS:
ABAB: "sole/cuore/parole/amore"
AABB: "notte/rotte/stelle/belle"
```

### VERIFICA QUALITÀ
```
✅ Ogni verso = stesso numero sillabe?
✅ Parole facili da pronunciare?
✅ Rime naturali, non forzate?
✅ Respiro corretto tra frasi?
✅ CHORUS: Rime presenti e orecchiabili?
```

### ESEMPIO FASE C
```
STRUCTURE: Intro-Verse-Pre-Chorus-Chorus-Verse-Bridge-Chorus-Outro

SILLABE CONSIGLIATE:
- Verse: 8 sillabe per verso (intimità cantabile)
- Pre-Chorus: 7 sillabe per verso (accelerazione)
- Chorus: 8 sillabe per verso (memorabilità)
- Bridge: 11 sillabe per verso (momento solenne)
- Outro: Libero (risoluzione naturale)
```

---

## 🎤 FASE D: CANZONE

### FORMATO TESTO FINALE
```
[Sezione: Descrizione musicale]
Testo pulito senza trattini
Rispettando sillabe pianificate

🚨 DIVIETO ASSOLUTO:
❌ Note esplicative nel testo (💡 NOTA RIME, spiegazioni, commenti)
❌ Spiegazioni delle rime o della metrica
❌ Commenti tra parentesi nel testo
✅ Solo testo cantabile pulito
```

### TAG SEZIONI CORRETTI
```
✅ CORRETTO:
[Verse: Intimate storytelling, fingerpicked guitar]
[Chorus: Explosive anthem, full band]
[Bridge: Epic emotional climax, orchestral swell]

❌ SBAGLIATO:
[Verse - 8 sillabe]
[Chorus: 8 syllables per line]
```

### ESEMPIO FASE D
```
[Intro: Ambient soundscape, distant piano]
Sussurri nel vento notturno
Storie che nessuno sa

[Verse 1: Intimate storytelling, fingerpicked guitar]
Ogni cicatrice racconta
Un momento di dolore
Ma guardo il cielo stellato
E vedo la mia rinascita

[Pre-Chorus: Building tension, synth entering]
Le stelle danzano
Sopra le mie ferite

[Chorus: Explosive electro-pop, full arrangement]
Sono costellazioni ora (A)
Queste cicatrici sul cuore (B)
Brillano nella notte scura (A)
Guide per chi sa guardare (B)



[Bridge: Contemplative jazz-fusion, sax solo]
L'alchimia del tempo trasforma tutto il dolore
In saggezza che illumina il cammino futuro

[Outro: Gospel finale, layered vocals fading]
Stelle che guidano
Vers'altri cieli
```

**📝 IMPORTANTE:** Style in inglese (nei tag delle sezioni), testo in italiano.

---

## 🚨 ERRORI CRITICI DA EVITARE

### ERRORI ANTI-GLITCH
```
❌ Stili narrativi complessi ("La storia inizia quando...")
❌ Riferimenti culturali esterni (film, luoghi, epoche)
❌ Descrizioni multi-paragrafo
❌ Metafore elaborate e filosofiche
✅ Descrizioni musicali dirette e tecniche
✅ Un paragrafo fluido sotto 1000 caratteri
```

### ERRORI STRUTTURALI
```
❌ Mescolare <SONG_DETAILS> con testo finale
❌ Aggiungere commenti narrativi nel testo
❌ Ripetere schema metrico nel testo finale
❌ Linguaggio descrittivo tra sezioni musicali
❌ Introduzioni narrative prima della canzone
❌ Spiegazioni dopo la canzone
❌ NOTE ESPLICATIVE nel testo (💡 NOTA RIME, spiegazioni)
❌ STYLE multi-paragrafo con a capo
❌ Commenti tra parentesi nel testo cantabile
```

### ERRORI CREATIVI
```
❌ Usare UN SOLO genere per tutto il brano
❌ Cliché lirici comuni
❌ Energia statica (stesso tempo/intensità)
❌ Strutture banali (solo Verse-Chorus)
❌ Strumentazione monotona
❌ Tag che menzionano solo sillabe
```

### ERRORI METRICI
```
❌ Metrica casuale nella stessa strofa
❌ Parole difficili da pronunciare
❌ Rime forzate per rispettare metrica
❌ Versi troppo lunghi per il respiro
❌ Ignorare conteggio sillabe
❌ Usare trattini sillabici nel testo finale
❌ CHORUS SENZA RIME: Il ritornello DEVE avere rime
❌ CHORUS COMPLESSO: Evitare parole difficili nel ritornello
```

---

## 🎯 LIBERTÀ CREATIVA

*Questa guida è uno strumento, non una gabbia.*

Segui il flusso **0→A→B→C→D** come meglio credi:
- Usa le tecniche che servono al tuo progetto
- Adatta la complessità al contesto
- Lascia che la creatività guidi le scelte
- La qualità nasce dall'equilibrio, non dalla rigidità

**🎵 Cosa vuole Suno**: Pensa a Suno come un musicista digitale che capisce "chitarra distorta" meglio di "dolore dell'anima". Preferisce istruzioni musicali a poesie elaborate.

**🎨 Beneficio del dubbio**: Le regole anti-glitch sono suggerimenti per evitare crash, non imposizioni creative. Scegli italiano se preferisci, sii poetico se vuoi, ma ricorda i limiti tecnici.

**Ricorda:** Ogni LLM ha il suo stile, ogni canzone ha le sue necessità. Questa guida ti dà gli strumenti, tu decidi come usarli.

---

## 🎭 CONCLUSIONE

*Le regole danno struttura, ma la vera musica trascende ogni schema.*
*Usa questa guida come trampolino, non come gabbia.*
*La magia nasce quando tecnica e anima si incontrano.*

**🎵 Crea con le regole, poi superale. 🎵**

---

**✨ Happy creating! ✨**