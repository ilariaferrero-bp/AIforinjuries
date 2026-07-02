# Investigation Pack Aree Prioritarie

Mese target: `2026-05-01`.
Questo pack unisce ranking area-mese, driver attivita/comportamenti e contesto eventi recente.

## Come usarlo

- Partire dal ranking baseline per scegliere le prime aree da investigare.
- Usare il punteggio expert come overlay sui comportamenti piu severi.
- Verificare sul campo i driver indicati: non sono prove causali, ma ipotesi operative prioritarie.

## 1. Stamperia Plastica

- Score baseline `0.867` (rank `1`), score expert `0.879` (rank `1`) per `target_month=2026-05-01`.
- Unsafe ultimi 12 mesi: `3.081%` su `12828` righe osservate.
- Eventi ultimi 12 mesi: `SMAT=631`, `primo soccorso=16`, `certificati=6`, `incidenti senza infortunio=10`.
- Problem code ricorrenti: C:276 | H:163 | D:87.
- Topic descrizione ricorrenti: Macchine / impianti / attrezzature:271 | Taglio / urto / schiacciamento:110 | DPI occhi / viso:103.
- Topic descrizione sugli eventi avversi: Taglio / urto / schiacciamento:15 | Macchine / impianti / attrezzature:14 | Carrelli / mezzi / AGV:7.
- Pattern ricorrenti dai casi simili: Carrelli / mezzi / AGV:2 | Macchine / impianti / attrezzature:2 | Taglio / urto / schiacciamento:2.
- Ultimo evento avverso noto: 2026-04-17 - Primo soccorso - C.
- Famiglie attivita driver: Spostamenti Trasporto e Stoccaggio (unsafe 4.5%, lift 1.45x); DPI e Abbigliamento (unsafe 3.8%, lift 1.24x); Ordine Pulizia e Area di Lavoro (unsafe 2.7%, lift 0.88x).
- Attivita da guardare: IGIENE DI SE', DELLE COSE E CORRETTO SMALTIMENTO (unsafe 6.3%, quota area 9.8%); Spostamenti (unsafe 5.6%, quota area 22.5%); TRASPORTO CON AUSILI DI POTENZIAMENTO MECCANICO (unsafe 6.1%, quota area 4.2%).
- Famiglie comportamento piu critiche: Elettrico / Emergenza / Vie di fuga (IR 1, unsafe 7.8%, expert prio 11.84); Macchine / Organi mobili / Protezioni (IR 1, unsafe 3.4%, expert prio 2.78); DPI / Abbigliamento / Protezione personale (IR 2, unsafe 4.0%, expert prio 2.46).
- Sottofamiglie comportamento piu critiche: Vie di fuga / porte tagliafuoco (IR 1, unsafe 7.9%, prio 2.10); DPI occhi / viso (IR 2, unsafe 7.2%, prio 1.43); DPI udito (IR 2, unsafe 6.1%, prio 0.81).
- Comportamenti da osservare: Occhiali di protezione (unsafe 7.2%, 809 righe); L'attrezzista allontana l'operatore durante l'uso del carroponte (unsafe 16.3%, 26 righe); Cammina entro le vie d'esodo segnalate per spostarsi all'interno del reparto (unsafe 9.1%, 197 righe).
- Ipotesi di lavoro: Rischio plausibilmente trainato da `Elettrico / Emergenza / Vie di fuga` durante `IGIENE DI SE', DELLE COSE E CORRETTO SMALTIMENTO`. Segnale secondario su `Macchine / Organi mobili / Protezioni`. Storico eventi recente coerente su `C:276 | H:163 | D:87`.
- Checklist campo: Verificare condizioni operative, standard e barriere collegati alla famiglia comportamento.
- Storico eventi recente: 2026-04-17 - Primo soccorso - C - L'operatore mentre nastrava ad acqua accidentalmente urtava con il... | 2026-04-16 - Incidente senza infortunio - A - La lavoratrice mentre spingeva un carretto degli ordini per gli AGV... | 2026-04-10 - Incidente senza infortunio - A - Nel corso della manutenzione periodica trimestrale sugli impianti d...
- Casi storici simili: 2021-10-05 - Stamperia Plastica - Incidente senza infortunio - H - sim 0.30 - dopo che l'attrezzista aveva poggiato lo stampo sul carrello dedicato e correttamente posizi... | 2020-07-31 - Stamperia Plastica - Primo soccorso - D - sim 0.27 - durante l'attività di sfiammatura (pulizia delle bussole dai residui plastici) si porcurava... | 2022-05-11 - Stamperia Plastica - Incidente senza infortunio - D - sim 0.26 - Durante la fase di sollevamento da parte dell'agv del carrello ordini, questo cadeva colpend...

