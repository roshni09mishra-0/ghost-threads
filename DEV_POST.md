---
title: Ghost Threads: Building an offline altar for 47 unkept promises with Gemma, TabPFN & Render
published: true
tags: devchallenge, hf26challenge, gemma, render
cover_image: https://raw.githubusercontent.com/roshni09mishra-0/ghost-threads/main/screenshots/ghost_threads_showcase.png
canonical_url: https://ghost-threads.onrender.com/
description: An offline conversational debt scanner that finds broken promises in WhatsApp chats using local Gemma 2B and Prior Labs' TabPFN, hosted on Render.
---

> *"Most AI projects help you remember what happened. Ghost Threads helps you remember what you promised."*

I have a bad habit that I suspect a lot of developers share: I make casual commitments in chat and let them vanish into thin air.

"Reviewing the pull request tonight."  
"Will send the slide deck tomorrow morning."  
"Let us catch up this weekend for sure, chai on me."  
"Two minutes, checking right now."

Nobody gets mad. Nobody sends an angry follow-up. The chat just moves on, buried under twenty new notifications, until bringing it up weeks later feels too awkward. But the promise never actually got resolved. It just hangs there in chat history like a ghost.

Last week, I was looking through a two-year-old WhatsApp backup for an old document link and kept stumbling into my own unfulfilled messages. It was genuinely uncomfortable to read. Not because anyone confronted me, but because people had simply stopped asking.

Instead of building yet another generic "chat with your PDF" bot, I decided to build **Ghost Threads**: an offline scanner that parses your chat archives, extracts forgotten promises using Google's open-weight Gemma 2B, calculates a technical unresolved risk score using Prior Labs' TabPFN tabular model, and renders the unkept lines on an interactive Día de los Muertos ofrenda altar.

Here is the quick video walkthrough (narrated in multilingual Hinglish with ElevenLabs):

{% youtube 0mPuCKG99-4 %}

---

## 🏆 Partner Prize Categories Alignment

Ghost Threads was intentionally architected around the official challenge sponsor technologies, pairing each with a genuine, demonstrable role:

- **Best Use of Gemma ($200):** Google Gemma 2 (2B) runs 100% locally in RAM via Ollama (`localhost:11434`) for zero-leakage commitment extraction, confidence scoring, and temporal anchor parsing across English and Hinglish vernacular.
- **Best Use of TabPFN ($200):** Prior Labs' TabPFN tabular foundation model evaluates **Unresolved Commitment Risk** using a 6-dimensional feature vector via in-context learning in a single forward pass without overfitting on small datasets.
- **Best Use of Render ($200):** Fast, global, zero-cold-start hosting of the interactive Web Audio & WebGL candlelit ofrenda presentation layer with zero server-side chat storage.
- **Best Use of ElevenLabs ($100):** High-fidelity multilingual voice narration (Hindi-English mix) in the video walkthrough explaining the technical pipeline, privacy rationale, and emotional mission.

---

## Live Links & Code

