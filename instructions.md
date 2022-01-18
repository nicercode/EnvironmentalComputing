---
title: Instructions 
---

```{r}
blogdown::install_hugo("0.91.2")

blogdown::check_hugo()
blogdown::build_site()
blogdown::serve_site()

blogdown::stop_server()
```

## Documentation website

This current documentation has been statically generated with Hugo with a simple command : `hugo -t hugo-theme-learn` -- source code is [available here at GitHub](https://github.com/matcornic/hugo-theme-learn)

{{% notice note %}}
Automatically published and hosted thanks to [Netlify](https://www.netlify.com/). Read more about [Automated HUGO deployments with Netlify](https://www.netlify.com/blog/2015/07/30/hosting-hugo-on-netlifyinsanely-fast-deploys/)
{{% /notice %}}
