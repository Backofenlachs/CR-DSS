# Git Commit Strategy

Dieses Projekt verwendet eine einfache, klare Commit-Strategie.
Ziel: nachvolziehbare Historie, kleine Änderungen, klare Aussagen.

---

## 1. Grundregeln

- Schreibe auf English im **Imperativ** (add, update, fix, refactor - nicht added/updated)
- Ein Commit = eine logische Änderung
- Keine Misch-Commits (zb. Architektur + Bugfix + Refactoring)
- Beschreibe das **Warum**, nicht nur das Was
- Halte Commit klein und nachvollziehbar

---

## 2. Commit-Typen (Prefix)

- `feat` --> Neue Funktion
- `fix` --> Bugfix
- `refactor` --> Code-Umstrukturierung ohne Verhaltensänderung
- `docs` --> Dokumentation / Diagramme / ADR
- `chore` --> Struktur, Setup, Konfiguration
- `test` --> Tests hinzugefügt oder angepasst

---

## 3. Format

(type)scope: kurze Beschreibung im Imperativ
- optionale Details
- weiter Änderungen
- ggf. Hinweis auf offene Punkte

---

## 4. Beispiele

### Neue Funktion
`(feat)scoring: add debt-to-income calculation`

### Bugfix
`(fix)annuity: correct interest calculation rounding`

### Refactoring
`(refactor)application: simplify credit evaluation flow`

### Dokumentation
`(docs)architecture: update v1.0 class diagram`

---

## 5. Vor jedem Commit prüfen

- [ ] Ist der Commit logisch abgeschlossen?
- [ ] Ist die Beschreibung klar und verständlch?
- [ ] Habe ich nichts Unfertiges mit committed?
- [ ] Entspricht der Prefix dem Inhalt?

---

## 6. Nicht erlaubt

- `update stuff`
- `fix bug`
- `changes`
- Große Sammel-Commits ohne Struktur

---

Diese Strategie soll einfach bleiben.
Bei Bedarf kann sie später erweitert werden.

---

# Template Aktivieren

Im Projekt-Root einmalig:
```bash
git config commit.template .gitmessage.txt
```

`git commit` öffnet dann immer automatisch das Template im Editor.