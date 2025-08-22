# GUIDA TECNICA AVANZATA SUNO
*Formato: Markdown (.md)*

*Flusso lineare: 0→A→B→C→D*

## 🔧 PHASE 0: CONFIGURATION

### ADVANCED OPTIONS
```
🎵 TITOLO: Evocativo, 5-6 parole max, senza caratteri speciali
🎛️ VOCAL GENDER: Male/Female/Auto - Imposta il genere della voce principale
🎛️ WEIRDNESS: 0% (normale) → 100% (sperimentale) - Controlla quanto sarà sperimentale il brano
🎛️ INFLUENCE: 0% (libero) → 100% (fedele) - Controlla quanto lo stile seguirà la descrizione
🎛️ EXCLUDE STYLES: "country, classical, opera, folk, bluegrass, gospel, traditional, orchestral, chamber music, baroque, romantic, medieval, gregorian, polka, waltz, tango, mariachi, flamenco, klezmer, bagpipe, didgeridoo, sitar, gamelan, throat singing, yodeling, sea shanty, military march, funeral dirge, lullaby, nursery rhyme, christmas carol, hymn, chant, ambient drone, field recording, nature sounds, white noise, silence"
**NOTA:** Rimuovi da questa lista gli stili che desideri includere e lascia solo quelli che NON vuoi nel brano
```

### 💡 ESEMPIO SETUP COMPLETO
```
Titolo: "Digital Echoes" | Vocal Gender: Female | Weirdness: 50% | Influence: 34%
Exclude: "country, classical, opera" (rimuovi generi desiderati)
```

---

## 🎵 PHASE A: <SONG_DETAILS>...</SONG_DETAILS>

> **NOTA IMPORTANTE:** La sezione SONG_DETAILS non è obbligatoria, ma è molto utile per ottenere risultati precisi. Suno tende a fraintendere descrizioni troppo "romanzate", quindi una struttura chiara con meta-tag aiuta a ottenere esattamente ciò che desideri.

> **NOTA TECNICA:** SONG_DETAILS utilizza **formato inglese standard** per massima compatibilità. Il formato inglese garantisce interpretazione più precisa e risultati più consistenti.

### ADVANCED MUSICAL PARAMETERS
- `[TEMPO: 120-140 BPM]` per controllo ritmo
- `[KEY: C Major]` per tonalità specifica
- `[TIME SIGNATURE: 4/4]` per metrica
- `[DURATION: 3:30]` per lunghezza target (fino a 8 minuti)

### ADVANCED SUNO FEATURES
- **Multi-Genre Fusion:** Supporto avanzato per fusion di generi con risultati coerenti
- **Generi Espansi:** Supporto completo per mashup di generi (es. "midwest emo + neosoul", "EDM + folk")
- **Voci Potenziate:** Gamma emotiva completa, da sussurri intimi a performance potenti con vibrato
- **Suoni Complessi:** Supporto per elementi sottili come "uplifting nostalgic tones", "leaf textures", "melodic whistling"
- **Prompt Enhancement Helper:** Tool automatico che elabora idee semplici in descrizioni ricche e dettagliate
- **Covers + Personas:** Combinazione per remix completi di voce, stile e struttura
- **Audio Professionale:** Mix bilanciati con qualità audio superiore

**MULTI-GENRE FUSION EXAMPLES (Style Field):**
```
"country hip-hop fusion with acoustic guitar riffs and 808 beats, featuring tight hip-hop drums and subtle banjo accents"
"indie-folk electronic with organic textures and digital elements"
"jazz-trap with complex harmonies and modern beats"
"rock-reggaeton with distorted guitars and latin percussion"
```

### BASE METRICS
```
SETTENARIO (7 sillabe) → Veloce, energico
OTTONARIO (8 sillabe) → Equilibrato, universale
ENDECASILLABO (11 sillabe) → Solenne, epico

CONTEGGIO:
PIANA (accento penultima) = normale
TRONCA (accento ultima) = +1 sillaba
SDRUCCIOLA (accento terzultima) = -1 sillaba
```

### GUIDA PASSO-PASSO PER CREARE SONG_DETAILS (FORMATO INGLESE)

**Cosa sono i SONG_DETAILS?** 
Una sezione che fornisce a Suno istruzioni chiare sulla struttura e lo stile della canzone usando il formato standard inglese.

**Passaggi per creare SONG_DETAILS efficaci:**

1. **Inizia con i tag di apertura e chiusura**
   - Apri con `<SONG_DETAILS>` e chiudi con `</SONG_DETAILS>`

