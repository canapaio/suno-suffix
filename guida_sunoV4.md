# GUIDA SUNO 4.5 - VERSIONE UNIFICATA

*Flusso lineare: A→B→C→D*

## [*] PIANIFICAZIONE STRATEGICA

## [A] FASE A: PROGETTAZIONE

**PERCHÉ QUESTA FASE:** Prima di scrivere una singola parola, devi avere una visione chiara del risultato finale. Questa fase ti permette di prendere decisioni strategiche che guideranno tutto il processo creativo, evitando di dover rifare il lavoro in seguito.

### MENTE LOCALE - DOMANDE CHIAVE

1. **COSA VOGLIO OTTENERE?** 
   - Che tipo di canzone sto creando? (genere, mood, energia)
   - Qual è il messaggio o l'emozione principale?
   - Chi è il pubblico target?

2. **COME USERÒ LE FASI?**
   - FASE B: Quali opzioni avanzate mi servono per questo brano?
   - FASE C: Che stile musicale descriverò? Quali strumenti e atmosfere?
   - FASE D: Come integrerò tempo musicale e metrica del testo?
   - FASE E: Come organizzerò le sezioni finali per massimo impatto?

3. **STRATEGIA IN PAROLE POVERE - GUIDA MENTALE:**
   - NON serve un piano tecnico, ma una bussola emotiva e creativa
   - Scrivi in 2-3 frasi semplici la "sensazione" che vuoi creare
   - Esempio: "Voglio che chi ascolta si senta nostalgico ma speranzoso. Inizierò dolce e piano, poi esploderò di energia nel ritornello."
   - Pensa come se stessi raccontando l'idea a un amico al bar

**RICORDA:** Questo non è un piano tecnico, ma una guida mentale per mantenere la direzione creativa durante tutto il processo.

---

## [B] FASE B: CONFIGURATION

**PERCHÉ QUESTA FASE:** Stabilisci le fondamenta tecniche del tuo brano prima di entrare nel creativo. Questi parametri influenzano direttamente come Suno interpreterà le tue istruzioni successive, garantendo coerenza tra visione artistica e risultato finale. Configurare correttamente significa avere controllo totale sul processo generativo.

### ADVANCED OPTIONS
```
[♪] TITOLO: Evocativo, 5-6 parole max, senza caratteri speciali
[>] VOCAL GENDER: Male/Female/Auto - Imposta il genere della voce principale
[>] WEIRDNESS: 0% (normale) → 100% (sperimentale) - Controlla quanto sarà sperimentale il brano
[>] INFLUENCE: 0% (libero) → 100% (fedele) - Controlla quanto lo stile seguirà la descrizione
[>] EXCLUDE STYLES: "country, classical, opera, folk, bluegrass, gospel, traditional, orchestral, chamber music, baroque, romantic, medieval, gregorian, polka, waltz, tango, mariachi, flamenco, klezmer, bagpipe, didgeridoo, sitar, gamelan, throat singing, yodeling, sea shanty, military march, funeral dirge, lullaby, nursery rhyme, christmas carol, hymn, chant, ambient drone, field recording, nature sounds, white noise, silence"
**NOTA:** Rimuovi da questa lista gli stili che desideri includere e lascia solo quelli che NON vuoi nel brano

**[!] CONSEGUENZE SEMANTICHE DELLE ESCLUSIONI:**
- **Vocal Types:** Escludere "male vocals" garantisce solo voci femminili, evitando mix indesiderati
- **Strumenti Specifici:** Escludere "piano, drums, synth" rimuove questi elementi dalla composizione
- **Effetti Audio:** Escludere "compression, distortion, noise" migliora la qualità audio percepita
- **Coerenza Genere:** Le esclusioni mantengono la purezza stilistica del genere scelto
- **Impatto STYLE:** Gli elementi esclusi non appariranno anche se menzionati nella descrizione dello stile
```

### [!] ESEMPIO SETUP COMPLETO
```
Titolo: "Digital Echoes" | Vocal Gender: Female | Weirdness: 50% | Influence: 34%
Exclude: "country, classical, opera" (rimuovi generi desiderati)
```

---

## [C] FASE C: STYLE

**PERCHÉ QUESTA FASE:** Traduci la tua visione musicale in linguaggio che Suno comprende perfettamente. Lo STYLE è il DNA sonoro del tuo brano - definisce strumenti, atmosfere e dinamiche che daranno vita alla tua idea. Una descrizione precisa **IN INGLESE** qui determina il 70% del carattere finale della canzone. L'inglese è fondamentale per l'efficacia del sistema.

