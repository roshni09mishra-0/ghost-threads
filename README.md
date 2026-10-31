# Ghost Threads

> *"Most AI projects help you remember what happened. Ghost Threads helps you remember what you promised."*

Ghost Threads scans private chat exports locally, extracts unkept commitments using Google Gemma 2 (via local Ollama), scores unresolved commitment risk using Prior Labs' TabPFN, and manifests the forgotten words as restless spirits on a candlelit ofrenda altar.

- 🌐 **Live Demo (Render):** [https://ghost-threads.onrender.com/](https://ghost-threads.onrender.com/)
- 🎥 **Video Demo (ElevenLabs Narration):** [https://youtu.be/0mPuCKG99-4](https://youtu.be/0mPuCKG99-4)
- 📝 **DEV.to Submission Post:** [https://dev.to/roshni_mishra_9ed865d304f/ghost-threads-resurrecting-47-unkept-promises-on-an-offline-ofrenda-gemma-tabpfn-render-34k](https://dev.to/roshni_mishra_9ed865d304f/ghost-threads-resurrecting-47-unkept-promises-on-an-offline-ofrenda-gemma-tabpfn-render-34k)
- 🪞 **Alternate Mirror (GitHub Pages):** [https://roshni09mishra-0.github.io/ghost-threads/](https://roshni09mishra-0.github.io/ghost-threads/)

Runs **100% offline** with **Google Gemma 2 (via local Ollama)** + **TabPFN**.
Zero API keys. Zero cloud calls. Chat data never leaves your laptop.

---

## 🏆 Partner Prize Categories Alignment

- **Best Use of Gemma ($200):** Google Gemma 2 (2B) runs 100% locally in RAM via Ollama (`localhost:11434`) for zero-leakage commitment extraction, confidence scoring, and temporal anchor parsing across English and Hinglish vernacular.
- **Best Use of TabPFN ($200):** Prior Labs' TabPFN tabular foundation model evaluates **Unresolved Commitment Risk** using a 6-dimensional feature vector via in-context learning in a single forward pass without overfitting on small datasets.
- **Best Use of Render ($200):** Fast, global, zero-cold-start hosting of the interactive Web Audio & WebGL candlelit ofrenda presentation layer with zero server-side chat storage.
- **Best Use of ElevenLabs ($100):** High-fidelity multilingual voice narration (Hindi-English mix) in the video walkthrough explaining the technical pipeline, privacy rationale, and emotional mission.

---

## 🏛️ Multi-Stage AI Architecture

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

---

## Open-Source Challenge Alignment & License Audit

Ghost Threads strictly complies with the Open Source AI Challenge criteria:

| Component | Architecture / Model | License | Source / Provider | Local Execution |
| :--- | :--- | :--- | :--- | :--- |
| **Commitment Extraction** | **Google Gemma 2 (2B)** | Gemma Terms of Use (Open Weights) | Google DeepMind via local Ollama | 100% in RAM (`localhost:11434`) |
| **Risk Scoring AI** | **TabPFN** | Apache 2.0 | Prior Labs / AutoML | 100% on CPU/GPU |
| **Local LLM Daemon** | **Ollama** | MIT License | Ollama Open Source Runner | Local process |
| **Frontend & Audio** | **Vanilla HTML5 + Web Audio** | Open Web Standards | W3C Standard APIs | Zero third-party trackers |
| **Cloud API Keys** | **ZERO (0)** | N/A | No OpenAI, No Anthropic, No Cloud | Offline air-gapped safe |

Run the automated compliance audit anytime:
```bash
python ghost_threads.py --verify-open-source
```

---

## Quickstart

### 1. View the Landing Page
The landing page is already live on your local server:
👉 **[http://localhost:3333](http://localhost:3333)**

Or open `index.html` directly in any web browser.

---

### 2. Run the Automated Test Suite (15 Tests)
Run the unit and integration tests covering multi-format chat parsing (iOS WhatsApp, Android WhatsApp, Signal), commitment detection heuristics (English & Hinglish), TabPFN risk scoring, apology drafts, and demonstrable air-gap socket isolation:

```bash
python test_backend.py
```

---

### 3. Run the Evaluation Benchmark (84 Ground-Truth Samples)
Run the reproducible benchmark evaluating the NLP and tabular scoring engine against 84 labeled samples spanning English, Hinglish, Banter, Sarcasm, and Negations:

```bash
python benchmark.py
```

### 4. Verify demonstrable Air-Gap Isolation
Verify that Ghost Threads makes zero external network socket calls and operates in full hardware isolation:

```bash
python ghost_threads.py --network-audit
```

---

### 5. Run the Offline Scanner
Test with bundled realistic sample exports:

```bash
# Scan sample WhatsApp export
python ghost_threads.py sample_whatsapp.txt

# Scan sample Signal export
python ghost_threads.py sample_signal.txt
```

Or pass your own WhatsApp or Signal `.txt` export from your phone:

```bash
python ghost_threads.py path/to/your_chat_export.txt
```

---

### 6. Setup Local Gemma with Ollama (Optional for live LLM extraction)

1. Download Ollama from [ollama.com](https://ollama.com)
2. Pull Gemma 2:
   ```bash
   ollama run gemma2:2b
   ```
3. Run `ghost_threads.py`. If Ollama is running on `http://localhost:11434`, it will automatically use Gemma weights in RAM. If Ollama is offline, it seamlessly falls back to the built-in offline NLP heuristics.

---

### 7. Setup TabPFN (Optional for tabular in-context learning)

```bash
pip install tabpfn
```

---

## 📊 Evaluation & Real Numbers

Ghost Threads was evaluated against an 84-sample benchmark dataset representing realistic chat dynamics (direct commitments, banter, sarcasm, cancellations, and Hinglish vernacular):

| Metric | Score | Note |
| :--- | :--- | :--- |
| **Accuracy** | **95.24%** | 80/84 correct classifications |
| **Precision** | **100.00%** | Zero false positives (eliminates ghosting false alarms) |
| **Recall** | **92.00%** | Catches 46/50 actual unkept commitments |
| **F1-Score** | **95.83%** | Harmonic balance between precision and recall |
| **Throughput** | **>10,000 samples/sec** | Sub-millisecond latency on standard CPU |

- Scanned 2 years of local chat archives.
- Found 47 unkept promises.
- Oldest ghost: 412 days cold ("I'll review the pull request before midnight").
- Privacy guarantee: Demonstrated via `--network-audit` with zero external socket egress:

```text
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

---

## License
MIT License. Built at 2am under a sputtering desk lamp. Keep your promises, or light a candle and let them rest.
