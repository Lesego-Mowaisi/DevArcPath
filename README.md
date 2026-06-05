# Reasoning Agents Challenge

# DevArcPath

## Overview
A multi‑agent system that helps CS students turn tutorial‑following into verified, job‑ready GitHub portfolios.

## How It Works (The DevArcPath Verification Loop)

1. **Upload** – Student provides tutorial repo URL or zip.
2. **Similarity Detection** – System computes a similarity score against known tutorial code.
3. **Challenge Generation** – If similarity > threshold, an LLM generates a real‑world problem in a modern domain (DevOps, Cloud, AI, etc.).
4. **Solution Submission** – Student uploads their solution.
5. **Automated Testing** – System runs 1–2 test cases (e.g., expected output, function presence).
6. **Feedback Loop** – If tests fail, student receives feedback and can resubmit (same challenge).
7. **Conceptual Verification** – System asks 2–3 follow‑up questions to confirm understanding.
8. **Pass** – If answers are satisfactory, system guides student to push the project to their GitHub portfolio.
9. **Completion** – Student has a verified, original project and a stronger grasp of the concept.

## Agents & Tools
- **Learning Path Curator** – Generates challenges using Foundry IQ (knowledge base of problem domains).
- **Assessment Agent** – Runs tests and evaluates submissions.
- **Foundry IQ** – Grounds challenge generation in curated synthetic documents.
- **GitHub API** – (Planned) For automated portfolio integration.

## Synthetic Data
- `problem_domains.json` – List of modern tech domains.
- `student_profiles.json` – Fake student submissions and scores.