### STYLE RULES
```
[+] TESTO TECNICO: Linguaggio musicale preciso e professionale
[+] LUNGHEZZA OTTIMALE: 300-400 caratteri (massimo 1000 ma sconsigliato)
[+] UN PARAGRAFO unico senza a capo
[+] INGLESE OBBLIGATORIO: Scrivere TUTTO lo style in inglese - è FONDAMENTALE per l'efficacia
[+] Frasi separate da punti
[-] NO a capo, elenchi, parentesi complesse
[-] NO "come se", "sembra", "storia", riferimenti culturali
```

**IMPORTANTE:** Lo STYLE deve essere un paragrafo unico senza a capo, solo frasi separate da punti.

### META-TAGS

**DOVE USARE I META-TAG:**
- I meta-tag funzionano **ESCLUSIVAMENTE** nel campo Custom Lyrics
- **NON** funzionano nel campo STYLE

**FORMATO E REGOLE DEI META-TAG:**
- Formato: `[Tag: Value]` con parentesi quadre
- Posizionare i tag chiave nei primi 20-30 caratteri per massima efficacia
- Usare 1 tag per categoria, massimo 2-3 strumenti per canzone
- Evitare tag conflittuali (es. Energy: High + Energy: Low)

**PAROLE PERICOLOSE DA EVITARE NELLO STYLE:**
Verse, Chorus, Bridge, Intro, Outro, Hook, Refrain, Solo, Break, Drop, Build, Fade, Repeat, Loop, Section, Part, Segment, Transition, Interlude, Coda

### [♪] ESEMPI STYLE COMPATTI (300-400 caratteri)

**ESEMPIO 1 - POP ENERGICO (320 caratteri):**
```
Upbeat GENERE_LIST with driving INSTRUMENTS_LIST, bright INSTRUMENTS_LIST, DYNAMICS_LIST. Modern production with punchy INSTRUMENTS_LIST, layered vocals, radio-friendly mix. Energetic tempo, major key progressions, commercial appeal.
```
*Riferimenti: GENERE_LIST, INSTRUMENTS_LIST, DYNAMICS_LIST - vedi sezioni LISTS*

**ESEMPIO 2 - ELECTRONIC DANCE (350 caratteri):**
```
High-energy GENERE_LIST with pulsing INSTRUMENTS_LIST, four-on-floor kick, filtered builds. Modern STYLE_LIST production, sidechain compression, melodic drops. Euphoric leads, atmospheric INSTRUMENTS_LIST, club-ready mix.
```
*Riferimenti: GENERE_LIST, INSTRUMENTS_LIST, STYLE_LIST - vedi sezioni LISTS*

### [♪] FUSIONI SEMANTICHE CREATIVE

**PRINCIPIO BASE:** Le fusioni più efficaci nascono dall'unione di elementi contrastanti che creano tensione creativa. Non limitarti a generi simili - l'innovazione nasce dal contrasto controllato.

**TECNICHE SEMANTICHE BASE:**
```
• Musical Storytelling: "narrative progression"
• Sound Metaphors: "notes like raindrops"
• Emotional Arc: "starts shy, explodes into passion"
• Cinematic Feel: "sunset atmosphere"
• Layered Description: strumenti + emozioni + dinamiche
```

**CRITERI SEMANTICI PER FUSIONI PERSONALIZZATE:**

**1. CONTRASTO TEMPORALE**
- Vintage + Modern: "80s synth-pop with modern trap production"
- Classico + Contemporaneo: "baroque harpsichord with electronic beats"
- Retro + Futuristico: "70s funk with cyberpunk synths"

**2. CONTRASTO CULTURALE**
- Oriente + Occidente: "traditional Japanese koto with western rock guitars"
- Nord + Sud: "Nordic folk with Latin percussion"
- Urbano + Rurale: "city trap with country banjo"

**3. CONTRASTO ENERGETICO**
- Calmo + Intenso: "ambient textures with aggressive metal riffs"
- Dolce + Aspro: "lullaby melodies with industrial noise"
- Organico + Sintetico: "acoustic guitar with glitchy electronics"

**4. CONTRASTO STRUMENTALE**
- Acustico + Elettronico: "fingerpicked guitar with heavy 808s"
- Tradizionale + Moderno: "Celtic flute with dubstep drops"
- Orchestrale + Digitale: "string quartet with trap hi-hats"

