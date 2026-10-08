# Cleaning the student dataset with the tidyverse.
# Run from the repository root:  Rscript r/clean_data.R

library(tidyverse)
df <- read_csv("data/raw_student_data.csv")
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
write_csv(df, "data/cleaned_student_data_r.csv")
