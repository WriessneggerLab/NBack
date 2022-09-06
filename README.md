# Research Template

A template to help you kickstart your neurophysiology research project (RP). Here you will find a folder structure, and some template files that might help you keep good practices when designing, executing, analyzing, visualizing, and writing your RP.

The objective of this template is to keep a clean, simple, agile[[1](1)], explainable, and reproducible research[[2](2)]. It is meant as an introduction to scientific project management, knowledge management, and reproducible science.

## How to use
Change what you need to adapt this template to your needs.

### Setup

[Use this template](https://github.com/WriessneggerLab/template-project/generate). This will create a copy of the repository in your github profile.

Clone to a local folder. This downloads the template to your computer.
```
git clone git@github.com:<YourUserame>/project-template.git
```

Install python requirements. Check the `requirements.txt` file to view the suggested python libraries.
```
pip install -r requirements.txt
```

Update the configure file `config.yml` with your own configurations. These depend fully on your project, but we suggest a couple useful ones that might enable you to use the tools we provide in the lab.

Update the [psychopy](https://www.psychopy.org/) paradigm under the `para` folder to fit your needs.

Start your data explorations in [Jupyter Notebooks](https://jupyter.org/):
```
jupyter lab
```

Build your scripts to run under the `src` folder. An example for loading your configuration is shown in load_config.py

### Folder Structure

- `doc`: Keep documentation for your project. Measurement Report Templates, participant information sheet, technical details about your configuration and setup.
- `nb`: Keep jupyter notebooks in this folder. This is meant for explainable explorations of your data.
- `para`: A folder for your paradigm data. In this template, a simple image presentation paradigm in psychopy is shown.
- `src`: The source code of your analysis pipeline.

We sugest you keep your dataset separate from the code repository, and in a [BIDS format](https://bids.neuroimaging.io/).

### Documentation
The development and usage of your project can be documented in different ways:

#### `README.md`
The readme file is intended as the first item of documentation for a project. It should be selfexplainatory, and give enough information for someone else to take it up, while at the same time keeping it short by pointing to further documentation.

Every folder can have it's own `README.md` file, just like the `para` folder contains a `README.md` that explains in more detail the workings of the example paradigm.

### `LOG.md`
Write your research log in this file. Keeping it in your git repo should allow you to visualize changes, challenges, and goals within your project. Be as descriptive as you'd like. This documentation is for you.

### Markdown
Markdown is a simple syntax for formating text. It can be rendered as HTML, PDF, $\LaTex$ with the help of tools like [`pandoc`](https://pandoc.org/). In many git servers like github it's automatically rendered to HTML

## License
A template for the open source MIT license is included as a suggestion.


## References

[1]: Hekler, E. B., Klasnja, P., Riley, W. T., Buman, M. P., Huberty, J., Rivera, D. E., & Martin, C. A. (2016). Agile science: creating useful products for behavior change in the real world. Translational behavioral medicine, 6(2), 317-328.

[2]: Arnold, B., Bowler, L., Gibson, S., Herterich, P., Higman, R., Krystalli, A., ... & Whitaker, K. (2019). The turing Way: a handbook for reproducible data science. Zenodo.