2. **Scegli i generi musicali** 
   - **OBBLIGATORIO:** Seleziona SOLO da GENRE_LIST (vedi sotto)
   - Esempio: `[GENRE: {scegli da GENRE_LIST}, {scegli da GENRE_LIST}]`

3. **Definisci il tipo di voci**
   - **OBBLIGATORIO:** Scegli SOLO da VOCALS_LIST (vedi sotto)
   - Esempio: `[VOCALS: {scegli da VOCALS_LIST}, {scegli da VOCALS_LIST}]`

4. **Specifica il tempo/ritmo**
   - **OBBLIGATORIO:** Usa SOLO valori da TEMPO_LIST (vedi sotto)
   - Esempio: `[TEMPO: {scegli da TEMPO_LIST}]`

5. **Indica l'energia**
   - **OBBLIGATORIO:** Scegli SOLO da ENERGY_LIST (vedi sotto)
   - Esempio: `[ENERGY: {scegli da ENERGY_LIST}]`

6. **Indica la struttura della canzone**
   - **OBBLIGATORIO:** Combina elementi da STRUCTURE_LIST (vedi sotto)
   - Esempio: `[STRUCTURE: {combina da STRUCTURE_LIST}]`

7. **Definisci l'atmosfera**
   - **OBBLIGATORIO:** Scegli SOLO da ATMOSPHERES_LIST (vedi sotto)
   - Esempio: `[MOOD: {scegli da ATMOSPHERES_LIST}]`

8. **Definisci il tema principale**
   - Descrivi brevemente l'argomento della canzone
   - Esempio: `[THEME: {descrizione libera del tema}]`

9. **Aggiungi parole chiave**
   - **RACCOMANDATO:** Usa elementi da INSTRUMENTS_LIST e DYNAMICS_LIST
   - Esempio: `[KEYWORDS: {parole chiave libere + elementi dalle liste}]`

### IMPORTANT RULES

- Usa **parentesi quadre** per ogni elemento: `[Tag: Valore]`
- Metti i tag più **importanti all'inizio** (generi e voci)
- Usa **un solo tag per categoria** per evitare conflitti
- Sii **specifico e conciso** - evita descrizioni vaghe
- Combina **elementi complementari** (es. generi compatibili)

### ⚠️ REGOLA CRITICA

**🚨 ATTENZIONE:** Quando crei SONG_DETAILS, devi:
- **CONSULTARE OBBLIGATORIAMENTE** le tabelle GENRE_LIST, VOCALS_LIST, TEMPO_LIST, ENERGY_LIST, ATMOSPHERES_LIST, STRUCTURE_LIST, INSTRUMENTS_LIST, DYNAMICS_LIST che trovi più avanti in questo documento
- **NON INVENTARE** valori di fantasia
- **NON USARE** valori non presenti nelle liste
- **SELEZIONARE SOLO** dai valori forniti nelle tabelle
- Se non trovi un valore adatto, scegli il più simile dalle liste

**VIOLAZIONE = RISULTATO SCADENTE**

### COMPLETE EXAMPLES FOR DIFFERENT GENRES

**Esempio 1: Alternative Rock (TEMPLATE)**
```
<SONG_DETAILS>
[GENRE: {scegli 2-3 da GENRE_LIST sezione Rock & Alternative}]
[VOCALS: {scegli da VOCALS_LIST per stile maschile/raw}]
[TEMPO: {scegli da TEMPO_LIST per rock}]
[ENERGY: {scegli da ENERGY_LIST}]
[STRUCTURE: {combina da STRUCTURE_LIST}]
[MOOD: {scegli da ATMOSPHERES_LIST per mood rock}]
[THEME: {descrizione libera del tema}]
[KEYWORDS: {combina parole libere + elementi da INSTRUMENTS_LIST}]
</SONG_DETAILS>
```

**Esempio 2: Electronic Dance Pop (TEMPLATE)**
```
<SONG_DETAILS>
[GENRE: {scegli 2-3 da GENRE_LIST sezione Electronic & Dance}]
[VOCALS: {scegli da VOCALS_LIST per stile femminile/ethereal}]
[TEMPO: {scegli da TEMPO_LIST per dance}]
[ENERGY: {scegli da ENERGY_LIST}]
[STRUCTURE: {combina da STRUCTURE_LIST con Drop}]
[MOOD: {scegli da ATMOSPHERES_LIST per mood uplifting}]
[THEME: {descrizione libera del tema}]
[KEYWORDS: {combina parole libere + elementi da INSTRUMENTS_LIST elettronici}]
</SONG_DETAILS>
```