**ESEMPI CONCRETI DI FUSIONI:**

```
# FUSIONE TEMPORALE
"Vintage 80s new-wave with modern future-bass drops and analog warmth"
"Medieval gregorian chant with contemporary hip-hop beats and vinyl crackle"

# FUSIONE CULTURALE  
"Brazilian bossa-nova guitar with Nordic ambient textures and soft vocals"
"Japanese city-pop with American southern rock guitar and warm production"

# FUSIONE ENERGETICA
"Lo-fi jazz piano with aggressive trap snares and ethereal vocal layers"
"Peaceful ambient pads with driving techno kicks and organic percussion"

# FUSIONE STRUMENTALE
"Acoustic folk storytelling with electronic glitch effects and tape saturation"
"Classical string arrangements with modern R&B groove and sidechain compression"
```

**BONUS: FORMULA FUSIONE PERSONALIZZATA**

**STEP 1 - SCEGLI BASE EMOTIVA:**
- Nostalgico, Energico, Malinconico, Euforico, Misterioso, Intimo

**STEP 2 - AGGIUNGI CONTRASTO:**
- Se Base = Nostalgico → Aggiungi elementi Futuristici
- Se Base = Energico → Aggiungi elementi Ambient
- Se Base = Malinconico → Aggiungi elementi Uplifting

**STEP 3 - DEFINISCI STRUMENTAZIONE:**
- Strumento Principale (da GENERE_LIST)
- Strumento Contrasto (da categoria diversa)
- Effetto Unificante (da STYLE_LIST)

**STEP 4 - APPLICA FORMULA:**
```
"[BASE EMOTIVA] [GENERE PRINCIPALE] with [CONTRASTO STRUMENTALE] and [EFFETTO UNIFICANTE]"
```

**ESEMPI FORMULA:**
```
"Nostalgic indie-folk with futuristic synth leads and analog warmth"
"Energetic trap with ambient string pads and vintage tape saturation"
"Melancholic jazz with uplifting gospel choir and modern production"
```

**REGOLE D'ORO FUSIONI:**
- Massimo 3 elementi contrastanti per mantenere coerenza
- Un elemento deve dominare, gli altri supportare
- Usa STYLE_LIST per unificare elementi diversi
- Testa sempre la leggibilità: se suona confuso, semplifica

### [♪] PROGRESSIONE ENERGETICA
```
Verse: Intimo → Pre-Chorus: Crescendo → Chorus: Esplosivo → Bridge: Contrasto
Cambia strumentazione ogni sezione per varietà
```

### STYLE LISTS

**GENERE_LIST:**
```
# Rock & Alternative
Grunge, Alternative-Rock, Indie-Rock, Post-Rock, Math-Rock, Shoegaze, 
Punk-Rock, Pop-Punk, Hard-Rock, Classic-Rock, Progressive-Rock, Psychedelic-Rock

# Electronic & Dance
Electro-Pop, Synth-Wave, Dance-Pop, EDM, House, Techno, Trance, Dubstep,
Ambient-House, Future-Bass, Chillwave, Vaporwave, Hardstyle, Drum-and-Bass

# Hip-Hop & R&B
Hip-Hop, Trap, Alternative-Hip-Hop, Boom-Bap, Gangsta-Rap, Cloud-Rap,
R&B, Neo-Soul, Alternative-R&B, Trap-Soul, Contemporary-R&B, Funk

# Pop & Indie
Indie-Pop, Dream-Pop, Electropop, Synth-Pop, Alternative-Pop, K-Pop, J-Pop,
Bubblegum-Pop, Dance-Pop, Folk-Pop, Indie-Folk, Alternative-Folk

# Metal & Heavy
Heavy-Metal, Thrash-Metal, Death-Metal, Black-Metal, Nu-Metal, Metalcore,
Progressive-Metal, Industrial-Metal, Alternative-Metal, Power-Metal

# Jazz & Soul
Jazz-Fusion, Jazz-House, Cool-Jazz, Smooth-Jazz, Big-Band, Bebop,
Soul, Gospel, Neo-Soul, Quiet-Storm

# Blues & Traditional
Chicago-Blues, Delta-Blues, Electric-Blues, Gospel-Blues, Country-Blues,
Rhythm-and-Blues, Acoustic-Blues, Slide-Guitar-Blues

# Country & Americana
Bluegrass, Country-Pop, Country-Rock, Nashville-Sound, Americana,
Outlaw-Country, Alt-Country, Folk-Country, Honky-Tonk

# Folk & World
Celtic-Music, Folk-Rock, Indie-Folk, Singer-Songwriter, Bossa-Nova,
Reggae, Afrobeat, Samba, Dancehall, Highlife, C-Pop

# Easy Listening & Ambient
Adult-Contemporary, Lounge-Music, Soft-Rock, Chillout, New-Age,
Downtempo, Trip-Hop, Elevator-Music

# Punk & Hardcore
Anarchos-Punk, Hardcore-Punk, Skate-Punk, Street-Punk, Post-Punk,
Pop-Punk, Emo-Punk, Crust-Punk

# Experimental & Fusion
Experimental, Avant-Garde, Industrial, Noise, Progressive, Post-Hardcore,
Midwest-Emo, Gregorian-Chant, Jazz-Metal, Folk-Metal, Rap-Metal
```

