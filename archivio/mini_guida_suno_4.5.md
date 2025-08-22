# MINI GUIDA SUNO 4.5 - ESSENZIALE PER LLM

## STRUTTURA BASE PROMPT

### MODALITÀ CUSTOM (OBBLIGATORIA)
- **Campo LYRICS**: Testo cantato + tag struttura
- **Campo STYLE**: Genere + strumenti + mood + tecnica

### REGOLE FONDAMENTALI
1. **LYRICS**: Solo testo cantato + [tag struttura] + <SONG_DETAILS> opzionale
2. **STYLE**: Descrizione narrativa in INGLESE, MAX 1000 caratteri
3. **Parentesi ()**: Adlib/background vocals
4. **Quadre []**: Istruzioni/sezioni NON cantate
5. **<SONG_DETAILS>**: Per controllo dettagliato (da inserire nei Lyrics)

## TEMPLATE LYRICS AVANZATO

### CREATIVITÀ E SPERIMENTAZIONE
**IMPORTANTE**: Questo template è solo un punto di partenza! Sperimenta con:
- **Strutture non convenzionali**: Inizia con un Chorus, salta il Pre-Chorus, usa doppi Bridge
- **Sezioni uniche**: Aggiungi [Interlude], [Breakdown], [Build-up], [Drop] per generi specifici
- **Variazioni dinamiche**: Alterna sezioni intense e intime per creare contrasto emotivo
- **Lunghezze diverse**: Versi corti + Chorus lunghi, o viceversa per ritmi inaspettati

```
[Intro: Soft, atmospheric]
(Yeah... let's go)

[Verse 1: Intimate, whispered]
Testo verso 1 linea 1
Testo verso 1 linea 2 (oh)
Testo verso 1 linea 3
Testo verso 1 linea 4

[Pre-Chorus: Building energy]
Testo pre-ritornello linea 1
Testo pre-ritornello linea 2

[Chorus: Powerful, anthemic]
Testo ritornello linea 1
Testo ritornello linea 2
Testo ritornello linea 3
Testo ritornello linea 4

[Verse 2: Confident, rhythmic]
[Pre-Chorus: Tension rising]
[Chorus: Explosive, full]
[Bridge: Emotional, stripped down]
[Final Chorus: Epic, layered vocals]
[Outro: Fading, reflective]
```

### ESEMPI DI STRUTTURE CREATIVE
**NOTA**: Gli esempi seguenti sono puramente dimostrativi e non regole da seguire rigidamente. Usa la tua creatività per inventare strutture completamente nuove!

```
# Struttura Cinematica
[Intro: Ambient] → [Verse] → [Chorus] → [Interlude: Instrumental] → [Verse] → [Bridge] → [Climax: Epic Chorus] → [Outro: Fade]

# Struttura EDM
[Intro] → [Build-up] → [Drop] → [Breakdown] → [Build-up] → [Drop] → [Outro]

# Struttura Narrativa
[Spoken Intro] → [Verse: Story setup] → [Chorus: Emotion] → [Verse: Plot twist] → [Bridge: Reflection] → [Final Chorus: Resolution]
```

### TAG DI PERSONALIZZAZIONE PER SEZIONI

#### STILI VOCALI
- `[Verse: Whispered]` - Voce sussurrata
- `[Chorus: Belted]` - Voce potente e sostenuta
- `[Bridge: Falsetto]` - Voce in falsetto
- `[Outro: Humming]` - Canticchiato
- `[Intro: Spoken word]` - Parlato
- `[Verse: Raspy]` - Voce roca
- `[Chorus: Harmonized]` - Voci armonizzate

#### DINAMICHE MUSICALI
- `[Verse: Stripped down]` - Arrangiamento minimale
- `[Chorus: Full band]` - Arrangiamento completo
- `[Bridge: Acoustic only]` - Solo acustico
- `[Intro: Ambient]` - Atmosferico
- `[Outro: A cappella]` - Solo voci
- `[Verse: Heavy drums]` - Batteria prominente
- `[Chorus: Orchestral]` - Con orchestra

#### INTENSITÀ EMOTIVA
- `[Verse: Melancholic]` - Malinconico
- `[Chorus: Euphoric]` - Euforico
- `[Bridge: Vulnerable]` - Vulnerabile
- `[Intro: Mysterious]` - Misterioso
- `[Outro: Hopeful]` - Pieno di speranza
- `[Verse: Aggressive]` - Aggressivo
- `[Chorus: Triumphant]` - Trionfante

