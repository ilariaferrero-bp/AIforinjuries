# Recap Completo del Modello di Rischio Operativo

## 1. Executive Summary

Questo documento riassume tutto il lavoro fatto sui due file Excel disponibili, dalla pulizia iniziale fino all'ultimo modello con tassonomia comportamentale v2, sottofamiglie, severità HSE e investigation pack.

La conclusione principale è questa: con i dati disponibili possiamo costruire un modello utile di **prioritizzazione del rischio operativo a livello area-mese**, non un modello che predice il singolo infortunio individuale.

Il sistema attuale risponde bene a queste domande:

- Quali aree sono più a rischio nel mese successivo?
- Quali segnali storici, comportamentali e testuali stanno accompagnando quel rischio?
- Quali attività, famiglie comportamento e sottofamiglie comportamento conviene investigare sul campo?
- Quali eventi storici simili possono aiutare HSE a preparare un sopralluogo?

Il sistema attuale non va letto così:

- Non dice quale persona si farà male.
- Non dimostra una causalità diretta tra una singola osservazione BBS e un singolo evento.
- Non predice in modo affidabile parte del corpo e causa specifica.
- Non trasforma l'assenza di osservazioni in sicurezza reale.

Il caso d'uso più robusto oggi è:

- scoring mensile area-mese;
- scelta delle prime 3-5 aree da investigare;
- deepdive su attività, famiglie comportamento e sottofamiglie comportamento;
- investigation pack per orientare audit, coaching e sopralluogo.

## 2. Input di Partenza

I file sorgente sono:

| File | Ruolo nel progetto | Righe input | Colonne input |
|---|---:|---:|---:|
| `SAMPLE 2 - Estratto_eventi_ITA_2016_2026WK16.xlsx` | Eventi HSE, target, storico eventi, SMAT, descrizioni | `25082` | `101` |
| `Osservazioni_Agordo_cf09b6dda9dc4bfbb40d2fee5335bf5d.xlsx` | Osservazioni BBS, comportamenti safe/unsafe, attività, gruppi | `608507` | n.d. |

La scelta teorica iniziale è stata fondamentale: i due dataset non hanno una chiave comune evento-persona-turno-macchina. Quindi non è possibile fare un merge individuale osservazione-evento. L'integrazione corretta è aggregata a livello:

```text
area_canonica x mese
```

Il file Eventi fornisce target e storico rischio. Il file Osservazioni/BBS fornisce esposizione comportamentale, safe/unsafe, attività osservate e segnali deboli.

## 3. Cleaning File Eventi

Sul file eventi sono state applicate queste regole:

| Operazione | Risultato |
|---|---:|
| Righe input | `25082` |
| Colonne input | `101` |
| Righe finali dopo cleaning | `24026` |
| Colonne finali utili | `35` |
| Righe COVID rimosse | `787` |
| Righe `Infortunio in itinere` rimosse | `269` |
| Righe senza data evento rimosse | `0` |
| Colonne completamente vuote rimosse | `7` |
| Colonne costanti rimosse | `12` |
| Cap giorni persi p99 | `247.3` |
| Outlier giorni persi flaggati | `4` |

Le colonne completamente vuote rimosse sono:

| Colonna rimossa |
|---|
| `Categoria_COVID_argomento` |
| `Codice Azione Preventiva` |
| `Codice Progetto HSE` |
| `Spesa (€)` |
| `Data chiusura Verifica Efficacia` |
| `Inabilità permanente` |
| `Grado inabilità (%)` |

Le colonne costanti rimosse sono:

| Colonna rimossa |
|---|
| `Sede Infortuni zero` |
| `V/F_est_in corso` |
| `Tipologia_NORM` |
| `Controllo Verifica Efficacia` |
| `Punto norma` |
| `Contratto atipico` |
| `Medicato in azienda` |
| `Ripreso il Lavoro` |
| `Mandato a Casa` |
| `Avviato all'ospedale` |
| `Morte` |
| `Richiesto agg. DVR` |

## 4. Normalizzazione Tipologie Evento

La variabile `tipologia_raw` è stata normalizzata in `tipologia_canonica`.

| Tipologia canonica | Righe dopo cleaning |
|---|---:|
| `SMAT Audit` | `22798` |
| `Primo soccorso` | `581` |
| `Infortunio con certificato` | `311` |
| `Incidente senza infortunio` | `258` |
| `Malattia Professionale` | `78` |

Gli accorpamenti principali sono stati:

| Raw / concetto | Canonico |
|---|---|
| `Non Conformità_SMAT Audit` | `SMAT Audit` |
| `Azione insicura` | `SMAT Audit` |
| `Condizione Insicura` | `SMAT Audit` |
| `BBS_Annotazioni_Strutturali` | `SMAT Audit` |
| `Incidente senza infortunio_no persone` | `Incidente senza infortunio` |
| `Malattia Professionale_*` | `Malattia Professionale` |

Decisione presa sugli SMAT:

- Gli `SMAT Audit` non sono target del modello.
- Gli `SMAT Audit` sono usati come feature storiche e contesto.
- Questo perché vogliamo usare segnali deboli e non conformità per anticipare eventi più pesanti, non predire altri SMAT.

Flag creati sugli eventi:

| Flag | Significato |
|---|---|
| `is_smat_audit` | evento di tipo SMAT Audit o assimilato |
| `is_first_aid` | primo soccorso |
| `is_certified_injury` | infortunio con certificato |
| `is_incident_without_injury` | incidente senza infortunio |
| `is_occupational_disease` | malattia professionale |
| `is_injury_like` | primo soccorso o infortunio con certificato |

## 5. Distribuzione Eventi per Problem Code

| Problem code | Famiglia | Righe |
|---|---|---:|
| `A` | Ambiente di lavoro | `7647` |
| `D` | Impianti e attrezzature | `4954` |
| `H` | Azioni e condizioni insicure | `4674` |
| `C` | DPI | `2471` |
| `F` | 5S / Ordine / Pulizia | `2241` |
| `B` | Formazione / Informazione / Addestramento | `578` |
| `E` | Regolamento interno | `503` |
| `G` | Ambiente | `371` |
| `Z` | Comportamenti sicuri | `239` |
| `UNKNOWN` | Non classificato | `204` |
| `I` | Idoneità sanitaria | `116` |
| `L` | Ditte esterne | `28` |

Questa distribuzione conferma che il file Eventi è dominato da non conformità, SMAT e segnalazioni. Gli eventi infortunistici veri sono molto meno numerosi.

## 6. Distribuzione Eventi per Area

