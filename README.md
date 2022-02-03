
<!-- README.md is generated from README.Rmd. Please edit that file -->

# Welcome to Environmental Computing

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

## Installation of `blogdown` and `hugo`

`blogdown` is a R interface to `hugo` and is super handy for our
purposes as most tutorials are written as R Markdown files which is
rendered into a hugo-friendly format.

Blogdown can be installed from either CRAN or directly from the RStudio
blogdown Github repository using the `remotes` package:

``` r
# Install from CRAN
install.packages("blogdown")

# Install from Github
remotes::install_github('rstudio/blogdown')
```

Once blogdown is installed, we can use this package to install `hugo`!

``` r
blogdown::install_hugo()
```

If you have old versions of `hugo` on your computer or having issues
installing hugo via blogdown you may want to run:

``` r
# Search for where hugo was previously installed, option to remove previous versions
blogdown::find_hugo() 

# Having issues with hugo, try using this handy function!
blogdown::check_hugo()
```

## Install dependencies

Once you have `blogdown` and `hugo` running happily, you will want to
make sure you have all the different packages that were used in the
tutorials. We created a `DESCRIPTION` file which lists out all the
current dependencies under `Imports`. As the website continues to grow,
you will need to manually edit the `DESCRIPTION` file to ensure the
dependencies match accordingly!

To install the dependencies listed in the `DESCRIPTION` file

``` r
remotes::install_deps()
```

## Structure of the director
