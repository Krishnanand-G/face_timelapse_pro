# Face Timelapse Generator

A Python tool that automatically detects and aligns faces across a series of photos to produce a smooth, face-centered timelapse video.

## How It Works

Given a folder of images (e.g. selfies taken over months or years), the script:

1. Detects the largest face in each image using OpenCV Haar cascades
2. Scales and centers the face to a fixed position in every frame
3. Optionally corrects head rotation using eye detection
4. Writes all frames to an `.avi` video file in the correct chronological order

## Demo

https://youtu.be/efOw1FrIRHU

## Requirements

```
opencv-python>=4
numpy
```

Install with:

```bash
pip install -r requirements.txt
```

## Usage

1. Put your images (`.jpg`) in the `./images/` folder, named numerically (`1.jpg`, `2.jpg`, …)
2. Run the script:

```bash
python face_lapse.py
```

If a face cannot be automatically detected in an image, it will be skipped. Set `manual_mode = True` in `main()` to manually draw a bounding box around the face instead.

## Configuration

Inside `face_lapse.py`, the `main()` function exposes these parameters:

| Parameter | Default | Description |
|---|---|---|
| `fps` | `8.0` | Frames per second in the output video |
| `face_height` | `400` | Target face height in pixels |
| `video_out_size` | `(1280, 720)` | Output video resolution |
| `manual_mode` | `False` | Fall back to manual face selection on detection failure |
| `correct_colour` | `False` | Experimental CLAHE colour correction |
| `min_haar_face_size` | `(200, 200)` | Minimum face size for Haar detection |

## Output

The output video is saved as `video.avi` in the project root.

## Project Structure

```
face_pro_lapse/
├── images/                  # Input images (1.jpg … N.jpg)
├── face_lapse.py            # Main script
├── rename_images.py         # Utility: clean up and reorder image filenames
├── haarcascade_*.xml        # OpenCV Haar cascade classifiers
├── requirements.txt
└── video.avi                # Generated timelapse output
```