| Area canonica | Righe evento |
|---|---:|
| `Montaggio e Finitura` | `7313` |
| `Stamperia Plastica` | `4364` |
| `Verniciatura` | `2653` |
| `Galvanica/Pulitura` | `2425` |
| `Manutenzione` | `1826` |
| `Stamperia Metallo` | `1706` |
| `Logistica e Magazzino` | `1600` |
| `Saldatura` | `1430` |
| `Aree Comuni` | `439` |
| `Uffici` | `88` |
| `Officina` | `73` |
| `Ricambi` | `59` |
| `Prototipia` | `19` |
| `Sample` | `9` |
| `Avanserie` | `7` |
| `Area mancante / non mappata` | `7` |
| `Aree tecniche/Tetti` | `6` |
| `Tutta la sede` | `1` |
| `Automation` | `1` |

Le aree `Galvanica` e `Pulitura` sono state unite in `Galvanica/Pulitura`, come richiesto.

## 7. Cleaning File Osservazioni / BBS

Sul file BBS sono state applicate queste regole:

| Operazione | Risultato |
|---|---:|
| Righe input | `608507` |
| Righe COVID rimosse | `56854` |
| Righe finali utili | `551653` |
| Gruppi raw | `48` |
| Attività raw totali | `164` |
| Attività raw tenute | `115` |
| Attività clean finali | `81` |
| Comportamenti raw | `1188` |
| Comportamenti clean | `978` |
| Comportamenti canonici v2 | `899` |
| Righe comportamento osservabile reale | `545130` |

Distribuzione dei tipi comportamento:

| Tipo comportamento | Righe |
|---|---:|
| `behavior` | `545130` |
| `message` | `4674` |
| `prompt_open_signal` | `997` |
| `prompt_near_miss` | `852` |

Decisione presa:

- Solo `behavior` entra nel ranking dei comportamenti osservabili.
- `message`, `prompt_open_signal` e `prompt_near_miss` sono tenuti come informazione, ma non devono essere letti come comportamenti unsafe reali.

## 8. Normalizzazione Gruppi e Aree BBS

Il file BBS ha `48` gruppi raw. Questi gruppi sono stati mappati verso `area_canonica`, cercando coerenza con `area_reparto` del file Eventi.

Esempi:

| Gruppo raw | Area canonica | Row count |
|---|---|---:|
| `Galvanica - Linee Galvaniche` | `Galvanica/Pulitura` | `37289` |
| `Galvanica - Pre e Post Galvanica` | `Galvanica/Pulitura` | `19082` |
| `Pulitura C - Pulitura e Buratti Japan` | `Galvanica/Pulitura` | `16931` |
| `Logistica` | `Logistica e Magazzino` | `30859` |
| `Manutenzione Area Nord` | `Manutenzione` | `15287` |
| `Finitura - Taglio Lenti e Macchine` | `Montaggio e Finitura` | `32985` |
| `Finitura - Premontaggio` | `Montaggio e Finitura` | `11906` |

Nota su `row_count` in `group_area_mapping.csv`:

- È il numero di righe osservazione BBS associate a quel `gruppo_raw` dopo il cleaning applicato alla sorgente osservazioni.
- Non è un numero di eventi HSE.
- Non è un numero di persone.
- Serve a capire quanto pesa ogni gruppo raw nella mappatura verso l'area canonica.

## 9. Tassonomia Attività

Le attività raw sono state normalizzate in `attivita_clean` e poi raggruppate in `attivita_famiglia`.

Numeriche principali:

| Misura | Valore |
|---|---:|
| Attività raw totali | `164` |
| Attività raw tenute dopo esclusione COVID | `115` |
| Attività clean finali | `81` |
| Famiglie attività nel dataset mensile BBS | `18` |

Esempi di attività normalizzate:

| Attività clean | Famiglia | Righe tenute | Varianti raw |
|---|---|---:|---:|
| `DPI` | `DPI e Abbigliamento` | `86318` | `16` |
| `Presidio sicurezza, evacuazione ed emergenza` | `Emergenza / Evacuazione` | `33759` | `2` |
| `ATTENZIONE E BUONE PRASSI` | `Comportamenti Generali e Buone Prassi` | `23205` | `1` |
| `ABBIGLIAMENTO DA LAVORO` | `DPI e Abbigliamento` | `17941` | `1` |
| `Tutte le attività` | `Attività Generiche` | `12625` | `2` |

Decisioni prese:

- Le attività COVID sono state escluse.
- Le attività troppo generiche sono mantenute nella base ma filtrate nei deepdive operativi quando rischiano di sporcare la classifica.
- `Incidenti sfiorati` è stato trattato come concetto separato, non come attività produttiva ordinaria.

## 10. Tassonomia Comportamenti v2

È stata integrata la tassonomia manuale v2 fornita nel file:

```text
artifacts/behavior_taxonomy_pipeline_v2.csv
```

Numeriche della tassonomia:

| Misura | Valore |
|---|---:|
| Righe input tassonomia v2 | `987` |
| Lookup effettivo usato dalla pipeline | `979` |
| Duplicati clean/type rimossi | `8` |
| Comportamenti canonici univoci | `899` |
| Famiglie comportamento v2 osservate | `11` |
| Sottofamiglie comportamento v2 osservate | `63` |

La nuova gerarchia è:

```text
comportamento_clean
-> comportamento_canonico
-> canonical_behavior_id
-> comportamento_famiglia
-> comportamento_sottofamiglia_v2
-> meccanismo_rischio_v2
-> presidio_v2
-> severity_rank_v2
```

Campi principali aggiunti:

| Campo | Uso |
|---|---|
| `comportamento_canonico` | Deduplica varianti testuali simili |
| `canonical_behavior_id` | ID stabile non dipendente dal testo |
| `comportamento_famiglia` | Famiglia HSE v2 compatibile con la pipeline |
| `comportamento_sottofamiglia_v2` | Driver più puntuale per deepdive |
| `meccanismo_rischio_v2` | Meccanismo di danno potenziale |
| `presidio_v2` | Controllo operativo atteso |
| `severity_rank_v2` | Ranking HSE da 1 a 5 |
| `taxonomy_confidence` | Confidenza classificazione |
| `merge_confidence` | Confidenza accorpamento |
| `review_flag` | Flag per review HSE |

La scala di severità è:

| Rank | Significato |
|---:|---|
| `1` | rischio molto alto |
| `2` | rischio alto |
| `3` | rischio medio |
| `4` | rischio basso |
| `5` | rischio molto basso |

Distribuzione righe comportamento osservabile per severità:

| Severity rank | Righe |
|---:|---:|
| `1` | `134780` |
| `2` | `201164` |
| `3` | `151296` |
| `4` | `57890` |
| `5` | `0` |

## 11. Famiglie Comportamento v2

Le famiglie comportamento osservabili sono `11`, le sottofamiglie osservabili sono `63`.