## 2. Montaggio e Finitura

- Score baseline `0.706` (rank `2`), score expert `0.717` (rank `2`) per `target_month=2026-05-01`.
- Unsafe ultimi 12 mesi: `1.726%` su `35630` righe osservate.
- Eventi ultimi 12 mesi: `SMAT=817`, `primo soccorso=13`, `certificati=2`, `incidenti senza infortunio=7`.
- Problem code ricorrenti: H:309 | D:167 | A:144.
- Topic descrizione ricorrenti: Materiali / stoccaggio:107 | Taglio / urto / schiacciamento:99 | Distrazione / comportamento:96.
- Topic descrizione sugli eventi avversi: Taglio / urto / schiacciamento:11 | Cadute / scivolamenti:7 | Movimentazione / ergonomia:5.
- Pattern ricorrenti dai casi simili: Macchine / impianti / attrezzature:2 | DPI occhi / viso:1 | Taglio / urto / schiacciamento:1.
- Ultimo evento avverso noto: 2026-04-14 - Incidente senza infortunio - H.
- Famiglie attivita driver: Spostamenti Trasporto e Stoccaggio (unsafe 3.6%, lift 2.09x); Ordine Pulizia e Area di Lavoro (unsafe 2.0%, lift 1.13x); Macchine Impianti e Sicurezze (unsafe 1.8%, lift 1.05x).
- Attivita da guardare: STOCCAGGIO MATERIALI (unsafe 6.6%, quota area 7.6%); USO ARIA COMPRESSA (unsafe 4.8%, quota area 1.4%); Uso taglierino / taglia-reggette (unsafe 5.7%, quota area 1.6%).
- Famiglie comportamento piu critiche: Stoccaggio / Materiali / Layout (IR 3, unsafe 4.6%, expert prio 2.74); Macchine / Organi mobili / Protezioni (IR 1, unsafe 2.0%, expert prio 1.47); Chimici / Aspirazione / Sostanze pericolose (IR 1, unsafe 2.0%, expert prio 1.29).
- Sottofamiglie comportamento piu critiche: Impilamento / stabilità / perimetro (IR 2, unsafe 6.5%, prio 1.72); Forni / essiccatori / parti calde (IR 1, unsafe 6.6%, prio 1.58); Utensili manuali / taglio / aria compressa (IR 2, unsafe 6.9%, prio 1.46).
- Comportamenti da osservare: Taglia in direzione opposta al corpo (unsafe 23.4%, 46 righe); Chiude l'aria quando non la usa (unsafe 17.6%, 51 righe); Inserisce l'avvitatore elettrico (Lecureaux) alla base quando lascia la postazione (unsafe 10.7%, 433 righe).
- Ipotesi di lavoro: Rischio plausibilmente trainato da `Stoccaggio / Materiali / Layout` durante `STOCCAGGIO MATERIALI`. Segnale secondario su `Macchine / Organi mobili / Protezioni`. Storico eventi recente coerente su `H:309 | D:167 | A:144`.
- Checklist campo: Verificare condizioni operative, standard e barriere collegati alla famiglia comportamento.
- Storico eventi recente: 2026-04-14 - Incidente senza infortunio - H - Il MIR mentre percorreva il corridoio del mondo 4 ha cambiato auton... | 2026-04-02 - Incidente senza infortunio - A - operatrice inserisce dito sul buco presente dell'armadietto (dove d... | 2026-03-19 - Incidente senza infortunio - H - Schienale sedia operatore si stacca e la persona ha rischiato di ca...
- Casi storici simili: 2018-07-19 - Stamperia Plastica - Incidente senza infortunio - D - sim 0.26 - rottura attacco rapido del'aria compressa del ribattitore GL. Il tubicino dell'aria compress... | 2019-07-15 - Stamperia Plastica - Incidente senza infortunio - D - sim 0.25 - la lavoratrice stava lavorando sulla postazione di nastratura manuale nr. 4 quando improvvis... | 2025-03-31 - Montaggio e Finitura - Primo soccorso - H - sim 0.24 - Operatore si taglia leggermente l'avambraccio mentre apriva una confezione di note non segue...

