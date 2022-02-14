library(tidyverse)
library(lubridate)
library(ggplot2)


df <- read_delim(
  '/home/viridis/Dropbox/PhD/thesis/thesis_stats/lines_of_code.dat',
  ' ',
  col_names = c('Timestamp', 'Lines_of_code')
) %>% 
  mutate('Date' = as_datetime(Timestamp))

theme_set(theme_classic())

thesis_counter <- ggplot(df, aes(Date, Lines_of_code)) +
  geom_line() +
  labs(
    title = "PhD Thesis writing progress over time",
    x = 'Date',
    y = 'Lines of code',
    caption = 'Lines of code in git repository for LaTeX source file'
  )

ggsave(
  'featured.jpg',
  plot = thesis_counter,
  path ='/home/viridis/academic-kickstart/'
)


