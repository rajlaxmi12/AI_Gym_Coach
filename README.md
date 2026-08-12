# 🏋️ AI Real-Time Gym Coach

> **Your personal AI-powered workout companion that sees, understands, counts, and coaches your movements in real time.**

An intelligent computer-vision-based fitness coaching platform that uses **MediaPipe Pose Landmarker, OpenCV, WebRTC, and Generative AI** to analyze exercise form, count repetitions, detect movement errors, track workout metrics, and provide real-time personalized coaching feedback.

The application transforms a regular webcam into an **AI fitness coach** capable of monitoring exercises such as squats, push-ups, biceps curls, shoulder presses, and lunges.

---

## ✨ Features

### 🎥 Real-Time Pose Detection

- Real-time webcam video processing
- Human body landmark detection using MediaPipe
- Frame-by-frame movement analysis
- Exercise-specific pose interpretation
- Browser-based camera streaming using WebRTC

### 🏋️ Exercise Recognition & Rep Counting

Currently supported exercises:

- 🦵 Squats
- 💪 Push-ups
- 💪 Biceps Curls
- 🏋️ Shoulder Press
- 🦵 Lunges

Each exercise has dedicated detection logic for:

- Rep counting
- Movement phases
- Joint-angle analysis
- Form validation
- Incorrect movement detection
- Exercise-state tracking

### 🧠 AI-Powered Coaching

The system integrates a Large Language Model to transform detected workout events into natural coaching feedback.

The AI coach provides:

- Exercise form corrections
- Motivational feedback
- Movement-error explanations
- Context-aware coaching
- Personalized workout guidance

### 🔊 Voice Feedback

The application includes text-to-speech capabilities so users can receive coaching without constantly looking at the screen.

```text
Exercise Event
      ↓
Movement Analysis
      ↓
AI Coach
      ↓
Feedback Text
      ↓
Text-to-Speech
      ↓
Voice Feedback