Queste numeriche sono calcolate solo sulle righe con:

```text
comportamento_tipo = behavior
```

Quindi escludono:

- messaggi;
- prompt near miss;
- prompt aperti tipo altri comportamenti/condizioni.

File di dettaglio generati:

| Artifact | Contenuto |
|---|---|
| `behavior_family_numeriche.csv` | Numeriche complete per famiglia comportamento |
| `behavior_subfamily_numeriche.csv` | Numeriche complete per sottofamiglia comportamento |
| `behavior_family_subfamily_numeriche.md` | Versione leggibile con famiglie e tutte le sottofamiglie |

Numeriche globali:

| Misura | Valore |
|---|---:|
| Righe comportamento osservabile | `545130` |
| Famiglie comportamento | `11` |
| Sottofamiglie comportamento | `63` |
| Comportamenti clean osservabili globali | `971` |
| Comportamenti canonici osservabili globali | `892` |

Numeriche per famiglia:

| Famiglia comportamento | Righe | Sottofamiglie | Clean | Canonici | Unsafe | Unsafe rate | IR mediana |
|---|---:|---:|---:|---:|---:|---:|---:|
| `DPI / Abbigliamento / Protezione personale` | `117238` | `12` | `126` | `104` | `8856` | `2.79%` | `2` |
| `Ordine / Pulizia / Housekeeping` | `84909` | `3` | `45` | `45` | `6262` | `3.76%` | `4` |
| `Mezzi / Carrelli / Transpallet / Viabilità` | `82621` | `7` | `166` | `128` | `4141` | `2.19%` | `3` |
| `Elettrico / Emergenza / Vie di fuga` | `56677` | `6` | `21` | `18` | `2407` | `3.32%` | `1` |
| `Attrezzature / Utensili / Dispositivi di presa` | `52945` | `7` | `133` | `131` | `2330` | `1.86%` | `2` |
| `Ergonomia / Movimentazione manuale` | `42576` | `5` | `78` | `77` | `2948` | `2.58%` | `3` |
| `Chimici / Aspirazione / Sostanze pericolose` | `32520` | `5` | `93` | `85` | `1276` | `2.62%` | `1` |
| `Stoccaggio / Materiali / Layout` | `32391` | `3` | `59` | `57` | `1589` | `2.40%` | `3` |
| `Macchine / Organi mobili / Protezioni` | `30750` | `7` | `178` | `176` | `1238` | `1.96%` | `1` |
| `Accessi / Scale / Lavori in quota` | `6578` | `5` | `43` | `43` | `210` | `1.49%` | `1` |
| `Interferenze / Coordinamento` | `5925` | `3` | `29` | `28` | `292` | `2.48%` | `2` |

Sottofamiglie più presenti:

| Sottofamiglia | Famiglia | Righe | Canonici | Unsafe | Unsafe rate | IR mediana |
|---|---|---:|---:|---:|---:|---:|
| `Postazione / area ordinata e pulita` | `Ordine / Pulizia / Housekeeping` | `57890` | `32` | `4151` | `3.00%` | `4` |
| `Spostamenti pedonali / attenzione / percorsi` | `Mezzi / Carrelli / Transpallet / Viabilità` | `49890` | `25` | `2824` | `2.03%` | `3` |
| `DPI piedi / calzature` | `DPI / Abbigliamento / Protezione personale` | `28440` | `4` | `373` | `0.42%` | `2` |
| `DPI mani / guanti` | `DPI / Abbigliamento / Protezione personale` | `24982` | `29` | `1940` | `2.88%` | `2` |
| `Macchine / attrezzaggio / processo sicuro` | `Macchine / Organi mobili / Protezioni` | `22661` | `129` | `966` | `2.02%` | `1` |
| `DPI occhi / viso` | `DPI / Abbigliamento / Protezione personale` | `22002` | `9` | `2183` | `3.92%` | `2` |
| `Vie di fuga / porte tagliafuoco` | `Elettrico / Emergenza / Vie di fuga` | `19209` | `5` | `984` | `3.69%` | `1` |
| `Pavimenti / asciutto / segnalazione bagnato` | `Ordine / Pulizia / Housekeeping` | `17782` | `4` | `675` | `3.76%` | `3` |
| `Quadri elettrici / cavi / accessibilità` | `Elettrico / Emergenza / Vie di fuga` | `17284` | `2` | `683` | `3.74%` | `1` |
| `Ganci / telai / morsetti / golfari` | `Attrezzature / Utensili / Dispositivi di presa` | `16307` | `47` | `748` | `1.64%` | `2` |
| `Aspirazione / cappe / ventilazione` | `Chimici / Aspirazione / Sostanze pericolose` | `15152` | `27` | `625` | `2.35%` | `1` |
| `Impilamento / stabilità / perimetro` | `Stoccaggio / Materiali / Layout` | `14164` | `16` | `590` | `2.94%` | `2` |
| `Presidi antincendio / primo intervento` | `Elettrico / Emergenza / Vie di fuga` | `13897` | `3` | `540` | `3.89%` | `1` |
| `Parcheggio / posizionamento mezzi e contenitori` | `Mezzi / Carrelli / Transpallet / Viabilità` | `13584` | `13` | `456` | `3.27%` | `3` |
| `Abbigliamento / capelli / oggetti pendenti` | `DPI / Abbigliamento / Protezione personale` | `13391` | `6` | `565` | `1.65%` | `2` |

Nota interpretativa:

- `row_count` misura quante righe BBS osservabili appartengono alla famiglia/sottofamiglia.
- `Clean` misura quante etichette `comportamento_clean` diverse sono presenti.
- `Canonici` misura quanti `canonical_behavior_id` diversi restano dopo deduplicazione v2.
- `Unsafe` è la somma di `comportamenti_non_sicuri`.
- `Unsafe rate` è `unsafe_total / (safe_total + unsafe_total)`.
- `IR mediana` è la mediana di `severity_rank_v2`, dove `1` è il rischio più alto e `5` il più basso.

## 12. Uso della Descrizione Evento

Il campo `descrizione_clean` del file Eventi è stato usato su tre livelli.

Livello 1: semantica latente.

| Elemento | Valore |
|---|---:|
| Metodo | TF-IDF + TruncatedSVD |
| Max feature TF-IDF | `600` |
| N-grammi | `1-2` |
| Min df | `5` |
| Max df | `0.85` |
| Componenti semantiche | `5` |
| Righe termini semantici prodotte | `120` |
| Righe area-mese con componenti semantiche | `1181` |

Livello 2: topic interpretabili.

| Elemento | Valore |
|---|---:|
| Topic descrizione finali | `15` |
| Righe topic area-mese | `1146` |
| Righe topic x problem family | `167` |