## 3. Stamperia Metallo

- Score baseline `0.620` (rank `3`), score expert `0.632` (rank `3`) per `target_month=2026-05-01`.
- Unsafe ultimi 12 mesi: `1.151%` su `14590` righe osservate.
- Eventi ultimi 12 mesi: `SMAT=138`, `primo soccorso=2`, `certificati=0`, `incidenti senza infortunio=2`.
- Problem code ricorrenti: D:60 | A:32 | B:17.
- Topic descrizione ricorrenti: Macchine / impianti / attrezzature:27 | Taglio / urto / schiacciamento:21 | Distrazione / comportamento:15.
- Topic descrizione sugli eventi avversi: Chimici / lavaggi / aspirazione:2 | Taglio / urto / schiacciamento:2 | Cadute / scivolamenti:1.
- Pattern ricorrenti dai casi simili: Taglio / urto / schiacciamento:3 | Chimici / lavaggi / aspirazione:3.
- Ultimo evento avverso noto: 2026-03-11 - Incidente senza infortunio - D.
- Famiglie attivita driver: Interferenze e Coordinamento (unsafe 2.2%, lift 1.95x); Ergonomia e Movimentazione (unsafe 1.6%, lift 1.38x); Comportamenti Generali e Buone Prassi (unsafe 1.6%, lift 1.41x).
- Attivita da guardare: Interferenze del personale di reparto in attivita' "extra reparto" (unsafe 2.2%, quota area 1.4%); Spostamenti (unsafe 1.9%, quota area 15.4%); SICUREZZE MACCHINE/IMPIANTI (unsafe 1.8%, quota area 1.9%).
- Famiglie comportamento piu critiche: Chimici / Aspirazione / Sostanze pericolose (IR 1, unsafe 1.3%, expert prio 0.62); DPI / Abbigliamento / Protezione personale (IR 2, unsafe 1.3%, expert prio 0.46); Interferenze / Coordinamento (IR 3, unsafe 1.5%, expert prio 0.25).
- Sottofamiglie comportamento piu critiche: Interazione pedoni-mezzi (IR 1, unsafe 3.1%, prio 0.56); DPI udito (IR 2, unsafe 2.8%, prio 0.30); DPI mani / guanti (IR 2, unsafe 2.0%, prio 0.20).
- Comportamenti da osservare: Il pedone dà la precedenza a transpallet/carrelli/gabbie/MIR (unsafe 7.0%, 60 righe); Guanto spalmato in poliuretano (unsafe 9.0%, 29 righe); Lavora con i contenitori delle sostanze e dei prodotti chimici di materiale idoneo ed adeguatamente etichettati (unsafe 3.0%, 23 righe).
- Ipotesi di lavoro: Rischio plausibilmente trainato da `Chimici / Aspirazione / Sostanze pericolose` durante `Interferenze del personale di reparto in attivita' "extra reparto"`. Segnale secondario su `DPI / Abbigliamento / Protezione personale`. Storico eventi recente coerente su `D:60 | A:32 | B:17`.
- Checklist campo: Verificare condizioni operative, standard e barriere collegati alla famiglia comportamento. | Verificare sovrapposizioni tra squadre, ditte esterne e passaggi di consegna.
- Storico eventi recente: 2026-03-11 - Incidente senza infortunio - D - Durante la fase di rabbocco saponi si stacca una cannetta della pom... | 2026-02-05 - Incidente senza infortunio - A - Entrando nel locale bagni, a causa del pavimento ancora bagnato dop... | 2025-10-16 - Primo soccorso - D - Durante la fase di pulizia della vasca della macchina 342 con l'asp...
- Casi storici simili: 2023-10-03 - Officina - Infortunio con certificato - D - sim 0.26 - Il lavoratore, nella fase di pulizia della macchina, (Macchina Spenta) rimuove dal collettor... | 2021-07-14 - Galvanica/Pulitura - Infortunio con certificato - D - sim 0.25 - si feriva durante un'attività di prelievo da una vasca di trattamento galvanico vendo urtato... | 2016-01-20 - Verniciatura - Primo soccorso - C - sim 0.24 - durante la fase di taglio guaine con apparecchiatura laser (durante la fase di rifilatura co...

