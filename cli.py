from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from risk_pipeline.pipeline_core import main as run_core_pipeline


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "pipeline_config.json"

CONFIG_TO_CORE_ARGS = {
    "events": "--events",
    "observations": "--observations",
    "output_dir": "--output-dir",
    "behavior_expert_ranks": "--behavior-expert-ranks",
    "behavior_taxonomy": "--behavior-taxonomy",
}


def load_config(path: Path | None) -> dict[str, Any]:
    if path is None or not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Il file config deve contenere un oggetto JSON: {path}")
    return payload


def build_core_argv(args: argparse.Namespace, config: dict[str, Any]) -> list[str]:
    values = {key: config.get(key) for key in CONFIG_TO_CORE_ARGS}
    for key in CONFIG_TO_CORE_ARGS:
        override = getattr(args, key, None)
        if override is not None:
            values[key] = override

    core_argv: list[str] = []
    for key, core_arg in CONFIG_TO_CORE_ARGS.items():
        value = values.get(key)
        if value:
            core_argv.extend([core_arg, str(value)])
    return core_argv


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Esegue la pipeline HSE Agordo con configurazione da file JSON o override CLI.",
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG_PATH),
        help="Percorso del file JSON di configurazione. Default: config/pipeline_config.json.",
    )
    parser.add_argument("--no-config", action="store_true", help="Ignora il file config e usa i default della pipeline.")
    parser.add_argument("--events", help="Override percorso file eventi Excel.")
    parser.add_argument("--observations", help="Override percorso file osservazioni Excel.")
    parser.add_argument("--output-dir", dest="output_dir", help="Override cartella output.")
    parser.add_argument("--behavior-expert-ranks", dest="behavior_expert_ranks", help="Override CSV ranking esperto IR-like.")
    parser.add_argument("--behavior-taxonomy", dest="behavior_taxonomy", help="Override CSV tassonomia comportamenti v2.")
    args = parser.parse_args(argv)

    config_path = None if args.no_config else Path(args.config).expanduser()
    if config_path is not None and not config_path.is_absolute():
        config_path = (PROJECT_ROOT / config_path).resolve()

    config = load_config(config_path)
    core_argv = build_core_argv(args, config)

    # Rendiamo i path relativi prevedibili anche se il comando viene lanciato da un'altra cartella.
    os.chdir(PROJECT_ROOT)
    run_core_pipeline(core_argv)