#### ESEMPI COMBINATI
```
[Verse 1: Intimate, acoustic guitar only]
[Pre-Chorus: Building, drums entering]
[Chorus: Explosive, full band, belted vocals]
[Verse 2: Confident, bass-driven, raspy voice]
[Bridge: Emotional breakdown, piano only, whispered]
[Final Chorus: Epic, orchestral, layered harmonies]
```

## TEMPLATE STYLE (V4.5 NARRATIVO)

### FORMATO DESCRITTIVO (max 1000 caratteri)
```
Un brano [GENERE] a [BPM] BPM in tonalità di [TONALITÀ].
L'intro inizia con [DESCRIZIONE INTRO].
I versi presentano [DESCRIZIONE VERSI].
Il ritornello esplode con [DESCRIZIONE CHORUS].
Vocale [TIPO VOCE] con [EFFETTI].
Mix [CARATTERISTICHE AUDIO].

SEE <SONG_DETAILS> IN THE LYRICS FIELD FOR DETAILED INFORMATION
```

### ESEMPIO CONCRETO
```
Un brano trap melodico a 140 BPM in tonalità di C# minor.
L'intro inizia con pad atmosferici e hi-hat sussurrati.
I versi presentano 808 profondi e synth cristallini.
Il ritornello esplode con vocal layering e lead synth.
Vocale maschile auto-tuned con riverbero spaziale.
Mix scuro e cinematico con sidechain pump.
```

## TECNICA AVANZATA: <SONG_DETAILS>

### QUANDO USARE
- Per controllo massimo su ogni aspetto
- Quando lo Style field non basta (1000 caratteri)
- Per specificare dettagli tecnici precisi
- Per progetti professionali

### TEMPLATE <SONG_DETAILS>
```
<SONG_DETAILS>

[GENRES: Indie Pop, Dream Pop, Ambient]

[STYLE: Ethereal, Atmospheric, Lush, Dreamy, Indie pop influenced, Dream pop elements]

[MOOD: Nostalgic, Melancholic, Hopeful, Introspective]

[VOCALS: Female, Breathy, Layered harmonies, Reverb-drenched]

[ARRANGEMENT: Slow build, Dynamic contrast, Textural layers]

[INSTRUMENTATION: Acoustic guitar, Synthesizers, Strings, Soft drums]

[TEMPO: Slow, 65-75 BPM]

[PRODUCTION: Warm analog, Vintage reverb, Soft compression, Hi-fidelity, Studio recording]

[STRUCTURE: Intro, Verse, Chorus, Verse, Chorus, Bridge, Outro]

[DYNAMICS: Intimate verses, Soaring choruses, Gradual builds]

[EMOTIONS: Longing, Wonder, Peacefulness, Contemplation]

</SONG_DETAILS>

[Intro: Soft, atmospheric]
(Testo introduttivo)
```

### ATTRIBUTI CHIAVE <SONG_DETAILS>
- **GENRES**: Generi specifici
- **STYLE**: Aggettivi stilistici (evitare riferimenti diretti ad artisti)
- **MOOD**: Atmosfera emotiva
- **VOCALS**: Tipo e stile vocale
- **ARRANGEMENT**: Struttura musicale
- **INSTRUMENTATION**: Strumenti specifici
- **TEMPO**: BPM e ritmo
- **PRODUCTION**: Qualità e tecnica
- **STRUCTURE**: Sezioni del brano
- **DYNAMICS**: Variazioni di intensità
- **EMOTIONS**: Sentimenti trasmessi

## TAG STRUTTURA ESSENZIALI
- `[Intro]` - Introduzione
- `[Verse]` - Strofa
- `[Pre-Chorus]` - Pre-ritornello
- `[Chorus]` - Ritornello
- `[Bridge]` - Ponte
- `[Outro]` - Finale
- `[Drop]` - Drop (EDM)
- `[Solo]` - Assolo strumentale

## EFFETTI SONORI E RUMORI

### SINTASSI CORRETTA (SEMPRE IN INGLESE)
```
(Sound of coffee grinder starting slowly)
(Dripping coffee like a heartbeat)
(Whispered, distant): "Here I am... awake"
(Soft whisper: 'Kagura is ready...')
(Vinyl crackle and ambient wind)
(Tape hiss fading in)
(Metallic percussion hits)
```