**Esempio 3: Hip-Hop Storytelling (TEMPLATE)**
```
<SONG_DETAILS>
[GENRE: {scegli 2-3 da GENRE_LIST sezione Hip-Hop & Urban}]
[VOCALS: {scegli da VOCALS_LIST per stile rap/flow}]
[TEMPO: {scegli da TEMPO_LIST per hip-hop}]
[ENERGY: {scegli da ENERGY_LIST}]
[STRUCTURE: {combina da STRUCTURE_LIST con Hook}]
[MOOD: {scegli da ATMOSPHERES_LIST per mood introspettivo}]
[THEME: {descrizione libera del tema}]
[KEYWORDS: {combina parole libere + elementi da DYNAMICS_LIST}]
</SONG_DETAILS>
```

### ADVANCED CATEGORIES
**Core Categories:**
- `[GENRE: ...]` - Primary musical genre
- `[VOCALS: ...]` - Voice type and characteristics
- `[STRUCTURE: ...]` - Song arrangement pattern
- `[THEME: ...]` - Lyrical theme and content
- `[KEYWORDS: ...]` - Style descriptors

**Enhanced Categories:**
- `[ENERGY: Low/Medium/High/Dynamic]` - Energy progression
- `[MOOD: Primary-Mood, Secondary-Mood]` - Emotional atmosphere

### CREATIVE LISTS (ENGLISH FORMAT)

**🔥 LISTE TECNICHE AUTORIZZATE 🔥**
**UTILIZZA ESCLUSIVAMENTE QUESTI VALORI - NIENTE ALTRO È ACCETTATO**

**GENRE_LIST:**
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

