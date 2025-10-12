"""
Quick test script to explore vision-agent capabilities for video analysis
"""

import vision_agent.tools as T
import os

def test_horse_tracking(video_path: str, output_path: str):
    """
    Test vision-agent's ability to track and segment a horse in video

    Args:
        video_path: Path to input video file
        output_path: Path to save processed video
    """

    # Check if video exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return None

    print(f"Video found: {video_path}")

    # Step 1: Extract frames from video
    print("Extracting frames from video...")
    frames_and_ts = T.extract_frames_and_timestamps(video_path)
    frames = [f["frame"] for f in frames_and_ts]

    print(f"Extracted {len(frames)} frames")

    # Sample only 10 frames to reduce API calls
    step = max(1, len(frames) // 10)
    sampled_frames = frames[::step][:10]
    print(f"Sampling to {len(sampled_frames)} frames to avoid rate limits")

    # Step 2: Track the horse
    print("\nTracking horse in video...")
    tracks = T.countgd_sam2_video_tracking("horse", sampled_frames)

    print(f"Tracking result type: {type(tracks)}")
    print(f"Number of detections: {len(tracks) if tracks else 0}")

    if tracks:
        print(f"First few tracks: {tracks[:2] if len(tracks) > 2 else tracks}")

        # Step 3: Visualize the results
        print("\nOverlaying segmentation masks...")
        viz = T.overlay_segmentation_masks(sampled_frames, tracks)

        # Step 4: Save the annotated video
        print(f"Saving video to {output_path}...")
        T.save_video(viz, output_path)

        print(f"✓ Success! Tracked video saved to: {output_path}")
        return tracks
    else:
        print("✗ No horse detected in video")
        return None


if __name__ == "__main__":
    # Example usage - update these paths with your actual video file
    input_video = "horse_video.mp4"  # Replace with your video path
    output_video = "tracked_horse.mp4"

    result = test_horse_tracking(input_video, output_video)