**STYLE_LIST:**
```
Modern-Production, Vintage-Sound, Lo-Fi-Aesthetic, Hi-Fi-Polish, Analog-Warmth,
Digital-Precision, Compressed-Punch, Dynamic-Range, Stereo-Width, Mono-Focus,
Reverb-Space, Dry-Intimate, Distorted-Grit, Clean-Clarity, Saturated-Warmth,
Crisp-Definition, Layered-Texture, Minimal-Space, Dense-Wall, Sparse-Arrangement,
Tight-Rhythm, Loose-Groove, Quantized-Perfect, Human-Feel, Organic-Flow,
Electronic-Grid, Live-Energy, Studio-Control, Raw-Emotion, Polished-Commercial
```

**INSTRUMENTS_LIST:**
```
Fingerpicked-Guitar, Deep-808s, Ethereal-Synths, Analog-Warmth,
Distorted-Bass, Crisp-Drums, Lush-Strings, Vintage-Keys, Glitchy-Beats,
Ambient-Pads, Brass-Stabs, Vinyl-Crackle, Tape-Saturation, Reverb-Tails,
Sidechain-Pump, Filter-Sweeps, Granular-Texture, Field-Recordings,
Electric-Guitar-Distorted, Acoustic-Guitar, Strings-Legato, Slap-Bass, 
Piano-Driven, Groovy-Rhythms, Pounding-Drums, Guitar-Loops, Steady-Rhythm
```

**ATMOSPHERES_LIST:**
```
Melancholic-Introspection, Urban-Solitude, Nostalgic-Warmth, Euphoric-Release,
Dark-Contemplation, Dreamy-Float, Gritty-Reality, Ethereal-Escape,
Intimate-Vulnerability, Epic-Grandeur, Mysterious-Depth, Playful-Energy,
Emotional-Catharsis, Cinematic-Drama, Minimalist-Space, Chaotic-Beauty,
Atmospheric, Emotional, Festive, Peaceful-Reflection, Joyful, Heartfelt, 
Vibrant, Cool, Eclectic, Progressive, Theatrical, Anthemic, Danceable, 
Groovy, Futuristic, Unusual, Operatic, Psychedelic, Mystical, Youthful, 
Powerful, Uplifting-Nostalgic
```

**DYNAMICS_LIST:**
```
Builds-Gradually, Explosive-Drops, Intimate-Whispers, Soaring-Climax,
Stripped-Back-Moments, Layered-Complexity, Rhythmic-Pulse, Floating-Weightless,
Driving-Forward, Gentle-Sway, Tension-Release, Organic-Flow, Electronic-Precision, 
Raw-Emotion, Buildup, Drop, Breakdown, Crescendo, Diminuendo, Staccato, Legato, 
Syncopation, Polyrhythm, Cross-Rhythm, Tempo-Shift, Dynamic-Contrast, 
Rhythmic-Displacement, Metric-Modulation, Energy-High, Energy-Medium, Energy-Low, 
Texture-Gritty, Mood-Uplifting, Mood-Intense, Catchy-Hook, Emotional-Bridge, 
Powerful-Outro, Pre-Chorus, Guitar-Solo, Female-Vocal, Male-Vocal, Harmony-Yes, 
Vocal-Effect-Reverb, Vocal-Effect-Delay, Vocal-Tone-Whisper
```

---

## [D] FASE D: TEMPO E METRICA

