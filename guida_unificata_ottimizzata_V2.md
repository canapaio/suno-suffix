# GUIDA SUNO 4.5 - SISTEMA LLM OTTIMIZZATO

*Flusso lineare: 0→A→B→C→D*

## 🔧 FASE 0: CONFIGURAZIONE

### ADVANCED OPTIONS
```
🎵 TITOLO: Evocativo, 5-6 parole max, senza caratteri speciali
🎛️ GENDER: Male/Female/Auto - Imposta il genere della voce principale
🎛️ WEIRDNESS: 0% (normale) → 100% (sperimentale) - Controlla quanto sarà sperimentale il brano
🎛️ INFLUENCE: 0% (libero) → 100% (fedele) - Controlla quanto lo stile seguirà la descrizione
🎛️ EXCLUDE STYLES: "country, classical, opera, folk, bluegrass, gospel, traditional, orchestral, chamber music, baroque, romantic, medieval, gregorian, polka, waltz, tango, mariachi, flamenco, klezmer, bagpipe, didgeridoo, sitar, gamelan, throat singing, yodeling, sea shanty, military march, funeral dirge, lullaby, nursery rhyme, christmas carol, hymn, chant, ambient drone, field recording, nature sounds, white noise, silence"
**NOTA:** Rimuovi da questa lista gli stili che desideri includere e lascia solo quelli che NON vuoi nel brano
```

### 💡 ESEMPIO SETUP COMPLETO
```
Titolo: "Digital Echoes" | Gender: Female | Weirdness: 50% | Influence: 34%
Exclude: "country, classical, opera" (rimuovi generi desiderati)
```

---

## 🎵 FASE A: <SONG_DETAILS>...</SONG_DETAILS>

> **NOTA IMPORTANTE:** La sezione SONG_DETAILS non è obbligatoria, ma è molto utile per ottenere risultati precisi. Suno tende a fraintendere descrizioni troppo "romanzate", quindi una struttura chiara con meta-tag aiuta a ottenere esattamente ciò che desideri.

### PARAMETRI MUSICALI AVANZATI
- `[Tempo: 120-140 BPM]` per controllo ritmo
- `[Key: C Major]` per tonalità specifica
- `[Time Signature: 4/4]` per metrica
- `[Duration: 3:30]` per lunghezza target (fino a 8 minuti)

### FUNZIONALITÀ SUNO AVANZATE
- **Generi Espansi:** Supporto completo per mashup di generi (es. "midwest emo + neosoul", "EDM + folk")
- **Voci Potenziate:** Gamma emotiva completa, da sussurri intimi a performance potenti con vibrato
- **Suoni Complessi:** Supporto per elementi sottili come "uplifting nostalgic tones", "leaf textures", "melodic whistling"
- **Prompt Enhancement:** Trasformazione automatica di idee semplici in descrizioni dettagliate
- **Covers + Personas:** Combinazione per remix completi di voce, stile e struttura
- **Audio Ottimizzato:** Mix bilanciati con qualità audio superiore

### METRICHE BASE
```
SETTENARIO (7 sillabe) → Veloce, energico
OTTONARIO (8 sillabe) → Equilibrato, universale
ENDECASILLABO (11 sillabe) → Solenne, epico

CONTEGGIO:
PIANA (accento penultima) = normale
TRONCA (accento ultima) = +1 sillaba
SDRUCCIOLA (accento terzultima) = -1 sillaba
```

### GUIDA PASSO-PASSO PER CREARE SONG_DETAILS

**Cosa sono i SONG_DETAILS?** 
Una sezione che fornisce a Suno istruzioni chiare sulla struttura e lo stile della canzone.

**Passaggi per creare SONG_DETAILS efficaci:**

1. **Inizia con i tag di apertura e chiusura**
   - Apri con `<SONG_DETAILS>` e chiudi con `</SONG_DETAILS>`

2. **Scegli i generi musicali** 
   - Seleziona 2-3 generi dall'ELENCO_GENERI
   - Esempio: `[GENERI: Indie-Folk, Electro-Pop]`

3. **Definisci il tipo di voci**
   - Scegli dall'ELENCO_VOCI per definire lo stile vocale
   - Esempio: `[VOCI: Breathy-to-Powerful, Layered-Harmonies]`

4. **Specifica il tempo/ritmo**
   - Usa l'ELENCO_BPM per indicare la velocità
   - Esempio: `[TEMPO: 90-100 (Moderate)]`

5. **Indica la struttura della canzone**
   - Scegli dall'ELENCO_STRUTTURE per definire le sezioni
   - Esempio: `[STRUTTURA: Verse-Chorus-Verse-Chorus-Bridge-Chorus]`

6. **Definisci il tema principale**
   - Descrivi brevemente l'argomento della canzone
   - Esempio: `[TEMA: Trasformazione personale]`

7. **Aggiungi parole chiave**
   - Usa l'ELENCO_METAFORE per arricchire il contenuto
   - Esempio: `[PAROLE CHIAVE: Metamorfosi-Rinascita, Architetture-Sogni]`