### ESEMPI EFFETTI COMUNI
- **Ambiente**: `(Rain sounds)`, `(Wind blowing)`, `(Ocean waves)`
- **Meccanici**: `(Clock ticking)`, `(Engine humming)`, `(Vinyl crackle)`
- **Naturali**: `(Birds chirping)`, `(Fire crackling)`, `(Footsteps)`
- **Elettronici**: `(Synth pad rising)`, `(Digital glitch)`, `(Reverb tail)`
- **Vocali**: `(Whispered)`, `(Humming)`, `(Breathing)`

## GENERI PRINCIPALI V4.5
- **Pop**: Pop, Dance Pop, Electropop
- **Rock**: Alternative Rock, Indie Rock, Hard Rock
- **Electronic**: EDM, House, Techno, Dubstep, Trap
- **Hip-Hop**: Trap, Boom Bap, Lo-fi Hip-Hop
- **R&B**: Neo-Soul, Contemporary R&B
- **Alternative**: Indie Folk, Dream Pop, Shoegaze

## MASHUP GENERI (NOVITÀ V4.5)
- Midwest Emo + Neo-Soul
- EDM + Folk
- Jazz + House
- Punk + Electronic
- Country + Trap

## TIPI VOCE
- **Maschile**: Deep male, Tenor, Falsetto, Raspy
- **Femminile**: Soprano, Alto, Breathy, Powerful
- **Effetti**: Auto-tuned, Reverb-heavy, Distorted, Clean

## STRUMENTI CHIAVE
- **Chitarre**: Acoustic, Electric, Distorted, Clean
- **Synth**: Lead, Pad, Bass, Arp
- **Batteria**: Acoustic, Electronic, 808, Trap
- **Bassi**: Electric, Synth, 808, Upright

## MOOD/ATMOSFERA
- **Energia**: Energetic, Chill, Aggressive, Mellow
- **Emozioni**: Nostalgic, Dark, Uplifting, Melancholic
- **Ambiente**: Cinematic, Intimate, Epic, Underground

## FUNZIONI AVANZATE V4.5

### PERSONAS
- Salva "DNA" vocale/stilistico di un brano
- Riutilizza su nuovi testi
- Combinabile con Covers

### COVERS
- Reinterpreta melodia esistente
- Mantiene struttura, cambia stile
- Combinabile con Personas

### EXTEND
- Estende brani fino a 8 minuti
- Mantiene coerenza stilistica

## PROMPT ENHANCEMENT
- Usa il bottone "Enhance" per espandere idee base
- Trasforma "ambient techno" in descrizione completa
- Modifica il risultato per personalizzare

## ERRORI DA EVITARE
1. **Lista tag nel Style**: "Pop, energetic, guitar" ❌
2. **Istruzioni nei Lyrics**: "This song is in C minor" ❌
3. **Prompt troppo corti**: "Sad song" ❌
4. **Mixing campi**: Genere nei Lyrics ❌
5. **Style in italiano**: Sempre scrivere in inglese ❌
6. **Style troppo lungo**: Max 1000 caratteri ❌
7. **Effetti in italiano**: `(Suono di caffè)` ❌ → `(Coffee sounds)` ✅
8. **Sintassi effetti sbagliata**: Usare sempre parentesi e inglese ❌
9. **"SOUNDS LIKE" vietato**: Suno vieta questo termine → Usare "INFLUENCES" ✅
10. **Riferimenti artisti diretti**: "Like Radiohead" ❌ → "Alternative rock influences" ✅

## BEST PRACTICES
1. **Descrizioni narrative** nel Style
2. **Struttura chiara** nei Lyrics
3. **Specifici ma concisi**
4. **Testa combinazioni** generi
5. **Usa Enhance** come punto di partenza

## LIMITI TECNICI
- **Lunghezza**: Max 8 minuti (prima generazione)
- **Qualità**: WAV solo Pro/Premier
- **Generazioni**: 500+/giorno Pro
- **Funzioni avanzate**: Solo account paganti

## CONCLUSIONE
La musica è fantasia ed ogni esempio ed ogni regola sopra è da scartare se il ritmo ti porta altrove.
---
*Guida ottimizzata per LLM - Versione compatta Suno 4.5*