Topic più frequenti:

| Topic | Eventi taggati | Eventi avversi | SMAT |
|---|---:|---:|---:|
| `Materiali / stoccaggio` | `4285` | `185` | `4096` |
| `Macchine / impianti / attrezzature` | `3755` | `348` | `3407` |
| `Taglio / urto / schiacciamento` | `2940` | `594` | `2331` |
| `Pavimenti / ordine / pulizia` | `2621` | `90` | `2531` |
| `Distrazione / comportamento` | `2334` | `132` | `2200` |
| `Vie di fuga / emergenza` | `1963` | `19` | `1944` |
| `Chimici / lavaggi / aspirazione` | `1939` | `72` | `1866` |
| `Cadute / scivolamenti` | `1732` | `283` | `1449` |

Livello 3: recupero casi storici simili.

| Misura | Valore |
|---|---:|
| Query area generate | `8` |
| Match storici totali | `24` |
| Aree con match | `8` |
| Casi simili per area | `3` |

Decisione presa:

- Il testo è molto utile per interpretabilità, topic e casi simili.
- Il testo non va usato da solo come predittore causale.
- I topic descrizione sono entrati anche nelle feature del modello area-mese.

## 13. Costruzione del Panel Area-Mese

Il panel finale è costruito come griglia completa:

```text
18 aree x 90 mesi = 1620 righe area-mese
```

Numeriche panel:

| Misura | Valore |
|---|---:|
| Righe panel finale | `1620` |
| Aree panel | `18` |
| Mesi panel | `90` |
| Periodo panel | `2018-12-01` -> `2026-05-01` |
| Righe BBS area-mese osservate | `543` |
| Righe con target disponibile | `1584` |
| Righe con copertura osservativa BBS | `543` |
| Righe modellabili target disponibile + BBS | `527` |

Aree nel panel:

| Area |
|---|
| `Aree Comuni` |
| `Aree tecniche/Tetti` |
| `Automation` |
| `Avanserie` |
| `Galvanica/Pulitura` |
| `Logistica e Magazzino` |
| `Manutenzione` |
| `Montaggio e Finitura` |
| `Officina` |
| `Prototipia` |
| `Ricambi` |
| `Saldatura` |
| `Sample` |
| `Stamperia Metallo` |
| `Stamperia Plastica` |
| `Tutta la sede` |
| `Uffici` |
| `Verniciatura` |

Tassi target:

| Base calcolo | Target adverse positivo | Target injury positivo |
|---|---:|---:|
| Panel completo | `0.259` | `0.226` |
| Solo righe modellabili con copertura BBS | `0.510` | `0.444` |

La differenza tra i due tassi è importante: il modello viene addestrato sulle righe dove esiste copertura osservativa BBS, quindi il tasso positivo reale del training set è più alto del tasso medio dell'intera griglia area-mese.

## 14. Feature del Modello

Feature BBS aggregate:

| Feature | Significato |
|---|---|
| `obs_rows` | righe osservazione BBS |
| `obs_safe_total` | totale comportamenti sicuri |
| `obs_unsafe_total` | totale comportamenti non sicuri |
| `obs_rows_with_unsafe` | righe con almeno un unsafe |
| `obs_unique_observations` | osservazioni uniche |
| `obs_unsafe_rate` | unsafe / totale comportamenti |
| `obs_unsafe_row_rate` | righe unsafe / righe osservate |
| `obs_family_*` | metriche per famiglia attività |

Feature eventi aggregate:

| Feature | Significato |
|---|---|
| `evt_total_rows` | eventi totali area-mese |
| `evt_smat_audit_count` | SMAT Audit e assimilati |
| `evt_first_aid_count` | primi soccorsi |
| `evt_certified_injury_count` | infortuni con certificato |
| `evt_incident_without_injury_count` | incidenti senza infortunio |
| `evt_occupational_disease_count` | malattie professionali |
| `evt_injury_like_count` | primi soccorsi + certificati |
| `evt_days_lost_sum` | somma giorni persi capped |
| `evt_days_lost_avg` | media giorni persi capped |
| `evt_days_lost_p95` | p95 giorni persi capped |
| `evt_problem_*` | conteggi per problem code |
| `evt_semantic_component_*` | componenti semantiche da descrizione |
| `evt_desc_topic_*` | topic descrizione interpretabili |

Feature temporali:

| Feature | Significato |
|---|---|
| `*_lag1` | valore del mese precedente |
| `*_roll3_mean` | media mobile sui 3 mesi precedenti |
| `months_since_last_injury` | mesi dall'ultimo injury-like |
| `obs_to_event_ratio` | rapporto eventi / osservazioni |
| `injury_flag_current_month` | presenza injury-like nel mese corrente |

Decisione presa:

- Le feature usano informazione disponibile fino al mese corrente.
- Il target guarda al mese successivo.
- Questo evita leakage temporale.

## 15. Target del Modello

Target principale:

```text
target_adverse_next_month = 1
se nel mese successivo, nella stessa area, c'è almeno un:
- Primo soccorso
- Infortunio con certificato
- Incidente senza infortunio
```

Target secondario:

```text
target_injury_next_month = 1
se nel mese successivo, nella stessa area, c'è almeno un:
- Primo soccorso
- Infortunio con certificato
```

Decisioni prese:

- `SMAT Audit` non è target.
- `SMAT Audit` è feature storica.
- `Malattia Professionale` non entra nel target operativo principale perché ha dinamiche diverse e meno immediate.
- `Infortunio in itinere` è escluso perché non rappresenta rischio operativo interno.
- `COVID-19` è escluso perché non coerente con il rischio operativo industriale che vogliamo modellare.

## 16. Modello Baseline Area-Mese

Modelli candidati:

| Modello | Note |
|---|---|
| `logistic_regression` | modello lineare, class_weight balanced, scaling |
| `random_forest` | modello non lineare, 500 alberi, `min_samples_leaf=4`, `class_weight=balanced_subsample` |

Split holdout temporale:

| Split | Periodo | Righe |
|---|---|---:|
| Train | `2018-12-01` -> `2024-03-01` | `340` |
| Validation | `2024-04-01` -> `2025-03-01` | `91` |
| Test | `2025-04-01` -> `2026-03-01` | `96` |

Tasso positivo per split:

| Split | Positive rate |
|---|---:|
| Train | `0.479` |
| Validation | `0.604` |
| Test | `0.531` |

Risultati validation baseline:

| Modello | PR-AUC | ROC-AUC | Brier |
|---|---:|---:|---:|
| `logistic_regression` | `0.711` | `0.614` | `0.368` |
| `random_forest` | `0.793` | `0.685` | `0.216` |

Risultati test baseline:

| Modello selezionato | Feature | PR-AUC | ROC-AUC | Brier |
|---|---:|---:|---:|---:|
| `random_forest` | `417` | `0.696` | `0.676` | `0.227` |

Decisione presa:

- La random forest è stata scelta perché migliore in validation.
- La lettura corretta è ranking/prioritizzazione, non probabilità puntuale perfetta.

## 17. Walk-Forward Backtest Baseline

Il walk-forward simula l'uso reale:

- per ogni mese predicibile si usa solo lo storico precedente;
- il modello viene selezionato su una validation window precedente;
- si predice out-of-sample il mese successivo.

Configurazione:

| Parametro | Valore |
|---|---:|
| Min history months | `18` |
| Validation window months | `12` |
| Predizioni area-mese | `440` |
| Mesi backtest | `65` |
| Event month range | `2020-11-01` -> `2026-03-01` |
| Target month range | `2020-12-01` -> `2026-04-01` |

Metriche baseline walk-forward:

| Metrica | Valore |
|---|---:|
| PR-AUC | `0.767` |
| ROC-AUC | `0.743` |
| Brier | `0.208` |
| Top-1 hit rate | `0.831` |
| Top-3 precision media | `0.744` |
| Top-3 recall media | `0.679` |
| Aree positive medie per mese | `3.554` |

Selezione modelli nel walk-forward:

| Modello | Mesi selezionati |
|---|---:|
| `random_forest` | `58` |
| `logistic_regression` | `7` |

Interpretazione business:

- Nel `83.1%` dei mesi la prima area proposta è realmente positiva nel mese target.
- Nelle prime 3 aree, in media il `74.4%` risultano davvero positive.
- Le prime 3 aree intercettano in media il `67.9%` delle aree positive del mese.

## 18. Esperimento Behavior Weighted Data-Driven

Obiettivo:

- Usare le famiglie comportamento BBS non solo come conteggi grezzi, ma pesandole in base alla loro associazione storica con il rischio futuro.

Formula:

```text
base_rate_t = media storica target fino a t-1
feature_rate_t = media target nei mesi/aree dove la feature era > 0 fino a t-1
raw_lift_t = feature_rate_t / base_rate_t
reliability_t = exposure_rows / (exposure_rows + 12)
risk_weight_t = clip(1 + reliability_t * (raw_lift_t - 1), 0.7, 2.0)
```

Numeriche:

| Misura | Valore |
|---|---:|
| Righe area-mese comportamento famiglia | `526` |
| Righe pesi storici famiglia | `913` |
| Panel finale | `1620` |
| Feature modello | `489` |

Metriche:

| Valutazione | PR-AUC | ROC-AUC | Brier | Top-1 | Top-3 precision | Top-3 recall |
|---|---:|---:|---:|---:|---:|---:|
| Holdout test | `0.696` | `0.677` | `0.227` | n.d. | n.d. | n.d. |
| Walk-forward | `0.767` | `0.746` | `0.207` | `0.877` | `0.769` | `0.710` |

Decisione presa:

- Questo ramo migliora le metriche business rispetto alla baseline.
- È un buon candidato come motore di scoring se vogliamo massimizzare performance e semplicità.

## 19. Esperimento Behavior Subfamily Weighted

Obiettivo:

- Provare un livello più granulare basato sulle `comportamento_sottofamiglia_v2`.
- Verificare se la tassonomia v2 più precisa aumenta la capacità predittiva.

Numeriche:

| Misura | Valore |
|---|---:|
| Sottofamiglie comportamento osservate | `63` |
| Righe area-mese sottofamiglia | `526` |
| Righe pesi storici sottofamiglia | `5229` |
| Panel finale | `1620` |
| Feature modello | `801` |

Metriche:

| Valutazione | PR-AUC | ROC-AUC | Brier | Top-1 | Top-3 precision | Top-3 recall |
|---|---:|---:|---:|---:|---:|---:|
| Holdout test | `0.705` | `0.693` | `0.223` | n.d. | n.d. | n.d. |
| Walk-forward | `0.756` | `0.741` | `0.210` | `0.892` | `0.769` | `0.704` |

Decisione presa:

- Il ramo sottofamiglia migliora l'holdout test.
- Nel walk-forward perde PR-AUC rispetto a baseline e behavior weighted famiglia.
- Ha molte più feature (`801`) e quindi più rischio di rumore/overfitting.
- È molto utile per interpretabilità e deepdive.
- Non lo promuoverei oggi a motore principale di scoring puro.

## 20. Esperimento Expert IR-Like

Obiettivo:

- Integrare un ranking esperto HSE simile alla logica IR.
- Dare più peso a famiglie comportamento intrinsecamente più severe, ad esempio macchine, elettrico, chimici, accessi e DPI.

File:

```text
artifacts/behavior_family_expert_risk_rank.csv
```

Scala:

| Rank | Significato |
|---:|---|
| `1` | rischio massimo |
| `5` | rischio minimo |

Famiglie mappate:

| Famiglia comportamento | Risk rank |
|---|---:|
| `Accessi / Scale / Lavori in quota` | `1` |
| `Chimici / Aspirazione / Sostanze pericolose` | `1` |
| `Elettrico / Emergenza / Vie di fuga` | `1` |
| `Macchine / Organi mobili / Protezioni` | `1` |
| `Attrezzature / Utensili / Dispositivi di presa` | `2` |
| `DPI / Abbigliamento / Protezione personale` | `2` |
| `Ergonomia / Movimentazione manuale` | `3` |
| `Interferenze / Coordinamento` | `3` |
| `Mezzi / Carrelli / Transpallet / Viabilità` | `3` |
| `Stoccaggio / Materiali / Layout` | `3` |
| `Ordine / Pulizia / Housekeeping` | `4` |

Metriche:

| Valutazione | PR-AUC | ROC-AUC | Brier | Top-1 | Top-3 precision | Top-3 recall |
|---|---:|---:|---:|---:|---:|---:|
| Holdout test | `0.701` | `0.678` | `0.228` | n.d. | n.d. | n.d. |
| Walk-forward | `0.765` | `0.745` | `0.208` | `0.892` | `0.774` | `0.711` |

Decisione presa:

- Non batte sempre il ramo data-driven in PR-AUC.
- È molto forte come overlay HSE.
- Ha il miglior equilibrio operativo tra interpretabilità e metriche business.
- È utile nel pack perché spiega perché un comportamento è prioritario anche se non è il più frequente.

## 21. Confronto Finale Varianti Modello