### REGOLE IMPORTANTI

- Usa **parentesi quadre** per ogni elemento: `[Tag: Valore]`
- Metti i tag più **importanti all'inizio** (generi e voci)
- Usa **un solo tag per categoria** per evitare conflitti
- Sii **specifico e conciso** - evita descrizioni vaghe
- Combina **elementi complementari** (es. generi compatibili)

### ESEMPIO COMPLETO
```
<SONG_DETAILS>
[GENERI: Indie-Folk, Electro-Pop]
[VOCI: Breathy-to-Powerful, Layered-Harmonies]
[TEMPO: 90-100 (Moderate)]
[STRUTTURA: Verse-Chorus-Verse-Chorus-Bridge-Chorus]
[TEMA: Trasformazione personale]
[PAROLE CHIAVE: Metamorfosi-Rinascita, Architetture-Sogni]
</SONG_DETAILS>
```

### ELENCHI CREATIVI

**ELENCO_GENERI:**
```
Indie-Folk, Electro-Pop, Jazz-Fusion, Trap-Soul, Dream-Pop, Post-Rock, 
Synth-Wave, Neo-Soul, Alternative-R&B, Experimental-Hip-Hop, Ambient-House,
Math-Rock, Shoegaze, Chillwave, Future-Bass, Lo-Fi-Hip-Hop, Psychedelic-Pop,
Indie-Electronic, Alternative-Folk, Progressive-Pop, Downtempo, Trip-Hop,
Jazz House, Punk Rock, Gregorian Chant, Midwest Emo, Neosoul, EDM Folk, 
Alternative Metal, Alternative Pop, Boom Bap, Hardcore Rap, Heavy Metal, 
Post-Hardcore, Synth Pop, Atlanta Rap, J-Pop, K-Pop, Lo-Fi, Baroque, 
Christmas, Dance Electronic, Girl Group, Indie Rock, Orchestra, Party, 
Pop-Rock, Romantic, Chill, African, Ballad, Christian Gospel, Country Americana
```

**ELENCO_VOCI:**
```
Breathy-to-Powerful, Whisper-to-Scream, Falsetto-Dynamics, Gospel-Choir,
Vocoder-Effects, Layered-Harmonies, Raw-Emotion, Intimate-Storytelling,
Ethereal-Float, Gritty-Urban, Soulful-Melisma, Robotic-Processing,
Acoustic-Natural, Auto-Tuned-Modern, Operatic-Range, Conversational-Rap,
Alto, Soprano, Tenor, Bass, Vibrato, Intimate, Delicate, Theatrical, 
Laid-back, Twangy, Storytelling, Lyrical, Aggressive, Ethereal, Danceable, 
Empowering, Soulful, Raw, Bold
```

**ELENCO_BPM:**
```
60-70 (Ballad), 70-80 (Slow), 80-90 (Mid-Tempo), 90-100 (Moderate),
100-110 (Upbeat), 110-120 (Energetic), 120-130 (Dance), 130-140 (High-Energy),
140+ (Intense), Variabile (70→120→90), Crescendo (80→140), Decrescendo (130→70)
```

**ELENCO_STRUTTURE:**
```
Intro-Verse-Chorus-Verse-Chorus-Bridge-Chorus-Outro,
Verse-Pre-Chorus-Chorus-Verse-Pre-Chorus-Chorus-Bridge-Chorus,
AABA, ABCB, ABAC, Intro-A-B-A-C-A-B-Outro,
Verse-Chorus-Verse-Chorus-Middle-8-Chorus-Coda,
Intro-Verse-Refrain-Verse-Refrain-Bridge-Refrain-Outro
```

**ELENCO_METAFORE:**
```
Alchimia-Trasformazione, Costellazioni-Cicatrici, Metamorfosi-Rinascita,
Echi-Digitali, Labirinti-Emotivi, Prismi-Sentimenti, Maree-Interiori,
Architetture-Sogni, Geografie-Cuore, Tessiture-Tempo, Cristalli-Memoria,
Oceani-Pensiero, Galassie-Emozioni, Ponti-Invisibili, Radici-Cielo
```

---

## 🎸 FASE B: STYLE

### REGOLE STYLE
```
✅ UN PARAGRAFO, max 1000 caratteri
✅ INGLESE per terminologia musicale (consigliato scrivere tutto lo style in iglese anche se la canzone sarà in italiano)
✅ Frasi separate da punti
❌ NO a capo, elenchi, parentesi complesse
❌ NO "come se", "sembra", "storia", riferimenti culturali
```

**IMPORTANTE:** Lo STYLE deve essere un paragrafo unico senza a capo, solo frasi separate da punti.

### META-TAG

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

### TECNICHE SEMANTICHE
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

### ELENCHI STYLE

