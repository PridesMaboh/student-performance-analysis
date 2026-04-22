> setwd("C:/Users/frupr/OneDrive/My Portfolios/R")
install.packages("tidyverse")
library(tidyverse)
.libPaths()
library(tidyverse)
.libPaths("C:/Users/frupr/AppData/Local/R/win-library/4.5")
library(tidyverse)
install.packages("tidyverse", lib = "C:/Users/frupr/AppData/Local/R/win-library/4.5")
.libPaths("C:/Users/frupr/Documents/Rpackages")
.libPaths()
install.packages("tidyverse", lib = "C:/Users/frupr/Documents/Rpackages")
library(tidyverse)
df <- read_csv("Raw data to be cleaned.csv")
glimpse(df)
df <- df %>%
  rename_with(~ .x %>%
                str_trim() %>%
                str_to_lower() %>%
                str_replace_all(" ", "_"))
numeric_cols <- c("age", "studyhours", "python", "db", "entryexam")

df <- df %>%
  mutate(across(all_of(numeric_cols), as.numeric))
names(df)
glimpse(df)
df <- df %>%
  mutate(gender = gender %>%
           str_trim() %>%
           str_to_title() %>%
           recode("F" = "Female",
                  "M" = "Male"))
unique(df$gender)
df <- df %>%
  mutate(country = country %>%
           str_trim() %>%
           str_to_title() %>%
           recode("Norge" = "Norway",
                  "Rsa" = "South Africa"))
unique(df$country)
df <- df %>%
  mutate(residence = residence %>%
           str_trim() %>%
           str_to_title() %>%
           recode("Bi-Residence" = "Bi Residence",
                  "Biresidence" = "Bi Residence"))
unique(df$residence)
df <- df %>%
  mutate(residence = residence %>%
           str_trim() %>%
           str_to_title() %>%
           str_replace_all("_", " ") %>%   # NEW: convert underscores to spaces
           recode("Bi-Residence" = "Bi Residence",
                  "Biresidence" = "Bi Residence"))
unique(df$residence)
df <- df %>%
  mutate(residence = residence %>%
           str_trim() %>%
           str_replace_all("_", " ") %>% 
           str_replace_all("-", " ") %>% 
           str_squish() %>% 
           str_to_title() %>%
           recode("Bi Residence" = "Bi Residence"))
unique(df$residence)
df <- df %>%
  mutate(preveducation = preveducation %>%
           str_trim() %>%
           str_to_title() %>%
           recode("Highschool" = "High School",
                  "Barrrchelors" = "Bachelors"))
unique(df$preveducation)
df <- df %>%
  mutate(preveducation = preveducation %>%
           str_trim() %>%
           str_to_title() %>%
           recode("Diplomaaa" = "Diploma"))
unique(df$preveducation)
unique(df)
print(n = ...)
colSums(is.na(df))
df <- df %>%
  mutate(python = ifelse(is.na(python),
                         mean(python, na.rm = TRUE),
                         python))
colSums(is.na(df))
df <- df %>% distinct()
str(df)
summary(df)
unique(df$gender)
unique(df$country)
unique(df$residence)
unique(df$preveducation)
colSums(is.na(df))
str(df)
summary(df)
unique(df$gender)
unique(df$country)
unique(df$residence)
unique(df$preveducation)
colSums(is.na(df))
str(df)
summary(df)
unique(df$gender)
unique(df$country)
unique(df$residence)
unique(df$preveducation)
colSums(is.na(df))
write_csv(df, "C:/Users/frupr/OneDrive/My Portfolios/R/cleaned_student_data_r.csv")
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("students_clean.csv")

# Quick peek
df.head()
df.info()
df.describe(include="all")
pip install pandas numpy seaborn matplotlib