**PERCHÉ QUESTA FASE:** Sincronizza matematicamente testo e musica per creare fluidità naturale. Il rapporto BPM-sillabe non è teoria musicale astratta, ma la chiave per testi che "suonano giusti". Questa mappatura elimina il trial-and-error e garantisce che ogni parola si incastri perfettamente nel groove musicale.

**[!] RACCOMANDAZIONE SEMANTICA:** Nella fase successiva (FASE E), privilegia la semplicità lessicale e usa meno parole per rispettare naturalmente le sillabe pianificate. La creatività si esprime meglio attraverso concetti chiari che attraverso complessità verbale.

### [♪] **MAPPATURA BPM-TEMPLATE INTEGRATA**

**TEMPLATE COMPLETI (BPM + Sillabe + Style):**
```
ROCK: 120 BPM → V(8), C(8) | "Driving rock with pounding drums"
POP: 110 BPM → V(8), C(7) | "Upbeat anthem with catchy hooks"
TRAP: 140 BPM → V(6), C(8) | "Hard-hitting with booming 808s"
ELECTRONIC: 128 BPM → V(6), C(7) | "Pulsing track with four-on-the-floor"
R&B: 85 BPM → V(12), C(10) | "Smooth groove with warm bass"
BALLAD: 70 BPM → V(11), C(10) | "Emotional ballad with piano"
```

**RANGE RAPIDI:**
```
60-90 BPM (Lenti): 10-14 sillabe | Ballad, Ambient, Soul
90-120 BPM (Medi): 8-10 sillabe | Pop, Rock, Funk, Reggae
120+ BPM (Veloci): 4-8 sillabe | Dance, Trap, D&B, Hardcore
```

**TAG TEMPO DINAMICI:**
```
[Accelerando], [Ritardando], [Rubato], [Stringendo], [Rallentando]
```

**SINTASSI CORRETTA:**
```
✓ "Upbeat pop at 120 BPM" → 8 sillabe
✗ [TEMPO: 120 BPM] ripetuto | Cambi BPM numerici
```

### [=] **PROCESSO RAPIDO**

**Steps:**
1. Scegli genere + BPM
2. Identifica target sillabe (vedi mappatura)
3. Scrivi verso nel range
4. Conta battendo ritmo
5. Se fuori → Riscrivi | Se dentro → Procedi

**Fix Veloce:**
- Troppo lungo → Rimuovi aggettivi
- Troppo corto → Aggiungi parole brevi
- Rima forzata → Cambia ultima parola

**REGOLA D'ORO:** Un BPM per canzone → Target sillabico coerente

**SOUND_EFFECTS_LIST:**
```
Effetti Ambientali: Birds-chirping, Bell-dings, Phone-ringing, Whistling, 
Applause, Cheering, Clapping
Effetti Vocali: Whispers, Chuckles, Giggling, Sighs, Groaning, Cough, Screams
Effetti Tecnici: Beeping, Bleep, Ringing, Static, Silence, Censored, Clears-throat
Voci Narrative: Announcer, Reporter, Female-narrator, Man, Woman, Boy, Girl, 
Audience-laughing
```

**STRUCTURAL_METATAGS_LIST:**
```
Structure: [Intro], [Verse], [Chorus], [Bridge], [Drop], [Outro], [Pre-Chorus]
Genre: [Genre: Pop], [Genre: Rock], [Style: Lo-fi], [Era: 2000s]
Instruments: [Instrument: Piano], [Instrument: Electric Guitar (Distorted)], 
[Instrument: Strings (Legato)]
Vocals: [Vocalist: Female], [Vocalist: Alto], [Harmony: Yes], [Vocal Effect: Reverb], 
[Vocal Tone: Whisper]
Energy: [Energy: High], [Energy: Medium], [Energy: Low], [Mood: Uplifting], 
[Tempo: Mid], [Texture: Gritty]
```

### CHORUS OPTIMIZATION

**REGOLE FONDAMENTALI:**
```
[+] RIME OBBLIGATORIE: ABAB (alternata) o AABB (baciata)
[+] PAROLE SEMPLICI: Max 3 sillabe per parola
[+] HOOK RIPETIBILE: Frase chiave memorabile
[+] IMPATTO EMOTIVO: Messaggio universale
[+] METRICA COSTANTE: 8 sillabe per riga (standard)
```

**TEMPLATE HOOK EFFICACI:**
```
• RIPETIZIONE EMOTIVA: "Voglio volare, voglio sognare"
• DOMANDA-RISPOSTA: "Dove vai? Verso il sole"
• CONTRASTO: "Buio e luce, pace e guerra"
• MANTRA: "Sempre avanti, mai indietro"
```