| Variante | Modello selezionato | Feature | Holdout PR-AUC | Holdout ROC-AUC | Holdout Brier | Walk PR-AUC | Walk ROC-AUC | Walk Brier | Top-1 | Top-3 precision | Top-3 recall |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `baseline` | `random_forest` | `417` | `0.696` | `0.676` | `0.227` | `0.767` | `0.743` | `0.208` | `0.831` | `0.744` | `0.679` |
| `behavior_weighted_experiment` | `random_forest` | `489` | `0.696` | `0.677` | `0.227` | `0.767` | `0.746` | `0.207` | `0.877` | `0.769` | `0.710` |
| `behavior_subfamily_weighted_experiment` | `random_forest` | `801` | `0.705` | `0.693` | `0.223` | `0.756` | `0.741` | `0.210` | `0.892` | `0.769` | `0.704` |
| `behavior_expert_weighted_experiment` | `random_forest` | `465` | `0.701` | `0.678` | `0.228` | `0.765` | `0.745` | `0.208` | `0.892` | `0.774` | `0.711` |

Decisione complessiva:

- Per performance pura stabile, il ramo `behavior_weighted_experiment` è ancora molto competitivo.
- Per governance HSE e ranking operativo leggibile, il ramo `behavior_expert_weighted_experiment` è il più convincente.
- Per deepdive e spiegabilità puntuale, la sottofamiglia v2 è molto utile.
- Il ramo `behavior_subfamily_weighted_experiment` non va scartato, ma oggi lo terrei come esperimento e layer diagnostico, non come default scoring engine.

## 22. Ultimo Scoring Aree

Ultimo scoring baseline:

| Area | Event month | Target month | Score rischio |
|---|---|---|---:|
| `Stamperia Plastica` | `2026-04-01` | `2026-05-01` | `0.867` |
| `Montaggio e Finitura` | `2026-04-01` | `2026-05-01` | `0.706` |
| `Stamperia Metallo` | `2026-04-01` | `2026-05-01` | `0.620` |
| `Galvanica/Pulitura` | `2026-04-01` | `2026-05-01` | `0.510` |
| `Saldatura` | `2026-04-01` | `2026-05-01` | `0.474` |
| `Verniciatura` | `2026-04-01` | `2026-05-01` | `0.432` |
| `Logistica e Magazzino` | `2026-04-01` | `2026-05-01` | `0.314` |
| `Manutenzione` | `2026-04-01` | `2026-05-01` | `0.193` |

Ultimo scoring sottofamiglia weighted:

| Area | Event month | Target month | Score rischio |
|---|---|---|---:|
| `Stamperia Plastica` | `2026-04-01` | `2026-05-01` | `0.828` |
| `Montaggio e Finitura` | `2026-04-01` | `2026-05-01` | `0.717` |
| `Stamperia Metallo` | `2026-04-01` | `2026-05-01` | `0.587` |
| `Galvanica/Pulitura` | `2026-04-01` | `2026-05-01` | `0.498` |
| `Verniciatura` | `2026-04-01` | `2026-05-01` | `0.461` |
| `Saldatura` | `2026-04-01` | `2026-05-01` | `0.448` |
| `Logistica e Magazzino` | `2026-04-01` | `2026-05-01` | `0.295` |
| `Manutenzione` | `2026-04-01` | `2026-05-01` | `0.233` |

## 23. Deepdive Operativo

Il deepdive è stato costruito per rispondere alla domanda:

```text
Una volta che l'area è ad alto rischio, dove guardiamo?
```

Finestra deepdive più recente:

| Misura | Valore |
|---|---:|
| Analysis window start | `2025-05-01` |
| Analysis window end | `2026-04-01` |
| Aree nel deepdive | `8` |
| Righe famiglia attività | `82` |
| Righe attività | `154` |
| Righe famiglia comportamento | `77` |
| Righe sottofamiglia comportamento | `278` |
| Righe comportamento focus | `737` |

Formula ranking diagnostico grezzo:

```text
priority_score_raw =
    unsafe_rate
    * log1p(obs_rows)
    * sqrt(lift_vs_area)
    * sqrt(lift_vs_company_same_item)
    * (1 + positive_trend)
```

Il ranking grezzo premia:

- unsafe rate alto;
- volume osservato sufficiente;
- peso sul totale unsafe dell'area;
- anomalia rispetto alla stessa area;
- anomalia rispetto al benchmark plant;
- trend recente in peggioramento.

## 24. Correzione Severity-Aware del Deepdive

È emerso un problema: alcune sottofamiglie a bassa severità, ad esempio `Rifiuti / trucioli / sfridi / contenitori`, potevano entrare in top 3 solo perché avevano unsafe rate e volume alti.

Decisione presa:

- Non cancellare questi segnali.
- Non trattarli come equivalenti a vie di fuga, macchine, elettrico, chimici o DPI critici.
- Salvare sia lo score grezzo sia lo score corretto per severità.

Formula finale:

```text
priority_score = priority_score_raw * severity_weight
```

Pesi applicati:

| Severity rank | Weight |
|---:|---:|
| `1` | `1.50` |
| `2` | `1.10` |
| `3` | `0.35` |
| `4` | `0.12` |
| `5` | `0.05` |

Regola di severità effettiva:

- Se la sottofamiglia è IR 1-2, resta guidata dalla sottofamiglia.
- Se la sottofamiglia è IR 3-5, eredita anche il profilo della famiglia madre.
- Questo evita che item di housekeeping appaiano come più prioritari di rischi critici solo per effetto volume.

Esempio su `Stamperia Plastica`:

| Rank | Sottofamiglia | Unsafe rate | IR | Score raw | Score finale |
|---:|---|---:|---:|---:|---:|
| `1` | `Vie di fuga / porte tagliafuoco` | `7.9%` | `1` | `1.403` | `2.105` |
| `2` | `DPI occhi / viso` | `7.2%` | `2` | `1.296` | `1.426` |
| `3` | `DPI udito` | `6.1%` | `2` | `0.732` | `0.805` |
| `4` | `Rifiuti / trucioli / sfridi / contenitori` | `23.5%` | `4` | `5.945` | `0.713` |
| `5` | `Forni / essiccatori / parti calde` | `4.9%` | `1` | `0.368` | `0.553` |
| `6` | `Macchine / attrezzaggio / processo sicuro` | `3.2%` | `1` | `0.328` | `0.492` |

Interpretazione:

- Rifiuti/sfridi non sparisce.
- Il suo score grezzo resta visibile.
- Il ranking operativo lo declassa perché IR 4.
- Questo rende il deepdive più coerente con la priorità HSE.

## 25. Investigation Pack

L'investigation pack aggrega per area:

- score baseline;
- score expert;
- unsafe rate 12 mesi;
- volumi BBS;
- eventi ultimi 12 mesi;
- SMAT, primi soccorsi, certificati, incidenti senza infortunio;
- top problem code;
- top topic descrizione;
- top famiglie attività;
- top attività;
- top famiglie comportamento expert;
- top sottofamiglie comportamento severity-aware;
- top comportamenti canonici;
- ipotesi investigativa;
- checklist campo;
- casi storici simili.

