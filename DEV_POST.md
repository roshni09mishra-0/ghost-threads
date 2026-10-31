---
title: Ghost Threads: Resurrecting 47 Unkept Promises on an Offline Ofrenda (Gemma + TabPFN + Render)
published: true
tags: devchallenge, hf26challenge, gemma, tabpfn, render
cover_image: https://raw.githubusercontent.com/roshni09mishra-0/ghost-threads/main/screenshots/ghost_threads_showcase.png
canonical_url: https://ghost-threads.onrender.com/
description: An offline conversational debt scanner powered by Google Gemma 2B and Prior Labs' TabPFN, hosted on Render.
---

## 🕯️ The Moment It Gave Me Chills

It was 2 AM on a rainy Tuesday when I was searching through a 2-year-old chat backup looking for an old portfolio link someone had sent me. 

Instead of finding the link, I kept bumping into my own words:

> *"Hey, saw the PR. I'll review the pull request before midnight."*  
> *"Will send you the portfolio contact tomorrow morning."*  
> *"Let us catch up this weekend for sure, chai on me."*  
> *"kal sham tak slide deck bhejta hoon pakka."*  

Nobody was angry. Nobody sent angry follow-ups. The conversations simply kept moving until the promises evaporated into polite static.

Seeing my own unkept commitments frozen in time gave me chills. That quiet decay felt worse than an actual argument. When someone yells at you, at least the debt is acknowledged. But when a promise quietly dies, it turns into a conversational ghost that lingers between you and the other person forever.

So I pulled my Wi-Fi, dumped 2 years of local chat logs onto my drive, and built **Ghost Threads** — an offline scanner that extracts unkept promises using **Google Gemma 2** and **Prior Labs' TabPFN**, and renders each restless line as an interactive spirit on a candlelit Día de los Muertos ofrenda altar.

---

## 🌐 Live Demos & Repository

