# Risk Pipeline Agordo

Pipeline per stimare e spiegare il rischio operativo a livello `area x mese`, integrando:

- eventi HSE da `SAMPLE 2 - Estratto_eventi_ITA_2016_2026WK16.xlsx`
- osservazioni BBS da `Osservazioni_Agordo_cf09b6dda9dc4bfbb40d2fee5335bf5d.xlsx`
- tassonomia comportamenti HSE v2
- ranking esperto IR-like delle famiglie comportamento

## Esecuzione

Comando standard:

```bash
python3 run_pipeline.py
```

Il comando legge i percorsi da:

```text
config/pipeline_config.json
```

Override da terminale:

```bash
python3 run_pipeline.py \
  --events "SAMPLE 2 - Estratto_eventi_ITA_2016_2026WK16.xlsx" \
  --observations "Osservazioni_Agordo_cf09b6dda9dc4bfbb40d2fee5335bf5d.xlsx" \
  --output-dir artifacts
```

## Struttura Consegna

- `run_pipeline.py`: comando unico per eseguire tutta la pipeline.
- `config/pipeline_config.json`: configurazione percorsi input/output.
- `src/risk_pipeline/pipeline_core.py`: logica completa di cleaning, feature engineering, modelli, backtest e report.
- `src/risk_pipeline/cli.py`: wrapper CLI che legge la configurazione.
- `docs/delivery_structure.md`: nota tecnica sulla struttura di consegna.
- `artifacts/behavior_taxonomy_pipeline_v2.csv`: tassonomia comportamenti canonici, famiglie, sottofamiglie, meccanismi di rischio e severita.
- `artifacts/behavior_family_expert_risk_rank.csv`: ranking IR-like delle famiglie comportamento.

## Input Richiesti

- `SAMPLE 2 - Estratto_eventi_ITA_2016_2026WK16.xlsx`
- `Osservazioni_Agordo_cf09b6dda9dc4bfbb40d2fee5335bf5d.xlsx`
- `artifacts/behavior_taxonomy_pipeline_v2.csv`
- `artifacts/behavior_family_expert_risk_rank.csv`

## Output Principali

La pipeline scrive gli output nella cartella configurata in `output_dir`, di default `artifacts`.

Output cliente principali:

- `area_investigation_pack_latest.csv`
- `area_investigation_pack_latest.md`
- `area_risk_deepdive_latest.md`
- `latest_risk_scores.csv`
- `behavior_subfamily_weighted_latest_risk_scores.csv`
- `main_model_variant_comparison.csv`
- `business_model_recap.md` oppure `business_model_recap_auto.md`

Output diagnostici principali:

- `cleaning_report.json`
- `model_report.json`
- `walk_forward_report.json`
- `behavior_subfamily_weighted_walk_forward_report.json`
- `feature_importance.csv`
- `behavior_subfamily_weighted_feature_importance.csv`

Output dati intermedi principali:

- `events_cleaned.csv`
- `observations_cleaned.csv`
- `risk_panel_area_month.csv`
- `risk_panel_area_month_behavior_subfamily_weighted.csv`
- `behavior_mapping.csv`
- `behavior_clean_summary.csv`
- `behavior_canonical_summary.csv`

## Nota sul Pack Investigativo

L'`investigation pack` finale e' centrato su:

- ranking area-mese
- famiglie comportamento
- sottofamiglie comportamento
- comportamenti osservati
- topic descrizione eventi
- storico eventi recente
- casi storici simili

Le attivita' non vengono piu' incluse nel pack finale, per evitare rumore informativo e mantenere il deliverable focalizzato sui driver comportamentali e sul contesto eventi.

## Target Modello

Il target principale e':

```text
target_adverse_next_month = 1
se nel mese successivo, nella stessa area, esiste almeno un:
- Primo soccorso
- Infortunio con certificato
- Incidente senza infortunio
```

Gli `SMAT Audit` non sono target, ma restano feature e contesto storico.

## Validazione

La pipeline include:

- split temporale train/validation/test
- confronto modelli baseline
- varianti con pesi comportamentali
- walk-forward backtest out-of-sample mese per mese
- metriche tecniche: `PR-AUC`, `ROC-AUC`, `Brier`
- metriche operative: `top_1_hit_rate`, `top_3_precision`, `top_3_recall`

## Installazione Dipendenze

```bash
python3 -m pip install -r requirements.txt
```