## 4. Galvanica/Pulitura

- Score baseline `0.510` (rank `4`), score expert `0.496` (rank `5`) per `target_month=2026-05-01`.
- Unsafe ultimi 12 mesi: `1.728%` su `18038` righe osservate.
- Eventi ultimi 12 mesi: `SMAT=346`, `primo soccorso=7`, `certificati=4`, `incidenti senza infortunio=6`.
- Problem code ricorrenti: A:137 | F:68 | H:67.
- Topic descrizione ricorrenti: Materiali / stoccaggio:97 | Vie di fuga / emergenza:74 | Chimici / lavaggi / aspirazione:36.
- Topic descrizione sugli eventi avversi: Materiali / stoccaggio:9 | Chimici / lavaggi / aspirazione:7 | Cadute / scivolamenti:6.
- Pattern ricorrenti dai casi simili: DPI occhi / viso:2 | Taglio / urto / schiacciamento:1 | Movimentazione / ergonomia:1.
- Ultimo evento avverso noto: 2026-03-11 - Primo soccorso - H.
- Famiglie attivita driver: Sostanze Chimiche e Lavaggi (unsafe 8.8%, lift 5.08x); DPI e Abbigliamento (unsafe 2.2%, lift 1.26x); Produzione e Processo (unsafe 2.4%, lift 1.37x).
- Attivita da guardare: Gestione / uso sostanze chimiche (unsafe 9.5%, quota area 8.7%); GALVANICA E LABORATORI (unsafe 6.8%, quota area 1.1%); DPI (unsafe 3.3%, quota area 21.3%).
- Famiglie comportamento piu critiche: Chimici / Aspirazione / Sostanze pericolose (IR 1, unsafe 3.4%, expert prio 3.37); DPI / Abbigliamento / Protezione personale (IR 2, unsafe 2.2%, expert prio 0.95); Attrezzature / Utensili / Dispositivi di presa (IR 2, unsafe 1.3%, expert prio 0.39).
- Sottofamiglie comportamento piu critiche: DPI occhi / viso (IR 2, unsafe 6.7%, prio 1.50); Stoccaggio infiammabili (IR 1, unsafe 6.3%, prio 1.17); Contenitori / etichettatura / chiusura (IR 1, unsafe 3.4%, prio 0.65).
- Comportamenti da osservare: Lavora con il tubo di aspirazione perpendicolare alla sostanza maneggiata (unsafe 26.4%, 39 righe); Abbassa il vetro della cappa del laboratorio analisi prima di allontanarsi (unsafe 11.0%, 45 righe); Lavora con i recipienti chiusi (unsafe 25.8%, 51 righe).
- Ipotesi di lavoro: Rischio plausibilmente trainato da `Chimici / Aspirazione / Sostanze pericolose` durante `Gestione / uso sostanze chimiche`. Segnale secondario su `DPI / Abbigliamento / Protezione personale`. Storico eventi recente coerente su `A:137 | F:68 | H:67`.
- Checklist campo: Verificare condizioni operative, standard e barriere collegati alla famiglia comportamento.
- Storico eventi recente: 2026-03-11 - Primo soccorso - H - Operatore laser UV n.24, urta accidentalmente il mignolo della mano... | 2026-03-11 - Infortunio con certificato - A - Mercoledì 18/03/2026 è stato consegnato presso l'ufficio verniciatu... | 2026-02-16 - Incidente senza infortunio - H - L'operatore segnala di aver inserito in vasca 126 (linea sverniciat...
- Casi storici simili: 2016-09-30 - Galvanica/Pulitura - Infortunio con certificato - A - sim 0.28 - La lavoratrice dichiara che venerdì 30 settembre, nel corso della prima ora di lavoro, avver... | 2023-02-03 - Stamperia Plastica - Infortunio con certificato - A - sim 0.27 - In data 07/02/2023 pervenuto certificato per dolore a mano e polso dx dopo movimento ripetit... | 2025-03-31 - Montaggio e Finitura - Infortunio con certificato - H - sim 0.23 - Avvitando gli occhiali avvertiva dolore al braccio dx. La lavoratrice si presenta in inferme...

## 5. Saldatura

- Score baseline `0.474` (rank `5`), score expert `0.499` (rank `4`) per `target_month=2026-05-01`.
- Unsafe ultimi 12 mesi: `1.426%` su `8730` righe osservate.
- Eventi ultimi 12 mesi: `SMAT=108`, `primo soccorso=2`, `certificati=2`, `incidenti senza infortunio=2`.
- Problem code ricorrenti: F:37 | A:28 | H:19.
- Topic descrizione ricorrenti: Distrazione / comportamento:17 | Materiali / stoccaggio:12 | Macchine / impianti / attrezzature:10.
- Topic descrizione sugli eventi avversi: Macchine / impianti / attrezzature:3 | Cadute / scivolamenti:1 | DPI mani / guanti:1.
- Pattern ricorrenti dai casi simili: Pavimenti / ordine / pulizia:2 | Taglio / urto / schiacciamento:1 | Cadute / scivolamenti:1.
- Ultimo evento avverso noto: 2026-03-10 - Incidente senza infortunio - A.
- Famiglie attivita driver: DPI e Abbigliamento (unsafe 2.2%, lift 1.55x); Ordine Pulizia e Area di Lavoro (unsafe 1.6%, lift 1.15x); Spostamenti Trasporto e Stoccaggio (unsafe 1.0%, lift 0.70x).
- Attivita da guardare: IGIENE DI SE', DELLE COSE E CORRETTO SMALTIMENTO (unsafe 4.5%, quota area 15.6%); DPI (unsafe 2.9%, quota area 58.6%); TRASPORTO SENZA AUSILI DI POTENZIAMENTO MECCANICO (unsafe 1.2%, quota area 2.1%).
- Famiglie comportamento piu critiche: DPI / Abbigliamento / Protezione personale (IR 2, unsafe 2.2%, expert prio 1.04); Ordine / Pulizia / Housekeeping (IR 4, unsafe 4.4%, expert prio 0.19); Interferenze / Coordinamento (IR 3, unsafe 1.2%, expert prio 0.11).
- Sottofamiglie comportamento piu critiche: DPI mani / chimico (IR 1, unsafe 13.5%, prio 7.47); Indumenti protettivi / chimico-processo (IR 2, unsafe 15.5%, prio 5.71); Rifiuti / trucioli / sfridi / contenitori (IR 4, unsafe 21.8%, prio 0.95).
- Comportamenti da osservare: Guanti protezione chimica (unsafe 13.5%, 246 righe); Falda in tyvek (unsafe 15.7%, 90 righe); Rifiuti industriali nei contenitori (unsafe 26.3%, 76 righe).
- Ipotesi di lavoro: Rischio plausibilmente trainato da `DPI / Abbigliamento / Protezione personale` durante `IGIENE DI SE', DELLE COSE E CORRETTO SMALTIMENTO`. Segnale secondario su `Ordine / Pulizia / Housekeeping`. Storico eventi recente coerente su `F:37 | A:28 | H:19`.
- Checklist campo: Verificare condizioni operative, standard e barriere collegati alla famiglia comportamento. | Verificare sovrapposizioni tra squadre, ditte esterne e passaggi di consegna.
- Storico eventi recente: 2026-03-10 - Incidente senza infortunio - A - L'impiegato resta impigliato con la maglietta sulla struttura di un... | 2026-03-05 - Incidente senza infortunio - A - L'attrezzista nel momento in cui si stava sedendo sul banco n. 18 d... | 2025-09-03 - Infortunio con certificato - UNKNOWN - Transitando per recarsi all'auto alla fine del turno si infortunava...
- Casi storici simili: 2019-10-30 - Officina - Infortunio con certificato - H - sim 0.30 - durante la pulizia a fine turno del tornio su cui aveva lavorato si feriva accidentalmente a... | 2024-05-30 - Stamperia Plastica - Infortunio con certificato - F - sim 0.28 - Mentre stava andando alla stazione di carico materiale dietro la pressa n.135 è scivolata su... | 2018-02-06 - Verniciatura - Primo soccorso - A - sim 0.27 - scendendo dalla sedia perdeva l'equilibrio e cadeva a terra procurandosi una contusione al p...

## Nota

Il pack serve per orientare audit e sopralluoghi: suggerisce dove cercare i driver del rischio, ma non dimostra causalita diretta.