**RIME SEMPLICI:**
```
PERFETTE: amore/cuore, vita/infinita, sole/parole
IMPERFETTE: notte/forte, mare/volare, tempo/momento
EVITARE: rime forzate, parole rare, costruzioni complesse
```

---

## [E] FASE E: FINAL TEXT

**PERCHÉ QUESTA FASE:** Trasforma tutto il lavoro preparatorio in testo cantabile che Suno può processare immediatamente. Qui applichi concretamente le scelte delle fasi precedenti, creando un prodotto finale pulito e professionale. La formattazione corretta è cruciale: un tag sbagliato può vanificare ore di pianificazione.

**[!] RACCOMANDAZIONE SEMANTICA:** Ricorda i target sillabici della Fase D e mantieni il testo semplice e diretto. Se una frase supera le sillabe previste, riduci aggettivi o sostituisci con parole più brevi. La fluidità ritmica è più importante della complessità lessicale.

### FORMAT OTTIMIZZATO

**STRUTTURA STANDARD:**
```
[Sezione: (ATMOSPHERES_LIST), (INSTRUMENTS_LIST), (DYNAMICS_LIST)]
Testo cantabile italiano
Rispettando target sillabico FASE D
```

**ESEMPI CORRETTI:**
```
[Verse: Intimate-Vulnerability, Fingerpicked-Guitar, Gentle-Sway]
[Chorus: Euphoric-Release, Electric-Guitar-Distorted, Explosive-Drops]
[Bridge: Melancholic-Introspection, Piano-Driven, Floating-Weightless]
```

**RIFERIMENTI LISTE FASE C:**
```
ATMOSPHERES_LIST: Melancholic-Introspection, Euphoric-Release, Intimate-Vulnerability...
INSTRUMENTS_LIST: Fingerpicked-Guitar, Electric-Guitar-Distorted, Piano-Driven...
DYNAMICS_LIST: Explosive-Drops, Gentle-Sway, Floating-Weightless...
```

**DIVIETI ASSOLUTI:**
```
[-] Note esplicative ([!] NOTA)
[-] Spiegazioni metrica
[-] Commenti tra parentesi
[+] Solo testo cantabile + tag dalle liste
```

### SECTION TAGS OTTIMIZZATI
```
[+] CORRETTO (usando liste ottimizzate):
[Verse: Intimate-Vulnerability, Fingerpicked-Guitar]
[Chorus: Euphoric-Release, Electric-Guitar-Distorted]
[Bridge: Melancholic-Introspection, Piano-Driven]

[-] SBAGLIATO:
[Verse - 8 sillabe]
[Chorus: 8 syllables per line]
[Verse: descrizione generica]
[Chorus: senza riferimento alle liste]
```

---

## [!] ERRORS TO AVOID

### ANTI-GLITCH
```
Terminologia musicale diretta (evita stili narrativi complessi)
Descrizioni sonore specifiche (evita riferimenti culturali esterni)
Paragrafo fluido <1000 caratteri (evita descrizioni multi-paragrafo)
Aggettivi tecnici efficaci (evita metafore elaborate)
```

### STRUCTURAL
```
Usa mappatura BPM-metrica integrata dalla FASE D per target sillabico (evita metrica casuale)
Progressione dinamica Verse→Chorus→Bridge con coerenza tempo-metrica dalla FASE D (evita energia statica)
Un solo BPM per canzone con target sillabico coerente dalla FASE D (evita tempi multipli e metrica scollegata)
```

### CREATIVE
```
Mashup creativi di 2-3 generi (evita un solo genere)
Immagini fresche e originali (evita cliché lirici)
Cambia strumenti ogni sezione (evita strumentazione monotona)
```

---

## [*] PHILOSOPHY

*Questa guida è uno strumento, non una gabbia.*

**Principi:**
- Usa le tecniche che servono
- Adatta al contesto
- Creatività guida le scelte
- Qualità = equilibrio, non rigidità

**Ricorda:** Suno capisce "chitarra distorta" meglio di "dolore dell'anima". Preferisce istruzioni musicali a poesie elaborate.

### ✨ ONE-SHOT PHILOSOPHY
```
Pianifica prima, esegui con fiducia
La creatività nasce dall'equilibrio tra struttura e spontaneità
```

---

**Crea con le regole, poi superale.**