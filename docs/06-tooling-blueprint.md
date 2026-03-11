# Tooling-Blueprint nach Unternehmensdomainen

## Grundsatz

Tools sollten nicht nach Trend, sondern nach Architekturrolle und Use Case eingefuehrt werden. Fuer jede Domaene ist zu klaeren:

- Welches Problem wird geloest?
- Ist das Tool systemkritisch oder komplementaer?
- Wie integriert es sich in die bestehende Landschaft?
- Wie werden Sicherheit, Rechte und Datenfluss kontrolliert?

## Tool-Domaenen

### Projekt- und Portfoliomanagement

Geeignet fuer:

- Priorisierung von Vorhaben
- Transparenz ueber Abhaengigkeiten
- KPI-Tracking und Entscheidungsboards

Worauf achten:

- Rollup-Faehigkeit fuer Management
- Verbindung zu Delivery-Daten
- Governance fuer Intake und Priorisierung

### Kollaboration und Wissensmanagement

Geeignet fuer:

- Dokumentation
- Wissensbasis
- Entscheidungsprotokolle
- teamuebergreifende Zusammenarbeit

Worauf achten:

- Suchqualitaet
- Rechtekonzept
- API-Zugriff fuer KI-Anwendungen

### Daten- und Analytics-Stack

Geeignet fuer:

- Datenintegration
- Standardberichte
- KPI-Steuerung
- Training oder Versorgung von KI-Systemen

Worauf achten:

- Datenmodellierung
- Ownership
- Governance
- Betriebsstabilitaet

### Automatisierung und Workflows

Geeignet fuer:

- standardisierte Freigaben
- repetitive Backoffice-Prozesse
- systemuebergreifende Orchestrierung

Worauf achten:

- Nachvollziehbarkeit
- Fehlerbehandlung
- Versionierung
- Security

### AI Enablement Stack

Geeignet fuer:

- LLM-Anwendungen
- Retrieval und Wissenssuche
- Modellzugriff
- Guardrails, Observability und Evaluation

Worauf achten:

- Datenfluss und Hosting
- Prompt-, Modell- und Evaluations-Governance
- Logging sensibler Inhalte
- Kostenkontrolle

## Auswahlprinzipien

- lieber weniger Tools mit klarer Rolle
- keine redundanten Plattformen
- zentrale Standards fuer Integration und Identity
- Buy vor Build, wenn Differenzierung gering ist
- Build nur dort, wo Prozess, Daten oder IP den Unterschied machen
