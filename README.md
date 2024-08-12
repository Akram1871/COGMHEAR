# COGMHEAR

![Overview Figure](https://github.com/akram1871/cogmhear/blob/main/overview.jpg?raw=true)

```text
# Expected directory structure
avsec3_data_root
├── dev
│   ├── lips
│   │   └── S37890_silent.mp4
│   └── scenes
│       ├── S37890_interferer.wav
│       ├── S37890_mixed.wav
│       ├── S37890_silent.mp4
│       └── S37890_target.wav
└── train
    ├── lips
    │   └── S34526_silent.mp4
    └── scenes
        ├── S34526_interferer.wav
        ├── S34526_mixed.wav
        ├── S34526_silent.mp4
        └── S34526_target.wav
```
- Change dataset root path in `config.py`.

### Clone the repository
```bash
git clone https://github.com/Akram1871/COGMHEAR.git
```

### Install requirements
```bash
cd /COGMHEAR/avse_challenge/baseline/avse3
pip install --quiet -U keras librosa soundfile decord opencv-python tqdm huggingface_hub transformers
```

### Train
To train the model, run the following command:
```bash
python train.py --data_root <avsec3_root> --max_epochs 150
```


### Test
To test the model, run the following command:
```bash
python test.py --data_root <avsec3_root> --weight_path <trained_model_weights> --save_root <path_to_save_enhanced_utterances>
```