# Experimental & Fusion
Experimental, Avant-Garde, Industrial, Noise, Progressive, Post-Hardcore,
Midwest-Emo, Gregorian-Chant, Jazz-Metal, Folk-Metal, Rap-Metal
```

**VOCALS_LIST:**
```
Breathy-to-Powerful, Whisper-to-Scream, Falsetto-Dynamics, Gospel-Choir,
Vocoder-Effects, Layered-Harmonies, Raw-Emotion, Intimate-Storytelling,
Ethereal-Float, Gritty-Urban, Soulful-Melisma, Robotic-Processing,
Acoustic-Natural, Auto-Tuned-Modern, Operatic-Range, Conversational-Rap,
Alto, Soprano, Tenor, Bass, Vibrato, Intimate, Delicate, Theatrical, 
Laid-back, Twangy, Storytelling, Lyrical, Aggressive, Ethereal, Danceable, 
Empowering, Soulful, Raw, Bold
```

**TEMPO_LIST:**
```
60-70 (Ballad), 70-80 (Slow), 80-90 (Mid-Tempo), 90-100 (Moderate),
100-110 (Upbeat), 110-120 (Energetic), 120-130 (Dance), 130-140 (High-Energy),
140+ (Intense), Variable (70→120→90), Crescendo (80→140), Decrescendo (130→70)
```

**ENERGY_LIST:**
```
Low (Calm, Peaceful, Relaxed, Meditative),
Medium (Balanced, Steady, Moderate, Flowing),
High (Energetic, Vibrant, Intense, Powerful),
Dynamic (Variable, Building, Contrasting, Evolving)
```

**STRUCTURE_LIST:**
```
Intro-Verse-Chorus-Verse-Chorus-Bridge-Chorus-Outro,
Verse-PreChorus-Chorus-Verse-PreChorus-Chorus-Bridge-Chorus,
AABA, ABCB, ABAC, Intro-A-B-A-C-A-B-Outro,
Verse-Chorus-Verse-Chorus-Middle-8-Chorus-Coda,
Intro-Verse-Refrain-Verse-Refrain-Bridge-Refrain-Outro,
Intro-Verse-PreChorus-Chorus-Verse-PreChorus-Chorus-Bridge-FinalChorus-Outro
```

**MOOD_LIST:**
```
Transformative, Energetic, Melancholic, Uplifting, Nostalgic, Romantic,
Mysterious, Peaceful, Intense, Playful, Dramatic, Contemplative,
Hopeful, Dreamy, Rebellious, Intimate, Epic, Ethereal,
Gritty, Smooth, Raw, Polished, Organic, Electronic
```

**KEYWORDS_INSPIRATION:**
```
Stone, breath, water, fire, earth, wind, light, shadow,
Ocean, mountain, river, forest, desert, sky, stars, moon,
Touch, growth, rhythm, dance, flow, rise, fall, transform,
Journey, path, bridge, door, window, step, leap, flight,
Courage, community, love, hope, fear, joy, pain, healing,
Connection, separation, unity, solitude, strength, vulnerability
```

---

## 🎸 PHASE B: STYLE

### STYLE RULES
```
✅ UN PARAGRAFO, max 1000 caratteri
✅ INGLESE per terminologia musicale (consigliato scrivere tutto lo style in iglese anche se la canzone sarà in italiano)
✅ Frasi separate da punti
❌ NO a capo, elenchi, parentesi complesse
❌ NO "come se", "sembra", "storia", riferimenti culturali
```

**IMPORTANTE:** Lo STYLE deve essere un paragrafo unico senza a capo, solo frasi separate da punti.

### META-TAGS

**DOVE USARE I META-TAG:**
- I meta-tag funzionano sia nel campo **Custom Lyrics** che nel campo **Style**
- Maggiore efficacia nel campo Custom Lyrics per controllo strutturale
- Nel campo Style per descrizioni di genere e atmosfera generale

**FORMATO E REGOLE DEI META-TAG:**
- Formato Strutturale: `[Tag: Value]` con parentesi quadre
- Formato Descrittivo: `[section: instruments, mood: emotion]` per sezioni specifiche
- Posizionare i tag chiave nei primi 20-30 caratteri per massima efficacia
- Usare 1 tag per categoria, massimo 2-3 strumenti per canzone
- Evitare tag conflittuali (es. Energy: High + Energy: Low)

**ESEMPI META-TAG DESCRITTIVI:**
```
[intro: soft piano, ambient pad, mood: reflective]
[chorus: hopeful, layered vocals]
[bridge: stripped back, intimate vocals]
[outro: fade with reverb tails, nostalgic]
```

**PAROLE PERICOLOSE DA EVITARE NELLO STYLE:**
Verse, Chorus, Bridge, Intro, Outro, Hook, Refrain, Solo, Break, Drop, Build, Fade, Repeat, Loop, Section, Part, Segment, Transition, Interlude, Coda

### SEMANTIC TECHNIQUES
```
1. Musical Storytelling: "narrative progression"
2. Sound Metaphors: "notes like raindrops"
3. Emotional Arc: "starts shy, explodes into passion"
4. Cinematic Feel: "sunset atmosphere"
5. Layered Description: strumenti + emozioni + dinamiche
```

### 🎵 PROGRESSIONE ENERGETICA
```
Verse: Intimo → Pre-Chorus: Crescendo → Chorus: Esplosivo → Bridge: Contrasto
Cambia strumentazione ogni sezione per varietà
```

### STYLE LISTS

**INSTRUMENTS_LIST:**
```
Fingerpicked-Guitar, Deep-808s, Ethereal-Synths, Analog-Warmth,
Distorted-Bass, Crisp-Drums, Lush-Strings, Vintage-Keys, Glitchy-Beats,
Ambient-Pads, Brass-Stabs, Vinyl-Crackle, Tape-Saturation, Reverb-Tails,
Sidechain-Pump, Filter-Sweeps, Granular-Texture, Field-Recordings,
Electric Guitar (Distorted), Acoustic Guitar, Strings (Legato), 808, 
Slap Bass, Crunchy Guitar Riffs, Piano-driven, Ambient Beats, Groovy Rhythms, 
Pounding Drums, Aggressive Riffs, Guitar Loops, Steady Rhythm
```

**ATMOSPHERES_LIST:**
```
Melancholic-Introspection, Urban-Solitude, Nostalgic-Warmth, Euphoric-Release,
Dark-Contemplation, Dreamy-Float, Gritty-Reality, Ethereal-Escape,
Intimate-Vulnerability, Epic-Grandeur, Mysterious-Depth, Playful-Energy,
Emotional-Catharsis, Cinematic-Drama, Minimalist-Space, Chaotic-Beauty,
Atmospheric, Ambient, Emotional, Festive, Peaceful, Joyful, Heartfelt, 
Vibrant, Cool, Eclectic, Progressive, Theatrical, Anthemic, Danceable, 
Groovy, Futuristic, Unusual, Operatic, Psychedelic, Mystical, Youthful, 
Intimate, Powerful, Leaf Textures, Uplifting Nostalgic Tones
```

**DYNAMICS_LIST:**
```
Builds-Gradually, Explosive-Drops, Intimate-Whispers, Soaring-Climax,
Stripped-Back-Moments, Layered-Complexity, Rhythmic-Pulse, Floating-Weightless,
Driving-Forward, Gentle-Sway, Intense-Energy, Calm-Reflection,
Tension-Release, Organic-Flow, Electronic-Precision, Raw-Emotion,
Buildup, Drop, Breakdown, Crescendo, Diminuendo, Staccato, Legato, Syncopation, 
Polyrhythm, Cross-rhythm, Tempo-shift, Dynamic-contrast, Rhythmic-displacement, 
Metric-modulation, Energy-High, Energy-Medium, Energy-Low, Tempo-Mid, 
Texture-Gritty, Mood-Uplifting, Mood-Intense, Catchy-Hook, Emotional-Bridge, 
Powerful-Outro, Pre-Chorus, Guitar-Solo, Female-Vocal, Male-Vocal, Harmony-Yes, 
Vocal-Effect-Reverb, Vocal-Effect-Delay, Vocal-Tone-Whisper
```

---

## 📐 PHASE C: METRIC STRUCTURE

### PROCESS
```
1. SCEGLI target sillabe da METRICS_LIST
2. SCRIVI verso
3. CONTA battendo ritmo
4. Se ≠ target → RISCRIVI
5. Se = target → PROCEDI
```

### 🧠 CONTEGGIO VELOCE
```
Batti il ritmo mentalmente mentre leggi
Se non "suona" giusto → troppo lungo/corto
```

### ⚡ FIX VELOCE
```
Troppo lungo → Rimuovi aggettivi | Troppo corto → Aggiungi articoli
Rima forzata → Cambia ultima parola
```

**METRICS_LIST:**
```
ROCK/METAL: Verse(8), Chorus(8), Bridge(11)
INDIE/ALT: Verse(7), Chorus(8), Bridge(9)
POP/COMMERCIAL: Verse(8), Chorus(7), Bridge(10)
RAP/HIP-HOP: Verse(variabile), Chorus(8), Bridge(6)
BALLAD: Verse(11), Chorus(8), Bridge(11)
ELETTRONICA: Verse(6), Chorus(7), Bridge(8)
```

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

### CHORUS RULES
```
✅ RIME (ABAB/AABB)
✅ PAROLE SEMPLICI
✅ ORECCHIABILITÀ
✅ RIPETIBILITÀ
✅ IMPATTO EMOTIVO
```

---

## 🎤 PHASE D: FINAL TEXT

### FORMAT
```
[Sezione: Descrizione da ATMOSPHERES_LIST]
Testo pulito italiano
Rispettando sillabe pianificate

