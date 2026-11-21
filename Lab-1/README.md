# Lab 1 – Requirements Engineering & UML Use-Case Modelling

**Name:** Varun CH | **SRN:** PES2UG24AM180
**Course:** PES University – Dept. of CSE
**Problem Statement #24:** Public Bus Live Tracking & Crowding Estimator (Smart Cities, Transport & Logistics)

## Overview
A municipal transit intelligence platform that ingests GPS feeds from city buses, estimates arrival times (ETA) at downstream stops, and computes passenger crowding levels from ticketing sensors.

**Actors:** Commuter, Fleet Controller (external systems: GPS Telematics Unit, Ticketing Sensor)

## Deliverables

| # | File | Description |
|---|---|---|
| 1 | `1_Requirements_Table_PES2UG24AM180.docx` | 5 Functional Requirements (FR-001 to FR-005) and 2 Non-Functional Requirements (NFR-001, NFR-002) with ID, Type, Description, Priority, Acceptance Criteria, Rationale and Comments |
| 2 | `2_UseCase_Diagram_PES2UG24AM180.pdf` | UML use-case diagram: 4 actors, 11 use cases (UC-01 to UC-11), 4 «include» and 2 «extend» relationships |
| 3 | `3_UseCase_Flow_UC03_PES2UG24AM180.docx` / `.pdf` | One-page flow for UC-03 "View Bus ETA at Stop": preconditions, postconditions, main success scenario, alternate flow A1 |

## Requirements Summary

| ID | Type | Summary | Priority |
|---|---|---|---|
| FR-001 | Functional | Ingest GPS every 5 s and recalculate ETAs | High |
| FR-002 | Functional | Search route/stop and show live bus positions | High |
| FR-003 | Functional | Compute and show bus crowding level | High |
| FR-004 | Functional | Fleet Controller dashboard with delay/overcrowding alerts | Medium |
| FR-005 | Functional | Arrival-alert subscription for commuters | Low |
| NFR-001 | Performance & Security | 1,000 vehicles, p95 latency ≤ 3 s, TLS 1.2+ | High |
| NFR-002 | Security & Availability | Role-based access for controller functions, ≥ 99.5% uptime | High |

## Use Cases
UC-01 Search Route / Stop · UC-02 View Live Bus Location · UC-03 View Bus ETA at Stop · UC-04 Check Bus Crowding Level · UC-05 Subscribe to Arrival Alert · UC-06 Monitor Fleet Dashboard · UC-07 Dispatch Additional Bus · UC-08 Authenticate Fleet Controller · UC-09 Calculate ETA · UC-10 Compute Crowding Level · UC-11 Ingest GPS Telemetry

**«include»:** UC-03→UC-09, UC-04→UC-10, UC-09→UC-11, UC-06→UC-08
**«extend»:** UC-05→UC-03, UC-07→UC-06

## Traceability

| Requirement | Use Cases |
|---|---|
| FR-001 | UC-03, UC-09, UC-11 |
| FR-002 | UC-01, UC-02 |
| FR-003 | UC-04, UC-10 |
| FR-004 | UC-06, UC-07, UC-08 |
| FR-005 | UC-05 |
| NFR-001 | UC-09, UC-11 |
| NFR-002 | UC-08 |
