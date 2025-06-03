# dpgan2cyclegan

## Comparison of test results for individual models

Structure of the folder containing the original masks:
```
mask_folder/
└── image_name_1/
│   ├── image_name_1_mask_0.png
│   ├── image_name_1_mask_1.png
│   │   ...
│   └── image_name_1_mask_15.png
├── image_name_2/
│   ...
└── image_name_N/
```

After training and testing the individual models, in accordance with the recommendations of the respective authors of each solution, we should obtain test result folders following the structure below:

- CycleGAN:

```
project_folder/
└── results/
    ├── cephalo_line_0/
    │   └── test_latest/
    │       └── images/
    │           ├── img1.png
    │           ├── img2.png
    │           │   ...
    │           └── imgN.png
    ├── cephalo_line_1/
    │   ...
    └── cephalo_line_15/
```

- DP-GAN and OASIS:

```
project_folder/
└── results/
    ├── cephalo_line_0/
    │   └── best/
    │       ├── image/
    │       │   └── ...
    │       └── label/
    │           ├── img1.png
    │           ├── img2.png
    │           │   ...
    │           └── imgN.png
    ├── cephalo_line_1/
    │   ...
    └── cephalo_line_15/
```



  
