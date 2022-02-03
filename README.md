
<!-- README.md is generated from README.Rmd. Please edit that file -->

# Welcome to Environmental Computing 👋

<!-- badges: start -->
<!-- badges: end -->

The goal of **Environmental Computing** is to provide accessible coding
and statistical tutorials to R users. If you would like to learn more
about this site, click
[here](https://deploy-preview-18--brave-bose-da028a.netlify.app/about-this-site/)

This repository contains the
[blogdown](https://bookdown.org/yihui/blogdown/) and
[hugo](https://gohugo.io/) backbone to build and maintain the website.
Below are important details to quickly orientate you to the
behind-the-scenes of this website

### Installation of `blogdown` and Hugo

`blogdown` is a R interface to Hugo and is super handy for our purposes
as most tutorials are written as R Markdown files which is rendered into
a hugo-friendly format.

Blogdown can be installed from either CRAN or directly from the RStudio
blogdown Github repository using the `remotes` package:

``` r
# Install from CRAN
install.packages("blogdown")

# Install from Github
remotes::install_github('rstudio/blogdown')
```

Once blogdown is installed, we can use this package to install Hugo!

``` r
blogdown::install_hugo()
```

If you have old versions of Hugo on your computer or having issues
installing Hugo via blogdown you may want to run:

``` r
# Search for where Hugo was previously installed, option to remove previous versions
blogdown::find_hugo() 

# Having issues with Hugo, try using this handy function!
blogdown::check_hugo()
```

### Install dependencies

Once you have `blogdown` and Hugo running happily, you will want to make
sure you have all the different packages that were used in the
tutorials. We created a `DESCRIPTION` file which lists out all the
current dependencies under `Imports`. As the website continues to grow,
you will need to manually edit the `DESCRIPTION` file to ensure the
dependencies match accordingly!

To install the dependencies listed in the `DESCRIPTION` file

``` r
remotes::install_deps()
```

### Structure of the major directories

The most important folders for this website are `content/`, `static/`
and `public/`.

Briefly: - `content/` is the backend of the website and is where you
will be working in the most. This is where all the .Rmd files for each
tutorial are kept. - `static/` is where the
[theme](https://learn.netlify.app/en/) of the website lives. Hugo
translates the websites content into static files. - These are
automatically copied into the `public/` directory each thing Hugo
renders the website. You don’t know need to physically edit the items in
`public/`.

For more info about this directories see
[here](https://bookdown.org/yihui/blogdown/hugo.html)

### Name and code style conventions

Please follow these conventions when creating new folders: - lowercase
names - using `-` hypthens to join separate words and numbers
e.g. `data-manipulation` - keep folder names to less than 3 concise
words if possible - use commonly used abbreviations e.g. `glms` instead
of `generalised-linear-models` - If there are multiple tutorials for a
given topic, use numbers beginning from 1 e.g `mixed-model-1`

We used the `styler` package to format all the content within chunks.

``` r
styler::????
```

### The anatomy of nested menus in `content/`

All of our tutorials are organised into major menus

    content/
    ├── about-this-site
    ├── coding-skills
    │   ├── asking-code-questions
    │   │   ├── _index.html
    │   │   ├── _index.rmd
    │   │   ├── stack.png
    │   ├── good-practice

I recommend taking a look at this
[website](https://mingchen0919.github.io/blogdown-website-with-hugo-theme-learn/)
to better understand the nestedness of the menus and how to set this up
using subfolders and `_index.Rmd` files.

### R Markdown and yamls

### Building the site

### Internal links
