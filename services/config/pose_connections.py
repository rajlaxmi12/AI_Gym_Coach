# Pose skeleton connections for MediaPipe PoseLandmarker.
# Each tuple is (start_landmark_index, end_landmark_index).
# Indices follow MediaPipe Pose landmark ordering.

# MediaPipe Pose has 33 landmarks.
# Reference: https://developers.google.com/mediapipe/solutions/pose#pose-landmark-model

POSE_CONNECTIONS = [
    (11, 13), (13, 15),  # Left arm
    (12, 14), (14, 16),  # Right arm
    (11, 23), (12, 24),  # Shoulders to hips
    (23, 24),            # Hips
    (23, 25), (25, 27), # Left leg
    (24, 26), (26, 28), # Right leg
    (27, 29), (28, 30), # Left/Right knee to ankle/foot base
    (29, 31), (30, 32), # Left/Right foot to toes
    (15, 21), (16, 20),  # Wrists to face/mid? (extra stability)
    (21, 17), (17, 19),  # Face/neck region connections
    (22, 18), (18, 20),  # Face/neck region connections
]

