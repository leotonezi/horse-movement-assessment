# Horse Movement Assessment System

An AI-powered video analysis tool that detects movement abnormalities and potential knee problems in horses using computer vision and pose estimation.

## Overview

This system helps veterinarians, trainers, and horse owners identify early signs of lameness and movement irregularities through automated video analysis. By combining DeepLabCut's pose estimation with LandingAI's preprocessing capabilities, we provide objective measurements of equine movement patterns.

## Features

- **Automated Pose Tracking**: Identifies and tracks 15-20 anatomical landmarks in real-time
- **Movement Analysis**: Measures joint angles, stride patterns, and limb symmetry
- **Anomaly Detection**: Flags potential issues like reduced knee flexion, uneven weight distribution, and irregular movement
- **Visual Reports**: Generates annotated videos and detailed analysis charts
- **Veterinary Support**: Provides actionable insights for professional assessment

## Key Technologies

- **DeepLabCut**: Markerless pose estimation for tracking horse anatomy
- **LandingAI**: Video preprocessing, quality validation, and segmentation
- **Python 3.8+**: Core application framework
- **OpenCV**: Video processing and manipulation
- **NumPy/Pandas**: Data analysis and metrics calculation

## Limitations

- This tool assists but does not replace professional veterinary examination
- Accuracy depends on video quality and proper filming technique
- Cannot assess pain or internal conditions, only visible movement patterns
- Best results with consistent lighting and clear side-view angles

## License

MIT License - see [LICENSE](LICENSE) file for details

## Acknowledgments

- Built with [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut)
- Powered by [LandingAI](https://landing.ai)
- Thanks to veterinary professionals for validation and feedback



- [ ] Integration with veterinary practice management systems
- [ ] Real-time analysis during live sessions
- [ ] Expanded detection for additional gait abnormalities