🚨 DIVIETI:
❌ Note esplicative (💡 NOTA RIME)
❌ Spiegazioni metrica
❌ Commenti tra parentesi
✅ Solo testo cantabile
```

### SECTION TAGS
```
✅ CORRETTO:
[Verse: Intimate storytelling, fingerpicked guitar]
[Chorus: Explosive anthem, full band]

❌ SBAGLIATO:
[Verse - 8 sillabe]
[Chorus: 8 syllables per line]
```

---

## 🚨 ERRORS TO AVOID

### ANTI-GLITCH
```
❌ Stili narrativi complessi
❌ Riferimenti culturali esterni
❌ Descrizioni multi-paragrafo
❌ Metafore elaborate
✅ Terminologia musicale diretta
✅ Paragrafo fluido <1000 caratteri
```

### STRUCTURAL
```
❌ Mescolare SONG_DETAILS con testo
❌ Commenti narrativi nel testo
❌ Note esplicative
❌ Style multi-paragrafo
```

### CREATIVE
```
❌ Un solo genere
❌ Cliché lirici
❌ Energia statica
❌ Strutture banali
❌ Strumentazione monotona
```

### METRIC
```
❌ Metrica casuale
❌ Parole difficili da pronunciare
❌ Rime forzate
❌ Versi troppo lunghi
❌ Chorus senza rime
```

---

## 🎯 PHILOSOPHY

*Questa guida è uno strumento, non una gabbia.*

**Principi:**
- Usa le tecniche che servono
- Adatta al contesto
- Creatività guida le scelte
- Qualità = equilibrio, non rigidità

**Ricorda:** Suno capisce "chitarra distorta" meglio di "dolore dell'anima". Preferisce istruzioni musicali a poesie elaborate.

---

**🎵 Crea con le regole, poi superale. 🎵**