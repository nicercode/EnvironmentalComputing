---
title: Instructions for building and editing Environmental Computing
---

The website is developed using the [Hugo](https://hugodocs.info) static site generator and deployed on [netifly](netlify.com). We're using the `learn`  theme [available here at GitHub](https://github.com/matcornic/hugo-theme-learn).

# Building site 

Following are our notes on site upkeep.

We deploy via R, using the blogdown package. You ran run Hugo independently, but we're assuming you use R. 

```
install.packages("blogdown")
```

The site requires a particular version of Hugo

```
blogdown::install_hugo("0.91.2")
blogdown::check_hugo()
```

To build the site:

```
blogdown::serve_site()
```

- This opens up a web page where the site is continually rebuilt. If you create a new `Rmd` it is automatically rendered and added to the site
- Build pages are deployed in the folder `public`. 
- Watch for error messages

To stop the server:

```
blogdown::stop_server()
```

# Writing content

## Folder structure

The side menu is created from the file structure in the folder `content`. Both Rmd and md pages are rendered into html. 

We're using a structure where each new page is stored in its own folder, along with all the images and data you need. Within that folder the rmd is file is named `_index.rmd`. Any images or files linked in the page can be stored in the folder too, enabling you to to use relative links in the rmd file. E.g.

```
├── page_name
|     ├── _index.rmd
|     ├── data.csv
|     ├── image.jpg
|     ├── ....
├── another_page
```

Creating a new page:

1. Make a new folder inside `content` (without spaces or special chars in the name)
2. In the folder, create a new file `_index.rmd` with yaml

```
---
title: "Making New Variables"
author: "Alistair Poore"
---
```


## Short codes

Hugo uses short codes to easily embed content. See https://gohugo.io/content-management/shortcodes/. When rendering files ia blogdown, you can't write the shortcodes directly, instead you can use the [`shortcode` function](https://rdrr.io/github/rstudio/blogdown/man/shortcode.html)



### Tweet
In an md file:

```
{{< tweet 306854385076543488 >}}
```

In an Rmd file

```
`r blogdown::shortcode("tweet", "306854385076543488")`
```
### Figure

In an md file:

```
{{< figure src="https://danielfalster.com/images/2016.06.27-useR/useR-600x300.png" height="100" width="100" >}}
```

In an Rmd file??

```
`r blogdown::shortcode("figure", src = "https://danielfalster.com/images/2016.06.27-useR/useR-600x300.png", alt = "A nice figure")`
```



