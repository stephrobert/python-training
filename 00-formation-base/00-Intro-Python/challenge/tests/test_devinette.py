import builtins
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from devinette import jeu_devinette

def test_shebang_present():
    chemin = os.path.join(os.path.dirname(__file__), "..", "devinette.py")
    with open(chemin, "r", encoding="utf-8") as f:
        premiere_ligne = f.readline().strip()
    assert premiere_ligne == "#!/usr/bin/env python3", "Le shebang est manquant ou incorrect"

def test_juste_en_trois_coups(monkeypatch, capsys):
    # Simule les entrées utilisateur
    # 50 → trop petit, 75 → trop grand, 65 → juste
    inputs = iter(["50", "75", "65"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Simule un nombre mystère connu
    jeu_devinette(nombre_mystere=65)

    # Capture la sortie terminal
    captured = capsys.readouterr()
    out = captured.out

    assert "c'est plus petit" in out.lower()
    assert "c'est plus grand" in out.lower()
    assert "bravo" in out.lower()
    assert "3 essais" in out
