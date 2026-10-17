# Migration report

Old site: `7b59e6f` (75 pages). Book chapters written: 50.

## preface.qmd
13 blocks from 1 old page(s). 4 matched the first conversion; **9 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 19 new blocks kept.

- EDIT: chunks left over from the R for Data Science template that show nothing (one never runs, the other is hidden)

<details><summary>Details</summary>

- restored `about-this-site`: **Site editors:**
- restored `about-this-site`: [Professor Alistair Poore](https://alistairpoore.org) 
- restored `about-this-site`: [Associate Professor Will Cornwell](http://willcornwell.org/)
- restored `about-this-site`: [Associate Professor Daniel Falster](https://danielfalster.com/)
- restored `about-this-site`: [Dr. Fonti Kar](https://fontikar.wordpress.com/)
- restored `about-this-site`: **Page authors:** Keryn Bain, Rachel Blakey, Stephanie Brodie, Corey Callaghan, Will Cornwell, Kingsley Griffi
- restored `about-this-site`: **Year:** 2016
- restored `about-this-site`: ## Contributors
- restored `about-this-site`: Thanks to them <i class="fas fa-heart"></i> for making Open Source Software a better place !
- kept new: ```{r}
- kept new: ## Acknowledgments
- kept new: ```{r}
- kept new: ```{r}
- kept new: Extra thanks to [R for Data Science](https://github.com/hadley/r4ds) team for the code which generated the lis
- kept new: ## Colophon
- kept new: The book is powered by [Quarto](https://quarto.org), which makes it easy to write books that combine text and 
- kept new: ```{r}
- kept new: ```{r}
- kept new: ## Site migration history
- kept new: ### 2026 migration from Hugo to Quarto
- kept new: In 2026 we migrated the site from Hugo to Quarto and substantially updated the website structure.
- kept new: Key structural changes:
- kept new: * Getting Started with R → split between `content/basics/` (installing R, projects) and `content/data-literacy
- kept new: Page migration table:
- kept new: | Old Hugo path | New Quarto path |
- kept new: ### 2022 migration from Wordpress to Hugo
- kept new: In Feb 2022, the site was migrated from Wordpress to Hugo. These old Wordpress URLs should be redirected to th
- kept new: - [/analysis-variance-factorial/](/analysis-variance-factorial/)

</details>

## basics/basics.qmd
13 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## basics/r.qmd
27 blocks from 1 old page(s). 27 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## basics/projects.qmd
24 blocks from 1 old page(s). 24 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## data-literacy/making-analysis-ready-data.qmd
8 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## data-literacy/reading/index.qmd
78 blocks from 1 old page(s). 78 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)
- EDIT: letter case `Importing_data_image.jpg` -> `Importing_data_image.JPG` (only worked on macOS)

## data-literacy/filter-rows/index.qmd
78 blocks from 1 old page(s). 78 matched the first conversion; **0 restored** (missing), **1 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (<font>/<center> tags: 8)
- EDIT: tidied markup (headings raised to start at ##: 1)

<details><summary>Details</summary>

- untrimmed `Data-Manipulation/subsetting-data`: You can experiment with a range of logical operators when using the `filter` function:  

</details>

## data-literacy/mutate/index.qmd
46 blocks from 1 old page(s). 46 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## data-literacy/joining-tables/index.qmd
49 blocks from 1 old page(s). 49 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## data-literacy/summarising-tables/index.qmd
50 blocks from 1 old page(s). 50 matched the first conversion; **0 restored** (missing), **1 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

<details><summary>Details</summary>

- untrimmed `Data-Manipulation/summarising-data`: ```{r}

</details>

## data-literacy/pivotting/index.qmd
56 blocks from 1 old page(s). 56 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)
- EDIT: dead link; reshape2 is superseded by tidyr's pivot functions

## data-visualisation/data-visualisation.qmd
11 blocks from 3 old page(s). Existing chapter was a placeholder: written from the old page(s).


## data-visualisation/ggplot.qmd
345 blocks from 10 old page(s). 195 matched the first conversion; **150 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 27 condensed rewrites replaced by the original, 2 new blocks kept. Original wording preferred throughout.

- EDIT: tidied markup (heading space: 6)
- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: colour chart PDF gone
- EDIT: link target split over two lines on the old page

<details><summary>Details</summary>

- restored `Graphics/basic-plotting`: ```{r}
- restored `Graphics/basic-plotting`: R has a very wide range of functions and packages for visualising data. Here is some help for some very simple
- restored `Graphics/basic-plotting`: * [one continuous variable](/graphics/basic-plotting/one-continuous/) - histograms and box plots  
- restored `Graphics/basic-plotting/one-continuous`: Remember that the median is the value that has 50% of values larger and 50% of values smaller. Similarly, the 
- restored `Graphics/basic-plotting/one-continuous`: These simple plots can be formatted using the basic R formatting in the graphics package. The code below gives
- restored `Graphics/basic-plotting/one-continuous`: **Plot alignment**
- restored `Graphics/basic-plotting/one-continuous`: Use the `horizontal=TRUE` argument to align the box plot horizontally - leave this out if you want a vertical 
- restored `Graphics/basic-plotting/one-continuous`: Here we will simply change the colour of the histogram.
- restored `Graphics/basic-plotting/one-continuous`: ### Further help
- restored `Graphics/basic-plotting/one-continuous`: **Author**: Stephanie Brodie
- restored `Graphics/basic-plotting/one-continuous`: **Year:** 2016
- restored `Graphics/basic-plotting/two-continuous`: ###Scatterplots###
- restored `Graphics/basic-plotting/two-continuous`: where *y* and *X* are two vectors of equal length. 
- restored `Graphics/basic-plotting/two-continuous`: Scatterplots can be formatted using the basic R formatting in the graphics package. The code below details som
- restored `Graphics/basic-plotting/two-continuous`: **Edit axis limits**
- restored `Graphics/basic-plotting/two-continuous`: Colour can be added to any part of the plots (axis, fonts etc.) using `col` argument. There are over 600 colou
- restored `Graphics/basic-plotting/two-continuous`: Here we will simply change the colour of the symbols to blue.
- restored `Graphics/basic-plotting/two-continuous`: See the page on [linear regression](/statistics/linear-models/linear-regression/) for the analysis of tree hei
- restored `Graphics/basic-plotting/two-continuous`: ### Further help
- restored `Graphics/basic-plotting/two-continuous`: **Authors**: Stephanie Brodie & Alistair Poore
- restored `Graphics/basic-plotting/two-continuous`: **Year:** 2016
- restored `Graphics/basic-plotting/one-continuous-one-factor`: These sorts of plots are very commonly used in the biological, earth and environmental sciences. For example, 
- restored `Graphics/basic-plotting/one-continuous-one-factor`: Firstly, download the sample data file, [Prawns_MR.csv](/datasets/Prawns_MR.csv), and import into R.
- restored `Graphics/basic-plotting/one-continuous-one-factor`: Boxplots are easily made with the `boxplot` function. Boxplots show the distribution of a variable by indicati
- restored `Graphics/basic-plotting/one-continuous-one-factor`: To contrast metabolic rate across the two species, we would use:
- restored `Graphics/basic-plotting/one-continuous-one-factor`: While commonly used, they are not so easy to create in the base functions in R. There are various ways to do t
- restored `Graphics/basic-plotting/one-continuous-one-factor`: Here is some sample code to plot means +/- standard deviations. For more control over error bars, we recommend
- restored `Graphics/basic-plotting/one-continuous-one-factor`: In a new data frame called Species.summary, we now have the means, standard deviations and the lower and upper
- restored `Graphics/basic-plotting/one-continuous-one-factor`: We can now use the `barplot` and `arrows` functions to make a plot with error bars.
- restored `Graphics/basic-plotting/one-continuous-one-factor`: Box plots and bar plots can be formatted using the basic R formatting in the base graphics package. The code b
- restored `Graphics/basic-plotting/one-continuous-one-factor`: **Add axis labels or titles**  
- restored `Graphics/basic-plotting/one-continuous-one-factor`: **Edit axis limits**  
- restored `Graphics/basic-plotting/one-continuous-one-factor`: **Renaming levels of the categorical factor**  
- restored `Graphics/basic-plotting/one-continuous-one-factor`: **Adding colour** 
- restored `Graphics/basic-plotting/one-continuous-one-factor`: Here we will simply change the colour of the bars in the bar plot to red.
- restored `Graphics/basic-plotting/one-continuous-one-factor`: ### Further help
- restored `Graphics/basic-plotting/one-continuous-one-factor`: **Authors**: Stephanie Brodie & Alistair Poore
- restored `Graphics/basic-plotting/one-continuous-one-factor`: **Year:** 2016
- restored `Graphics/ggplot`: [ggplot2](https://ggplot2.tidyverse.org) is a powerful graphing package in R that can be used to create profes
- restored `Graphics/ggplot`: The package is named after a book called [The Grammar of Graphics](https://books.google.com.au/books/about/The
- restored `Graphics/ggplot`: Start with the [basics](/graphics/ggplot/ggplot-basics) to learn the basic syntax of making a graph
- restored `Graphics/ggplot`: Then, visit our other pages to further customise the aesthetics of the graph, including colour and formatting:
- restored `Graphics/ggplot`: Help on all the ggplot functions can be found at the [The master ggplot help site](https://ggplot2.tidyverse.o
- restored `Graphics/ggplot`: A useful cheat sheet on commonly used functions can be downloaded [here](https://raw.githubusercontent.com/rst
- restored `Graphics/ggplot`: <p style="margin-left: .5in; text-indent: -.5in;">Chang, W (2012) *R Graphics cookbook.* O'Reilly Media. - a g
- restored `Graphics/ggplot`: **Year:** 2016
- restored `Graphics/ggplot/ggplot-basics`: ```{r}
- restored `Graphics/ggplot/ggplot-basics`: First, you will need to install the package ggplot2 on your machine, then load the package with the usual `lib
- restored `Graphics/ggplot/ggplot-basics`: Ensure there is a open and closed bracket after the `geom` code. This tells R to make the graph with the basic
- restored `Graphics/ggplot/ggplot-basics`: In these examples, let's use a data set that is already in R with the length and width of floral parts for thr
- restored `Graphics/ggplot/ggplot-basics`: Note how `aes` included the *x* then the *y* variables which you wanted to plot, and that `+ geom_boxplot()` s
- restored `Graphics/ggplot/ggplot-basics`: ###Further help
- restored `Graphics/ggplot/ggplot-basics`: To further customise the aesthetics of the graph, including colour and formatting, see our other ggplot help p
- restored `Graphics/ggplot/ggplot-basics`: Help on all the ggplot functions can be found at the [The master ggplot help site](https://ggplot2.tidyverse.o
- restored `Graphics/ggplot/ggplot-basics`: A useful cheat sheet on commonly used functions can be downloaded [here](https://raw.githubusercontent.com/rst
- restored `Graphics/ggplot/ggplot-basics`: <p style="margin-left: .5in; text-indent: -.5in;">Chang, W (2012) *R Graphics cookbook.* O'Reilly Media. - a g
- restored `Graphics/ggplot/ggplot-basics`: **Author**: Fiona Robinson
- restored `Graphics/ggplot/ggplot-basics`: **Year:** 2016
- restored `Graphics/ggplot/ggplot-labels`: **ggplots** are almost entirely customisable. This gives you the freedom to create a plot design that perfectl
- restored `Graphics/ggplot/ggplot-labels`: Before you get started, read the page on the [basics](/graphics/ggplot/ggplot-basics/) of plotting with ggplot
- restored `Graphics/ggplot/ggplot-labels`: ```{r}
- restored `Graphics/ggplot/ggplot-labels`: ![](images/ggplot1_basics_image.JPG)
- restored `Graphics/ggplot/ggplot-labels`: In these examples, let's use a data set that is already in R with the length and width of floral parts for thr
- restored `Graphics/ggplot/ggplot-labels`: ```{r}
- restored `Graphics/ggplot/ggplot-labels`: To add a title to your plot, add the code `+ggtitle("Your Title Here")` to your line of basic ggplot code. Ens
- restored `Graphics/ggplot/ggplot-labels`: If you have a particulary long title that would work better on two lines, use `\n` for a new line. Make sure t
- restored `Graphics/ggplot/ggplot-labels`: For example:
- restored `Graphics/ggplot/ggplot-labels`: ### Altering the text style of your legend, axis or title
- restored `Graphics/ggplot/ggplot-labels`: Where "title type" specifies which particular text you want to edit. These can be:
- restored `Graphics/ggplot/ggplot-labels`: **Formatting choices**
- restored `Graphics/ggplot/ggplot-labels`: * family. - the font style. Examples of fonts include: "Palatino", "Helvetica", "Courier", "Times". Further fo
- restored `Graphics/ggplot/ggplot-labels`: ### Example code
- restored `Graphics/ggplot/ggplot-labels`: Here is an example of a theme that customises the title, the legend, the axis labels and specifies the font, e
- restored `Graphics/ggplot/ggplot-labels`: ### Removing a label
- restored `Graphics/ggplot/ggplot-labels`: Another option is to remove the text from the plot entirely. To do this you use the code `= element_blank()`, 
- restored `Graphics/ggplot/ggplot-labels`: ###Further help
- restored `Graphics/ggplot/ggplot-labels`: To further customise the aesthetics of the graph, including colour and formatting, see our other ggplot help p
- restored `Graphics/ggplot/ggplot-labels`: Help on all the ggplot functions can be found at the [The master ggplot help site](https://ggplot2.tidyverse.o
- restored `Graphics/ggplot/ggplot-labels`: A useful cheat sheet on commonly used functions can be downloaded [here](https://raw.githubusercontent.com/rst
- restored `Graphics/ggplot/ggplot-labels`: <p style="margin-left: .5in; text-indent: -.5in;">Chang, W (2012) *R Graphics cookbook.* O'Reilly Media. - a g
- restored `Graphics/ggplot/ggplot-labels`: **Author**: Fiona Robinson
- restored `Graphics/ggplot/ggplot-labels`: **Year:** 2016
- restored `Graphics/ggplot/ggplot-colour-shapes`: Before you get started, read the page on the [basics](/graphics/ggplot/ggplot-basics/) of plotting with ggplot
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: ![](images/ggplot1_basics_image.JPG)
- restored `Graphics/ggplot/ggplot-colour-shapes`: In these examples, let's use a data set that is already in R with the length and width of floral parts for thr
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: The following plots will be used as the base code throughout of this tutorial  
- restored `Graphics/ggplot/ggplot-colour-shapes`: ### Changing the colour of the whole plot or its outline
- restored `Graphics/ggplot/ggplot-colour-shapes`: To colour your entire plot one colour, add `fill = "colour"` or `colour = "colour"` into the brackets followin
- restored `Graphics/ggplot/ggplot-colour-shapes`: For example, to make a blue box plot with a red outline, or a yellow histogram with an green outline::
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: The plots and outlines can be changed to any colour listed [here](http://www.stat.columbia.edu/~tzheng/files/R
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: The basic format for colouring a continuous variable is very similar to a categorical variable. The only real 
- restored `Graphics/ggplot/ggplot-colour-shapes`: To make the gradient more effective, specify two colours within the `+ scale_colour_gradient` brackets to repr
- restored `Graphics/ggplot/ggplot-colour-shapes`: ### Choosing your own colours for these variables
- restored `Graphics/ggplot/ggplot-colour-shapes`: `print(your.basic.graph + your.theme + scale_colour_yourchoice())`
- restored `Graphics/ggplot/ggplot-colour-shapes`: There are numerous options for the `+ scale_colour_yourchoice()` part.
- restored `Graphics/ggplot/ggplot-colour-shapes`: This can then be added to the end of your graph code just like the others `+ scale_colour_brewer(palette = "ch
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: Different symbols can be used to group data in a scatterplot. This can be very helpful when printing in black 
- restored `Graphics/ggplot/ggplot-colour-shapes`: To do this, you need to add  `shape = variable.name` within your basic plot `aes` brackets, where `variable.na
- restored `Graphics/ggplot/ggplot-colour-shapes`: ```{r}
- restored `Graphics/ggplot/ggplot-colour-shapes`: ###Further help
- restored `Graphics/ggplot/ggplot-colour-shapes`: To further customise the aesthetics of the graph, including colour and formatting, see our other ggplot help p
- restored `Graphics/ggplot/ggplot-colour-shapes`: Help on all the ggplot functions can be found at the [The master ggplot help site](https://ggplot2.tidyverse.o
- restored `Graphics/ggplot/ggplot-colour-shapes`: A useful cheat sheet on commonly used functions can be downloaded [here](https://raw.githubusercontent.com/rst
- restored `Graphics/ggplot/ggplot-colour-shapes`: <p style="margin-left: .5in; text-indent: -.5in;">Chang, W (2012) *R Graphics cookbook.* O'Reilly Media. - a g
- restored `Graphics/ggplot/ggplot-colour-shapes`: **Author**: Fiona Robinson
- restored `Graphics/ggplot/ggplot-colour-shapes`: **Year:** 2016
- restored `Graphics/ggplot/ggplot-barplot`: Before you get started, read the page on the [basics](../ggplot-basics/) of plotting with ggplot and install t
- restored `Graphics/ggplot/ggplot-barplot`: ```{r}
- restored `Graphics/ggplot/ggplot-barplot`: ![](images/ggplot1_basics_image.JPG)
- restored `Graphics/ggplot/ggplot-barplot`: In this examples, let's use a data set that is already in R with the length and width of floral parts for thre
- restored `Graphics/ggplot/ggplot-barplot`: ```{r}
- restored `Graphics/ggplot/ggplot-barplot`: The following code will make a new data frame with the summary data per species.
- restored `Graphics/ggplot/ggplot-barplot`: ```{r}
- restored `Graphics/ggplot/ggplot-barplot`: ###Further help
- restored `Graphics/ggplot/ggplot-barplot`: To further customise the aesthetics of the graph, including colour and formatting, see our other ggplot help p
- restored `Graphics/ggplot/ggplot-barplot`: Help on all the ggplot functions can be found at the [The master ggplot help site](https://ggplot2.tidyverse.o
- restored `Graphics/ggplot/ggplot-barplot`: A useful cheat sheet on commonly used functions can be downloaded [here](https://raw.githubusercontent.com/rst
- restored `Graphics/ggplot/ggplot-barplot`: <p style="margin-left: .5in; text-indent: -.5in;">Chang, W (2012) *R Graphics cookbook.* O'Reilly Media. - a g
- restored `Graphics/ggplot/ggplot-barplot`: **Author**: Alistair Poore (small edits by Will Cornwell)
- restored `Graphics/ggplot/ggplot-barplot`: **Year:** 2016
- restored `Graphics/ggplot/ggplot-appearance`: **ggplots** are almost entirely customisable. This gives you the freedom to create a plot design that perfectl
- restored `Graphics/ggplot/ggplot-appearance`: The overall appearance can be edited by changing the style or prescence of grid lines, axis notches, panel col
- restored `Graphics/ggplot/ggplot-appearance`: Before you get started, read the page on the [basics](/graphics/ggplot/ggplot-basics/) of plotting with ggplot
- restored `Graphics/ggplot/ggplot-appearance`: ```{r}
- restored `Graphics/ggplot/ggplot-appearance`: ![](images/ggplot1_basics_image.JPG)
- restored `Graphics/ggplot/ggplot-appearance`: In these examples, let's use a data set that is already in R with the length and width of floral parts for thr
- restored `Graphics/ggplot/ggplot-appearance`: ```{r}
- restored `Graphics/ggplot/ggplot-appearance`: The following code for a scatter plot of petal length vs sepal length with the three species colour-coded is t
- restored `Graphics/ggplot/ggplot-appearance`: ```{r}
- restored `Graphics/ggplot/ggplot-appearance`: We would then reprint the base plot with this theme added:
- restored `Graphics/ggplot/ggplot-appearance`: ```{r}
- restored `Graphics/ggplot/ggplot-appearance`: The plot and legend background can be changed to any colour listed [here](http://www.stat.columbia.edu/~tzheng
- restored `Graphics/ggplot/ggplot-appearance`: To demonstrate how this works, here is a ugly theme with obvious colours chosen to demonstrate the differences
- restored `Graphics/ggplot/ggplot-appearance`: where `(your format)` specifies the colour and thickness of the lines. 
- restored `Graphics/ggplot/ggplot-appearance`: Formats include:  
- restored `Graphics/ggplot/ggplot-appearance`: Putting these together in a theme would look like this:
- restored `Graphics/ggplot/ggplot-appearance`: ### Altering the x and y axis lines 
- restored `Graphics/ggplot/ggplot-appearance`: The size and colour of axis lines themselves can be customised in the same way as the grid lines (above), usin
- restored `Graphics/ggplot/ggplot-appearance`: ### Altering the axis ticks/notches
- restored `Graphics/ggplot/ggplot-appearance`: The size and colour of the ticks can be altered using `axis.ticks = element_line(your format)`. For example:
- restored `Graphics/ggplot/ggplot-appearance`: Here is an example of a ggplot with many of the elements customised. This is obviously a lot of code, but reme
- restored `Graphics/ggplot/ggplot-appearance`: ###Further help
- restored `Graphics/ggplot/ggplot-appearance`: To further customise the aesthetics of the graph, including colour and formatting, see our other ggplot help p
- restored `Graphics/ggplot/ggplot-appearance`: **Author**: Fiona Robinson
- replaced rewrite: This page introduces plotting in R. We start with base R graphics for quick exploratory plots, then cover ggpl
- replaced rewrite: **Add axis labels or titles**
- replaced rewrite: **Edit axis limits**
- replaced rewrite: **Symbol style**
- replaced rewrite: **Add axis labels**
- replaced rewrite: **Edit axis limits**
- replaced rewrite: **Rename levels of the categorical factor**
- replaced rewrite: **Adding colour**
- replaced rewrite: First, install and load ggplot2:
- replaced rewrite: Add `+ggtitle("Your Title Here")` to your ggplot code.
- replaced rewrite: For a long title, use `\n` for a new line:
- replaced rewrite: ### Altering text style
- replaced rewrite: Where "title type" is one of:
- replaced rewrite: **Formatting choices** within `element_text()`:
- replaced rewrite: * `family` — the font style, e.g. `"Palatino"`, `"Helvetica"`, `"Courier"`, `"Times"`
- replaced rewrite: To remove a text element entirely, use `= element_blank()`:
- replaced rewrite: This section covers changing the colours and symbol shapes in your ggplots.
- replaced rewrite: The following three plots will serve as base code throughout this section:
- replaced rewrite: ### Changing the colour of the whole plot
- replaced rewrite: Use `+ scale_colour_gradient(low = "colour1", high = "colour2")` to map a continuous variable to colour:
- replaced rewrite: ### Choosing your own colours
- replaced rewrite: To use different symbols for each group, add `shape = variable.name` within your `aes` brackets:
- replaced rewrite: ```{r,warning=F,message=F}
- replaced rewrite: This section covers customising the overall appearance of a ggplot by changing the style or presence of grid l
- replaced rewrite: ### Altering the axis lines
- replaced rewrite: ### Altering the axis ticks
- replaced rewrite: **Authors**: Stephanie Brodie, Alistair Poore, Fiona Robinson (small edits by Will Cornwell)
- kept new: ### Scatterplots
- kept new: ## Further help

</details>

## data-visualisation/multi-panel-figures.qmd
54 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## data-visualisation/rasters.qmd
102 blocks from 1 old page(s). 102 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **1 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 1 new blocks kept.

- EDIT: Simple maps is its own chapter, not a section of this one
- EDIT: rgdal was retired from CRAN in 2023; raster now reads files through terra
- EDIT: rgdal was retired from CRAN in 2023
- EDIT: rgdal was retired from CRAN in 2023
- EDIT: reading .img files through terra names layers "Layer_1", not after the file, so name them explicitly

<details><summary>Details</summary>

- updated `Graphics/spatial-vis/basic-raster`: Download the data files needed for this tutorial: [Cairns_Mangroves_30m.tif](/datasets/Cairns_Mangroves_30m.ti
- kept new: ## The Basics of Rasters

</details>

## data-visualisation/simple-maps.qmd
46 blocks from 1 old page(s). 46 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.


## data-visualisation/pca.qmd
49 blocks from 1 old page(s). 49 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (stray ## made siblings of ###: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## data-visualisation/heatmaps.qmd
60 blocks from 1 old page(s). 60 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## statistical-methods/statistical-methods.qmd
17 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## statistical-methods/linear-models.qmd
5 blocks from 1 old page(s). 0 matched the first conversion; **5 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 3 new blocks kept.

- EDIT: duplicate of the numbered chapter list above (whose "Interpreting coefficients" link also went to the GLM page on the old site)
- EDIT: the confidence intervals chapter is still a placeholder and is not published, so the link would point at its raw source file

<details><summary>Details</summary>

- restored `Statistics/linear-models`: These pages have some introductions to commonly used linear models that test the response of a continuous depe
- restored `Statistics/linear-models`: ```{r}
- restored `Statistics/linear-models`: * [Linear regression](linear-regression/)
- restored `Statistics/linear-models`: **Author**: Alistair Poore
- restored `Statistics/linear-models`: **Year:** 2016
- kept new: This section introduces linear-model-based methods for testing differences among groups and understanding fact
- kept new: The core chapters are:
- kept new: 1. [Confidence intervals](confidence-intervals.qmd)

</details>

## statistical-methods/linear-regression.qmd
46 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).

- EDIT: words in maths were typeset as italic variables ("plantheight"), and "." used for multiplication

## statistical-methods/interpret-lm-coeffs.qmd
40 blocks from 1 old page(s). 40 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## statistical-methods/t-tests.qmd
125 blocks from 4 old page(s). 123 matched the first conversion; **2 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 3 new blocks kept.

- EDIT: since R 4.4, t.test() no longer accepts paired = TRUE with a formula
- EDIT: since R 4.4, t.test() no longer accepts paired = TRUE with a formula

<details><summary>Details</summary>

- restored `Statistics/t-tests`: Some simple hypothesis tests with the t statistic:
- restored `Statistics/t-tests`: * [One sample t tests](one-sample-t-test) to contrasting a single sample parameter to a population parameter  
- kept new: ---
- kept new: ---
- kept new: ---

</details>

## statistical-methods/anova.qmd
163 blocks from 4 old page(s). 152 matched the first conversion; **11 restored** (missing), **9 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 1 condensed rewrites replaced by the original, 2 new blocks kept.

- EDIT: the single-factor page repeated the parent page's introduction, so it appeared twice in a row

<details><summary>Details</summary>

- restored `Statistics/linear-models/anova`: Analysis of variance (ANOVA) is one of the most frequently used techniques in the biological and environmental
- restored `Statistics/linear-models/anova`: Where an independent samples *t*-test would be used for comparison of group means across two levels, ANOVA is 
- restored `Statistics/linear-models/anova/anova-factorial`: Athough we have two factors, and an interaction effect, this requires fitting more than 3 parameters in our mo
- restored `Statistics/linear-models/anova/anova-factorial`: There is a fair bit of debate on this in the statistical literature, but many advise using what are called Typ
- restored `Statistics/linear-models/anova/anova-factorial`: **Independence.** ANOVA assumes that all replicate measures are independent of each other (i.e., equally likel
- restored `Statistics/linear-models/anova/anova-factorial`: There are a variety of measures for dealing with non-independence. These include ensuring all important predic
- restored `Statistics/linear-models/anova/anova-factorial`: Remember that the interpretation of the main effects is complicated when there is a significant interaction (s
- restored `Statistics/linear-models/anova/anova-nested`: ### Usage
- restored `Statistics/linear-models/anova/anova-nested`: We advocate a qualitative evalutation of the assumptions, rather than a formal test suc has Cochran's test. Li
- restored `Statistics/linear-models/anova/anova-nested`: ```{r}
- restored `Statistics/linear-models/anova/anova-nested`: ```{r}
- untrimmed `Statistics/linear-models/anova/anova-factorial`: **Balanced and unbalanced designs.** Ideally, factorial ANOVA should be conducted with a balanced design - one
- untrimmed `Statistics/linear-models/anova/anova-factorial`: **Normality.** The assumption of normality can be checked by a frequency histogram of the residuals or by usin
- untrimmed `Statistics/linear-models/anova/anova-factorial`: **Homogeneity of variance.** The assumption of homgeneity of variance, namely that the variation in the residu
- untrimmed `Statistics/linear-models/anova/anova-factorial`: Heterogeneous variances are indicated by non-random pattern in the residuals vs. fitted plot. Look for an even
- untrimmed `Statistics/linear-models/anova/anova-factorial`: **Written.**  The results of the main effects and any interaction should be described in the text of a results
- untrimmed `Statistics/linear-models/anova/anova-factorial`: **Visual.** A boxplot or column graph with error bars are suitable for contrasting a continuous variable acros
- untrimmed `Statistics/linear-models/anova/anova-nested`: Where there are greater than 2 levels of the the fixed factor of interest, post-hoc analysis can be used to de
- untrimmed `Statistics/linear-models/anova/anova-nested`: The same assumptions of linear models apply to nested ANOVAs; independence, normality and heterogeneity of var
- untrimmed `Statistics/linear-models/anova/anova-nested`: The assumption of normality can be checked by a frequency histogram of the residuals or using a quantile plot 
- replaced rewrite: **Independence.** ANOVA assumes that all replicate measures are independent of each other. This issue needs to
- kept new: ---
- kept new: ---

</details>

## statistical-methods/understanding-interactions.qmd
19 blocks from 1 old page(s). 19 matched the first conversion; **0 restored** (missing), **1 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 1 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

<details><summary>Details</summary>

- untrimmed `Statistics/linear-models/interactions`: Sampling or experimental designs with more than one factor give us the opportunity to test whether the factors
- kept new: - Does the effect of removing predators vary between habitats?  

</details>

## statistical-methods/generalised-linear-models.qmd
100 blocks from 3 old page(s). 94 matched the first conversion; **6 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 1 new blocks kept.


<details><summary>Details</summary>

- restored `Statistics/glms`: Generalised linear models (GLMs) are used when the distribution of data do not conform to the assumptions of l
- restored `Statistics/glms`: * [Generalised linear models 1](glm-1): Introduction and binomial data  
- restored `Statistics/glms/glm-1`: **Introduction and binomial data**
- restored `Statistics/glms/glm-1`: More advice on [interpreting coefficients in glms](/statistics/glms/interpret-glm-coeffs/)
- restored `Statistics/glms/glm-2`: **Count data**
- restored `Statistics/glms/glm-2`: More advice on [interpreting coefficients in glms](/../statistics/glms/interpret-glm-coeffs/)
- kept new: ---

</details>

## statistical-methods/interpret-glm-coeffs.qmd
43 blocks from 1 old page(s). 43 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)
- EDIT: the old page linked to itself here instead of the linear-models page the text names

## statistical-methods/mixed-effects-models.qmd
209 blocks from 4 old page(s). 202 matched the first conversion; **7 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 5 new blocks kept.

- EDIT: tidied markup (heading space: 3)
- EDIT: glmmADMB is no longer maintained; glmmTMB is its successor
- EDIT: the draft chapter is gone; the published paper by lme4's authors replaces it

<details><summary>Details</summary>

- restored `Statistics/mixed-models`: Mixed models are those with a mixture of fixed and random effects. Random effects are categorical factors wher
- restored `Statistics/mixed-models`: * [Mixed models 1](mixed-model-1): Linear mixed models with one random effect  
- restored `Statistics/mixed-models`: ![](images/Mixed_models_intro_image.jpg)
- restored `Statistics/mixed-models/mixed-model-1`: **Linear mixed models with one random effect**
- restored `Statistics/mixed-models/mixed-model-1`: ###FAQ for mixed models
- restored `Statistics/mixed-models/mixed-model-3`: ###Running the analysis
- restored `Statistics/mixed-models/mixed-model-3`: ###Communicating results
- kept new: ### FAQ for mixed models
- kept new: ---
- kept new: ---
- kept new: ### Running the analysis
- kept new: ### Communicating results

</details>

## statistical-methods/generalised-additive-models.qmd
82 blocks from 1 old page(s). 82 matched the first conversion; **0 restored** (missing), **1 restored** (trimmed), **1 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (stray ## made siblings of ###: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)
- EDIT: words in maths were typeset as italic variables; "intrannual" misspelt
- EDIT: words in maths were typeset as italic variables
- EDIT: further reading suggested in #38

<details><summary>Details</summary>

- updated `Statistics/gams`: You can have combinations of linear and smooth terms in your model, for example
- untrimmed `Statistics/gams`: We'll now look at a quick real example - we'll just scratch the surface, and in a future We'll now look at a q

</details>

## statistical-methods/time-series-analysis.qmd
47 blocks from 1 old page(s). 44 matched the first conversion; **3 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 3 new blocks kept.

- EDIT: tidied markup (heading space: 3)
- EDIT: tidied markup (headings raised to start at ##: 1)

<details><summary>Details</summary>

- restored `Statistics/time-series`: ###Simple exponential smoothing models
- restored `Statistics/time-series`: ###Models incorporating seasonal variability
- restored `Statistics/time-series`: ###Further help
- kept new: ### Simple exponential smoothing models
- kept new: ### Models incorporating seasonal variability
- kept new: ### Further help

</details>

## statistical-methods/MVabund.qmd
60 blocks from 1 old page(s). 60 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## statistical-methods/cluster-analysis.qmd
43 blocks from 1 old page(s). 43 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## statistical-methods/mds.qmd
52 blocks from 1 old page(s). 52 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (stray ## made siblings of ###: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## statistical-methods/meta-analysis.qmd
174 blocks from 4 old page(s). 167 matched the first conversion; **7 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 2 new blocks kept.

- EDIT: ape's site moved
- EDIT: metafor's example datasets moved to the metadat package
- EDIT: metafor's example datasets moved to the metadat package
- EDIT: metafor's example datasets moved to the metadat package

<details><summary>Details</summary>

- restored `Statistics/meta-analysis`: Meta-analyses are increasingly used in ecology, evolution and the environmental sciences to find general patte
- restored `Statistics/meta-analysis`: * [Meta-analyses 1](meta-analysis-1): Introduction and calculating effect sizes  
- restored `Statistics/meta-analysis`: ![](images/4666102_orig.jpg)
- restored `Statistics/meta-analysis/meta-analysis-1`: ### Background
- restored `Statistics/meta-analysis/meta-analysis-1`: Once you have calculated effect sizes, move on to the next page: [Meta-analysis 2: fixed-effect and random-eff
- restored `Statistics/meta-analysis/meta-analysis-2`: If you are happy with all this, move on the [more complex models](/statistics/meta-analysis/meta-analysis-3)
- restored `Statistics/meta-analysis/meta-analysis-2`: Any questions? Or email me (s(-dot-)nakagawa(-at-)unsw(-dot-)edu(-dot-)au). Also visit our [website](http://ww
- kept new: ---
- kept new: ---

</details>

## coding-skills/coding-skills.qmd
6 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## coding-skills/good-practice.qmd
90 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## coding-skills/functions.qmd
167 blocks from 1 old page(s). 164 matched the first conversion; **3 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 3 condensed rewrites replaced by the original, 3 new blocks kept.

- EDIT: letter case `images/Functions_image.jpg` -> `images/Functions_image.JPG` (only worked on macOS)

<details><summary>Details</summary>

- restored `Coding-Skills/writing-functions`: <!-- ## Goals for this post
- restored `Coding-Skills/writing-functions`: **It's short**
- restored `Coding-Skills/writing-functions`: **It does one thing well**
- replaced rewrite: **It's short**
- replaced rewrite: **It does one thing well**
- replaced rewrite: **It has an intuitive name**
- kept new: ## Types of function {#types}
- kept new: ## Why use functions? {#why}
- kept new: ## Writing your own functions {#how}

</details>

## coding-skills/loops.qmd
39 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## coding-skills/version-control.qmd
55 blocks from 1 old page(s). 54 matched the first conversion; **1 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 1 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

<details><summary>Details</summary>

- restored `Coding-Skills/version-control`: ```git clone https://UNSW_EnvComp@bitbucket.org/UNSW_EnvComp/unsw_envcomp.git```
- replaced rewrite: ```

</details>

## coding-skills/asking-code-questions.qmd
81 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).

- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: tidied markup (stray ## made siblings of ###: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)
- EDIT: Stack Overflow renamed the page

## misc/misc.qmd
2 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


## misc/data-entry.qmd
22 blocks from 1 old page(s). 22 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## misc/data-types-structure.qmd
48 blocks from 1 old page(s). 48 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)
- EDIT: Quick-R page gone

## misc/rstudio-notebooks.qmd
62 blocks from 1 old page(s). 62 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (stray ## made siblings of ###: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## misc/interactive-maps.qmd
26 blocks from 1 old page(s). 26 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.


## misc/contingency-tables.qmd
49 blocks from 1 old page(s). 49 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## misc/fishers-exact.qmd
20 blocks from 1 old page(s). 20 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.


## misc/goodness-of-fit.qmd
44 blocks from 1 old page(s). 44 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (<font>/<center> tags: 1)
- EDIT: tidied markup (headings raised to start at ##: 1)

## misc/power-analysis.qmd
62 blocks from 1 old page(s). 62 matched the first conversion; **0 restored** (missing), **0 restored** (trimmed), **0 updated** (changed on the old site since the first conversion), 0 condensed rewrites replaced by the original, 0 new blocks kept.

- EDIT: tidied markup (headings raised to start at ##: 1)

## datasets.qmd
47 blocks from 1 old page(s). Existing chapter was a placeholder: written from the old page(s).