- **Live Altar (Hosted on Render):** [https://ghost-threads.onrender.com/](https://ghost-threads.onrender.com/)
- **GitHub Repository:** [https://github.com/roshni09mishra-0/ghost-threads](https://github.com/roshni09mishra-0/ghost-threads)
- **Alternate Mirror (GitHub Pages):** [https://roshni09mishra-0.github.io/ghost-threads/](https://roshni09mishra-0.github.io/ghost-threads/)
- **YouTube Walkthrough:** [https://youtu.be/0mPuCKG99-4](https://youtu.be/0mPuCKG99-4)

---

## Why this refuses to be a cloud service

The first engineering rule for this project was simple: **zero cloud calls, zero external API keys.**

Private chat exports are probably the most personal files sitting on any person's hard drive. They contain passwords sent in panic, doctor appointments, late-night arguments, and family discussions. There was zero chance I was going to write a script that sends raw chat text to a third-party proprietary API. 

The entire extraction pipeline had to run completely on-device, air-gapped, using open-weight models.

![Ghost Threads Altar Showcase](https://raw.githubusercontent.com/roshni09mishra-0/ghost-threads/main/screenshots/ghost_threads_showcase.png)

---

## Complete Multi-Stage AI Architecture

```
[ WhatsApp / Signal Export (.txt) ]
               │
               ▼
   Regex Parser (iOS, Android, Signal timestamps)
               │
               ▼
   STAGE 1: Google Gemma 2 (2B Local via Ollama)
   (Extracts: Promise Text, Sender, Date, Temporal Anchor, Confidence)
               │
               ▼
   STAGE 2: Multi-Turn Context Analysis
   (Identifies: Deadline Passed, Follow-Up Detected, Resolution Status, Sarcasm Filter)
               │
               ▼
   STAGE 3: Prior Labs TabPFN (Tabular Foundation Model)
   (In-context classification: Evaluates 6-Feature Vector -> Unresolved Commitment Risk)
               │
               ▼
   STAGE 4: Ghost State Classification
   (Restless Spirit, Fading Spirit, Resolved, False Alarm)
               │
               ▼
   Render Static Site (Interactive Ofrenda Web App & The Resurrection Moment)
```

### 1. Ingesting messy chat formats
Chat exports are wildly inconsistent depending on whether they come from iOS or Android:
- iOS WhatsApp: `[15/09/23, 23:14:02] You: I'll review before midnight.`
- Android WhatsApp: `15/09/2023, 11:14 pm - You: Will send tomorrow.`
- Signal: `[2023-09-15 23:14:02] You: I will push the branch.`

The parser handles multi-line continuations and isolates messages sent by you, feeding only your outgoing promises down the pipeline.

### 2. Extracting commitments with Google Gemma 2 (2B)
To spot commitments across mixed English and casual Hinglish ("kal sham tak bhejta hoon pakka"), I used **Gemma 2 (2B)** running locally in memory through Ollama (`localhost:11434`). 

Gemma is lightweight enough to run smoothly on a laptop without bogging down the CPU. We pass it a structured prompt:

```python
prompt = (
    "Analyze if this message contains a commitment or promise. "
    "Reply strictly with JSON: {\"is_promise\": true/false, \"anchor\": \"<time_period>\"}\n"
    f"Message: \"{content}\""
)
```

Gemma strips away the conversational filler and pulls out the commitment together with the temporal anchor ("before midnight", "tomorrow", "this weekend"). If Ollama isn't running, the script seamlessly falls back to a built-in heuristic regex matcher (10,400+ samples/sec) so the CLI never crashes.

### 3. Why TabPFN? (Predicting Technical Risk, Not Guessing Feelings)
Judges often ask: *Why use a tabular foundation model instead of a simple formula or a random forest?*

Here is the engineering reality:
1. **The Small-Sample Limitation of Classical ML:** Traditional classifiers (Random Forests, XGBoost, MLPs) require hundreds or thousands of labeled rows to tune decision boundaries without catastrophic overfitting. In private chat logs, a user may only have 30–80 unkept promises.
2. **Prior-Data Fitted Networks:** TabPFN by Prior Labs is an in-context learning tabular transformer pre-trained offline on synthetic causal Bayesian priors. It performs tabular inference in a single forward pass without iterative gradient descent.
3. **Objective Technical Features:** TabPFN doesn't pretend to read human minds or guess guilt. It evaluates an objective 6-dimensional feature vector:
   - `days_since_commitment`: Temporal distance in days.
   - `deadline_passed`: Binary flag (1 if anchor elapsed, 0 if still future).
   - `follow_up_detected`: Binary flag (1 if recipient pinged, 0 otherwise).
   - `resolution_status`: Binary flag (1 if resolved/cancelled, 0 if active unkept).
   - `commitment_urgency`: Weight derived from anchor (e.g. *midnight/asap* = 1.5, *someday* = 0.5).
   - `message_confidence`: Extraction confidence score from Gemma (0.0 to 1.0).

```python
from tabpfn import TabPFNClassifier
import numpy as np

clf = TabPFNClassifier(device='cpu')

# 6-Feature vector: [days, deadline_passed, follow_up, resolution, urgency, confidence]
X_train, y_train = generate_synthetic_tabpfn_prior(n_samples=100)
X_test = np.array([[412.0, 1.0, 0.0, 0.0, 1.5, 0.98]])

clf.fit(X_train, y_train)
unresolved_risk = float(clf.predict_proba(X_test)[0][1]) # e.g. 0.95
```

- A promise like *"I'll review the pull request before midnight"* that is 412 days cold with zero follow-up or resolution gets assigned a maximum risk score of `0.95` (**Restless Spirit**).
- If a resolution message was detected or marked fulfilled, TabPFN drops the risk to `0.05` (**Resolved**).

### 4. Hosting the front end on Render
The front end is deployed on **Render** as a static site at [ghost-threads.onrender.com](https://ghost-threads.onrender.com).

Deploying as a static site on Render gave us instantaneous loading with zero cold starts, continuous deployment from GitHub, and global SSL without running unnecessary server processes.

![Interactive Altar](https://raw.githubusercontent.com/roshni09mishra-0/ghost-threads/main/screenshots/ghost_threads_altar.png)

---

## 🕯️ The Resurrection Moment & Altar Features

Rather than just showing a passive table of shame, the web interface gives users real closure:

1. **The Resurrection Moment (3 Interactive Actions):**
   - **Fulfill:** You finally do the task right now. Clicking "Fulfill" converts the restless ghost into an honorable closure with an emerald resolution receipt.
   - **Apologize:** Generates a blunt, honest, non-defensive apology draft ("Maafi-Nama") ready to paste.
   - **Release Spirit:** You accept that the moment has passed and let the promise go. Lighting a terracotta diya fades the spirit peacefully from the ledger.
2. **🟢 Local Processing Verified Badge:** An active visual audit indicator confirming that chat ingestion, Gemma inference, and TabPFN scoring occurred strictly on the client/local runtime with 0 outbound telemetry packets.
3. **AI Trace Inspector (Explainability):** Click the "AI Trace Inspector" button on any ghost card to inspect the exact internal tensors across all 4 stages: Gemma extraction confidence, temporal anchor, the 6-feature TabPFN vector, and the decision boundary.
4. **Living Calavera Eyes:** The sugar skull illustrations on the altar physically track your mouse cursor across the screen in real time.
5. **The Séance Theater:** Clicking "Séance shuru karo" on any ghost card triggers a retro chat window that replays the exact original conversation line-by-line until the ghost manifests.
6. **Web Audio Synthesizer:** A built-in synthesizer uses the Web Audio API to create the sound of 2 AM rain and flickering candle crackles natively in the browser without loading heavy audio files.

---

## Benchmark results and privacy verification

Rather than relying on vague claims, we built a formal benchmark script (`python benchmark.py`) evaluating the extraction pipeline across **84 ground-truth labeled samples** spanning English, Hinglish, casual banter, explicit sarcasm, and negated commitments:

| Metric | Score | Note |
| :--- | :--- | :--- |
| **Accuracy** | **95.24%** | 80/84 correct classifications |
| **Precision** | **100.00%** | Zero false positives (banter & jokes cleanly suppressed) |
| **Recall** | **92.00%** | Catches 46/50 actual unkept commitments |
| **F1-Score** | **95.83%** | Harmonic balance between precision and recall |
| **Throughput** | **10,400+ samples/sec** | Sub-millisecond latency on standard CPU |
| **Test Suite** | **15/15 Passing** | Unit, integration & air-gap socket isolation tests (`test_backend.py`) |

### Demonstrable Air-Gap Privacy Audit
To prove that zero chat logs leave your device, run the automated isolation audit:

```bash
python ghost_threads.py --network-audit
```

**Terminal Output:**
```
====================================================================
 [VERIFIED] PRIVACY VERIFICATION BADGE // 100% LOCAL PROCESSING AUDIT
====================================================================
 [OK] Chat Ingestion:    100% On-Device (Zero cloud uploads)
 [OK] LLM Inference:     Local Google Gemma 2 (Ollama / Local RAM)
 [OK] Tabular AI:        TabPFN In-Context Learning (Local CPU/GPU)
 [OK] External AI APIs:  None (Zero calls to OpenAI, Claude, etc.)
 [OK] Network Sockets:   0 External outbound packets
 [OK] Ephemeral Data:    Temporary embeddings wiped on process exit
 [OK] Cloud Keys:        Zero (0) required
====================================================================
```

### Where the parser still stumbles (The Sarcasm Problem)
I want to be completely honest about where the system struggled: **sarcasm**.

In group chats with close friends, Gemma initially flagged dry sarcastic banter as high-priority commitments. When a friend complained about bills and I replied *"sure, I will buy you a private island on Friday"*, Gemma flagged it as an unkept promise with a Friday time anchor. We added an active sarcasm suppression filter to eliminate these edge cases and protect precision.

---

## Try it on your own chats

You can clone the repo and audit your own chat archives locally:

```bash
# Clone the repository
git clone https://github.com/roshni09mishra-0/ghost-threads.git
cd ghost-threads

# Run the 15 automated tests
python test_backend.py

# Run the 84-sample benchmark report
python benchmark.py

# Verify 100% open-source challenge compliance & air-gap audit
python ghost_threads.py --network-audit

# Scan a sample chat export
python ghost_threads.py sample_whatsapp.txt
```

To run with your own WhatsApp logs: open WhatsApp on your phone, export any chat without media as `.txt`, and pass the file to `python ghost_threads.py your_chat.txt`.

---

## Final thought

We spend half our lives inside text messages, making casual promises we genuinely intend to keep in the moment. When they slip away, nobody holds a trial. But having an offline altar that mirrors those forgotten words back to you is a surprisingly grounding reminder to respect other people's time.

Keep your promises, or light a candle and let them rest.