**ELENCO_STRUMENTI:**
```
Fingerpicked-Guitar, Deep-808s, Ethereal-Synths, Analog-Warmth,
Distorted-Bass, Crisp-Drums, Lush-Strings, Vintage-Keys, Glitchy-Beats,
Ambient-Pads, Brass-Stabs, Vinyl-Crackle, Tape-Saturation, Reverb-Tails,
Sidechain-Pump, Filter-Sweeps, Granular-Texture, Field-Recordings,
Electric Guitar (Distorted), Acoustic Guitar, Strings (Legato), 808, 
Slap Bass, Crunchy Guitar Riffs, Piano-driven, Ambient Beats, Groovy Rhythms, 
Pounding Drums, Aggressive Riffs, Guitar Loops, Steady Rhythm
```

**ELENCO_ATMOSFERE:**
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

**ELENCO_DINAMICHE:**
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

## 📐 FASE C: STRUTTURA METRICA

### PROCESSO
```
1. SCEGLI target sillabe da ELENCO_METRICHE
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

**ELENCO_METRICHE:**
```
ROCK/METAL: Verse(8), Chorus(8), Bridge(11)
INDIE/ALT: Verse(7), Chorus(8), Bridge(9)
POP/COMMERCIAL: Verse(8), Chorus(7), Bridge(10)
RAP/HIP-HOP: Verse(variabile), Chorus(8), Bridge(6)
BALLAD: Verse(11), Chorus(8), Bridge(11)
ELETTRONICA: Verse(6), Chorus(7), Bridge(8)
```

**ELENCO_EFFETTI_SONORI:**
```
Effetti Ambientali: Birds-chirping, Bell-dings, Phone-ringing, Whistling, 
Applause, Cheering, Clapping
Effetti Vocali: Whispers, Chuckles, Giggling, Sighs, Groaning, Cough, Screams
Effetti Tecnici: Beeping, Bleep, Ringing, Static, Silence, Censored, Clears-throat
Voci Narrative: Announcer, Reporter, Female-narrator, Man, Woman, Boy, Girl, 
Audience-laughing
```

**ELENCO_META_TAG_STRUTTURALI:**
```
Struttura: [Intro], [Verse], [Chorus], [Bridge], [Drop], [Outro], [Pre-Chorus]
Genere: [Genre: Pop], [Genre: Rock], [Style: Lo-fi], [Era: 2000s]
Strumenti: [Instrument: Piano], [Instrument: Electric Guitar (Distorted)], 
[Instrument: Strings (Legato)]
Vocali: [Vocalist: Female], [Vocalist: Alto], [Harmony: Yes], [Vocal Effect: Reverb], 
[Vocal Tone: Whisper]
Energia: [Energy: High], [Energy: Medium], [Energy: Low], [Mood: Uplifting], 
[Tempo: Mid], [Texture: Gritty]
```

### REGOLE CHORUS
```
✅ RIME OBBLIGATORIE (ABAB/AABB)
✅ PAROLE SEMPLICI
✅ ORECCHIABILITÀ
✅ RIPETIBILITÀ
✅ IMPATTO EMOTIVO
```

---

## 🎤 FASE D: TESTO FINALE

### FORMATO
```
[Sezione: Descrizione da ELENCO_ATMOSFERE]
Testo pulito italiano
Rispettando sillabe pianificate

🚨 DIVIETI:
❌ Note esplicative (💡 NOTA RIME)
❌ Spiegazioni metrica
❌ Commenti tra parentesi
✅ Solo testo cantabile
```

### TAG SEZIONI
```
✅ CORRETTO:
[Verse: Intimate storytelling, fingerpicked guitar]
[Chorus: Explosive anthem, full band]

❌ SBAGLIATO:
[Verse - 8 sillabe]
[Chorus: 8 syllables per line]
```

---

## 🚨 ERRORI DA EVITARE

### ANTI-GLITCH
```
❌ Stili narrativi complessi
❌ Riferimenti culturali esterni
❌ Descrizioni multi-paragrafo
❌ Metafore elaborate
✅ Terminologia musicale diretta
✅ Paragrafo fluido <1000 caratteri
```

### STRUTTURALI
```
❌ Mescolare SONG_DETAILS con testo
❌ Commenti narrativi nel testo
❌ Note esplicative
❌ Style multi-paragrafo
```

### CREATIVI
```
❌ Un solo genere
❌ Cliché lirici
❌ Energia statica
❌ Strutture banali
❌ Strumentazione monotona
```

### METRICI
```
❌ Metrica casuale
❌ Parole difficili da pronunciare
❌ Rime forzate
❌ Versi troppo lunghi
❌ Chorus senza rime
```

---

## 🎯 FILOSOFIA

*Questa guida è uno strumento, non una gabbia.*

**Principi:**
- Usa le tecniche che servono
- Adatta al contesto
- Creatività guida le scelte
- Qualità = equilibrio, non rigidità

**Ricorda:** Suno capisce "chitarra distorta" meglio di "dolore dell'anima". Preferisce istruzioni musicali a poesie elaborate.

### ✨ FILOSOFIA ONE-SHOT
```
Pianifica prima, esegui con fiducia
La creatività nasce dall'equilibrio tra struttura e spontaneità
```

---

**🎵 Crea con le regole, poi superale. 🎵**