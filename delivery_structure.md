# Struttura di Consegna

La pipeline e' organizzata per separare il comando di esecuzione dalla logica analitica.

- `run_pipeline.py`: entrypoint unico da lanciare.
- `config/pipeline_config.json`: percorsi di input/output modificabili senza toccare il codice.
- `src/risk_pipeline/pipeline_core.py`: motore completo della pipeline.
- `src/risk_pipeline/cli.py`: lettura config e passaggio parametri al motore.
- `artifacts/deliverable/`: cartella prevista per gli output finali da condividere.
- `artifacts/diagnostics/`: cartella prevista per metriche, backtest e controlli tecnici.
- `artifacts/intermediate/`: cartella prevista per output intermedi e dataset di lavoro.

Il comando standard rimane:

```bash
python3 run_pipeline.py
```

Per cambiare i percorsi si puo' modificare `config/pipeline_config.json` oppure usare override CLI:

```bash
python3 run_pipeline.py --output-dir artifacts
```