Numeriche:

| Misura | Valore |
|---|---:|
| Righe pack | `8` |
| Aree nel report markdown | `5` |
| Analysis window start | `2025-05-01` |
| Analysis window end | `2026-04-01` |
| Query similarity | `8` |
| Match storici | `24` |
| Aree con match | `8` |
| Casi simili per area | `3` |

Esempi top sottofamiglie nel pack:

| Area | Top sottofamiglie |
|---|---|
| `Stamperia Plastica` | `Vie di fuga / porte tagliafuoco`; `DPI occhi / viso`; `DPI udito` |
| `Montaggio e Finitura` | `Impilamento / stabilità / perimetro`; `Forni / essiccatori / parti calde`; `Utensili manuali / taglio / aria compressa` |
| `Stamperia Metallo` | `Interazione pedoni-mezzi`; `DPI udito`; `DPI mani / guanti` |
| `Galvanica/Pulitura` | `DPI occhi / viso`; `Stoccaggio infiammabili`; `Contenitori / etichettatura / chiusura` |
| `Saldatura` | `DPI mani / chimico`; `Indumenti protettivi / chimico-processo`; `Rifiuti / trucioli / sfridi / contenitori` |
| `Verniciatura` | `Trasporto / percorsi / stoccaggio operativo`; `Taglio / lame / reggette`; `DPI vie respiratorie` |
| `Logistica e Magazzino` | `Rifiuti / trucioli / sfridi / contenitori`; `Accessi / lavori speciali`; `Utensili manuali / taglio / aria compressa` |
| `Manutenzione` | `PLE / piattaforme elevabili`; `DPI mani / chimico`; `Uso carrelli/transpallet/gabbie` |

Nota importante:

- In `Logistica e Magazzino`, rifiuti resta alto perché l'unsafe rate è molto forte.
- Però compare con IR 4, quindi va interpretato come segnale di housekeeping, non come rischio critico equivalente a accessi, chimici o macchine.

## 26. Secondo Stadio Injury: Causa e Parte del Corpo

È stato testato un secondo modello per predire dettagli injury-like.

Dataset:

| Misura | Valore |
|---|---:|
| Righe injury-like | `464` |
| Feature | `433` |
| Train range | `2019-01-01` -> `2024-04-01` |
| Validation range | `2024-05-01` -> `2025-04-01` |
| Test range | `2025-05-01` -> `2026-04-01` |

Distribuzione macro-causa:

| Macro-causa | Righe |
|---|---:|
| `Procedure / attenzione` | `132` |
| `Altro / Non definita` | `125` |
| `Cadute / urti` | `119` |
| `Movimenti / postura` | `63` |
| `Manipolazione / posizionamento` | `25` |

Distribuzione macro-parte-del-corpo:

| Macro parte corpo | Righe |
|---|---:|
| `Mani e dita` | `211` |
| `Arto inferiore` | `93` |
| `Testa / occhi / collo` | `73` |
| `Arto superiore` | `47` |
| `Tronco / schiena` | `24` |
| `Altro / Non definita` | `16` |

Risultati test:

| Target | Modello selezionato | Accuracy | Balanced accuracy | Macro-F1 | Top-3 accuracy |
|---|---|---:|---:|---:|---:|
| `tipologia_causa_macro` | `logistic_regression` | `0.290` | `0.197` | `0.171` | `0.696` |
| `parte_del_corpo_macro` | `logistic_regression` | `0.159` | `0.198` | `0.126` | `0.449` |

Benchmark aggiuntivi:

| Esperimento | Target | Miglior risultato test |
|---|---|---:|
| Target corrente | `tipologia_causa_macro` | Macro-F1 circa `0.168-0.171` |
| Senza `Altro` | `tipologia_causa_macro` | Macro-F1 `0.200`, ma solo `35` casi test |
| Target corrente | `parte_del_corpo_macro` | Macro-F1 circa `0.164` con testo |
| Senza `Altro` | `parte_del_corpo_macro` | Macro-F1 circa `0.184` |
| Corpo semplificato 3 classi senza `Altro` | `body_part_3class` | Macro-F1 `0.375` |

Decisione presa:

- La causa può essere usata come shortlist top-3 interpretativa.
- La parte del corpo non è abbastanza affidabile come output decisionale.
- Il collo di bottiglia non è solo il modello, ma dimensione campione, sbilanciamento classi e qualità target.

## 27. Interpretabilità del Modello Principale

Top feature baseline:

| Feature | Importanza |
|---|---:|
| `evt_desc_topic_taglio_urto_schiacciamento_count_roll3_mean` | `0.0217` |
| `evt_desc_topic_macchine_impianti_attrezzature_count_roll3_mean` | `0.0214` |
| `evt_desc_topic_tagged_rows_roll3_mean` | `0.0208` |
| `evt_injury_like_count_roll3_mean` | `0.0205` |
| `evt_semantic_component_2_roll3_mean` | `0.0166` |
| `evt_semantic_component_2` | `0.0158` |
| `evt_first_aid_count_roll3_mean` | `0.0146` |
| `obs_family_produzione_e_processo_rows_roll3_mean` | `0.0144` |
| `evt_desc_topic_cadute_scivolamenti_adverse_count_roll3_mean` | `0.0136` |
| `evt_problem_d_count_roll3_mean` | `0.0131` |
| `obs_family_dpi_e_abbigliamento_rows` | `0.0127` |
| `evt_total_rows_roll3_mean` | `0.0114` |

Lettura:

- Lo storico eventi recente conta molto.
- I topic descrizione sono tra le feature più informative.
- Il codice problema `D` legato a impianti e attrezzature è rilevante.
- Anche la composizione BBS per famiglie attività porta segnale.

Top feature ramo expert:

| Feature | Importanza |
|---|---:|
| `evt_desc_topic_macchine_impianti_attrezzature_count_roll3_mean` | `0.0239` |
| `evt_injury_like_count_roll3_mean` | `0.0219` |
| `evt_desc_topic_tagged_rows_roll3_mean` | `0.0188` |
| `evt_semantic_component_2` | `0.0175` |
| `evt_semantic_component_2_roll3_mean` | `0.0151` |
| `obs_family_produzione_e_processo_rows_roll3_mean` | `0.0145` |
| `evt_first_aid_count_roll3_mean` | `0.0144` |
| `evt_desc_topic_taglio_urto_schiacciamento_count_roll3_mean` | `0.0143` |

Lettura:

- L'overlay expert non sostituisce lo storico eventi.
- L'overlay expert migliora soprattutto la leggibilità del rischio comportamentale.

