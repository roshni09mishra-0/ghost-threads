"""
Unit & Integration Test Suite for Ghost Threads Backend
Validates chat parsing, commitment detection, TabPFN scoring,
apology generation, and Open-Source Challenge compliance.
"""

import os
import json
import unittest
from datetime import datetime
from ghost_threads import (
    parse_timestamp,
    parse_chat_lines,
    heuristic_promise_detector,
    evaluate_tabpfn_ghost_score,
    generate_maafi_nama,
    scan_chats,
    OPEN_SOURCE_MANIFEST
)

class TestChatParser(unittest.TestCase):
    def test_ios_whatsapp_format(self):
        text = "[15/09/23, 23:14:02] You: I'll review before midnight."
        messages = parse_chat_lines(text)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["sender"], "You")
        self.assertEqual(messages[0]["content"], "I'll review before midnight.")
        self.assertEqual(messages[0]["datetime"].year, 2023)
        self.assertEqual(messages[0]["datetime"].month, 9)
        self.assertEqual(messages[0]["datetime"].day, 15)

    def test_android_whatsapp_format(self):
        text = "12/05/2024, 6:30 pm - You: Will send the portfolio tomorrow."
        messages = parse_chat_lines(text)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["sender"], "You")
        self.assertEqual(messages[0]["datetime"].hour, 18)
        self.assertEqual(messages[0]["datetime"].minute, 30)

    def test_signal_iso_format(self):
        text = "[2023-09-15 23:14:02] You: I will push the bugfix branch."
        messages = parse_chat_lines(text)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["sender"], "You")
        self.assertEqual(messages[0]["datetime"].year, 2023)

    def test_multiline_continuation(self):
        text = (
            "[15/09/23, 23:14:02] You: Starting the draft now.\n"
            "Will share the link shortly.\n"
            "Chai on me this weekend."
        )
        messages = parse_chat_lines(text)
        self.assertEqual(len(messages), 1)
        self.assertIn("Will share the link shortly", messages[0]["content"])
        self.assertIn("Chai on me", messages[0]["content"])

class TestPromiseDetector(unittest.TestCase):
    def test_english_promises(self):
        is_p, anchor = heuristic_promise_detector("I'll review the pull request before midnight.")
        self.assertTrue(is_p)
        self.assertEqual(anchor, "before midnight")

        is_p, anchor = heuristic_promise_detector("Will send you the portfolio tomorrow morning.")
        self.assertTrue(is_p)
        self.assertEqual(anchor, "tomorrow")

    def test_hinglish_promises(self):
        is_p, anchor = heuristic_promise_detector("kal sham tak slide deck bhejta hoon pakka")
        self.assertTrue(is_p)
        self.assertEqual(anchor, "tomorrow")

        is_p, anchor = heuristic_promise_detector("pakka weekend pe call karta hu for code review")
        self.assertTrue(is_p)
        self.assertEqual(anchor, "this weekend")

    def test_non_promises(self):
        is_p, _ = heuristic_promise_detector("ha theek hai")
        self.assertFalse(is_p)

        is_p, _ = heuristic_promise_detector("Good morning, reaching office in 5 mins")
        self.assertFalse(is_p)

        is_p, _ = heuristic_promise_detector("Merged it anyway.")
        self.assertFalse(is_p)

    def test_negated_commitments(self):
        is_p, _ = heuristic_promise_detector("I can't send the deck tonight, busy with errands.")
        self.assertFalse(is_p)

        is_p, _ = heuristic_promise_detector("aaj nahi kar paunga bhai")
        self.assertFalse(is_p)

class TestTabPFNScorer(unittest.TestCase):
    def test_score_bounds(self):
        score_new = evaluate_tabpfn_ghost_score(days_cold=5, has_resolution=False)
        score_old = evaluate_tabpfn_ghost_score(days_cold=412, has_resolution=False)
        self.assertGreaterEqual(score_new, 0.0)
        self.assertLessEqual(score_new, 1.0)
        self.assertGreaterEqual(score_old, 0.0)
        self.assertLessEqual(score_old, 1.0)
        self.assertGreaterEqual(score_old, score_new)

    def test_resolved_promise(self):
        score_resolved = evaluate_tabpfn_ghost_score(days_cold=412, has_resolution=True)
        self.assertLessEqual(score_resolved, 0.1)

class TestApologyGenerator(unittest.TestCase):
    def test_maafi_nama_structure(self):
        draft = generate_maafi_nama("review PR tonight", 412, "Alex")
        self.assertIn("Alex", draft)
        self.assertIn("412", draft)
        self.assertIn("review PR tonight", draft)
        self.assertIn("No excuses", draft)

class TestOpenSourceCompliance(unittest.TestCase):
    def test_manifest_requirements(self):
        self.assertTrue(OPEN_SOURCE_MANIFEST["zero_cloud_keys"])
        components = OPEN_SOURCE_MANIFEST["components"]
        names = [c["name"] for c in components]
        self.assertTrue(any("Gemma" in n for n in names))
        self.assertTrue(any("TabPFN" in n for n in names))
        
        # Verify no component calls cloud
        for c in components:
            self.assertFalse(c["cloud_call"], f"{c['name']} must be local offline")

    def test_air_gap_privacy_verification(self):
        from ghost_threads import verify_air_gap_isolation
        audit = verify_air_gap_isolation()
        self.assertEqual(audit["status"], "AIR_GAP_VERIFIED")
        self.assertEqual(audit["external_endpoints_called"], 0)
        self.assertEqual(len(audit["cloud_api_keys_in_env"]), 0)

    def test_synthetic_tabpfn_prior_structure(self):
        from ghost_threads import generate_synthetic_tabpfn_prior
        X, y = generate_synthetic_tabpfn_prior(n_samples=100)
        self.assertEqual(X.shape[0], 100)
        self.assertEqual(X.shape[1], 3) # [days_cold, has_resolution, urgency]
        self.assertEqual(len(y), 100)
        # Verify binary classification targets
        self.assertTrue(set(y).issubset({0, 1}))

class TestEndToEndScanner(unittest.TestCase):
    def test_scan_sample_export(self):
        curr_dir = os.path.dirname(__file__)
        sample_path = os.path.join(curr_dir, "sample_whatsapp.txt")
        out_path = os.path.join(curr_dir, "test_output_ghosts.json")
        
        ghosts = scan_chats(sample_path, out_path)
        self.assertGreaterEqual(len(ghosts), 4)
        self.assertTrue(os.path.exists(out_path))
        
        # Verify JSON structure
        with open(out_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), len(ghosts))
            for item in data:
                self.assertIn("promise", item)
                self.assertIn("days_cold", item)
                self.assertIn("ghost_score", item)
                self.assertIn("apology_draft", item)
                
        # Clean up test output
        if os.path.exists(out_path):
            os.remove(out_path)

if __name__ == "__main__":
    unittest.main(verbosity=2)