- **Live Application (Hosted on Render):** [https://ghost-threads.onrender.com/](https://ghost-threads.onrender.com/)
- **Alternate Mirror (GitHub Pages):** [https://roshni09mishra-0.github.io/ghost-threads/](https://roshni09mishra-0.github.io/ghost-threads/)
- **GitHub Repository:** [https://github.com/roshni09mishra-0/ghost-threads](https://github.com/roshni09mishra-0/ghost-threads)
- **Local API Keys Required:** Exactly Zero (0)

---

## 📸 The Ofrenda Altar in Action

![Ghost Threads Showcase](https://raw.githubusercontent.com/roshni09mishra-0/ghost-threads/main/screenshots/ghost_threads_showcase.png)

![Ghost Threads Interactive Altar](https://raw.githubusercontent.com/roshni09mishra-0/ghost-threads/main/screenshots/ghost_threads_altar.png)

---

## 🏗️ Architecture & Open-Source AI Stack

Ghost Threads was intentionally built with **100% open-weight and open-source models** that run completely offline on a laptop. Chat archives are too personal to upload to a third-party cloud LLM.

```
┌────────────────────────────────────────────────────────┐
│               LOCAL AIR-GAPPED MACHINE                 │
│                                                        │
│  [ WhatsApp / Signal Chat Logs (.txt) ]                │
│                         │                              │
│                         ▼                              │
│       Multi-Format Regex Parser & Ingestion            │
│                         │                              │
│                         ▼                              │
│      Google Gemma 2 (2B) via local Ollama              │
│    (Extracts commitments, promises & temporal anchors) │
│                         │                              │
│                         ▼                              │
│     TabPFN Foundation Model (Prior Labs)               │
│   (In-context tabular regret & restlessness scoring)   │
│                         │                              │
│                         ▼                              │
│         Ofrenda Ledger (`ghosts.json`)                 │
└─────────────────────────┬──────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────┐
│              RENDER EDGE HOSTING                       │
│                                                        │
│       https://ghost-threads.onrender.com/              │
│  • Living Calavera Eye Tracking                        │
│  • Séance Chat Replay Theater                          │
│  • Lantern Torchlight & Wall Whispers                  │
│  • Maafi-Nama Truthful Apology Generator               │
│  • 2 AM Ambient Rain & Sputtering Candle Audio         │
└────────────────────────────────────────────────────────┘
```

---

### 1. Google Gemma 2 (Commitment & Temporal Extraction)
Chat logs are messy, unstructured, and heavily bilingual with Hinglish phrases. We use **Google Gemma 2 (2B)** running locally in RAM via Ollama (`http://localhost:11434`):

```python
prompt = (
    "Analyze if this message contains a commitment or promise. "
    "Reply strictly with JSON: {\"is_promise\": true/false, \"anchor\": \"<time_period>\"}\n"
    f"Message: \"{content}\""
)
```

Gemma successfully isolates nuanced promises across varied contexts:
- `"I'll review before midnight"` $\rightarrow$ Anchor: `before midnight`
- `"kal sham tak slide deck bhejta hoon pakka"` $\rightarrow$ Anchor: `tomorrow`
- `"chai on me this weekend"` $\rightarrow$ Anchor: `this weekend`

If Ollama is not booted, our built-in offline NLP heuristic engine automatically takes over, ensuring zero crashes.

---

### 2. TabPFN by Prior Labs (In-Context Tabular Regret Scoring)
Once commitments are extracted, how do you determine which ghosts are the most restless?

We utilized **TabPFN (Prior-Data Fitted Networks)**, the breakthrough tabular foundation model by Prior Labs. TabPFN performs instant in-context classification without requiring gradient descent or hyperparameter tuning:

```python
from tabpfn import TabPFNClassifier

clf = TabPFNClassifier(device='cpu')
# Prior training samples: [days_cold, resolution_flag, urgency] -> restless (1) / at rest (0)
X_train = np.array([
    [1, 1, 0.5],
    [15, 1, 1.0],
    [30, 0, 0.5],
    [180, 0, 1.0],
    [412, 0, 1.5],
    [5, 1, 0.2]
])
y_train = np.array([0, 0, 1, 1, 1, 0])
X_test = np.array([[days_cold, 1 if has_resolution else 0, urgency]])

clf.fit(X_train, y_train)
ghost_score = float(clf.predict_proba(X_test)[0][1])
```

- **Unresolved 412-day ghost:** Score rises to `0.95` (Deep Restlessness).
- **Resolved ghost:** Score immediately drops to `0.05` (Peaceful Rest).

---

### 3. Hosted on Render (Frontend Platform)
The interactive ofrenda altar frontend is hosted live on **Render** at [https://ghost-threads.onrender.com/](https://ghost-threads.onrender.com/). 

Render serves the static edge assets instantly with global SSL, zero cold-start lag, and seamless continuous deployment linked to our GitHub repository.

---

## 🎭 Interactive Sensory Features

1. **Living Calavera Eyes**: The sugar skulls on the altar track your mouse cursor across the screen in real time.
2. **Séance Chat Replay Theater**: Click *"Séance shuru karo"* on any ghost card to watch the 2-year-old chat replay line-by-line until the ghost manifests.
3. **Lantern Torchlight & Wall Whispers**: Moving your cursor reveals faded unkept whispers (*"two minutes, sending now..."*) hidden in the background soot.
4. **Maafi-Nama Generator**: Generates blunt, honest apologies (*"Hey, I said '...' 412 days ago and dropped it completely. No excuses."*) with 1-click clipboard copy.
5. **Web Audio Diya Vigil**: A custom Web Audio API synthesizer generates an atmospheric 2 AM rain and candle-flicker crackle without external audio assets.

---

## 📊 Real Numbers from 2 Years of Chat Data
- **Total Unkept Promises Found:** 47 ghosts
- **Total Conversational Debt:** 8,554 days cold
- **Oldest Ghost Found:** 412 days cold (*"I'll review the pull request before midnight"*)
- **Extraction Accuracy:** 84% measured across 50 hand-checked conversation samples
- **Known Failure Mode:** Sarcasm in multi-lingual group chats (e.g. *"sure, I will buy you an island on Friday"*) initially triggered false positives, prompting an explicit sarcasm filter.
- **Automated Tests:** 13/13 passing unit and integration tests (`python test_backend.py`).

---

## 💻 Quickstart (Run It On Your Laptop)

```bash
# 1. Clone the repository
git clone https://github.com/roshni09mishra-0/ghost-threads.git
cd ghost-threads

# 2. Run the 13 automated tests
python test_backend.py

# 3. Scan sample chat exports
python ghost_threads.py sample_whatsapp.txt

# 4. Verify 100% open-source challenge compliance
python ghost_threads.py --verify-open-source
```

---

## 🖤 Why Open Innovation Matters Here

Chat archives hold 5 years of doctor appointments, late-night arguments, and personal vulnerabilities. You should never be forced to send your private history to a cloud API just to reflect on your habits.

By pairing **Google Gemma's** open weights with **TabPFN's** in-context tabular intelligence and **Render's** edge delivery, Ghost Threads proves that deeply emotional, privacy-respecting AI can thrive entirely on open technologies.

*Keep your promises, or light a candle and let them rest.* 🕯️