## 28. Cosa Ha Funzionato

Ha funzionato bene:

- Cleaning eventi e osservazioni.
- Normalizzazione aree.
- Esclusione COVID e in itinere.
- Accorpamento SMAT, azioni insicure, condizioni insicure e annotazioni BBS nel mondo SMAT Audit.
- Integrazione area-mese.
- Target next month.
- Walk-forward backtest.
- Uso del testo descrizione per topic e similarity retrieval.
- Tassonomia comportamenti v2.
- Canonicalizzazione comportamenti.
- Separazione messaggi/prompt/comportamenti reali.
- Ranking expert IR-like.
- Deepdive severity-aware.
- Investigation pack.

## 29. Cosa Non Ha Funzionato o È Stato Ridimensionato

È stato scartato o ridimensionato:

- Merge evento-per-evento tra BBS ed Eventi.
- Modello persona-level.
- Lettura causale diretta osservazione -> infortunio.
- Uso di tutte le 101 colonne raw.
- Inclusione COVID.
- Inclusione in itinere nel rischio operativo interno.
- Uso di `SMAT Audit` come target.
- Uso di messaggi e prompt checklist come comportamenti unsafe reali.
- Promozione del modello causa/corpo a motore principale.
- Promozione immediata del ramo sottofamiglia weighted a score engine principale.

## 30. Nota sui Comportamenti Non Osservati

I comportamenti non osservati non sono stati trattati come automaticamente sicuri o unsafe.

Motivo:

- Una mancata osservazione può significare assenza di esposizione.
- Può significare assenza di audit.
- Può significare copertura BBS incompleta.
- Può significare che il comportamento non era applicabile in quell'area/mese.

Decisione presa:

- Non codificare l'assenza del comportamento come `safe`.
- Usare invece metriche di copertura, volumi osservativi e rapporti osservazioni/eventi.
- In futuro si può introdurre un catalogo di comportamenti attesi per area/attività, ma serve una matrice HSE di applicabilità.

## 31. Limiti Attuali

Limiti principali:

- Mancano ore lavorate.
- Mancano headcount per area/mese.
- Mancano turni, straordinari, mix personale interno/esterno.
- Mancano volumi produttivi.
- Mancano dati macchina/linea/workcell.
- Mancano timestamp abbastanza granulari per collegare comportamento ed evento.
- Il target injury-like è piccolo.
- Parte del corpo e causa sono molto sbilanciate.
- Le probabilità non sono ancora calibrate per uso quantitativo forte.
- Alcune aree hanno poca copertura BBS.

## 32. Raccomandazione Operativa

Uso consigliato oggi:

1. Usare il ranking area-mese per scegliere le prime 3-5 aree.
2. Usare il ramo `behavior_weighted_experiment` o `behavior_expert_weighted_experiment` come scoring principale.
3. Usare il deepdive sottofamiglia severity-aware per capire dove investigare.
4. Usare l'investigation pack per trasformare score e driver in sopralluogo.
5. Non usare causa/parte del corpo come previsione decisionale autonoma.

Scelta consigliata:

| Componente | Uso consigliato |
|---|---|
| `baseline` | riferimento stabile |
| `behavior_weighted_experiment` | buon motore scoring data-driven |
| `behavior_expert_weighted_experiment` | miglior overlay HSE operativo |
| `behavior_subfamily_weighted_experiment` | layer diagnostico e spiegabilità |
| `injury_detail_model` | shortlist interpretativa, non core |
| `area_investigation_pack_latest` | output operativo per HSE |

## 33. Miglioramenti Prioritari

Priorità alta:

- Aggiungere ore lavorate per area/mese.
- Aggiungere headcount per area/mese.
- Aggiungere turni e straordinari.
- Aggiungere volumi produttivi.
- Aggiungere presenza ditte esterne.
- Costruire matrice area-attività-comportamenti attesi.
- Calibrare meglio probabilità se devono essere usate come soglie quantitative.

Priorità media:

- Revisionare manualmente `review_flag` della tassonomia v2.
- Consolidare sottofamiglie con pochi casi.
- Costruire scenari di rischio ricorrenti dai casi simili.
- Valutare panel area-settimana solo se la copertura BBS regge.
- Integrare severità anche su specifici presidi e meccanismi di rischio.

Priorità bassa:

- Riprendere parte del corpo solo con target più coarse.
- Riprendere causa solo con più dati injury-like.
- Testare modelli più complessi solo dopo aver aggiunto esposizione reale.

## 34. Artifact Principali

| Artifact | Contenuto |
|---|---|
| `events_cleaned.csv` | Eventi puliti |
| `observations_cleaned.csv` | Osservazioni BBS pulite con tassonomia v2 |
| `risk_panel_area_month.csv` | Panel baseline area-mese |
| `risk_panel_area_month_behavior_weighted.csv` | Panel con pesi data-driven famiglia |
| `risk_panel_area_month_behavior_subfamily_weighted.csv` | Panel con pesi data-driven sottofamiglia |
| `risk_panel_area_month_behavior_expert_weighted.csv` | Panel con ranking expert IR-like |
| `main_model_variant_comparison.csv` | Confronto metriche varianti |
| `walk_forward_predictions.csv` | Predizioni walk-forward baseline |
| `behavior_expert_walk_forward_predictions.csv` | Predizioni walk-forward expert |
| `behavior_subfamily_weighted_walk_forward_predictions.csv` | Predizioni walk-forward sottofamiglia |
| `area_behavior_family_deepdive.csv` | Deepdive famiglie comportamento |
| `area_behavior_subfamily_deepdive.csv` | Deepdive sottofamiglie severity-aware |
| `area_behavior_deepdive.csv` | Deepdive comportamenti canonici |
| `area_investigation_pack_latest.csv` | Pack operativo tabellare |
| `area_investigation_pack_latest.md` | Pack operativo leggibile |
| `area_similar_historical_events_latest.csv` | Eventi storici simili |
| `injury_detail_model_report.json` | Report modello causa/corpo |

## 35. Conclusione Finale

La direzione confermata è:

- modello principale area-mese;
- validazione walk-forward;
- ranking operativo top aree;
- drilldown attività/comportamenti/sottofamiglie;
- severità HSE nel deepdive;
- investigation pack per passare dal modello all'azione.

La direzione non prioritaria oggi è:

- predire singola causa con alta confidenza;
- predire parte del corpo con alta confidenza;
- usare il modello come prova causale;
- usare la granularità sottofamiglia come score engine principale senza ulteriori dati di esposizione.

Il progetto oggi è maturo per uso HSE come sistema di:

- early warning;
- prioritizzazione aree;
- audit planning;
- investigazione guidata;
- supporto decisionale, non decisione automatica.
