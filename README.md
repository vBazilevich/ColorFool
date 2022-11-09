# ColorFool

This is a fork of official repository of [ColorFool: Semantic Adversarial Colorization](https://arxiv.org/pdf/1911.10891.pdf), a work published in The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Seattle, Washington, USA, 14-19 June, 2020.<br>

![Alt Text](ColorFool.gif)
<b>Example of results</b>

| Original Image | Attack AlexNet | Attack ResNet18 | Attack ResNet50 |
|---|---|---|---|
| ![Original Image](Dataset/ILSVRC2012_val_00003533.JPEG) | ![Attack AlexNet](Sample_results/ILSVRC2012_val_00003533_alexnet.png) |![Attack ResNet18](Sample_results/ILSVRC2012_val_00003533_resnet18.png) | ![Attack ResNet50](Sample_results/ILSVRC2012_val_00003533_resnet50.png) |

This fork is aimed to simplify integration of the model into REST API.

## Setup
1. Download source code from GitHub
   ```
    git clone https://github.com/vBazilevich/ColorFool.git
   ```
2. Create [conda](https://docs.conda.io/en/latest/miniconda.html) virtual-environment
   ```
    conda create --name ColorFool python=3.5.6
   ```
3. Activate conda environment
   ```
    source activate ColorFool
   ```
4. Install requirements
   ```
    pip install -r requirements.txt
   ```

*Note:* you can get rid of `conda` but be ready to handle dependencies manually.


## Description
Just pass a binary array to `colorize` function from `ColorFool` module.

*Note:* to make it working you must download segmentation model (both encoder and decoder) from [here](https://drive.google.com/drive/folders/1FjZTweIsWWgxhXkzKHyIzEgBO5VTCe68) and locate in "Segmentation/models" directory.
   

### Output
Function `colorize` returns a binary array that encodes produced colorful image.


## Authors
* [Ali Shahin Shamsabadi](mailto:a.shahinshamsabadi@qmul.ac.uk)
* [Ricardo Sanchez-Matilla](mailto:ricardo.sanchezmatilla@qmul.ac.uk)
* [Andrea Cavallaro](mailto:a.cavallaro@qmul.ac.uk)


## References

      @InProceedings{shamsabadi2020colorfool,
        title = {ColorFool: Semantic Adversarial Colorization},
        author = {Shamsabadi, Ali Shahin and Sanchez-Matilla, Ricardo and Cavallaro, Andrea},
        booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
        year = {2020},
        address = {Seattle, Washington, USA},
        month = June
      }

## License
This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
