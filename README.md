
<!-- README.md is generated from README.Rmd. Please edit that file -->

# Welcome to Environmental Computing 👋

<img src="static/images/hexsticker_EC.png" align="right" alt="" width="150" />

<!-- badges: start -->

[![Netlify
Status](https://api.netlify.com/api/v1/badges/7ebc3505-9fc4-4bed-b0d4-fd75daa3bd7f/deploy-status)](https://app.netlify.com/sites/environmentalcomputing/deploys)
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
a Hugo-friendly format.

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

If you have older versions of Hugo on your computer or having issues
installing Hugo via blogdown you may want to run:

``` r
# Search for where Hugo was previously installed, option to remove previous versions
blogdown::find_hugo() 

# Having issues with Hugo? Try using this handy function!
blogdown::check_hugo()
```

### Install dependencies

Once you have `blogdown` and Hugo installed, you will want to make sure
you have all the different packages that were used in the tutorials. We
created a `DESCRIPTION` file which lists out all the current
dependencies under `Imports`. As the website continues to grow, you will
need to manually edit the `DESCRIPTION` file to ensure the dependencies
match accordingly! Please make sure the dependencies are listed in
**alphabetical order**.

To install the dependencies listed in the `DESCRIPTION` file

``` r
remotes::install_deps()
```

### Structure of the major directories

The most important directories for the website are `content/`, `static/`
and `public/`.

Briefly:

-   `content/` is the backend of the website and is where you will be
    working in the most. This is where all the .Rmd files for each
    tutorial are kept.
-   `static/` is where the [theme](https://learn.netlify.app/en/) of the
    website lives. Hugo translates the websites content into static
    files.
-   These are automatically copied into the `public/` directory each
    thing Hugo renders the website. You don’t know need to physically
    edit the items in `public/`.

For more info about these directories see
[here](https://bookdown.org/yihui/blogdown/hugo.html)

### Name and code style conventions

Please follow these conventions when creating new folders:

-   lowercase names
-   using `-` hypthens to join separate words and numbers
    e.g. `meta-analysis-1`
-   keep folder names to less than 3 concise words if possible
-   use commonly used abbreviations e.g. `glms` instead of
    `generalised-linear-models`
-   If there are multiple tutorials for a given topic, use numbers
    beginning from 1 e.g. `mixed-model-1`

We used the `styler` package to format all the content within chunks.

``` r
# An example

styler::style_file("content/Data-Manipulation/combining-datasets/_index.Rmd")
```

### The anatomy of nested menus

All of our tutorials are organised into major menus (`coding-skills/`,
`statistics/`, `graphics/` etc). Sub-menus are created by putting a
folder within the main folder e.g. `asking-code-questions/` is a
subfolder within `coding-skills/`. Any files (.Rmd, .html and images)
associated with the subtopic will live in that subfolder
e.g. \_index.rmd, stack.png

    content/
    ├── about-this-site
    ├── coding-skills
    │   ├── asking-code-questions
    │   │   ├── _index.html
    │   │   ├── _index.rmd
    │   │   ├── stack.png
    │   ├── good-practice

#### The order of menus

Each folder contains a `_index.rmd` which creates its associated
`_index.html` file. It is crucial to set this file up correctly to
organise the menu and pages. The yaml header of each `_index.rmd` file
looks a bit like this and this section controls the order of the pages.

    ---
    title: "Getting Started with R"
    output: html_document
    weight: 2
    ---

-   The `title:` parameter becomes the name of the menu. Note that each
    word in `title:` is **capitalised**
-   The `weight:` parameter denotes the **order** of the page. 1 being
    the first, 2 being the second and so forth.
-   The `output:` parameter determines what format the .rmd is rendered
    to. For Hugo’s sake, we need it to render an `html_document`.

In the yaml example above, the `weight:` parameter is 2, notice that the
second menu on the [website](environmentalcomputing.net) is “Getting
Started in R”.

Once you enter a menu e.g. “Getting Started in R”, the sequence for the
`weight:` restarts so that you can set the order for subtopics within
“Getting Started in R”.

For example, `weight: 1` for “Installing R and RStudio”, `weight: 2` for
“Using R Notebooks” and so forth.

I recommend taking a look at this
[website](https://mingchen0919.github.io/blogdown-website-with-hugo-theme-learn/)
to better understand the nestedness of the menus and how to set this up
using subfolders and `_index.Rmd` files.

### Building the site

Once you are happy with the format of a new page you created, using the
following function to render your page. Knitting your .rmd will also do
the trick!

``` r
blogdown::build_site(build_rmd = 'newfile')

# and then to preview your site, open in browser and explore your work :) 
blogdown::serve_site()
```

Occasionally, you will want to make edits to some .rmds, to re-render
these pages use:

``` r
blogdown::build_site(build_rmd = 'timestamp')
```

Sometimes, you’ll notice that despite knitting or using the above
functions, your page is not showing up. This is where the following
function comes in handy:

``` r
blogdown::check_site()

# There are various blogdown::check_ functions, check_site() does it all-in-one
```

This function will prompt to you fix your issues, usually you will need
to remove incompatible files, restart RStudio and use again. No worries!

If you are already previewing your site, you will notice upon saving
your .rmd, the site will usually dynamically update itself but its good
practice to occasionally use the above `r blogdown::build_site()`
functions to ensure proper rendering.

To stop previewing the site:

``` r
blogdown::stop_server()
```

### Internal links

In some tutorials there are references to other pages. For example the
[Statistics page](environmentalcomputing.net/statistics) provides links
to all the subtopics under “Statistics”. Please follow these conventions
when adding internal links in your .rmd

Lets say you are working on a page under `data-manipulation/` and you
want to reference to a page under `graphics/`. In this circumstance, you
are linking to an entirely different major menu, so we recommend using
**absolute paths**. This is denoted by the `/` preceding `statistics/`
which searches for a folder in the entire project directory named
`statistics`

    Once you have summarised your data, you can easily [plot it!]("/statistics/graphics/ggplot")

Alternatively, if you are working of a page within the same menu
e.g. `data-manipulation/subsetting-data` and want to reference a page
within the same menu e.g. `data-manipulation/combining-datasets`, we
recommend using **relative paths**. This is denoted by the `..`
preceding `/combining-datasets`. The `..` means ‘going up a directory
level’ and then `/combining-datasets` means going into the
`combining-datasets` subfolder.

    You can [merge]("../combining-datasets") your newly subsetted data to another dataframe.

### Aliases

[Aliases](https://gohugo.io/content-management/urls/#example-aliases)
help redirect existing, outdated or alternative URLs to specific pages
in the website. Aliases were particularly useful when we were
reorganising old tutorial pages to the new blogdown/Hugo system. For
example, in the first generation of the website the URL for the ‘Asking
Code Questions’ page was accessed using:

    environmentalcomputing.net/asking-coding-questions/ # OLD

In the new generation of the website the same ‘Asking Code Questions’
page is accessed via:

    environmentalcomputing.net/coding-skills/asking-coding-questions/ # NEW

We created an aliases so that the old URL can still work and direct to
the new site. This can be achieved by simply adding an `aliases:`
parameter in the yaml in the .rmd.

    ---
    title: "Asking Code Questions"
    output: html_document
    aliases: /asking-coding-questions/
    weight: 5
    ---
