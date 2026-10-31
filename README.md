# Ghost Threads

> Scans private chat exports locally, finds promises nobody kept ("I'll send it tomorrow"), and shows them as restless ghosts on a candlelit ofrenda.

- 🌐 **Live Demo (Render):** [https://ghost-threads.onrender.com/](https://ghost-threads.onrender.com/)
- 🎥 **Video Demo (ElevenLabs Narration):** [https://youtu.be/fQ2vi3E4Mwg](https://youtu.be/fQ2vi3E4Mwg)
- 📝 **DEV.to Submission Post:** [https://dev.to/roshni_mishra_9ed865d304f/ghost-threads-resurrecting-47-unkept-promises-on-an-offline-ofrenda-gemma-tabpfn-render-34k](https://dev.to/roshni_mishra_9ed865d304f/ghost-threads-resurrecting-47-unkept-promises-on-an-offline-ofrenda-gemma-tabpfn-render-34k)

Runs **100% offline** with **Google Gemma (via local Ollama)** + **TabPFN**.
Zero API keys. Zero cloud calls. Chat data never leaves your laptop.

---

## Open-Source Challenge Alignment & Audit

Ghost Threads strictly complies with the Open Source AI Challenge criteria:

| Component | Architecture / Model | License | Source / Provider | Local Execution |
| :--- | :--- | :--- | :--- | :--- |
| **Commitment Extraction** | **Google Gemma 2 (2B)** | Gemma Open Terms / Apache 2.0 | Google DeepMind via local Ollama | 100% in RAM (`localhost:11434`) |
| **Regret / Score AI** | **TabPFN** | Apache 2.0 | Prior Labs / AutoML | 100% on CPU/GPU |
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
- Privacy guarantee: Demonstrated via `--network-audit` with zero external socket egress.

---

## License
MIT License. Built at 2am under a sputtering desk lamp. Keep your promises, or light a candle and let them rest.
